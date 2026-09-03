#!/usr/bin/env python3
"""
fpl_pre_pull.py — weekly PRE-cadence pull for group A (account & market) of the FPL data inventory.

Standard library only. Runs on GitHub Actions, a Mac (cron/launchd), or any shell with open internet.
Writes two files per run into --out:
    GW{N}_PRE_{UTC-stamp}.json   full machine-readable snapshot (raw + derived + coverage)
    GW{N}_PRE_{UTC-stamp}.md     human brief for the Claude session

Usage
    python3 fpl_pre_pull.py                       # live pull, only inside the PRE window (default 30 h before deadline)
    python3 fpl_pre_pull.py --force               # live pull regardless of the window
    python3 fpl_pre_pull.py --offline fixtures/   # test against saved JSON (no network)

No login of any kind. The authenticated my-team/ endpoint (FPL uses an OpenID Connect bearer token from
account.premierleague.com, renewed every few minutes, so no static secret can call it) is NOT used: purchase
prices come from element-summary (GW1 price) and the transfers endpoint (element_in_cost), selling prices from
FPL's sell-on rule in game_settings, free transfers from the transfer history, chips from bootstrap chips
minus history chips. All labelled DERIVED; exact unless a Free Hit has been played (see A1 note).
"""
import argparse, json, os, sys, time, glob, gzip, zlib, unicodedata, urllib.request, urllib.error, urllib.parse
from datetime import datetime, timezone

ENTRY_ID = 6048651
FPL = "https://fantasy.premierleague.com/api/"
LFPL = "https://livefpl.us/"
UA = {"User-Agent": "Mozilla/5.0 (fpl-pre-pull; personal use)"}

