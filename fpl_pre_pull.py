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
    python3 fpl_pre_pull.py --cookie-file ~/.fpl_cookie   # optional: adds my-team/ (selling prices, FTs, chips)

The cookie file is a single line, the browser's `Cookie:` header for fantasy.premierleague.com. Create it
yourself from your own logged-in browser; the script never handles a password.
"""
import argparse, json, os, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone

ENTRY_ID = 6048651
FPL = "https://fantasy.premierleague.com/api/"
LFPL = "https://livefpl.us/"
UA = {"User-Agent": "Mozilla/5.0 (fpl-pre-pull; personal use)"}

# ----------------------------------------------------------------------------- fetch layer
class Source:
    def __init__(self, offline_dir=None, cookie=None):
        self.offline = offline_dir
        self.cookie = cookie
        self.log = []  # (url, status, bytes, ms)

    def _get(self, url, auth=False):
        t0 = time.time()
        hdr = dict(UA)
        if auth and self.cookie:
            hdr["Cookie"] = self.cookie
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
    def my_team(self):
        if self.offline or not self.cookie:
            return None
        return self._get(FPL + f"my-team/{ENTRY_ID}/", auth=True)
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
    my_team = src.my_team()

    # -------- A1 owned 15
    owned = []
    if picks and picks.get("picks"):
        mt_by_el = {p["element"]: p for p in (my_team or {}).get("picks", [])}
        for p in picks["picks"]:
            e = el.get(p["element"])
            if not e:
                warn.append(f"A1: element {p['element']} in picks but not in bootstrap (trimmed offline file?)")
                continue
            m = mt_by_el.get(p["element"], {})
            owned.append({
                "id": e["id"], "name": e["web_name"], "team": teams.get(e["team"]), "pos": pos.get(e["element_type"]),
                "slot": p["position"], "multiplier": p["multiplier"], "captain": p["is_captain"], "vice": p["is_vice_captain"],
                "now_cost": e["now_cost"] / 10,
                "purchase_price": (m.get("purchase_price") or 0) / 10 if m else None,
                "selling_price": (m.get("selling_price") or 0) / 10 if m else None,
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
        cov["A1"] = {"status": "OK" if my_team else "PARTIAL", "source": f"entry/{ENTRY_ID}/event/{last_gw}/picks + bootstrap",
                     "note": "purchase/selling price present (my-team auth)" if my_team else
                             "public picks endpoint has NO purchase_price/selling_price — needs authenticated my-team/ (cookie) or read from the FPL site"}
    else:
        cov["A1"] = {"status": "MISSING", "source": "picks", "note": "picks endpoint failed (404 until the first deadline of the season passes)"}

    # -------- A2 bank, FTs, chips
    eh = (picks or {}).get("entry_history", {})
    bank = eh.get("bank")
    chips_used = (hist or {}).get("chips", [])
    if my_team:
        ft = my_team.get("transfers", {})
        a2 = {"bank": ft.get("bank", bank) / 10 if ft.get("bank") is not None else None, "free_transfers": ft.get("limit"),
              "transfers_made_this_gw": ft.get("made"), "chips": my_team.get("chips")}
        cov["A2"] = {"status": "OK", "source": "my-team (auth)", "note": ""}
    else:
        # Derive FTs from history: 1 per GW, rolling, cap 5 (2024/25+ rules), reset by WC/FH.
        ft = 1
        rows = sorted((hist or {}).get("current", []), key=lambda r: r["event"])
        chip_gw = {c["event"]: c["name"] for c in chips_used}
        for r in rows:
            if r["event"] == 1:
                ft = 1  # after GW1 deadline you hold 1 FT for GW2
                continue
            if chip_gw.get(r["event"]) in ("wildcard", "freehit"):
                ft = min(ft + 1, 5)   # transfers made on a WC/FH week do not consume the banked FT
                continue
            used = r["event_transfers"]
            paid = r["event_transfers_cost"] // 4
            ft = max(0, ft - (used - paid))
            ft = min(ft + 1, 5)       # +1 for the coming GW, banked to a maximum of 5 (2024/25+ rule)
        a2 = {"bank": bank / 10 if bank is not None else None, "free_transfers": ft, "free_transfers_label": "DERIVED",
              "transfers_made_this_gw": None,
              "chips_used": chips_used,
              "chips_available_note": "public API lists USED chips only; the available set is inferred from the rules"}
        cov["A2"] = {"status": "DERIVED", "source": "picks.entry_history.bank + entry/history (chips used) + FT rule",
                     "note": "free-transfer count is NOT in any public endpoint; derived from transfer history with the 1/GW-roll-to-5 rule. my-team/ (auth) gives it exactly"}

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

    # -------- owned per-element histories (form inputs, price history) — only when online (15 calls)
    if not src.offline:
        for o in owned:
            es = src.element_summary(o["id"])
            if es:
                o["history"] = [{"gw": h["round"], "opp": teams.get(h["opponent_team"]), "home": h["was_home"], "min": h["minutes"], "pts": h["total_points"],
                                 "bps": h["bps"], "bonus": h["bonus"], "xgi": h["expected_goal_involvements"], "defcon": h["defensive_contribution"],
                                 "value": h["value"] / 10, "net_transfers": h["transfers_balance"]} for h in es["history"]]
                o["upcoming"] = [{"gw": f["event"], "opp": teams.get(f["team_a"] if f["is_home"] else f["team_h"]), "home": f["is_home"], "fdr": f["difficulty"]} for f in es["fixtures"][:6]]

    snap = {
        "generated_utc": now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"), "mode": "offline" if src.offline else "live",
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
    a10 = s["A10_flags"]
    L.append(f"Deadline **{a10['deadline_utc']}** — {a10['hours_to_deadline']} h away. Last GW{a10['last_gw']}: finished={a10['finished']}, data_checked={a10['data_checked']}.")
    a9 = s["A9_rank"]; a2 = s["A2_bank_ft_chips"]
    L.append(f"Overall rank **{a9['overall_rank']:,}**, total {a9['total_points']}, last GW {a9['gw_points']} (GW rank {a9['gw_rank']:,}). Team value {a9['team_value']}m, bank {a9['bank']}m, free transfers **{a2.get('free_transfers')}** ({a2.get('free_transfers_label','my-team')}).\n")
    L.append("## Owned 15\n")
    L.append("| # | Player | Pos | £ | Sell | Status | Price Δ% (proj tonight) | Net tr. | Own% | EO top10k | C% top10k | C% my band | Last GW |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for o in s["A1_owned"]:
        proj = (o.get("price_projections") or [{}])[0].get("projected_percent")
        role = " (C)" if o["captain"] else (" (V)" if o["vice"] else "")
        lg = o.get("last_gw") or {}
        st = o["status"] + (f" {o['chance_next']}%" if o.get("chance_next") not in (None, 100) else "") + (f" — {o['news']}" if o["news"] else "")
        L.append(f"| {o['slot']} | {o['name']}{role} | {o['pos']} {o['team']} | {o['now_cost']} | {o.get('selling_price') if o.get('selling_price') is not None else '—'} | {st} | "
                 f"{o.get('price_change_percent')} ({proj}) | {o.get('net_transfers_event'):+,} | {o['selected_by']} | {o.get('eo_top10k')} | {o.get('cap_top10k')} | {o.get('cap_myband')} | "
                 f"{lg.get('pts','—')} pts / {lg.get('min','—')}' / bps {lg.get('bps','—')} |")
    L.append("\n## Market flow (net transfers this GW, all players)\n")
    L.append("In: " + ", ".join(f"{n} ({t}) {v:+,}" for n, t, v in s["A7_flow"]["top_in"]))
    L.append("Out: " + ", ".join(f"{n} ({t}) {v:+,}" for n, t, v in s["A7_flow"]["top_out"]))
    L.append("\n## Next fixtures\n")
    for f in a10["fixtures_next"]:
        L.append(f"- {f['kickoff']}  {f['home']} (FDR {f['fdr_h']}) v {f['away']} (FDR {f['fdr_a']})")
    L.append("\n## Coverage A1–A11\n")
    L.append("| # | Status | Source | Note |\n|---|---|---|---|")
    for k in ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11"]:
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
    ap.add_argument("--cookie-file", help="file containing the Cookie header for fantasy.premierleague.com (enables my-team/)")
    a = ap.parse_args()
    cookie = open(os.path.expanduser(a.cookie_file)).read().strip() if a.cookie_file and os.path.exists(os.path.expanduser(a.cookie_file)) else None
    snap = build(Source(a.offline, cookie), force=a.force, window_h=a.window_hours)
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
