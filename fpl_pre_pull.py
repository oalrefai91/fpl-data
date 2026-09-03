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
import argparse, json, os, sys, time, urllib.request, urllib.error
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
            with urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=30) as r:
                body = r.read()
                self.log.append((url, r.status, len(body), int((time.time() - t0) * 1000)))
                return json.loads(body)
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

    # -------- A1 owned 15
    owned = []
    if picks and picks.get("picks"):
        for p in picks["picks"]:
            e = el.get(p["element"])
            if not e:
                warn.append(f"A1: element {p['element']} in picks but not in bootstrap (trimmed offline file?)")
                continue
            pp, pp_src = purchase_price(p["element"])
            sp = selling_price(pp, e["now_cost"])
            es = esum.get(p["element"]) or {}
            owned.append({
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
            })
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

    consistency = {}
    diffs = []
    for o in owned:
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
        "A1_owned": owned, "A2_bank_ft_chips": a2, "A7_flow": flow, "A9_rank": a9, "A10_flags": a10,
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
    a = ap.parse_args()
    snap = build(Source(a.offline, prev_dir=a.out), force=a.force, window_h=a.window_hours)
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