# ----------------------------------------------------------------------------- fetch layer
class Source:
    def __init__(self, offline_dir=None, prev_dir=None):
        self.offline = offline_dir
        self.prev_dir = prev_dir
        self.log = []  # (url, status, bytes, ms)

    def _get(self, url, headers=None):
        t0 = time.time()
        hdr = dict(headers or UA)
        try:
            hdr.setdefault("Accept-Encoding", "gzip, deflate")
            with urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=30) as r:
                body = r.read()
                enc = (r.headers.get("Content-Encoding") or "").lower()
                if enc == "gzip" or body[:2] == b"\x1f\x8b":
                    body = gzip.decompress(body)
                elif enc == "deflate":
                    body = zlib.decompress(body)
                self.log.append((url, r.status, len(body), int((time.time() - t0) * 1000)))
                return json.loads(body.decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            self.log.append((url, e.code, 0, int((time.time() - t0) * 1000)))
            return None
        except Exception as e:  # network / proxy / JSON
            self.log.append((url, f"ERR {type(e).__name__}", 0, int((time.time() - t0) * 1000)))
            return None

    def _file(self, name):
        p = os.path.join(self.offline, name)
        if not os.path.exists(p):
            self.log.append((p, "MISSING", 0, 0))
            return None
        with open(p) as f:
            d = json.load(f)
        self.log.append((p, "FILE", os.path.getsize(p), 0))
        return d

    # FPL
    def bootstrap(self):        return self._file("bootstrap.json") if self.offline else self._get(FPL + "bootstrap-static/")
    def entry(self):            return self._file("entry.json") if self.offline else self._get(FPL + f"entry/{ENTRY_ID}/")
    def history(self):          return self._file("history.json") if self.offline else self._get(FPL + f"entry/{ENTRY_ID}/history/")
    def picks(self, gw):        return self._file("picks.json") if self.offline else self._get(FPL + f"entry/{ENTRY_ID}/event/{gw}/picks/")
    def transfers(self):        return self._file("transfers.json") if self.offline else self._get(FPL + f"entry/{ENTRY_ID}/transfers/")
    def fixtures(self, gw):     return self._file("fixtures.json") if self.offline else self._get(FPL + f"fixtures/?event={gw}")
    def live(self, gw):         return self._file("live.json") if self.offline else self._get(FPL + f"event/{gw}/live/")
    def element_summary(self, i): return self._file(f"element_{i}.json") if self.offline else self._get(FPL + f"element-summary/{i}/")
    def fixtures_all(self):   return self._file("fixtures_all.json") if self.offline else self._get(FPL + "fixtures/")
    # ESPN hidden JSON (cups, European ties, odds) — open, no key
    def espn(self, league, d1, d2):
        key = {"uefa.champions": "ucl", "uefa.europa": "uel", "uefa.europa.conf": "uecl", "eng.league_cup": "efl", "eng.fa": "fa", "eng.1": "pl"}[league]
        if self.offline:
            return self._file(f"espn_{key}.json")
        # ESPN's edge returned 403 to the GitHub runner with a plain UA (3 Sep 2026); send browser-like headers and fall back to the core host
        h = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
             "Accept": "application/json, text/plain, */*", "Accept-Language": "en-GB,en;q=0.9", "Referer": "https://www.espn.com/", "Origin": "https://www.espn.com"}
        j = self._get(f"https://site.api.espn.com/apis/site/v2/sports/soccer/{league}/scoreboard?dates={d1}-{d2}", headers=h)
        if j: return j
        j = self._get(f"https://site.web.api.espn.com/apis/site/v2/sports/soccer/{league}/scoreboard?dates={d1}-{d2}", headers=h)
        if j: return j
        return self._get(f"https://cdn.espn.com/core/soccer/scoreboard?xhr=1&league={league}&dates={d1}-{d2}", headers=h)
    # Open-Meteo — open, no key; hourly forecast at a venue for one UTC day
    def meteo(self, lat, lon, day):
        if self.offline:
            return self._file("meteo_sample.json")
        return self._get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation_probability,precipitation,wind_speed_10m,wind_gusts_10m&wind_speed_unit=kmh&timezone=UTC&start_date={day}&end_date={day}")
    # football-data.co.uk season CSV — open; referee, cards, shots, corners, xG, odds per finished match
    def fdcsv(self, season="2627"):
        if self.offline:
            p = os.path.join(self.offline, "fdcsv_sample.csv")
            return open(p).read() if os.path.exists(p) else None
        t0 = time.time()
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://www.football-data.co.uk/mmz4281/{season}/E0.csv", headers=UA), timeout=30) as r:
                body = r.read().decode("utf-8", "replace"); self.log.append((r.url, r.status, len(body), int((time.time() - t0) * 1000))); return body
        except Exception as e:
            self.log.append(("football-data.co.uk E0.csv", f"ERR {type(e).__name__}", 0, 0)); return None
    # Understat — JSON endpoints behind the site pages; the X-Requested-With header is required (3 Sep 2026). 3–12 calls per GW.
    US_H = {"X-Requested-With": "XMLHttpRequest", "Accept": "application/json", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0.0.0 Safari/537.36", "Referer": "https://understat.com/"}
    def understat_team(self, title, season):
        if self.offline:
            return self._file(f"understat_team_{title}.json")
        return self._get(f"https://understat.com/getTeamData/{urllib.parse.quote(title)}/{season}", headers=self.US_H)
    def understat_match(self, mid):
        return self._file(f"understat_match_{mid}.json") if self.offline else self._get(f"https://understat.com/getMatchData/{mid}", headers=self.US_H)
    # FotMob — same-origin data proxy used by the site; Opta-fed. Untested from GitHub (3 Sep 2026); fails gracefully.
    FM_H = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0.0.0 Safari/537.36", "Accept": "application/json", "Referer": "https://www.fotmob.com/"}
    def fotmob_league(self, season="2026/2027"):
        return self._file("fotmob_leagues.json") if self.offline else self._get(f"https://www.fotmob.com/api/data/leagues?id=47&season={urllib.parse.quote(season, safe='')}", headers=self.FM_H)
    def fotmob_match(self, mid):
        return self._file(f"fotmob_match_{mid}.json") if self.offline else self._get(f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}", headers=self.FM_H)
    # LiveFPL (.us JSON)
    def lf(self, name, gw=None):
        fname = "livefpl_" + name.replace("api/", "").replace(".json", "").replace(f"_{gw}", "") + ".json"
        return self._file(fname) if self.offline else self._get(LFPL + name)


# ----------------------------------------------------------------------------- helpers
def now_utc():
    return datetime.now(timezone.utc)

def parse_ts(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

def pct(x, nd=1):
    return None if x is None else round(float(x), nd)


# ----------------------------------------------------------------------------- group B reference tables
# Stadium coordinates (home venue per FPL short_name), 2026/27. Everton = Hill Dickinson Stadium.
VENUE = {"ARS": (51.5549, -0.1084), "AVL": (52.5092, -1.8847), "BOU": (50.7352, -1.8383), "BRE": (51.4907, -0.2889),
         "BHA": (50.8616, -0.0837), "CHE": (51.4817, -0.1910), "COV": (52.4481, -1.4956), "CRY": (51.3983, -0.0855),
         "EVE": (53.4109, -2.9925), "FUL": (51.4750, -0.2217), "HUL": (53.7466, -0.3677), "IPS": (52.0549, 1.1447),
         "LEE": (53.7778, -1.5721), "LIV": (53.4308, -2.9608), "MCI": (53.4831, -2.2004), "MUN": (53.4631, -2.2913),
         "NEW": (54.9756, -1.6217), "NFO": (52.9399, -1.1329), "SUN": (54.9144, -1.3882), "TOT": (51.6043, -0.0665)}
# ESPN numeric team id -> FPL short_name (H7 crosswalk, verified 3 Sep 2026 from the eng.1 scoreboard).
# Never map by abbreviation: ESPN uses "MUN" for Bayern Munich and "MAN" for Manchester United.
ESPN_ID_TO_FPL = {"306": "HUL", "331": "BHA", "337": "BRE", "349": "BOU", "357": "LEE", "359": "ARS", "360": "MUN", "361": "NEW", "362": "AVL",
                  "363": "CHE", "364": "LIV", "366": "SUN", "367": "TOT", "368": "EVE", "370": "FUL", "373": "IPS", "382": "MCI", "384": "CRY",
                  "388": "COV", "393": "NFO"}
# football-data.co.uk team names -> FPL short_name
FD_TO_FPL = {"Arsenal": "ARS", "Aston Villa": "AVL", "Bournemouth": "BOU", "Brentford": "BRE", "Brighton": "BHA", "Chelsea": "CHE",
             "Coventry": "COV", "Crystal Palace": "CRY", "Everton": "EVE", "Fulham": "FUL", "Hull": "HUL", "Ipswich": "IPS", "Leeds": "LEE",
             "Liverpool": "LIV", "Man City": "MCI", "Man United": "MUN", "Newcastle": "NEW", "Nott'm Forest": "NFO", "Sunderland": "SUN", "Tottenham": "TOT"}
# FIFA men's international windows touching 2026/27 (beIN Sports 24 Aug 2026; merged Sep/Oct window per FIFA 2025–30 calendar)
FIFA_WINDOWS = [("2026-09-21", "2026-10-06", "Sep/Oct merged window (16 days, up to 4 matches)"), ("2026-11-09", "2026-11-17", "November window"),
                ("2027-03-22", "2027-03-30", "March window [PROJECTED — confirm on FIFA calendar]")]


def build_schedule(src, bs, N, teams, cov, warn, prev):
    """Group B: fixtures, FDR, DGW/BGW, deadlines, breaks, cups, rest days, weather, referees."""
    from datetime import timedelta
    fx = src.fixtures_all() or []
    ev = {e["id"]: e for e in bs["events"]}
    horizon = [g for g in range(N, min(N + 6, 39))]
    out = {}
    # B1/B2/B3: next-6 per team, plus B4 map
    per_team = {t: [] for t in teams.values()}
    counts = {g: {} for g in horizon}
    fdr_now = {}
    for f in fx:
        if f["event"] in horizon:
            h, a = teams[f["team_h"]], teams[f["team_a"]]
            per_team[h].append({"gw": f["event"], "opp": a, "home": True, "fdr": f["team_h_difficulty"], "ko": f["kickoff_time"], "fixture_id": f["id"]})
            per_team[a].append({"gw": f["event"], "opp": h, "home": False, "fdr": f["team_a_difficulty"], "ko": f["kickoff_time"], "fixture_id": f["id"]})
            counts[f["event"]][h] = counts[f["event"]].get(h, 0) + 1; counts[f["event"]][a] = counts[f["event"]].get(a, 0) + 1
            fdr_now[str(f["id"])] = [f["team_h_difficulty"], f["team_a_difficulty"]]
    for t in per_team: per_team[t].sort(key=lambda x: x["gw"])
    out["fixtures_next6"] = per_team
    out["dgw_bgw"] = {g: {"double": [t for t, c in counts[g].items() if c > 1], "blank": [t for t in teams.values() if t not in counts[g]]} for g in horizon}
    unscheduled = [f["id"] for f in fx if f["event"] is None or not f["kickoff_time"]]
    cov["B1"] = {"status": "OK", "source": "fixtures/ (380, all scheduled)" if not unscheduled else f"fixtures/ ({len(unscheduled)} unscheduled — postponed/TBC)", "note": ""}
    cov["B2"] = {"status": "OK", "source": "fixtures/ kickoff_time; ESPN eng.1 and PL SDP API agreed to the minute on 3 Sep", "note": ""}
    # B3 FDR + change detection vs previous snapshot
    prev_fdr = ((prev or {}).get("B_schedule") or {}).get("fdr_by_fixture") or {}
    changes = [{"fixture_id": k, "was": prev_fdr[k], "now": v} for k, v in fdr_now.items() if k in prev_fdr and prev_fdr[k] != v]
    out["fdr_by_fixture"] = fdr_now
    out["fdr_changes_since_last_snapshot"] = changes
    if changes: warn.append(f"B3: FPL revised FDR on {len(changes)} fixture(s) since the last snapshot")
    cov["B3"] = {"status": "OK", "source": "fixtures/ team_h/a_difficulty (= element-summary difficulty, 12/12 checked)", "note": "team strength_attack/defence fields are 0 in bootstrap — only strength_overall is populated; FDR revisions are diffed against the previous snapshot"}
    cov["B4"] = {"status": "OK (DERIVED)", "source": "fixture count per team per event", "note": "none in the next 6 GW" if not any(v["double"] or v["blank"] for v in out["dgw_bgw"].values()) else "DGW/BGW present — see map"}
    # B8 deadlines, B7 breaks
    out["deadlines"] = [{"gw": g, "deadline_utc": ev[g]["deadline_time"]} for g in horizon]
    gaps = []
    ids = sorted(ev)
    for i in range(1, len(ids)):
        d = (parse_ts(ev[ids[i]]["deadline_time"]) - parse_ts(ev[ids[i - 1]]["deadline_time"])).total_seconds() / 86400
        if d > 8.5:
            a, b = ev[ids[i - 1]]["deadline_time"][:10], ev[ids[i]]["deadline_time"][:10]
            label = next((w[2] for w in FIFA_WINDOWS if a <= w[0] <= b), "no FIFA window — cup round or scheduling gap")
            gaps.append({"after_gw": ids[i - 1], "before_gw": ids[i], "days": round(d, 1), "label": label})
    out["breaks"] = gaps
    cov["B8"] = {"status": "OK", "source": "bootstrap events.deadline_time", "note": ""}
    cov["B7"] = {"status": "PARTIAL", "source": "deadline gaps > 8.5 d labelled with the FIFA window table", "note": "break DATES are derived; per-player call-ups and return-travel distance (D16) are not fetched — manual per break"}
    # B5 cups via ESPN (window: today .. last deadline in horizon + 8 d)
    today = now_utc().strftime("%Y%m%d"); until = (parse_ts(ev[horizon[-1]]["deadline_time"]) + timedelta(days=8)).strftime("%Y%m%d")
    cups = {t: [] for t in teams.values()}
    espn_ok = 0
    fpl_names = set(teams.values())
    for league, label in [("uefa.champions", "UCL"), ("uefa.europa", "UEL"), ("uefa.europa.conf", "UECL"), ("eng.league_cup", "EFL Cup"), ("eng.fa", "FA Cup")]:
        j = src.espn(league, today, until)
        if not j: continue
        espn_ok += 1
        for e in j.get("events", []):
            comp = e["competitions"][0]
            sides = {c["homeAway"]: c["team"] for c in comp.get("competitors", [])}
            for ha, team in sides.items():
                ab = ESPN_ID_TO_FPL.get(str(team["id"]))
                if ab and ab in fpl_names:
                    opp = sides["away" if ha == "home" else "home"]
                    cups[ab].append({"date": e["date"], "comp": label, "opp": opp["displayName"], "home": ha == "home", "espn_id": e["id"]})
    for t in cups: cups[t].sort(key=lambda x: x["date"])
    out["cup_fixtures"] = {t: v for t, v in cups.items() if v}
    cov["B5"] = {"status": "OK" if espn_ok == 5 else ("PARTIAL" if espn_ok else "MISSING"), "source": "ESPN site.api.espn.com scoreboard (uefa.champions, uefa.europa, uefa.europa.conf, eng.league_cup, eng.fa)", "note": f"{espn_ok}/5 competitions fetched; FA Cup has no PL-club ties until January"}
    # B6 rest days: last match of any competition before the next PL fixture, and next match after it
    def esdate(s): return datetime.strptime(s[:16], "%Y-%m-%dT%H:%M").replace(tzinfo=timezone.utc)
    all_matches = {t: [] for t in teams.values()}
    for f in fx:
        if f.get("kickoff_time"):
            for t in (teams[f["team_h"]], teams[f["team_a"]]): all_matches[t].append((parse_ts(f["kickoff_time"]), "PL"))
    for t, v in cups.items():
        for c in v: all_matches[t].append((esdate(c["date"]), c["comp"]))
    rest = {}
    for t, lst in all_matches.items():
        nxt = next((x for x in per_team[t] if x["gw"] == N), None)
        if not nxt: continue
        ko = parse_ts(nxt["ko"]); lst.sort()
        before = [m for m in lst if m[0] < ko]; after = [m for m in lst if m[0] > ko]
        rest[t] = {"next_pl": nxt["ko"], "days_since_last": round((ko - before[-1][0]).total_seconds() / 86400, 1) if before else None, "last_comp": before[-1][1] if before else None,
                   "days_to_next": round((after[0][0] - ko).total_seconds() / 86400, 1) if after else None, "next_comp": after[0][1] if after else None,
                   "matches_in_7d_before": sum(1 for m in before if (ko - m[0]).total_seconds() < 7 * 86400)}
    out["rest"] = rest
    cov["B6"] = {"status": "OK (DERIVED)", "source": "fixtures/ + ESPN cup dates", "note": "days since last match (any comp) before the GW fixture; congestion flag = matches in the 7 days before"}
    # B10 weather for GW N fixtures within 7 days
    wx = []
    for f in fx:
        if f["event"] == N and f.get("kickoff_time"):
            ko = parse_ts(f["kickoff_time"]); h = teams[f["team_h"]]
            if 0 <= (ko - now_utc()).total_seconds() <= 7 * 86400 and h in VENUE:
                j = src.meteo(VENUE[h][0], VENUE[h][1], ko.strftime("%Y-%m-%d"))
                if j and "hourly" in j:
                    key = ko.strftime("%Y-%m-%dT%H:00"); hh = j["hourly"]
                    i = hh["time"].index(key) if key in hh["time"] else None
                    if i is not None:
                        wx.append({"fixture": f"{h} v {teams[f['team_a']]}", "kickoff": f["kickoff_time"], "temp_c": hh["temperature_2m"][i], "precip_prob": hh["precipitation_probability"][i],
                                   "precip_mm": hh["precipitation"][i], "wind_kmh": hh["wind_speed_10m"][i], "gust_kmh": hh["wind_gusts_10m"][i],
                                   "flag": "WINDY" if hh["wind_speed_10m"][i] >= 30 or hh["wind_gusts_10m"][i] >= 50 else ("WET" if hh["precipitation_probability"][i] >= 60 else "")})
    out["weather"] = wx
    cov["B10"] = {"status": "OK" if wx else "PARTIAL", "source": "Open-Meteo hourly at the home venue (no key)", "note": "only for kick-offs within 7 days; re-run at XI"}
    # B9 referees: appointments not in any JSON found; football-data.co.uk gives referee + cards per finished match (G7 stats)
    csv_txt = src.fdcsv()
    refs = {}; last = []
    if csv_txt:
        import csv, io
        for row in csv.DictReader(io.StringIO(csv_txt)):
            r = row.get("Referee"); 
            if not r: continue
            d = refs.setdefault(r, {"matches": 0, "yellows": 0, "reds": 0, "fouls": 0})
            d["matches"] += 1; d["yellows"] += int(row.get("HY") or 0) + int(row.get("AY") or 0); d["reds"] += int(row.get("HR") or 0) + int(row.get("AR") or 0); d["fouls"] += int(row.get("HF") or 0) + int(row.get("AF") or 0)
            last.append({"date": row["Date"], "home": FD_TO_FPL.get(row["HomeTeam"], row["HomeTeam"]), "away": FD_TO_FPL.get(row["AwayTeam"], row["AwayTeam"]), "ref": r, "xg": [row.get("HxG"), row.get("AxG")]})
        for r, d in refs.items(): d["yellows_per_match"] = round(d["yellows"] / d["matches"], 2)
    out["referee_season_stats"] = refs
    out["referee_last_matches"] = last[-10:]
    cov["B9"] = {"status": "PARTIAL", "source": "football-data.co.uk E0.csv (referee per finished match, season card rates)", "note": "appointments for the coming GW are published by the PL (Tue/Wed) but exist in no JSON endpoint found — the PL SDP match API has no officials field and no 'Match officials' article appeared in the content feed; attended web step"}
    return out


# ----------------------------------------------------------------------------- group C reference tables
US_TITLE = {"ARS": "Arsenal", "AVL": "Aston Villa", "BOU": "Bournemouth", "BRE": "Brentford", "BHA": "Brighton", "CHE": "Chelsea", "COV": "Coventry",
            "CRY": "Crystal Palace", "EVE": "Everton", "FUL": "Fulham", "HUL": "Hull", "IPS": "Ipswich", "LEE": "Leeds", "LIV": "Liverpool",
            "MCI": "Manchester City", "MUN": "Manchester United", "NEW": "Newcastle United", "NFO": "Nottingham Forest", "SUN": "Sunderland", "TOT": "Tottenham"}
FOTMOB_ID_TO_FPL = {"8455": "CHE", "8456": "MCI", "8463": "LEE", "8472": "SUN", "8586": "TOT", "8650": "LIV", "8667": "HUL", "8668": "EVE", "8669": "COV",
                    "8678": "BOU", "9825": "ARS", "9826": "CRY", "9879": "FUL", "9902": "IPS", "9937": "BRE", "10203": "NFO", "10204": "BHA",
                    "10252": "AVL", "10260": "MUN", "10261": "NEW"}
SOFASCORE_ID_TO_FPL = {"7": "CRY", "11": "COV", "14": "NFO", "17": "MCI", "30": "BHA", "32": "IPS", "33": "TOT", "34": "LEE", "35": "MUN", "38": "CHE",
                       "39": "NEW", "40": "AVL", "41": "SUN", "42": "ARS", "43": "FUL", "44": "LIV", "48": "EVE", "50": "BRE", "60": "BOU", "96": "HUL"}


def load_pool(bs, top10k, out_dir, owned_ids):
    """Buying pool = manual list (pool.json) + automatic rules. Returns list of element ids (not owned)."""
    cfg = {"manual": [], "auto": {"top_transfers_in": 8, "top_form_per_position": 3, "min_selected_pct": 3.0, "top10k_eo_min": 40}}
    for cand in ("pool.json", os.path.join(out_dir, "..", "pool.json")):
        if os.path.exists(cand):
            try:
                cfg.update(json.load(open(cand)))
            except Exception:
                pass
            break
    el = bs["elements"]; by_id = {e["id"]: e for e in el}; by_name = {}
    for e in el:
        by_name.setdefault(_norm(e["web_name"]), []).append(e["id"])
    pool = set()
    reasons = {}
    for m in cfg.get("manual", []):
        ids = [m] if isinstance(m, int) else by_name.get(_norm(str(m)), [])
        for i in ids:
            pool.add(i); reasons.setdefault(i, []).append("manual/watchlist")
    a = cfg.get("auto", {})
    avail = [e for e in el if e["status"] == "a"]
    for e in sorted(avail, key=lambda e: -((e.get("transfers_in_event") or 0) - (e.get("transfers_out_event") or 0)))[: a.get("top_transfers_in", 0)]:
        pool.add(e["id"]); reasons.setdefault(e["id"], []).append("top net transfers in")
    for pos in (1, 2, 3, 4):
        cands = [e for e in avail if e["element_type"] == pos and float(e["selected_by_percent"]) >= a.get("min_selected_pct", 0)]
        for e in sorted(cands, key=lambda e: -float(e.get("form") or 0))[: a.get("top_form_per_position", 0)]:
            pool.add(e["id"]); reasons.setdefault(e["id"], []).append("top form in position")
    if top10k:
        for k, v in top10k.items():
            if v * 100 >= a.get("top10k_eo_min", 999) and int(k) in by_id:
                pool.add(int(k)); reasons.setdefault(int(k), []).append(f"top-10k EO {round(v*100,1)}%")
    pool -= set(owned_ids)
    return sorted(pool), reasons


def _norm(sname):
    return "".join(c for c in unicodedata.normalize("NFKD", sname or "") if not unicodedata.combining(c)).lower().replace(".", " ").replace("'", " ")

def _match_name(fpl_el, candidates, key):
    """Best-effort name match: FPL first/second/web names vs a provider's display name. Returns (candidate, score)."""
    toks = set(t for t in _norm(f"{fpl_el.get('first_name','')} {fpl_el.get('second_name','')} {fpl_el.get('web_name','')}").replace("-", " ").split() if len(t) >= 3)
    best, bs = None, 0
    for c in candidates:
        ct = set(t for t in _norm(key(c)).replace("-", " ").split() if len(t) >= 3)
        sc = len(toks & ct)
        if sc > bs:
            best, bs = c, sc
    return (best, bs) if bs >= 1 else (None, 0)


def build_post(src, bs, owned_ids, out_dir, force=False, pool_ids=None):
    """Group C: per-player per-match facts for the last finished GW, three providers, consistency, gate."""
    cov, warn = {}, {}
    ev = bs["events"]; cur = next((e for e in ev if e["is_current"]), None)
    if not cur:
        return None, "no current event"
    L = cur["id"]
    if not (cur["finished"] and cur["data_checked"]) and not force and not src.offline:
        return None, f"GW{L} not yet finished+data_checked — POST pull waits (use --force)"
    if not force and not src.offline and glob.glob(os.path.join(out_dir, f"GW{L}_POST_*.json")):
        return None, f"GW{L} POST snapshot already exists"
    el = {e["id"]: e for e in bs["elements"]}; teams = {t["id"]: t["short_name"] for t in bs["teams"]}
    live = src.live(L) or {"elements": []}; live_by = {e["id"]: e for e in live["elements"]}
    fx = [f for f in (src.fixtures_all() or []) if f.get("event") == L]
    fx_by_id = {f["id"]: f for f in fx}
    season = int(cur["deadline_time"][:4]) if int(cur["deadline_time"][5:7]) >= 7 else int(cur["deadline_time"][:4]) - 1
    gw_date = None
    # ----- Understat per owned club
    tracked = list(owned_ids) + [i for i in (pool_ids or []) if i not in owned_ids]
    clubs = sorted({teams[el[i]["team"]] for i in tracked if i in el})
    us_matches = {}   # fpl_short -> (match_id, match json, side)
    us_ok = 0
    for club in clubs:
        tj = src.understat_team(US_TITLE[club], season)
        if not tj: continue
        us_ok += 1
        # the club's fixture in GW L: match by date window of the GW's fixtures
        gw_kos = [parse_ts(f["kickoff_time"]) for f in fx if teams[f["team_h"]] == club or teams[f["team_a"]] == club]
        for d in tj.get("dates", []):
            if not d.get("isResult"): continue
            dt = datetime.strptime(d["datetime"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            if any(abs((dt - k).total_seconds()) < 36 * 3600 for k in gw_kos):
                side = "h" if d["h"]["title"] == US_TITLE[club] else "a"
                mj = src.understat_match(d["id"])
                us_matches[club] = {"id": d["id"], "side": side, "xG": d["xG"], "goals": d["goals"], "match": mj, "opp": d["a" if side == "h" else "h"]["title"]}
    # ----- FotMob per fixture involving an owned club
    fm_matches = {}
    lg = src.fotmob_league()
    fm_ids = {}
    if lg:
        for m in (lg.get("fixtures", {}).get("allMatches") or []):
            if str(m.get("round")) == str(L):
                h, a = FOTMOB_ID_TO_FPL.get(str(m["home"]["id"])), FOTMOB_ID_TO_FPL.get(str(m["away"]["id"]))
                if h in clubs or a in clubs: fm_ids[m["id"]] = (h, a)
    elif src.offline:
        for f in glob.glob(os.path.join(src.offline, "fotmob_match_*.json")):
            j = json.load(open(f)); g = j.get("general", {})
            if g.get("finished"):
                h, a = FOTMOB_ID_TO_FPL.get(str(g.get("homeTeam", {}).get("id"))), FOTMOB_ID_TO_FPL.get(str(g.get("awayTeam", {}).get("id")))
                fm_ids[str(g.get("matchId"))] = (h, a)
    fm_ok = 0
    for mid, (h, a) in fm_ids.items():
        j = src.fotmob_match(mid)
        if not j: continue
        fm_ok += 1
        c = j.get("content", j)     # live shape has .content; offline sample is already trimmed
        ps = c.get("playerStats", {})
        flat_ps = {}
        for pid, pp in ps.items():
            if "stats" in pp and isinstance(pp["stats"], dict):
                flat_ps[pid] = pp
            else:
                flat = {}
                for grp in pp.get("stats", []):
                    for k, v in (grp.get("stats") or {}).items():
                        flat[k] = (v.get("stat", {}).get("value") if isinstance(v, dict) else v)
                flat_ps[pid] = {"id": pp.get("id"), "name": pp.get("name"), "teamId": pp.get("teamId"), "stats": flat}
        info = (c.get("matchFacts", {}).get("infoBox") if "matchFacts" in c else c.get("infoBox")) or {}
        ref = info.get("Referee") or {}
        events = c.get("matchFacts", {}).get("events", {}).get("events") if "matchFacts" in c else c.get("events")
        shots = c.get("shotmap", {}).get("shots") if isinstance(c.get("shotmap"), dict) else c.get("shotmap")
        stats = c.get("stats", {}).get("Periods", {}).get("All", {}).get("stats") if isinstance(c.get("stats"), dict) else c.get("stats")
        fm_matches[mid] = {"home": h, "away": a, "players": flat_ps, "referee": ref.get("text"), "referee_stats": ref.get("stats"), "events": events or [], "shots": shots or [], "stats": stats or [], "weather": c.get("weather")}
    # ----- per owned player
    rows = []; cons = {"minutes": [], "xg": [], "points": []}
    for i in tracked:
        e = el.get(i)
        if not e: continue
        club = teams[e["team"]]
        lv = live_by.get(i, {}).get("stats", {})
        expl = live_by.get(i, {}).get("explain", [])
        fid = expl[0]["fixture"] if expl else None
        f = fx_by_id.get(fid) if fid else None
        row = {"id": i, "name": e["web_name"], "club": club, "pos": {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}[e["element_type"]], "owned": i in owned_ids,
               "opp": (teams[f["team_a"]] if f and f["team_h"] == e["team"] else (teams[f["team_h"]] if f else None)), "home": (f["team_h"] == e["team"]) if f else None,
               "fpl": {k: lv.get(k) for k in ["minutes", "starts", "total_points", "goals_scored", "assists", "clean_sheets", "goals_conceded", "own_goals", "penalties_saved", "penalties_missed",
                                                "yellow_cards", "red_cards", "saves", "bonus", "bps", "defensive_contribution", "clearances_blocks_interceptions", "recoveries", "tackles",
                                                "expected_goals", "expected_assists", "expected_goal_involvements", "expected_goals_conceded", "influence", "creativity", "threat", "ict_index"]},
               "status_now": e["status"], "news_now": e.get("news") or ""}
        row["absent_reason"] = ("did not play — " + (e.get("news") or "no FPL news; check reports")) if (lv.get("minutes") or 0) == 0 else None
        # Understat
        um = us_matches.get(club)
        if um and um.get("match"):
            roster = list((um["match"].get("rosters", {}).get(um["side"]) or {}).values())
            cand, sc = _match_name(e, roster, lambda r: r["player"])
            if cand:
                shots = [sh for sh in (um["match"].get("shots", {}).get(um["side"]) or []) if sh.get("player") == cand["player"]]
                row["understat"] = {"player_id": cand["player_id"], "name": cand["player"], "match_score": sc, "min": int(cand["time"]), "position": cand["position"], "shots": int(cand["shots"]),
                                    "xG": round(float(cand["xG"]), 3), "xA": round(float(cand["xA"]), 3), "key_passes": int(cand["key_passes"]), "goals": int(cand["goals"]), "assists": int(cand["assists"]),
                                    "xGChain": round(float(cand["xGChain"]), 3), "xGBuildup": round(float(cand["xGBuildup"]), 3),
                                    "shot_list": [{"min": int(sh["minute"]), "result": sh["result"], "xG": round(float(sh["xG"]), 3), "X": round(float(sh["X"]), 3), "Y": round(float(sh["Y"]), 3), "situation": sh["situation"], "body": sh["shotType"], "last_action": sh.get("lastAction")} for sh in shots]}
            else:
                row["understat"] = {"unmatched": True, "roster_names": [r["player"] for r in roster][:25]}
        # FotMob
        for mid, m in fm_matches.items():
            if club not in (m["home"], m["away"]): continue
            cand, sc = _match_name(e, list(m["players"].values()), lambda p: p.get("name") or "")
            if cand:
                st = cand["stats"]
                sub = next((ev_ for ev_ in m["events"] if ev_.get("type") == "Substitution" and cand.get("name") in (ev_.get("swap") or [])), None)
                shots = [sh for sh in m["shots"] if str(sh.get("playerId")) == str(cand.get("id"))]
                row["fotmob"] = {"player_id": cand.get("id"), "name": cand.get("name"), "match_score": sc, "min": st.get("Minutes played"), "shots": st.get("Total shots"), "sot": st.get("Shots on target"),
                                 "xG": st.get("Expected goals (xG)"), "xGOT": st.get("Expected goals on target (xGOT)"), "xA": st.get("Expected assists (xA)"), "npxG": st.get("xG Non-penalty"),
                                 "chances_created": st.get("Chances created"), "big_chances_created": st.get("Big chances created"), "touches": st.get("Touches"), "touches_opp_box": st.get("Touches in opposition box"),
                                 "tackles": st.get("Tackles"), "interceptions": st.get("Interceptions"), "clearances": st.get("Clearances"), "blocks": st.get("Blocks"), "recoveries": st.get("Recoveries"),
                                 "aerials_won": st.get("Aerial duels won"), "crosses_acc": st.get("Accurate crosses"), "dribbles": st.get("Successful dribbles"), "passes_final_third": st.get("Passes into final third"),
                                 "distance_m": st.get("Distance covered"), "fantasy_points": st.get("Fantasy points"),
                                 "sub_event": sub and {"min": sub.get("time"), "swap": sub.get("swap"), "injured": sub.get("injuredPlayerOut")},
                                 "shot_list": [{"min": sh.get("min"), "result": sh.get("eventType"), "xG": round(float(sh.get("expectedGoals") or 0), 3), "xGOT": round(float(sh.get("expectedGoalsOnTarget") or 0), 3), "situation": sh.get("situation"), "body": sh.get("shotType"), "x": sh.get("x"), "y": sh.get("y")} for sh in shots]}
                row["referee"] = m["referee"]
            else:
                row["fotmob"] = {"unmatched": True}
        # consistency
        mins = {"fpl": row["fpl"]["minutes"], "understat": row.get("understat", {}).get("min"), "fotmob": row.get("fotmob", {}).get("min")}
        xg = {"fpl": row["fpl"]["expected_goals"], "understat": row.get("understat", {}).get("xG"), "fotmob(opta)": row.get("fotmob", {}).get("xG")}
        row["consistency"] = {"minutes": mins, "xG": xg, "fpl_points_vs_fotmob_fantasy": [row["fpl"]["total_points"], row.get("fotmob", {}).get("fantasy_points")]}
        present = [v for v in mins.values() if v is not None]
        if len(set(present)) > 1: cons["minutes"].append((row["name"], mins))
        xs = [float(v) for v in xg.values() if v not in (None, "")]
        if len(xs) >= 2 and max(xs) - min(xs) > 0.25: cons["xg"].append((row["name"], xg))
        fp = row["consistency"]["fpl_points_vs_fotmob_fantasy"]
        if fp[1] is not None and fp[0] != fp[1]: cons["points"].append((row["name"], fp))
        rows.append(row)
    # ----- team-level (free from the same calls)
    team_level = {}
    for club, um in us_matches.items():
        team_level.setdefault(club, {})["understat"] = {"match_id": um["id"], "home": um["side"] == "h", "opp": um["opp"], "goals": um["goals"], "xG": um["xG"]}
    for mid, m in fm_matches.items():
        for club in (m["home"], m["away"]):
            if club in clubs:
                tl = team_level.setdefault(club, {})
                tl["fotmob"] = {"match_id": mid, "referee": m["referee"], "referee_stats": m["referee_stats"], "stats": [{"title": st.get("title"), "stats": st.get("stats")} for grp in m["stats"] for st in (grp.get("stats") or []) if any(k in (st.get("title") or "") for k in ("Expected goals", "xG", "Ball possession", "Total shots", "Corners", "Big chances", "Offsides", "Crosses", "Fouls", "Yellow", "Red"))]}
    # ----- coverage C1–C19
    n_us = sum(1 for r in rows if r.get("understat") and not r["understat"].get("unmatched")); n_fm = sum(1 for r in rows if r.get("fotmob") and not r["fotmob"].get("unmatched"))
    n = len(rows)
    def st_(k, ok_cond, partial_cond, src_, note):
        cov[k] = {"status": "OK" if ok_cond else ("PARTIAL" if partial_cond else "MISSING"), "source": src_, "note": note}
    st_("C1", True, True, "event/N/live minutes", "official FPL minutes")
    st_("C2", n_us == n and n_fm == n, n_us + n_fm > 0, f"Understat ({n_us}/{n}) + FotMob/Opta ({n_fm}/{n})", "SofaScore minutes are browser-only")
    st_("C3", n_fm == n, n_fm > 0, "FotMob events (sub minute, injuredPlayerOut flag)", "the REASON (tactical/game state) is a MID-cadence report item")
    st_("C4", True, True, "live minutes/starts + bootstrap status/news", "why-absent text = FPL news; empty news → check reports")
    st_("C5", False, True, "derived across GWs", "needs a per-club regular-starter baseline — not yet computed")
    st_("C6", True, True, "event/N/live total_points", "")
    st_("C7", True, True, "event/N/live", "")
    st_("C8", True, True, "event/N/live bonus + bps", "final after data_checked")
    st_("C9", True, True, "event/N/live defensive_contribution, CBI, recoveries, tackles", "")
    st_("C10", n_fm == n, n_fm > 0, "FPL saves; goals prevented needs xGOT faced (FotMob/SofaScore GK stats)", "GK-only")
    st_("C11", n_us == n and n_fm == n, True, "FPL own xG/xA/xGI + Understat + FotMob(Opta)", "three models; FotMob and SofaScore share the Opta feed — count them as ONE provider")
    st_("C12", n_fm == n, n_fm > 0, "FotMob total/on-target shots, big chances; Understat shots", "")
    st_("C13", False, n_us + n_fm > 0, "key passes/chances created (Understat, FotMob); xGChain/xGBuildup (Understat); passes into final third, touches in box (FotMob)", "xT, SCA, GCA, deep completions, zone-14: FBref only — Cloudflare-blocked, attended")
    st_("C14", True, True, "event/N/live cards", "")
    st_("C15", n_us == n, n_us + n_fm > 0, "Understat shot list (X, Y, xG, result, situation, body, last action) + FotMob shotmap (xGOT)", "")
    st_("C16", False, False, "SofaScore /event/{id}/player/{pid}/heatmap — browser only", "not scriptable; attended POST step or device-bound task")
    st_("C17", True, True, "fixtures/?event=N (opponent, venue)", "archetype comes from the team profile (F5)")
    st_("C18", n_fm == n, n_fm > 0, "FotMob tackles/interceptions/clearances/blocks/aerials/recoveries", "")
    st_("C19", False, n_fm > 0, "FotMob accurate crosses, dribbles, passes into final third", "through balls, progressive carries, offsides per player: SofaScore (browser) or FBref (blocked)")
    hold = [{"param": k, "status": c["status"], "source": c["source"], "needs": c["note"] or "confirm", "options": ["provide a source URL", "paste the data manually", "skip this GW (output is labelled with the gap)", "abort"]} for k, c in cov.items() if not c["status"].startswith("OK")]
    for r in rows:
        if r.get("understat", {}).get("unmatched") or r.get("fotmob", {}).get("unmatched"):
            hold.append({"param": f"NAME-MATCH {r['name']}", "status": "UNMATCHED", "source": "provider roster", "needs": "confirm the provider's spelling of this player and add to the crosswalk", "options": ["paste the name", "skip", "abort"]})
    snap = {"generated_utc": now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"), "mode": "offline" if src.offline else "live", "cadence": "POST", "gw": L,
            "readiness": {"verdict": "HOLD" if hold else "GO", "gate_items": hold, "rule": "POST facts feed Form/Minutes; anything not OK needs a human decision before the next PRE run uses it"},
            "sources_ok": {"understat_clubs": f"{us_ok}/{len(clubs)}", "fotmob_matches": f"{fm_ok}/{len(fm_ids)}"},
            "players": rows, "team_level": team_level, "consistency_flags": cons, "coverage": cov,
            # every player's official line for this GW — the raw material for the D-group percentiles (season store)
            "all_players_live": {str(pid): {k: st.get(k) for k in ["minutes", "total_points", "bps", "bonus", "goals_scored", "assists", "clean_sheets", "goals_conceded", "saves", "defensive_contribution",
                                                                     "clearances_blocks_interceptions", "recoveries", "tackles", "expected_goals", "expected_assists", "expected_goal_involvements", "expected_goals_conceded", "starts"]}
                                 for pid, st in ((e_["id"], e_["stats"]) for e_ in live["elements"])},
            "fetch_log": [{"url": u, "status": s_, "bytes": b, "ms": ms} for (u, s_, b, ms) in src.log]}
    return snap, None


def brief_post(s):
    L = []
    L.append(f"# POST snapshot — GW{s['gw']} (generated {s['generated_utc']}, {s['mode']})\n")
    R = s["readiness"]
    L.append(f"## ⛔ GATE: {R['verdict']} — {len(R['gate_items'])} item(s)\n")
    L.append("| # | Param | Status | What is needed |\n|---|---|---|---|")
    for i, g in enumerate(R["gate_items"], 1): L.append(f"| {i} | {g['param']} | {g['status']} | {g['needs']} |")
    L.append(f"\nSources: Understat clubs {s['sources_ok']['understat_clubs']}, FotMob matches {s['sources_ok']['fotmob_matches']}.\n")
    L.append("## Tracked players — per-match facts (owned first, then pool)\n")
    L.append("| Player | Opp | Min FPL/US/FM | Pts | G/A | xG FPL / US / Opta | xA US / Opta | Shots (SoT) | KP | DefCon (CBI+R+T) | BPS/Bonus | Sub | Ref |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(s["players"], key=lambda r: (not r.get("owned", True), r.get("pos"))):
        f = r["fpl"]; u = r.get("understat", {}); m = r.get("fotmob", {})
        sub = m.get("sub_event"); subtxt = f"off {sub['min']}'" + (" (inj)" if sub and sub.get("injured") else "") if sub else ("90" if (f.get("minutes") or 0) >= 90 else (f"{f.get('minutes')}'" if f.get("minutes") else "DNP"))
        L.append(f"| {r['name']} ({r['club']}){'' if r.get('owned', True) else ' [pool]'} | {'v' if r['home'] else '@'} {r['opp']} | {f.get('minutes')}/{u.get('min','—')}/{m.get('min','—')} | {f.get('total_points')} | {f.get('goals_scored')}/{f.get('assists')} | "
                 f"{f.get('expected_goals')} / {u.get('xG','—')} / {m.get('xG','—')} | {u.get('xA','—')} / {m.get('xA','—')} | {m.get('shots','—')} ({m.get('sot','—')}) | {u.get('key_passes', m.get('chances_created','—'))} | "
                 f"{f.get('defensive_contribution')} ({f.get('clearances_blocks_interceptions')}+{f.get('recoveries')}+{f.get('tackles')}) | {f.get('bps')}/{f.get('bonus')} | {subtxt} | {r.get('referee','—')} |")
    c = s["consistency_flags"]
    L.append("\n## Consistency flags\n")
    L.append(f"- Minutes disagree: {c['minutes'] or 'none'}")
    L.append(f"- xG models differ by >0.25: {c['xg'] or 'none'}")
    L.append(f"- FPL points vs FotMob fantasy points: {c['points'] or 'all equal'}")
    L.append("\n## Team level\n")
    for club, t in s["team_level"].items():
        u = t.get("understat", {}); fm = t.get("fotmob", {})
        xg = [x for x in fm.get("stats", []) if x["title"] in ("Expected goals (xG)", "xG open play", "xG set play", "xG non-penalty")]
        L.append(f"- {club}: Understat xG {u.get('xG')} goals {u.get('goals')} ({'H' if u.get('home') else 'A'} v {u.get('opp')}); FotMob ref {fm.get('referee')}; " + "; ".join(f"{x['title']} {x['stats']}" for x in xg[:4]))
    L.append("\n## Coverage C1–C19\n")
    L.append("| # | Status | Source | Note |\n|---|---|---|---|")
    for k in [f"C{i}" for i in range(1, 20)]:
        cc = s["coverage"].get(k, {}); L.append(f"| {k} | {cc.get('status')} | {cc.get('source')} | {cc.get('note')} |")
    return "\n".join(L) + "\n"


# ----------------------------------------------------------------------------- main build
def build(src, force=False, window_h=30.0):
    cov = {}   # A1..A11 -> {"status": OK|PARTIAL|DERIVED|MISSING, "source": ..., "note": ...}
    warn = []
    bs = src.bootstrap()
    if not bs:
        sys.exit("bootstrap-static unreachable — nothing else is resolvable without it")

    events = bs["events"]
    cur = next((e for e in events if e["is_current"]), None)
    nxt = next((e for e in events if e["is_next"]), None)
    if nxt is None:  # season over or between-season
        nxt = cur
    N = nxt["id"]
    deadline = parse_ts(nxt["deadline_time"])
    hours_to_deadline = (deadline - now_utc()).total_seconds() / 3600
    in_window = 0 <= hours_to_deadline <= window_h
    if not in_window and not force and not src.offline:
        print(f"GW{N} deadline {nxt['deadline_time']} is {hours_to_deadline:.1f} h away — outside the {window_h} h PRE window. Exiting (use --force).")
        return None

    el = {e["id"]: e for e in bs["elements"]}
    teams = {t["id"]: t["short_name"] for t in bs["teams"]}
    pos = {t["id"]: t["singular_name_short"] for t in bs["element_types"]}

    entry = src.entry()
    hist = src.history()
    last_gw = cur["id"] if cur else max(1, N - 1)
    picks = src.picks(last_gw)
    transfers = src.transfers()
    fx_next = src.fixtures(N)
    live_cur = src.live(last_gw) if cur else None
    esum = {p["element"]: src.element_summary(p["element"]) for p in (picks or {}).get("picks", [])}

    # purchase price: latest transfer-in cost if the player was bought in-season, else his GW1 price (initial squad)
    sell_fee = float(bs.get("game_settings", {}).get("transfers_sell_on_fee", 0.5))
    max_ft = int(bs.get("game_settings", {}).get("max_extra_free_transfers", 4)) + 1
    started = (entry or {}).get("started_event", 1)
    bought_at = {}
    for tr in sorted(transfers or [], key=lambda t: (t["event"], t["time"])):
        bought_at[tr["element_in"]] = tr["element_in_cost"]          # later transfers overwrite earlier ones
    def purchase_price(eid):
        if eid in bought_at:
            return bought_at[eid], "transfers endpoint"
        es = esum.get(eid)
        if es and es.get("history"):
            first = min(es["history"], key=lambda h: h["round"])
            if first["round"] <= started:
                return first["value"], f"element-summary GW{first['round']} price"
            return first["value"], f"element-summary GW{first['round']} price (first appearance after your start — check)"
        return None, "unknown"
    def selling_price(purchase, now):
        if purchase is None:
            return None
        if now <= purchase:
            return now                                                  # no profit: sell at current price
        return purchase + int((now - purchase) * sell_fee)             # half the profit, rounded down (tenths)

    # -------- A1 owned 15 (+ buying pool rows built the same way)
    owned = []
    def player_row(e, p, esum_entry, pp, pp_src, sp):
            es = esum_entry or {}
            return {
                "id": e["id"], "name": e["web_name"], "team": teams.get(e["team"]), "pos": pos.get(e["element_type"]),
                "slot": p["position"], "multiplier": p["multiplier"], "captain": p["is_captain"], "vice": p["is_vice_captain"],
                "now_cost": e["now_cost"] / 10,
                "purchase_price": pp / 10 if pp is not None else None, "purchase_source": pp_src,
                "selling_price": sp / 10 if sp is not None else None,
                "history": [{"gw": h["round"], "opp": teams.get(h["opponent_team"]), "home": h["was_home"], "min": h["minutes"], "pts": h["total_points"],
                             "bps": h["bps"], "bonus": h["bonus"], "xgi": h["expected_goal_involvements"], "defcon": h["defensive_contribution"],
                             "value": h["value"] / 10, "net_transfers": h["transfers_balance"]} for h in es.get("history", [])],
                "upcoming": [{"gw": f["event"], "opp": teams.get(f["team_a"] if f["is_home"] else f["team_h"]), "home": f["is_home"], "fdr": f["difficulty"]} for f in es.get("fixtures", [])[:6]],
                "status": e["status"], "chance_next": e.get("chance_of_playing_next_round"), "news": e.get("news") or "",
                "news_added": e.get("news_added"),
                "selected_by": float(e["selected_by_percent"]),
                "price_change_percent": float(e["price_change_percent"]) if e.get("price_change_percent") not in (None, "") else None,
                "price_change_hourly": e.get("price_change_hourly_rate"),
                "price_projections": e.get("price_change_projections"),
                "price_locked_until": e.get("price_change_locked_until"),
                "transfers_in_event": e.get("transfers_in_event"), "transfers_out_event": e.get("transfers_out_event"),
                "net_transfers_event": (e.get("transfers_in_event") or 0) - (e.get("transfers_out_event") or 0),
                "form": e.get("form"), "total_points": e.get("total_points"), "event_points": e.get("event_points"),
                "scout_risks": e.get("scout_risks"),
                "set_pieces": {"corners": e.get("corners_and_indirect_freekicks_order"), "dfk": e.get("direct_freekicks_order"), "pens": e.get("penalties_order")},
                "yellow_cards": e.get("yellow_cards"),
            }
    if picks and picks.get("picks"):
        for p in picks["picks"]:
            e = el.get(p["element"])
            if not e:
                warn.append(f"A1: element {p['element']} in picks but not in bootstrap (trimmed offline file?)")
                continue
            pp, pp_src = purchase_price(p["element"])
            sp = selling_price(pp, e["now_cost"])
            owned.append(player_row(e, p, esum.get(p["element"]), pp, pp_src, sp))
        fh_played = any(c["name"] == "freehit" for c in (hist or {}).get("chips", []))
        cov["A1"] = {"status": "DERIVED", "source": f"entry/{ENTRY_ID}/event/{last_gw}/picks + bootstrap + element-summary (GW1 price) + transfers (element_in_cost) + sell-on rule {sell_fee}",
                     "note": ("purchase/selling prices derived from public data; exact for an initial-squad player or an in-season buy" +
                              (" — A FREE HIT WAS PLAYED: players re-bought after it may carry the wrong purchase price, verify on the site" if fh_played else ""))}
    else:
        cov["A1"] = {"status": "MISSING", "source": "picks", "note": "picks endpoint failed (404 until the first deadline of the season passes)"}

    # -------- A2 bank, FTs, chips
    eh = (picks or {}).get("entry_history", {})
    bank = eh.get("bank")
    chips_used = (hist or {}).get("chips", [])
    if True:
        # Derive FTs from history: 1 per GW, rolling, banked to max_ft (game_settings.max_extra_free_transfers + 1).
        ft = 1
        rows = sorted((hist or {}).get("current", []), key=lambda r: r["event"])
        chip_gw = {c["event"]: c["name"] for c in chips_used}
        for r in rows:
            if r["event"] == 1:
                ft = 1  # after GW1 deadline you hold 1 FT for GW2
                continue
            if chip_gw.get(r["event"]) in ("wildcard", "freehit"):
                ft = min(ft + 1, max_ft)   # transfers made on a WC/FH week do not consume the banked FT
                continue
            used = r["event_transfers"]
            paid = r["event_transfers_cost"] // 4
            ft = max(0, ft - (used - paid))
            ft = min(ft + 1, max_ft)       # +1 for the coming GW, banked to the cap
        used_names = {(c["name"], c["event"]) for c in chips_used}
        chips_state = []
        for c in bs.get("chips", []):
            in_half = c["start_event"] <= N <= c["stop_event"]
            used_ev = next((ev for (nm, ev) in used_names if nm == c["name"] and c["start_event"] <= ev <= c["stop_event"]), None)
            chips_state.append({"chip": c["name"], "window": f"GW{c['start_event']}-{c['stop_event']}", "current_half": in_half,
                                "status": f"used GW{used_ev}" if used_ev else ("available" if in_half or N < c["start_event"] else "expired")})
        a2 = {"bank": bank / 10 if bank is not None else None, "free_transfers": ft, "free_transfers_label": "DERIVED", "ft_cap": max_ft,
              "chips": chips_state}
        cov["A2"] = {"status": "DERIVED", "source": "picks.entry_history.bank + entry/history (transfers, chips used) + bootstrap.chips + game_settings",
                     "note": "free-transfer count is not in any public endpoint; derived with the 1/GW roll rule. Chips = bootstrap chip windows minus history.chips"}

    # -------- A3 prices + predictor (FPL native since 2026/27)
    has_pc = any(o.get("price_change_percent") is not None for o in owned)
    cov["A3"] = {"status": "OK" if has_pc else "PARTIAL", "source": "bootstrap elements.now_cost + price_change_percent/projections",
                 "note": "FPL now publishes its own price-change progress and 3-night projection; LiveFPL /prices re-renders the same numbers" if has_pc else "price_change_* fields absent"}

    # -------- A4/A5/A6 EO and captaincy by cohort (LiveFPL .us)
    top10k = src.lf("top10k.json")
    elite = src.lf("elite.json")
    locals_ = src.lf(f"locals_{last_gw}.json", gw=last_gw)
    games = src.lf("api/games.json")
    players_lf = src.lf("players.json")

    games_by_id = {}
    if games:
        for m in games:
            for i in range(12, len(m)):
                if isinstance(m[i], list):
                    for p in m[i]:
                        if isinstance(p, list) and len(p) >= 5 and isinstance(p[4 if len(p) == 5 else 5], int):
                            pid = p[4] if len(p) == 5 else p[5]
                            games_by_id[pid] = {"eo_idx1": p[1], "eo_idx2": p[2], "pts": p[3]}

    band_by_name = {}
    if locals_:
        for b in locals_.get("locals", []):
            band_by_name[b["name"]] = b

    def band_for_rank(rank):
        if rank is None:
            return None
        edges = [(100, "Top 100"), (1000, "Top 1K"), (10000, "Top 10K"), (100000, "Top 100K"), (200000, "100K-200K"),
                 (300000, "200K-300K"), (400000, "300K-400K"), (500000, "400K-500K"), (600000, "500K-600K"), (700000, "600K-700K"),
                 (800000, "700K-800K"), (900000, "800K-900K"), (1000000, "900K-1M"), (1500000, "1M-1.5M"), (2000000, "1.5M-2M"),
                 (3000000, "2M-3M"), (6000000, "3M-6M")]
        for lim, name in edges:
            if rank <= lim:
                return name
        return "Overall"

    overall_rank = eh.get("overall_rank") or (entry or {}).get("summary_overall_rank")
    my_band = band_for_rank(overall_rank)
    cap_top10k = {c[0]: c[1] for c in band_by_name.get("Top 10K", {}).get("captains", [])}
    cap_myband = {c[0]: c[1] for c in band_by_name.get(my_band, {}).get("captains", [])} if my_band else {}
    cap_overall = {c[0]: c[1] for c in band_by_name.get("Overall", {}).get("captains", [])}

    # -------- buying pool (Tier 2 candidates): manual list + automatic rules, same fields as the owned rows
    pool_ids, pool_reasons = load_pool(bs, top10k, os.path.dirname(os.path.abspath(src.prev_dir or "snapshots")), [o["id"] for o in owned])
    pool = []
    for i in pool_ids:
        e = el.get(i)
        if not e: continue
        if not src.offline:
            esum[i] = src.element_summary(i)
        r = player_row(e, {"position": None, "multiplier": None, "is_captain": False, "is_vice_captain": False}, esum.get(i), None, "pool", None)
        r["pool_reason"] = pool_reasons.get(i, [])
        pool.append(r)

    consistency = {}
    diffs = []
    for o in owned + pool:
        i = o["id"]
        o["eo_top10k"] = pct(top10k.get(str(i), 0) * 100, 2) if top10k else None
        o["eo_elite_json"] = pct(elite.get(str(i), 0) * 100, 2) if elite else None
        g = games_by_id.get(i)
        o["eo_games_idx1"] = g["eo_idx1"] if g else None
        o["eo_games_idx2_UNVERIFIED"] = g["eo_idx2"] if g else None
        o["cap_top10k"] = pct(cap_top10k.get(i, 0) * 100, 2) if cap_top10k else None
        o["cap_myband"] = pct(cap_myband.get(i, 0) * 100, 2) if cap_myband else None
        o["cap_overall"] = pct(cap_overall.get(i, 0) * 100, 2) if cap_overall else None
        if g and top10k and str(i) in top10k:
            diffs.append(abs(g["eo_idx1"] - top10k[str(i)] * 100))
    if diffs:
        consistency["top10k_json_vs_games_idx1_max_abs_pp"] = round(max(diffs), 2)
    # elite.json staleness heuristic: if elite EO of the most-owned players sits far from top10k for several owned players, suspect stale
    if top10k and elite:
        # compare on the 10 most-owned players in the top-10k cohort: a fresh elite.json tracks them within ~20 pp
        top_ids = sorted(top10k, key=lambda k: -top10k[k])[:10]
        gaps = {(players_lf or {}).get(k, k): round((elite.get(k, 0) - top10k[k]) * 100, 1) for k in top_ids}
        consistency["elite_json_minus_top10k_pp_top10_players"] = gaps
        if max(abs(v) for v in gaps.values()) > 30:
            warn.append("elite.json differs from top10k.json by >30 pp on a top-10-EO player — elite.json is probably STALE (previous GW). Do not use without a freshness check.")

    cov["A4"] = {"status": "PARTIAL" if top10k else "MISSING", "source": "livefpl.us top10k.json (+ locals bands, + FPL selected_by_percent)",
                 "note": "top10k cohort OK and cross-checked vs games.json idx1; OVERALL-cohort EO has no verified source: livefpl.net /EO Overall column renders 0% (GW1 and GW2), games.json idx2 does not match any displayed cohort. FPL selected_by_percent is raw ownership, not EO."}
    cov["A5"] = {"status": "OK" if locals_ else "MISSING", "source": f"livefpl.us locals_{last_gw}.json captains per band",
                 "note": f"bands available: Top100…3M-6M, Top 1M, Elite, Overall. User band = {my_band}. locals_{N}.json for the coming GW appears only after its deadline."}
    cov["A6"] = {"status": "PARTIAL" if top10k else "MISSING", "source": "top10k.json (= /EO Top10k column exactly)", "note": "same Overall-cohort gap as A4"}

    # -------- A7 transfer flow
    cov["A7"] = {"status": "OK", "source": "bootstrap elements.transfers_in_event / transfers_out_event (all 650 players)",
                 "note": "pair-level flow (who → who) is only on livefpl.net /prices Trends tab (browser only)"}
    movers = sorted(bs["elements"], key=lambda e: (e.get("transfers_in_event") or 0) - (e.get("transfers_out_event") or 0))
    flow = {"top_in": [(e["web_name"], teams.get(e["team"]), e["transfers_in_event"] - e["transfers_out_event"]) for e in movers[-8:][::-1]],
            "top_out": [(e["web_name"], teams.get(e["team"]), e["transfers_in_event"] - e["transfers_out_event"]) for e in movers[:8]]}

    # -------- A8 Safety Score / Template Rating
    cov["A8"] = {"status": "MISSING", "source": "livefpl.net (rendered app only)",
                 "note": "Safety Score and Template Rating are computed client-side on livefpl.net/<team-id>; no JSON endpoint found. Browser step only. locals_N band means allow a rough Safety-Score interpolation (see live-rank.md)."}

    # -------- A9 ranks/points
    a9 = {"overall_rank": overall_rank, "total_points": eh.get("total_points"), "gw_points": eh.get("points"), "gw_rank": eh.get("rank"),
          "percentile": eh.get("percentile_rank"), "team_value": (eh.get("value") or 0) / 10, "bank": (bank or 0) / 10,
          "note": "official; final only if A10 flags both true for the last GW"}
    cov["A9"] = {"status": "OK", "source": "picks.entry_history / entry / history", "note": "lags live during a GW — see live-rank.md"}

    # -------- A10 finished/data_checked
    a10 = {"last_gw": last_gw, "finished": cur["finished"] if cur else None, "data_checked": cur["data_checked"] if cur else None,
           "next_gw": N, "deadline_utc": nxt["deadline_time"], "hours_to_deadline": round(hours_to_deadline, 1),
           "fixtures_next": [{"id": f["id"], "kickoff": f["kickoff_time"], "home": teams.get(f["team_h"]), "away": teams.get(f["team_a"]),
                              "fdr_h": f["team_h_difficulty"], "fdr_a": f["team_a_difficulty"], "finished": f["finished"], "started": f.get("started")} for f in (fx_next or [])]}
    cov["A10"] = {"status": "OK", "source": "bootstrap events + fixtures/?event=N", "note": ""}

    # -------- A11 bonus projection (LIVE cadence; at PRE we record last GW's final BPS as a sanity check)
    if live_cur:
        le = {e["id"]: e["stats"] for e in live_cur["elements"]}
        for o in owned:
            s = le.get(o["id"])
            o["last_gw"] = {"pts": s["total_points"], "min": s["minutes"], "bps": s["bps"], "bonus": s["bonus"]} if s else None
        cov["A11"] = {"status": "OK (POST)", "source": f"event/{last_gw}/live bps+bonus", "note": "live top-3 BPS projection is a LIVE-cadence job; games.json idx 11 carries LiveFPL's provisional bonus during matches"}
    else:
        cov["A11"] = {"status": "MISSING", "source": "event/N/live", "note": "unreachable"}

    prev = None
    try:
        with open(os.path.join(src.prev_dir or "snapshots", "latest.json")) as f: prev = json.load(f)
    except Exception:
        pass
    B = build_schedule(src, bs, N, teams, cov, warn, prev)

    # -------- readiness gate: every parameter is GO only if fully fetched for THIS gameweek; everything else needs a human decision
    gen = now_utc()
    hold = []
    for k, c in cov.items():
        st = c["status"]
        if st.startswith("OK"):
            continue
        need = {"A1": "log in to FPL in the browser pane and read my-team/, or confirm the derived prices against the Transfers page",
                "A2": "confirm free transfers and chips on the FPL site (derived from history)",
                "A4": "overall-cohort EO: no source — skip, or paste a figure from LiveFPL /EO if the Overall column is populated this week",
                "A6": "overall-cohort EO: same as A4",
                "A8": "read Safety Score and Template Rating from livefpl.net/6048651 in the browser pane, or paste them",
                "B5": "cup/European fixtures: ESPN blocked — paste the owned clubs' midweek fixtures, or supply another source URL",
                "B7": "player call-ups for the next break: paste, or skip until the break is within 10 days",
                "B9": "referee appointments: read premierleague.com 'Match officials for Matchweek N' (check the season!) or skip",
                "B10": "weather: kick-offs are beyond the 7-day forecast horizon — re-run closer, or skip"}.get(k, c.get("note", ""))
        hold.append({"param": k, "status": st, "source": c.get("source"), "needs": need,
                     "options": ["provide a source URL", "paste the data manually", "skip this GW (output is labelled with the gap)", "abort"]})
    # freshness: cohort data (A4–A6) is always the last finished GW; snapshot must be inside the PRE window
    freshness = {"snapshot_generated_utc": gen.strftime("%Y-%m-%dT%H:%M:%SZ"), "hours_to_deadline": round(hours_to_deadline, 1),
                 "cohort_data_gw": last_gw, "cohort_note": f"EO/captaincy figures are GW{last_gw} actuals used as the GW{N} baseline — confirm or skip",
                 "in_pre_window": in_window}
    if not in_window and not src.offline:
        hold.append({"param": "FRESHNESS", "status": "STALE", "source": "snapshot timing", "needs": f"snapshot is {round(hours_to_deadline,1)} h from the deadline (outside the {window_h} h window) — re-run the pull",
                     "options": ["re-run the pull", "proceed with this snapshot (labelled STALE)", "abort"]})
    hold.append({"param": "A4-A6 baseline", "status": f"GW{last_gw} actuals", "source": "livefpl.us", "needs": freshness["cohort_note"],
                 "options": ["use as baseline", "skip cohort-dependent outputs", "abort"]})
    readiness = {"verdict": "HOLD" if hold else "GO", "gate_items": hold, "freshness": freshness,
                 "rule": "The selection model must not run while verdict is HOLD. Each gate item needs an explicit human choice; PARTIAL and DERIVED are not silently accepted."}

    snap = {
        "generated_utc": now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"), "mode": "offline" if src.offline else "live",
        "readiness": readiness,
        "B_schedule": B,
        "gw_next": N, "gw_last": last_gw, "in_pre_window": in_window,
        "A1_owned": owned, "pool": pool, "A2_bank_ft_chips": a2, "A7_flow": flow, "A9_rank": a9, "A10_flags": a10,
        "coverage": cov, "consistency": consistency, "warnings": warn,
        "fetch_log": [{"url": u, "status": s, "bytes": b, "ms": ms} for (u, s, b, ms) in src.log],
        "transfers_made": transfers or [],
    }
    return snap


# ----------------------------------------------------------------------------- markdown brief
def brief(s):
    L = []
    L.append(f"# PRE snapshot — GW{s['gw_next']} (generated {s['generated_utc']}, {s['mode']})\n")
    R = s.get("readiness") or {}
    if R:
        L.append(f"## ⛔ GATE: {R['verdict']} — {len(R['gate_items'])} item(s) need a decision before the model runs\n")
        L.append(R["rule"] + "\n")
        L.append("| # | Param | Status | What is needed | Options |\n|---|---|---|---|---|")
        for i, g in enumerate(R["gate_items"], 1):
            L.append(f"| {i} | {g['param']} | {g['status']} | {g['needs']} | {' / '.join(g['options'])} |")
        fr = R["freshness"]
        L.append(f"\nFreshness: snapshot {fr['snapshot_generated_utc']}, {fr['hours_to_deadline']} h to deadline, in PRE window = {fr['in_pre_window']}; cohort data = GW{fr['cohort_data_gw']}.\n")
    a10 = s["A10_flags"]
    L.append(f"Deadline **{a10['deadline_utc']}** — {a10['hours_to_deadline']} h away. Last GW{a10['last_gw']}: finished={a10['finished']}, data_checked={a10['data_checked']}.")
    a9 = s["A9_rank"]; a2 = s["A2_bank_ft_chips"]
    L.append(f"Overall rank **{a9['overall_rank']:,}**, total {a9['total_points']}, last GW {a9['gw_points']} (GW rank {a9['gw_rank']:,}). Team value {a9['team_value']}m, bank {a9['bank']}m, free transfers **{a2.get('free_transfers')}** (DERIVED, cap {a2.get('ft_cap')}). Chips this half: " + ", ".join(f"{c['chip']} {c['status']}" for c in a2.get('chips', []) if c['current_half']) + "\n")
    L.append("## Owned 15\n")
    L.append("| # | Player | Pos | £ | Bought | Sell |Status | Price Δ% (proj tonight) | Net tr. | Own% | EO top10k | C% top10k | C% my band | Last GW |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for o in s["A1_owned"]:
        proj = (o.get("price_projections") or [{}])[0].get("projected_percent")
        role = " (C)" if o["captain"] else (" (V)" if o["vice"] else "")
        lg = o.get("last_gw") or {}
        st = o["status"] + (f" {o['chance_next']}%" if o.get("chance_next") not in (None, 100) else "") + (f" — {o['news']}" if o["news"] else "")
        L.append(f"| {o['slot']} | {o['name']}{role} | {o['pos']} {o['team']} | {o['now_cost']} | {o.get('purchase_price') if o.get('purchase_price') is not None else '—'} | {o.get('selling_price') if o.get('selling_price') is not None else '—'} | {st} | "
                 f"{o.get('price_change_percent')} ({proj}) | {o.get('net_transfers_event'):+,} | {o['selected_by']} | {o.get('eo_top10k')} | {o.get('cap_top10k')} | {o.get('cap_myband')} | "
                 f"{lg.get('pts','—')} pts / {lg.get('min','—')}' / bps {lg.get('bps','—')} |")
    if s.get("pool"):
        L.append(f"\n## Buying pool ({len(s['pool'])} players — watchlist + top transfers-in + top form per position + top-10k EO ≥ threshold; edit pool.json)\n")
        L.append("| Player | Pos | £ | Status | Price Δ% (proj) | Net tr. | Own% | EO top10k | Form | Pts | Why in pool | Next 3 |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for o in sorted(s["pool"], key=lambda x: (x["pos"], -float(x.get("form") or 0))):
            proj = (o.get("price_projections") or [{}])[0].get("projected_percent")
            st = o["status"] + (f" {o['chance_next']}%" if o.get("chance_next") not in (None, 100) else "") + (f" — {o['news'][:40]}" if o["news"] else "")
            nxt = ", ".join(f"{'v' if u['home'] else '@'}{u['opp']}({u['fdr']})" for u in (o.get("upcoming") or [])[:3])
            L.append(f"| {o['name']} ({o['team']}) | {o['pos']} | {o['now_cost']} | {st} | {o.get('price_change_percent')} ({proj}) | {o.get('net_transfers_event'):+,} | {o['selected_by']} | {o.get('eo_top10k')} | {o.get('form')} | {o.get('total_points')} | {'; '.join(o.get('pool_reason', []))} | {nxt} |")
    L.append("\n## Market flow (net transfers this GW, all players)\n")
    L.append("In: " + ", ".join(f"{n} ({t}) {v:+,}" for n, t, v in s["A7_flow"]["top_in"]))
    L.append("Out: " + ", ".join(f"{n} ({t}) {v:+,}" for n, t, v in s["A7_flow"]["top_out"]))
    L.append("\n## Next fixtures\n")
    for f in a10["fixtures_next"]:
        L.append(f"- {f['kickoff']}  {f['home']} (FDR {f['fdr_h']}) v {f['away']} (FDR {f['fdr_a']})")
    B = s.get("B_schedule") or {}
    if B:
        owned_teams = sorted({o["team"] for o in s["A1_owned"]})
        L.append("\n## Schedule (group B)\n")
        L.append("Deadlines: " + ", ".join(f"GW{d['gw']} {d['deadline_utc']}" for d in B["deadlines"]))
        if B["breaks"]: L.append("Breaks: " + "; ".join(f"after GW{g['after_gw']} ({g['days']} d — {g['label']})" for g in B["breaks"]))
        dg = [(g, v) for g, v in B["dgw_bgw"].items() if v["double"] or v["blank"]]
        L.append("DGW/BGW next 6: " + ("; ".join(f"GW{g}: double {v['double']} blank {v['blank']}" for g, v in dg) if dg else "none"))
        if B["fdr_changes_since_last_snapshot"]: L.append(f"FDR revised on {len(B['fdr_changes_since_last_snapshot'])} fixtures since last snapshot: {B['fdr_changes_since_last_snapshot']}")
        L.append("\n| Team (owned) | Next 6 (H/A, FDR) | Cup/Europe in window | Rest before GW | Matches 7 d before |\n|---|---|---|---|---|")
        for t in owned_teams:
            n6 = ", ".join(f"GW{x['gw']} {'v' if x['home'] else '@'} {x['opp']} ({x['fdr']})" for x in B["fixtures_next6"].get(t, []))
            cups = "; ".join(f"{c['date'][:10]} {c['comp']} {'v' if c['home'] else '@'} {c['opp']}" for c in B["cup_fixtures"].get(t, [])) or "—"
            r = B["rest"].get(t, {})
            L.append(f"| {t} | {n6} | {cups} | {r.get('days_since_last')} d ({r.get('last_comp')}) | {r.get('matches_in_7d_before')} |")
        if B["weather"]:
            L.append("\nWeather at kick-off (Open-Meteo): " + "; ".join(f"{w['fixture']} {w['temp_c']}°C, rain {w['precip_prob']}%, wind {w['wind_kmh']} (gust {w['gust_kmh']}) km/h{' **' + w['flag'] + '**' if w['flag'] else ''}" for w in B["weather"]))
        if B["referee_season_stats"]:
            top = sorted(B["referee_season_stats"].items(), key=lambda kv: -kv[1]["matches"])[:6]
            L.append("Referees this season (football-data.co.uk, POST): " + "; ".join(f"{r} {d['matches']} m, {d['yellows_per_match']} Y/m, {d['reds']} R" for r, d in top))
            L.append("Appointments for this GW: not in any JSON source — check premierleague.com 'Match officials' (attended).")
    L.append("\n## Coverage A1–A11, B1–B10\n")
    L.append("| # | Status | Source | Note |\n|---|---|---|---|")
    for k in ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]:
        c = s["coverage"].get(k, {})
        L.append(f"| {k} | {c.get('status')} | {c.get('source')} | {c.get('note')} |")
    L.append("\n## Consistency\n")
    for k, v in s["consistency"].items():
        L.append(f"- {k}: {v}")
    for w in s["warnings"]:
        L.append(f"- ⚠️ {w}")
    L.append("\n## Fetch log\n")
    for f in s["fetch_log"]:
        L.append(f"- {f['status']} {f['bytes']}B {f['ms']}ms {f['url']}")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", help="directory of saved JSON (test mode)")
    ap.add_argument("--out", default="snapshots")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--window-hours", type=float, default=30.0)
    ap.add_argument("--mode", choices=["pre", "post"], default="pre", help="pre = deadline snapshot (groups A, B); post = last finished GW facts (group C)")
    ap.add_argument("--fill", help="JSON file of browser-fetched items {param: {status, source, fetched_utc, data}} to merge into the latest snapshot of --mode; recomputes the gate")
    a = ap.parse_args()
    if a.fill:
        name = "latest_post" if a.mode == "post" else "latest"
        path = os.path.join(a.out, name + ".json")
        snap = json.load(open(path)); fill = json.load(open(a.fill))
        for k, v in fill.items():
            snap["coverage"][k] = {"status": v.get("status", "OK [BROWSER-FILL]"), "source": v.get("source", "browser pane"), "note": f"filled {v.get('fetched_utc')}"}
            snap.setdefault("browser_fill", {})[k] = v
        R = snap["readiness"]; R["gate_items"] = [g for g in R["gate_items"] if g["param"] not in fill]
        R["verdict"] = "HOLD" if R["gate_items"] else "GO"
        json.dump(snap, open(path, "w"), indent=1, ensure_ascii=False)
        md = brief_post(snap) if a.mode == "post" else brief(snap)
        open(os.path.join(a.out, name + ".md"), "w").write(md)
        print(f"merged {len(fill)} item(s) into {path}; gate={R['verdict']} ({len(R['gate_items'])} open)")
        return
    src = Source(a.offline, prev_dir=a.out)
    if a.mode == "post":
        bs = src.bootstrap()
        if not bs: sys.exit("bootstrap-static unreachable")
        cur = next((e for e in bs["events"] if e["is_current"]), None)
        picks = src.picks(cur["id"]) if cur else None
        owned = [p["element"] for p in (picks or {}).get("picks", [])]
        top10k = src.lf("top10k.json")
        pool_ids, _ = load_pool(bs, top10k, os.path.dirname(os.path.abspath(a.out)), owned)
        snap, why = build_post(src, bs, owned, a.out, force=a.force, pool_ids=pool_ids)
        if snap is None:
            print(why); return
        os.makedirs(a.out, exist_ok=True)
        stem = os.path.join(a.out, f"GW{snap['gw']}_POST_{snap['generated_utc'].replace(':','').replace('-','')}")
        with open(stem + ".json", "w") as f: json.dump(snap, f, indent=1, ensure_ascii=False)
        with open(stem + ".md", "w") as f: f.write(brief_post(snap))
        for ext in (".json", ".md"):
            with open(os.path.join(a.out, "latest_post" + ext), "w") as f: f.write(open(stem + ext).read())
        print(f"wrote {stem}.json / .md  (coverage: " + ", ".join(f"{k}={v['status']}" for k, v in snap["coverage"].items()) + f") gate={snap['readiness']['verdict']}")
        return
    snap = build(src, force=a.force, window_h=a.window_hours)
    if snap is None:
        return
    os.makedirs(a.out, exist_ok=True)
    stem = os.path.join(a.out, f"GW{snap['gw_next']}_PRE_{snap['generated_utc'].replace(':','').replace('-','')}")
    with open(stem + ".json", "w") as f:
        json.dump(snap, f, indent=1, ensure_ascii=False)
    with open(stem + ".md", "w") as f:
        f.write(brief(snap))
    # stable "latest" pointers so a reader never has to list the directory
    for ext in (".json", ".md"):
        with open(os.path.join(a.out, "latest" + ext), "w") as f:
            f.write(open(stem + ext).read())
    print(f"wrote {stem}.json / .md  (coverage: " + ", ".join(f"{k}={v['status']}" for k, v in snap["coverage"].items()) + ")")
    if snap["warnings"]:
        print("warnings:\n  - " + "\n  - ".join(snap["warnings"]))


if __name__ == "__main__":
    main()
