# Liverpool FC — data doc
*Feeder-written (2026-11-03 07:42 UTC); do not edit. Narrative: `profiles/teams/liverpool.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-03 07:42 UTC)
**Manager:** Andoni Iraola · **Venue:** Anfield · **SofaScore:** https://www.sofascore.com/football/team/liverpool/44 · **FPL code:** LIV
**Table:** 5th, 15 pts (4W 3D 2L, GF 11 GA 9) · Home 15th (1-2-2, 4:6) · Away 2nd (3-1-0, 7:3)
**Standing context (F15):** 29 league games left · points v 4th -1, v 5th +0, v 17th (last safe) +8, v 18th +8 · goal difference +2
**Suspension watch (D7, all players of the club):** Virgil — 🟨 2 from a ban (3/5); Kerkez — 🟨 2 from a ban (3/5); Mac Allister — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 9 league matches):** goals after 75′ — for 2/11 (18%), against 1/9 (11%) · scored first 3, conceded first 5 (56% of matches), goalless 1 · points from losing positions 5 of 15 (5 matches behind at some point) · points from winning positions 12 of 12 (4 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Virgil (DEF) 9.4/90, hit 5/9; Jacquet (DEF) 9.3/90, hit 4/9; Araujo (DEF) 8.6/90, hit 3/9; Mac Allister (MID) 10.8/90, hit 1/9; Szoboszlai (MID) 9.7/90, hit 1/7; Gakpo (MID) 7.2/90, hit 1/7
**Manager tenure (F13, SofaScore):** Andoni Iraola since 01 Jul 2026 · 14 matches in charge, all competitions (9W 3D 2L) · 9 league matches this season · contract to 30 Jun 2028 · previous club Bournemouth · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Everton — last 4: Apr 2026 Premier League Everton 1–2 Liverpool FC (yellows 2–0, xG 0.79–1.45); Sep 2025 Premier League Liverpool FC 2–1 Everton (yellows 2–3, xG 0.90–0.70); Apr 2025 Premier League Liverpool FC 1–0 Everton (yellows 2–2, xG 1.47–0.67); Feb 2025 Premier League Everton 2–2 Liverpool FC (yellows 4–4, reds 1–1, xG 0.95–0.62) · 19 yellows in 4 | v Manchester United — last 4: May 2026 Premier League Manchester United 3–2 Liverpool FC (yellows 2–2, xG 2.34–0.89); Oct 2025 Premier League Liverpool FC 1–2 Manchester United (yellows 0–2, xG 2.74–1.34); Jan 2025 Premier League Liverpool FC 2–2 Manchester United (yellows 2–4, xG 2.82–1.05); Sep 2024 Premier League Manchester United 0–3 Liverpool FC (yellows 4–1, xG 1.36–1.79) · 17 yellows in 4
**Archetype (F5):** used **TR** — derived TR [DERIVED] · signals, last 6 league matches: possession 49.5%, PPDA 10.3 (Understat, 5 matches; lower = harder press), opponent offsides forced 2.3/match (line height), fast breaks 1.4/match (season), both sides' xG 2.29/match (openness) · note: computed from 5 of 6 GWs (no PPDA/possession for GW9). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 12 (permanent 8, loan 1, free 0, loan returns 3) · out 12 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 9 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 13.17 | 11 | Big chances against | 18 | 6 |
| xGOT | 12.00 | 8 | Box shots against | 68 | 5 |
| xA | 8.27 | 10 | Corners against | 37 | 4 |
| Shots | 140 | 5 | Crosses faced | 135 | 4 |
| SoT | 39 | 9 | Dribbled past | 54 | 2 |
| Big chances | 12 | 19 | Errors→shot | 6 | 8 |
| Shots in box | 85 | 9 | GK goals prevented | 0.24 | 11 |
| Corners | 45 | 7 | Clearances | 237 | 11 |
| Crosses | 172 | 7 | Tackles | 146 | 9 |
| Fast breaks | 13 | 5 | Interceptions | 84 | 8 |
| FK shots | 9 | 1 | Def. contributions | 502 | 9 |
| Possession % | 53.56 | 7 | Aerial % | 58.14 | 1 |
| Pass % | 83.16 | 9 | Duel % | 51.06 | 7 |
| Long balls | 343 | 4 | Fouls | 128 | 20 |
| Dribbles | 76 | 3 | Yellows | 22 | 17 |
| Shots against | 110 | 8 | Km covered | 1001 | 20 |
| SoT against | 28 | 3 | Sprints | 1164 | 1 |
Per match: xG 1.46 · xGOT 1.33 · shots 15.6 · shots against 12.2 · big chances 1.3 for / 2.0 against · corners 5.0 / 4.1 · crosses 19.1 / 15.0 · possession 53.555555555556%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | H | Fulham | 0–0 | 1.28/1.80 | 0.70/0.93 | 56 | 14/10 | 3/4 | 9/8 | 5/3 | 4/1 | 5/8 | 25/5 v 17/4 | 1/1 |
| 5 | A | Bournemouth | 1–0 | 1.65/1.36 | 0.79/0.94 | 54 | 12/9 | 3/2 | 7/5 | 6/2 | 1/1 | 3/3 | 13/1 v 27/6 | 4/2 |
| 6 | H | Manchester City | 0–3 | 0.94/0.76 | 1.28/1.59 | 35 | 13/15 | 6/4 | 6/8 | 4/4 | 0/3 | 5/6 | 13/2 v 12/2 | 2/2 |
| 7 | A | Brentford | 2–1 | 1.64/1.55 | 0.88/0.86 | 60 | 21/10 | 5/2 | 10/10 | 4/4 | 1/2 | 9/3 | 15/2 v 16/2 | 1/2 |
| 8 | H | Brighton & Hove Albion | 2–0 | 1.20/1.28 | 1.32/1.31 | 36 | 13/17 | 4/1 | 10/10 | 3/7 | 1/1 | 4/2 | 5/2 v 23/5 | 3/3 |
| 9 | H | Arsenal | 0–1 | 1.05/— | 0.98/— | 56 | 17/10 | 0/3 | 14/6 | 9/3 | 1/2 | 7/4 | 33/5 v 10/4 | 3/2 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | H | Fulham | 0–0 | 4-2-3-1 | 11/8 | 0/1 | 0/0 | 494/398 | 70/46 | Bradley (Knee Injury), Chiesa (Back Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Gomez (Strain Injury) | Cairney (Knee Injury) | Thomas Bramall |
| 5 | A | Bournemouth | 1–0 | 4-2-3-1 | 13/11 | 2/1 | 0/0 | 473/383 | 74/82 | Bradley (Knee Injury), Chiesa (Back Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury) | Adli (Calf Injury), Kroupi (Foot Injury), Araujo (Thigh Injury) | Michael Oliver |
| 6 | H | Manchester City | 0–3 | 4-2-3-1 | 19/14 | 4/2 | 1/0 | 301/562 | 41/48 | Isak (Thigh Injury), Gakpo (Ankle Injury), Bradley (Knee Injury), Szoboszlai (Hamstring Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury) | Foden (ban (red)) | Chris Kavanagh |
| 7 | A | Brentford | 2–1 | 4-2-3-1 | 13/7 | 3/4 | 0/2 | 503/330 | 61/50 | Gravenberch (ban (cards)), Bradley (Knee Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury) | Milambo (Cruciate Ligament Injury), Dasilva (Hamstring Injury), Furo (Knee Surgery) | John Brooks |
| 8 | H | Brighton & Hove Albion | 2–0 | 4-2-3-1 | 13/9 | 0/2 | 0/0 | 326/579 | 57/77 | Bradley (Knee Injury), Szoboszlai (Hamstring Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Frimpong (Hamstring Injury), Muñoz (injury; doubtful) | Ferguson (Ankle Injury), Azeez (Muscle Injury), Mitoma (Hamstring Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Yohanna (Knock Injury), Struijk (Lack of Fitness; doubtful) | Samuel Barrott |
| 9 | H | Arsenal | 0–1 | 4-2-3-1 | 18/10 | 4/4 | 0/0 | 464/372 | 72/45 | Bradley (Knee Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Frimpong (Hamstring Injury) | Dowman (ban (red)), Saka (Muscle Injury), Saliba (Back Injury) | Andy Madley |
Per match: fouls 14.2 / 10.1 · yellows 2.56 / 2.44 · reds 1 / 2 (season) · offsides forced 2.3, committed 2.2 · crosses attempted 19.1 / faced 15.0. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 1.24 for / 1.32 against per match · Away (4): xG 1.74 / 1.00. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW9 H v Arsenal 0–1 (Sun 01 Nov 16:30 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Alisson | G | 90 | 6.7 | 0.00 | 0.01 | 0 | 0 | 0 | 0 | 29 |
| Ronald Araújo | D | 81 | 7 | 0.19 | 0.01 | 0 | 2 | 12 | 2 | 43 |
| Jérémy Jacquet | D | 90 | 6.5 | 0.00 | 0.05 | 1 | 0 | 9 | 2 | 69 |
| Virgil van Dijk | D | 90 | 7.3 | 0.05 | 0.11 | 2 | 2 | 7 | 0 | 80 |
| Miloš Kerkez | D | 81 | 7.2 | 0.12 | 0.18 | 3 | 1 | 7 | 8 | 56 |
| Alexis Mac Allister | M | 90 | 7.3 | 0.11 | 0.15 | 1 | 2 | 4 | 1 | 72 |
| Trey Nyoni | M | 58 | 7 | 0.00 | 0.08 | 0 | 0 | 2 | 0 | 61 |
| Cody Gakpo | M | 67 | 6.6 | 0.04 | 0.11 | 1 | 1 | 2 | 8 | 31 |
| Florian Wirtz | M | 81 | 6.1 | 0.28 | 0.06 | 0 | 3 | 2 | 1 | 52 |
| Bradley Barcola | M | 90 | 6.4 | 0.07 | 0.14 | 1 | 1 | 3 | 4 | 57 |
| Alexander Isak | F | 90 | 6.7 | 0.08 | 0.13 | 1 | 2 | 1 | 1 | 25 |
Subs used: Dominik Szoboszlai (32'), Rio Ngumoha (23'), Kostas Tsimikas (9'), Víctor Muñoz (9'), Lewis Koumas (9')
Goals: 16' Kai Havertz (assist Declan Rice) [opp]
Substitutions (own): 58' Dominik Szoboszlai for Trey Nyoni; 67' Rio Ngumoha for Cody Gakpo; 81' Lewis Koumas for Florian Wirtz; 81' Víctor Muñoz for Ronald Araújo; 81' Kostas Tsimikas for Miloš Kerkez
Cards: 45' Bradley Barcola (yellow, own); 55' Noni Madueke (yellow, opp); 67' Miloš Kerkez (yellow, own); 72' Myles Lewis-Skelly (yellow, opp); 80' Jurriën Timber (yellow, opp); 80' Alexis Mac Allister (yellow, own); 90' Virgil van Dijk (yellow, own); 90' David Raya (yellow, opp)
**Baseline XI change vs GW8 (4-2-3-1 → 4-2-3-1):** in — Trey Nyoni; out — Ryan Gravenberch.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 5 | A Bournemouth | 57' | FOR | Alexander Isak | — | open play | 0.51 |
| 6 | H Manchester City | 65' | AGAINST | Erling Haaland | — | open play | 0.09 |
| 6 | H Manchester City | 68' | AGAINST | Jérémy Doku | Elliot Anderson | open play | 0.06 |
| 6 | H Manchester City | 78' | AGAINST | Rayan Cherki | Joško Gvardiol | open play | 0.75 |
| 7 | A Brentford | 44' | AGAINST | Keane Lewis-Potter | Igor Thiago | open play | 0.26 |
| 7 | A Brentford | 62' | FOR | Víctor Muñoz | Florian Wirtz | open play | 0.18 |
| 7 | A Brentford | 70' | FOR | Alexander Isak | Bradley Barcola | open play | 0.13 |
| 8 | H Brighton & Hove Albion | 17' | FOR | Pascal Groß | — | own goal | — |
| 8 | H Brighton & Hove Albion | 21' | FOR | Alexander Isak | Bradley Barcola | open play | 0.60 |
| 9 | H Arsenal | 16' | AGAINST | Kai Havertz | Declan Rice | [no Understat] | — |
Scored 11: open play 9, penalty 1, own goal 1 · Conceded 9: open play 7, penalty 1, [no Understat] 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW7 AG v Brentford 44' Keane Lewis-Potter (assist Igor Thiago): G O O O A A A L - Keane Lewis-Potter from Brentford heads the ball home! · before: 44' The cross by Igor Thiago from Brentford successfully finds a teammate in the box. ‹ 44' Ronald Araujo successfully blocks the shot ‹ 44' A shot by Jaidon Anthony is blocked.
- GW7 FOR v Brentford 62' Victor Munoz (assist Florian Wirtz, key pass Jeremy Jacquet): G O O O A A A L - Victor Munoz scores with the left foot! · before: 62' Liverpool start a counter attack. ‹ 62' Trey Nyoni relieves the pressure with a clearance ‹ 62' Mamadou Sangare makes the tackle and wins possession for his team
- GW7 FOR v Brentford 70' Alexander Isak (assist Bradley Barcola, key pass Alexis Mac Allister): G O O O A A A L - Alexander Isak scores with the left foot! · before: 70' Bradley Barcola creates a scoring opportunity for his teammate ‹ 70' The cross by Alexis Mac Allister from Liverpool successfully finds a teammate in the box. ‹ 69' Igor Thiago successfully blocks the shot
- GW8 AG v Brighton & Hove Albion 17' Pascal Groß [OG]: OWN GOAL - Pascal Gross sends the ball into his own net! · before: 17' Florian Wirtz from Liverpool sends an effort wide of target ‹ 17' Pascal Gross from Brighton intercepts a cross aimed towards the box. ‹ 17' Ronald Araujo makes the tackle and wins possession for his team
- GW8 FOR v Brighton & Hove Albion 21' Alexander Isak (assist Bradley Barcola): G O O O A A A L - Alexander Isak scores with the left foot! · before: 21' Bradley Barcola creates a scoring opportunity for his teammate ‹ 21' Liverpool with a potentially dangerous attack. ‹ 21' Bradley Barcola makes the tackle and wins possession for his team
- GW9 AG v Arsenal 16' Kai Havertz (assist Declan Rice, key pass Noni Madueke): G O O O A A A L - Kai Havertz scores with the left foot! · before: 16' The cross by Declan Rice from Arsenal successfully finds a teammate in the box. ‹ 16' Goal kick for Liverpool. ‹ 16' Declan Rice from Arsenal tries to score from outside the penalty box, but the shot is nowhe

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW6 H v Manchester City 65' Erling Haaland: no structured culprit — reports only
- GW6 H v Manchester City 68' Jérémy Doku: no structured culprit — reports only
- GW6 H v Manchester City 78' Rayan Cherki: no structured culprit — reports only
- GW7 A v Brentford 44' Keane Lewis-Potter: no structured culprit — reports only
  · GW7 other flags: Jérémy Jacquet lastManTackle 1
- GW9 H v Arsenal 16' Kai Havertz: Alisson error leading to the goal [CONFIRMED — SofaScore error flag]; Jérémy Jacquet error leading to the goal [CONFIRMED — SofaScore error flag]
  · GW9 other flags: Bradley Barcola errorLeadToAShot 1

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 88 | 7.74 | 9 | 84 | 9.24 | 7 |
| corner | 21 | 2.72 | 0 | 9 | 0.42 | 0 |
| set piece | 5 | 0.27 | 0 | 3 | 0.14 | 0 |
| direct FK | 8 | 0.42 | 0 | 4 | 0.20 | 0 |
| penalty | 1 | 0.76 | 1 | 1 | 0.76 | 1 |
Totals per match: xG 1.49 (npxG 1.39) for, xGA 1.34 (np 1.25) against · dead-ball share of xG 35% for, 14% against · penalties won 1, conceded 1 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 21 shots, xG 2.72, 0 goals, headed 9: 6-yard box, central 4 shots, xG 1.89, 0 goals; penalty area, central 4 shots, xG 0.26, 0 goals; 6-yard box, right 3 shots, xG 0.24, 0 goals · against — 9 shots conceded, xG 0.42, 0 goals, headed 4: penalty area, central 2 shots, xG 0.17, 0 goals; penalty area, right 2 shots, xG 0.09, 0 goals; 6-yard box, central 1 shots, xG 0.08, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 33 · corner shots conceded 9 (headed 4), xG 0.42, goals 0 · xG per corner faced 0.013 (rank 20 of 20, 1 = weakest) · weak zone: none stands out · signal: **STRONG — no corner pairing against them** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–9 [CONFIRMED — LiveScore Block L, 71 corners; side L/R as LiveScore records it; foot from SofaScore]: Dominik Szoboszlai 24 (13L/11R, 3 short, right foot); Konstantinos Tsimikas 17 (6L/11R, 3 short, left foot); Alexis Mac Allister 12 (5L/7R, 5 short, right foot); Florian Wirtz 10 (7L/3R, 2 short, right foot). First contact on corners that ended in a shot (Understat) — for: Alexander Isak 4 (4 headed), Alexis Mac Allister 4 (3 headed), Cody Gakpo 2 (1 headed), Víctor Muñoz 2 (1 headed), Florian Wirtz 2 · against (who beat them): Joshua King 2, Elliot Anderson 2, Murillo 1 (1 headed), Calvin Bassey 1 (1 headed), Ryan Christie 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 43.0 (rank 5 of 20, 1 = highest line) · block length 24.0 (rank 19, 1 = most compact) · width 68.2. Per match: GW4 H v Fulham 4-2-3-1: back line 45, front 69, length 24, width 64 (56% poss); GW5 A v Bournemouth 4-2-3-1: back line 40, front 66, length 26, width 73 (54% poss); GW6 H v Manchester City 4-2-3-1: back line 38, front 58, length 20, width 70 (35% poss); GW7 A v Brentford 4-2-3-1: back line 43, front 70, length 27, width 71 (60% poss); GW8 H v Brighton & Hove Albion 4-2-3-1: back line 37, front 56, length 19, width 67 (36% poss); GW9 H v Arsenal 4-2-3-1: back line 46, front 68, length 23, width 62 (56% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 1 league match(es) v LB-coded sides — xG 0.69/match and 3.0 pts/match v 1.56 and 1.5 against the rest → **struggles — chance creation drops** (threshold: xG v LB at least 90% of the rest). GW3 A v Ipswich Town 2–0, xG 0.69, box shots 5, poss 55%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Wirtz 6, Szoboszlai 5, Ngumoha 1** · FPL editorial order: Szoboszlai #1, Mac Allister #2, Wirtz #3
- Direct free-kick shooters: **Szoboszlai 6, Allister 2** · FPL order: Szoboszlai #1, Wirtz #2, Mac Allister #3
- Penalties taken: **Szoboszlai 1** · FPL order: Szoboszlai #1, Isak #2, Gakpo #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Szoboszlai 2, Jacquet 1, Wirtz 1**
- Corner targets (headed shots from corners): **Isak 4, Allister 3, Muñoz 1, Gakpo 1** · corner shots 21
- **DISAGREEMENT:** observed corner taker Florian Wirtz (6) v FPL #1 Szoboszlai — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Cody Gakpo 4 (0.68/90, percentile 95, 528 min); Alexis Mac Allister 5 (0.67/90, percentile 94, 668 min); Florian Wirtz 5 (0.64/90, percentile 93, 705 min) · club total 17 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 306 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 7, field tilt 70.5, possession 60%, box entries 9, direct speed 2.2, SCA 50; GW2: PPDA 4.89, field tilt 72.8, possession 68.3%, box entries 12, direct speed 1.97, SCA 26; GW3: PPDA 10.88, field tilt 58, possession 54.1%, box entries 8, direct speed 1.83, SCA 19; GW4: PPDA 9.48, field tilt 63.3, possession 55.5%, box entries 9, direct speed 2.72, SCA 26; GW5: PPDA 9.83, field tilt 44.8, possession 53.4%, box entries 10, direct speed 2.71, SCA 24; GW6: PPDA 9.5, field tilt 35.3, possession 35.4%, box entries 6, direct speed 3.1, SCA 21; GW7: PPDA 7.29, field tilt 68.8, possession 60.1%, box entries 21, direct speed 2.3, SCA 41; GW8: PPDA 16.41, field tilt 39.5, possession 36.5%, box entries 11, direct speed 3.59, SCA 19

**Zone 14 (C13, SofaScore heat-map points, 9 league matches):** for 38.9/match (rank 4 of 20) · conceded 22.1/match (rank 18 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 6.6/match · allowed 8.4/match · PPDA 9.2. Per match for/allowed: GW3 6/5; GW4 5/9; GW5 8/8; GW6 3/11; GW7 14/9; GW8 9/16 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 9 league matches, weights last-3 ×3 / older ×1
- GK: Alisson (15, 3/3)
- DEF: Jérémy Jacquet (15, 3/3), Virgil van Dijk (15, 3/3), Miloš Kerkez (14, 3/3), Ronald Araújo (13, 3/3)
- MID: Florian Wirtz (15, 3/3), Alexis Mac Allister (13, 3/3), Cody Gakpo (10, 2/3), Dominik Szoboszlai (8, 1/3), Ryan Gravenberch (6, 1/3)
- FWD: Alexander Isak (14, 3/3)
- Contested slots: none · Excluded (FPL flag): none
- Absent last match (E12, SofaScore list): Bradley (Knee Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Frimpong (Hamstring Injury)
- Substitutions this season (C3): GW7 52' Jeremie Frimpong→Rio Ngumoha INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW7 46' Ronald Araújo→Jeremie Frimpong HALF-TIME; GW7 32' Dominik Szoboszlai→Trey Nyoni INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW8 88' Miloš Kerkez→Kostas Tsimikas LATE; GW8 77' Alexander Isak→Lewis Koumas GAME-STATE; GW8 77' Bradley Barcola→Rio Ngumoha GAME-STATE; GW8 65' Florian Wirtz→Trey Nyoni INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW9 81' Florian Wirtz→Lewis Koumas CHASING; GW9 81' Ronald Araújo→Víctor Muñoz CHASING; GW9 81' Miloš Kerkez→Kostas Tsimikas CARD-RISK; GW9 67' Cody Gakpo→Rio Ngumoha CHASING; GW9 58' Trey Nyoni→Dominik Szoboszlai CHASING

### First-choice players and absences (F14) — generated 2026-11-03 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Alisson | start weight 15 | OK | a | — | — |
| CB | Jérémy Jacquet | start weight 15 | OK | a 100% | Miloš Kerkez (DEF, not a CB by heat map) | — |
| CB | Virgil van Dijk | start weight 15 | OK | a | Miloš Kerkez (DEF, not a CB by heat map) | — |
| xGI #1 | Alexander Isak | xGI 4.62 | OK | a 100% | Dominik Szoboszlai | — |
| xGI #2 | Cody Gakpo | xGI 3.09 | OK | a 100% | Dominik Szoboszlai | — |
| Penalties #1 (FPL) | Szoboszlai | FPL order | OK | a 100% | Isak | — |
| Direct FK #1 (FPL) | Szoboszlai | FPL order | OK | a 100% | Wirtz | — |
| Corners (observed) | Dominik Szoboszlai | 24 corners taken | OK | a 100% | Konstantinos Tsimikas | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 A Newcastle United: all started · GW2 H Nottingham Forest: all started · GW3 A Ipswich Town: all started · GW4 H Fulham: Cody Gakpo (did not start) · GW5 A Bournemouth: all started · GW6 H Manchester City: Alexander Isak (Thigh Injury), Cody Gakpo (Ankle Injury) · GW7 A Brentford: Cody Gakpo (did not start) · GW8 H Brighton & Hove Albion: all started · GW9 H Arsenal: all started

### Next fixtures (all competitions)
- Wed 04 Nov 17:45 UTC · UEFA Champions League R4 · A v Fenerbahçe
- Sun 08 Nov 14:00 UTC · Premier League R10 · A v Crystal Palace
- Sun 22 Nov 16:30 UTC · Premier League R11 · H v Manchester United
- Wed 25 Nov 20:00 UTC · UEFA Champions League R5 · A v Club Brugge KV
- Sun 29 Nov 12:00 UTC · Premier League R12 · A v Everton
- Wed 02 Dec 19:30 UTC · Premier League R13 · H v Sunderland

### FPL availability flags (players with league minutes this season)
Frimpong — Hamstring injury - Unknown return date (0%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 A Newcastle United 2–2 · xG 2.98–1.58 · poss 61% · 4-2-3-1 · scorers: Cody Gakpo 55', Dominik Szoboszlai 90'
- GW2 H Nottingham Forest 2–2 · xG 1.75–2.30 · poss 69% · 4-2-3-1 · scorers: Alexander Isak 60', Víctor Muñoz 82'
- GW3 A Ipswich Town 2–0 · xG 0.69–0.75 · poss 55% · 4-2-3-1 · scorers: Alexander Isak 6', Alexander Isak 9'
- GW4 H Fulham 0–0 · xG 1.28–0.70 · poss 56% · 4-2-3-1 · scorers: none
- GW5 A Bournemouth 1–0 · xG 1.65–0.79 · poss 54% · 4-2-3-1 · scorers: Alexander Isak 57'
- GW6 H Manchester City 0–3 · xG 0.94–1.28 · poss 35% · 4-2-3-1 · scorers: none
- GW7 A Brentford 2–1 · xG 1.64–0.88 · poss 60% · 4-2-3-1 · scorers: Víctor Muñoz 62', Alexander Isak 70'
- GW8 H Brighton & Hove Albion 2–0 · xG 1.20–1.32 · poss 36% · 4-2-3-1 · scorers: Pascal Groß 17', Alexander Isak 21'
- GW9 H Arsenal 0–1 · xG 1.05–0.98 · poss 56% · 4-2-3-1 · scorers: none
### Corner takers observed (LiveScore Block L)
- Dominik Szoboszlai: 24 corners (13 left, 11 right, 3 short)
- Konstantinos Tsimikas: 17 corners (6 left, 11 right, 3 short)
- Alexis Mac Allister: 12 corners (5 left, 7 right, 5 short)
- Florian Wirtz: 10 corners (7 left, 3 right, 2 short)
- Cody Gakpo: 6 corners (4 left, 2 right, 1 short)
- Luke Chambers: 1 corners (0 left, 1 right)
- Milos Kerkez: 1 corners (0 left, 1 right)
