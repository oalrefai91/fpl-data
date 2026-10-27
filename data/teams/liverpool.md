# Liverpool FC — data doc
*Feeder-written (2026-10-27 07:42 UTC); do not edit. Narrative: `profiles/teams/liverpool.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-10-27 07:42 UTC)
**Manager:** Andoni Iraola · **Venue:** Anfield · **SofaScore:** https://www.sofascore.com/football/team/liverpool/44 · **FPL code:** LIV
**Table:** 4th, 15 pts (4W 3D 1L, GF 11 GA 8) · Home 12th (1-2-1, 4:5) · Away 1st (3-1-0, 7:3)
**Standing context (F15):** 30 league games left · points v 4th +0, v 5th +2, v 17th (last safe) +8, v 18th +9 · goal difference +3
**Suspension watch (D7, all players of the club):** nobody within 2 yellows of a ban, nobody suspended [FPL]
**Goal timing & game state (F17, 8 league matches):** goals after 75′ — for 2/11 (18%), against 1/8 (12%) · scored first 3, conceded first 4 (50% of matches), goalless 1 · points from losing positions 5 of 12 (4 matches behind at some point) · points from winning positions 12 of 12 (4 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Virgil (DEF) 9.8/90, hit 5/8; Jacquet (DEF) 9.4/90, hit 4/8; Araujo (DEF) 7.8/90, hit 2/8; Mac Allister (MID) 10.8/90, hit 1/8; Szoboszlai (MID) 9.0/90, hit 1/6; Gakpo (MID) 7.4/90, hit 1/6
**Manager tenure (F13, SofaScore):** Andoni Iraola since 01 Jul 2026 · 12 matches in charge, all competitions (8W 3D 1L) · 8 league matches this season · contract to 30 Jun 2028 · previous club Bournemouth · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Everton — last 4: Apr 2026 Premier League Everton 1–2 Liverpool FC (yellows 2–0, xG 0.79–1.45); Sep 2025 Premier League Liverpool FC 2–1 Everton (yellows 2–3, xG 0.90–0.70); Apr 2025 Premier League Liverpool FC 1–0 Everton (yellows 2–2, xG 1.47–0.67); Feb 2025 Premier League Everton 2–2 Liverpool FC (yellows 4–4, reds 1–1, xG 0.95–0.62) · 19 yellows in 4 | v Manchester United — last 4: May 2026 Premier League Manchester United 3–2 Liverpool FC (yellows 2–2, xG 2.34–0.89); Oct 2025 Premier League Liverpool FC 1–2 Manchester United (yellows 0–2, xG 2.74–1.34); Jan 2025 Premier League Liverpool FC 2–2 Manchester United (yellows 2–4, xG 2.82–1.05); Sep 2024 Premier League Manchester United 0–3 Liverpool FC (yellows 4–1, xG 1.36–1.79) · 17 yellows in 4
**Archetype (F5):** used **TR** — derived TR [DERIVED] · signals, last 6 league matches: possession 49.3%, PPDA 10.7 (Understat, 6 matches; lower = harder press), opponent offsides forced 2.7/match (line height), fast breaks 1.4/match (season), both sides' xG 2.19/match (openness). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap).
**Squad changes (F20, since 01 Jun 2026):** in 12 (permanent 8, loan 1, free 0, loan returns 3) · out 12 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 8 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 12.12 | 8 | Big chances against | 16 | 6 |
| xGOT | 12.00 | 7 | Box shots against | 62 | 5 |
| xA | 7.04 | 9 | Corners against | 33 | 4 |
| Shots | 123 | 4 | Crosses faced | 125 | 6 |
| SoT | 39 | 6 | Dribbled past | 47 | 2 |
| Big chances | 11 | 19 | Errors→shot | 5 | 6 |
| Shots in box | 71 | 10 | GK goals prevented | -0.20 | 12 |
| Corners | 38 | 9 | Clearances | 214 | 8 |
| Crosses | 139 | 12 | Tackles | 129 | 11 |
| Fast breaks | 11 | 8 | Interceptions | 72 | 8 |
| FK shots | 8 | 1 | Def. contributions | 448 | 10 |
| Possession % | 53.25 | 7 | Aerial % | 58.41 | 1 |
| Pass % | 83.32 | 8 | Duel % | 51.81 | 4 |
| Long balls | 309 | 4 | Fouls | 110 | 17 |
| Dribbles | 70 | 3 | Yellows | 18 | 15 |
| Shots against | 100 | 7 | Km covered | 889 | 20 |
| SoT against | 25 | 2 | Sprints | 1026 | 1 |
Per match: xG 1.52 · xGOT 1.50 · shots 15.4 · shots against 12.5 · big chances 1.4 for / 2.0 against · corners 4.8 / 4.1 · crosses 17.4 / 15.6 · possession 53.25%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | A | Ipswich Town | 2–0 | 0.69/0.74 | 0.75/0.60 | 55 | 10/14 | 7/5 | 5/4 | 2/4 | —/— | 3/4 | 11/3 v 15/4 | 5/4 |
| 4 | H | Fulham | 0–0 | 1.28/1.80 | 0.70/0.93 | 56 | 14/10 | 3/4 | 9/8 | 5/3 | 4/1 | 5/8 | 25/5 v 17/4 | 1/1 |
| 5 | A | Bournemouth | 1–0 | 1.65/1.36 | 0.79/0.94 | 54 | 12/9 | 3/2 | 7/5 | 6/2 | 1/1 | 3/3 | 13/1 v 27/6 | 4/2 |
| 6 | H | Manchester City | 0–3 | 0.94/0.76 | 1.28/1.59 | 35 | 13/15 | 6/4 | 6/8 | 4/4 | 0/3 | 5/6 | 13/2 v 12/2 | 2/2 |
| 7 | A | Brentford | 2–1 | 1.64/1.55 | 0.88/0.86 | 60 | 21/10 | 5/2 | 10/10 | 4/4 | 1/2 | 9/3 | 15/2 v 16/2 | 1/2 |
| 8 | H | Brighton & Hove Albion | 2–0 | 1.20/1.28 | 1.32/1.31 | 36 | 13/17 | 4/1 | 10/10 | 3/7 | 1/1 | 4/2 | 5/2 v 23/5 | 3/3 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | A | Ipswich Town | 2–0 | 4-2-3-1 | 13/6 | 3/1 | 0/0 | 531/428 | 67/46 | Bradley (Knee Injury), Chiesa (Back Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Gomez (Strain Injury) | Matusiwa (Muscle Injury), Taylor (Knee Injury), Philogene-Bidace (Ankle Injury) | Darren England |
| 4 | H | Fulham | 0–0 | 4-2-3-1 | 11/8 | 0/1 | 0/0 | 494/398 | 70/46 | Bradley (Knee Injury), Chiesa (Back Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Gomez (Strain Injury) | Cairney (Knee Injury) | Thomas Bramall |
| 5 | A | Bournemouth | 1–0 | 4-2-3-1 | 13/11 | 2/1 | 0/0 | 473/383 | 74/82 | Bradley (Knee Injury), Chiesa (Back Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury) | Adli (Calf Injury), Kroupi (Foot Injury), Araujo (Thigh Injury) | Michael Oliver |
| 6 | H | Manchester City | 0–3 | 4-2-3-1 | 19/14 | 4/2 | 1/0 | 301/562 | 41/48 | Isak (Thigh Injury), Gakpo (Ankle Injury), Bradley (Knee Injury), Szoboszlai (Hamstring Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury) | Foden (ban (red)) | Chris Kavanagh |
| 7 | A | Brentford | 2–1 | 4-2-3-1 | 13/7 | 3/4 | 0/2 | 503/330 | 61/50 | Gravenberch (ban (cards)), Bradley (Knee Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury) | Milambo (Cruciate Ligament Injury), Dasilva (Hamstring Injury), Furo (Knee Surgery) | John Brooks |
| 8 | H | Brighton & Hove Albion | 2–0 | 4-2-3-1 | 13/9 | 0/2 | 0/0 | 326/579 | 57/77 | Bradley (Knee Injury), Szoboszlai (Hamstring Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Frimpong (Hamstring Injury), Muñoz (injury; doubtful) | Ferguson (Ankle Injury), Azeez (Muscle Injury), Mitoma (Hamstring Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Yohanna (Knock Injury), Struijk (Lack of Fitness; doubtful) | Samuel Barrott |
Per match: fouls 13.8 / 10.1 · yellows 2.38 / 2.25 · reds 1 / 2 (season) · offsides forced 2.2, committed 2.2 · crosses attempted 17.4 / faced 15.6. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 1.29 for / 1.40 against per match · Away (4): xG 1.74 / 1.00. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW8 H v Brighton & Hove Albion 2–0 (Sun 25 Oct 14:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Alisson | G | 90 | 6.9 | 0.00 | 0.00 | 0 | 0 | 0 | 0 | 33 |
| Ronald Araújo | D | 90 | 8 | 0.06 | 0.01 | 0 | 1 | 11 | 0 | 59 |
| Jérémy Jacquet | D | 90 | 8.3 | 0.00 | 0.04 | 0 | 0 | 10 | 0 | 40 |
| Virgil van Dijk | D | 90 | 7.7 | 0.00 | 0.01 | 0 | 0 | 13 | 0 | 58 |
| Miloš Kerkez | D | 88 | 6.9 | 0.00 | 0.02 | 1 | 0 | 3 | 2 | 57 |
| Ryan Gravenberch | M | 90 | 7.2 | 0.00 | 0.07 | 0 | 0 | 8 | 0 | 45 |
| Alexis Mac Allister | M | 90 | 7 | 0.05 | 0.02 | 1 | 1 | 4 | 0 | 48 |
| Bradley Barcola | M | 77 | 7.8 | 0.07 | 0.37 | 1 | 1 | 5 | 0 | 29 |
| Florian Wirtz | M | 65 | 7.4 | 0.07 | 0.24 | 2 | 1 | 4 | 3 | 57 |
| Cody Gakpo | M | 90 | 7.1 | 0.56 | 0.04 | 2 | 6 | 1 | 0 | 51 |
| Alexander Isak | F | 77 | 7.3 | 0.40 | 0.03 | 3 | 3 | 0 | 0 | 20 |
Subs used: Trey Nyoni (25'), Lewis Koumas (13'), Rio Ngumoha (13'), Kostas Tsimikas (2')
Goals: 17' Pascal Groß [own, ownGoal]; 21' Alexander Isak (assist Bradley Barcola) [own]
Substitutions (own): 65' Trey Nyoni for Florian Wirtz [injury]; 77' Lewis Koumas for Alexander Isak; 77' Rio Ngumoha for Bradley Barcola; 88' Kostas Tsimikas for Miloš Kerkez
Cards: 45' Olivier Boscagli (yellow, opp); 73' Costinha (yellow, opp)
**Baseline XI change vs GW7 (4-2-3-1 → 4-2-3-1):** in — Cody Gakpo, Ryan Gravenberch; out — Dominik Szoboszlai, Víctor Muñoz.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 3 | A Ipswich Town | 6' | FOR | Alexander Isak | Cody Gakpo | open play | 0.12 |
| 3 | A Ipswich Town | 9' | FOR | Alexander Isak | Cody Gakpo | open play | 0.13 |
| 5 | A Bournemouth | 57' | FOR | Alexander Isak | — | open play | 0.51 |
| 6 | H Manchester City | 65' | AGAINST | Erling Haaland | — | open play | 0.09 |
| 6 | H Manchester City | 68' | AGAINST | Jérémy Doku | Elliot Anderson | open play | 0.06 |
| 6 | H Manchester City | 78' | AGAINST | Rayan Cherki | Joško Gvardiol | open play | 0.75 |
| 7 | A Brentford | 44' | AGAINST | Keane Lewis-Potter | Igor Thiago | open play | 0.26 |
| 7 | A Brentford | 62' | FOR | Víctor Muñoz | Florian Wirtz | open play | 0.18 |
| 7 | A Brentford | 70' | FOR | Alexander Isak | Bradley Barcola | open play | 0.13 |
| 8 | H Brighton & Hove Albion | 17' | FOR | Pascal Groß | — | own goal | — |
| 8 | H Brighton & Hove Albion | 21' | FOR | Alexander Isak | Bradley Barcola | open play | 0.60 |
Scored 11: open play 9, penalty 1, own goal 1 · Conceded 8: open play 7, penalty 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW6 AG v Manchester City 65' Erling Haaland: G O O O A A A L - Erling Haaland reacts first on the loose ball and puts it away with the left! · before: 65' Alexis Mac Allister successfully blocks the shot ‹ 65' A shot by Jeremy Doku is blocked. ‹ 62' SENT OFF! - After a tactical foul, Ryan Gravenberch gets his second yellow card.
- GW6 AG v Manchester City 68' Jérémy Doku (assist Elliot Anderson): G O O O A A A L - Jeremy Doku scores with the right foot! · before: 67' The referee signals a free kick as Josko Gvardiol from Manchester City trips Ronald Araujo ‹ 67' Ronald Araujo relieves the pressure with a clearance ‹ 66' Nico O'Reilly is leaving the field to be replaced by Josko Gvardiol in a tactical substitut
- GW6 AG v Manchester City 78' Rayan Cherki (assist Josko Gvardiol, key pass Elliot Anderson): G O O O A A A L - Rayan Cherki scores with the right foot! · before: 78' Josko Gvardiol creates a scoring opportunity for his teammate ‹ 76' Antoine Semenyo is penalised for pushing Milos Kerkez. ‹ 75' Goal kick for Liverpool.
- GW7 AG v Brentford 44' Keane Lewis-Potter (assist Igor Thiago): G O O O A A A L - Keane Lewis-Potter from Brentford heads the ball home! · before: 44' The cross by Igor Thiago from Brentford successfully finds a teammate in the box. ‹ 44' Ronald Araujo successfully blocks the shot ‹ 44' A shot by Jaidon Anthony is blocked.
- GW7 FOR v Brentford 62' Victor Munoz (assist Florian Wirtz, key pass Jeremy Jacquet): G O O O A A A L - Victor Munoz scores with the left foot! · before: 62' Liverpool start a counter attack. ‹ 62' Trey Nyoni relieves the pressure with a clearance ‹ 62' Mamadou Sangare makes the tackle and wins possession for his team
- GW7 FOR v Brentford 70' Alexander Isak (assist Bradley Barcola, key pass Alexis Mac Allister): G O O O A A A L - Alexander Isak scores with the left foot! · before: 70' Bradley Barcola creates a scoring opportunity for his teammate ‹ 70' The cross by Alexis Mac Allister from Liverpool successfully finds a teammate in the box. ‹ 69' Igor Thiago successfully blocks the shot
- GW8 AG v Brighton & Hove Albion 17' Pascal Groß [OG]: OWN GOAL - Pascal Gross sends the ball into his own net! · before: 17' Florian Wirtz from Liverpool sends an effort wide of target ‹ 17' Pascal Gross from Brighton intercepts a cross aimed towards the box. ‹ 17' Ronald Araujo makes the tackle and wins possession for his team
- GW8 FOR v Brighton & Hove Albion 21' Alexander Isak (assist Bradley Barcola): G O O O A A A L - Alexander Isak scores with the left foot! · before: 21' Bradley Barcola creates a scoring opportunity for his teammate ‹ 21' Liverpool with a potentially dangerous attack. ‹ 21' Bradley Barcola makes the tackle and wins possession for his team

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW6 H v Manchester City 65' Erling Haaland: no structured culprit — reports only
- GW6 H v Manchester City 68' Jérémy Doku: no structured culprit — reports only
- GW6 H v Manchester City 78' Rayan Cherki: no structured culprit — reports only
- GW7 A v Brentford 44' Keane Lewis-Potter: no structured culprit — reports only
  · GW7 other flags: Jérémy Jacquet lastManTackle 1

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

**Corners (E10 data layer):** observed takers GW1–8 [CONFIRMED — LiveScore Block L, 64 corners; side L/R as LiveScore records it; foot from SofaScore]: Dominik Szoboszlai 23 (13L/10R, 3 short, right foot); Konstantinos Tsimikas 17 (6L/11R, 3 short, left foot); Alexis Mac Allister 12 (5L/7R, 5 short, right foot); Florian Wirtz 10 (7L/3R, 2 short, right foot). First contact on corners that ended in a shot (Understat) — for: Alexander Isak 4 (4 headed), Alexis Mac Allister 4 (3 headed), Cody Gakpo 2 (1 headed), Víctor Muñoz 2 (1 headed), Florian Wirtz 2 · against (who beat them): Joshua King 2, Elliot Anderson 2, Murillo 1 (1 headed), Calvin Bassey 1 (1 headed), Ryan Christie 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 42.7 (rank 5 of 20, 1 = highest line) · block length 24.2 (rank 19, 1 = most compact) · width 69.0. Per match: GW3 A v Ipswich Town 4-2-3-1: back line 42, front 66, length 24, width 73 (55% poss); GW4 H v Fulham 4-2-3-1: back line 45, front 69, length 24, width 64 (56% poss); GW5 A v Bournemouth 4-2-3-1: back line 40, front 66, length 26, width 73 (54% poss); GW6 H v Manchester City 4-2-3-1: back line 38, front 58, length 20, width 70 (35% poss); GW7 A v Brentford 4-2-3-1: back line 43, front 70, length 27, width 71 (60% poss); GW8 H v Brighton & Hove Albion 4-2-3-1: back line 37, front 56, length 19, width 67 (36% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 2 league match(es) v LB-coded sides — xG 1.22/match and 2.0 pts/match v 1.61 and 1.8 against the rest → **struggles — chance creation drops** (threshold: xG v LB at least 90% of the rest). GW2 H v Nottingham Forest 2–2, xG 1.75, box shots 8, poss 69%; GW3 A v Ipswich Town 2–0, xG 0.69, box shots 5, poss 55%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Wirtz 6, Szoboszlai 5, Ngumoha 1** · FPL editorial order: Szoboszlai #1, Mac Allister #2, Wirtz #3
- Direct free-kick shooters: **Szoboszlai 6, Allister 2** · FPL order: Szoboszlai #1, Wirtz #2, Mac Allister #3
- Penalties taken: **Szoboszlai 1** · FPL order: Szoboszlai #1, Isak #2, Gakpo #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Szoboszlai 2, Jacquet 1, Wirtz 1**
- Corner targets (headed shots from corners): **Isak 4, Allister 3, Muñoz 1, Gakpo 1** · corner shots 21
- **DISAGREEMENT:** observed corner taker Florian Wirtz (6) v FPL #1 Szoboszlai — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Cody Gakpo 4 (0.78/90, percentile 95, 461 min); Florian Wirtz 5 (0.72/90, percentile 94, 624 min); Alexis Mac Allister 4 (0.62/90, percentile 92, 578 min) · club total 14 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 289 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 7, field tilt 70.5, possession 60%, box entries 9, direct speed 2.2, SCA 50; GW2: PPDA 4.89, field tilt 72.8, possession 68.3%, box entries 12, direct speed 1.97, SCA 26; GW3: PPDA 10.88, field tilt 58, possession 54.1%, box entries 8, direct speed 1.83, SCA 19; GW4: PPDA 9.48, field tilt 63.3, possession 55.5%, box entries 9, direct speed 2.72, SCA 26; GW5: PPDA 9.83, field tilt 44.8, possession 53.4%, box entries 10, direct speed 2.71, SCA 24; GW6: PPDA 9.5, field tilt 35.3, possession 35.4%, box entries 6, direct speed 3.1, SCA 21; GW7: PPDA 7.29, field tilt 68.8, possession 60.1%, box entries 21, direct speed 2.3, SCA 41; GW8: PPDA 16.41, field tilt 39.5, possession 36.5%, box entries 11, direct speed 3.59, SCA 19

**Zone 14 (C13, SofaScore heat-map points, 8 league matches):** for 35.9/match (rank 5 of 20) · conceded 22.6/match (rank 18 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 6.6/match · allowed 8.4/match · PPDA 9.2. Per match for/allowed: GW3 6/5; GW4 5/9; GW5 8/8; GW6 3/11; GW7 14/9; GW8 9/16 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 8 league matches, weights last-3 ×3 / older ×1
- GK: Alisson (14, 3/3)
- DEF: Jérémy Jacquet (14, 3/3), Virgil van Dijk (14, 3/3), Miloš Kerkez (13, 3/3), Ronald Araújo (12, 3/3)
- MID: Alexis Mac Allister (12, 3/3), Ryan Gravenberch (8, 2/3), Cody Gakpo (7, 1/3), Rio Ngumoha (1, 0/3)
- FWD: Bradley Barcola (11, 3/3)
- Contested slots: F Bradley Barcola 11 v Alexander Isak 11 · Excluded (FPL flag): Florian Wirtz — Ankle injury - 75% chance of playing; Dominik Szoboszlai — Hamstring injury - Unknown return date
- Absent last match (E12, SofaScore list): Bradley (Knee Injury), Szoboszlai (Hamstring Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Frimpong (Hamstring Injury), Muñoz (injury; doubtful)
- Substitutions this season (C3): GW6 75' Lewis Koumas→Rio Ngumoha CHASING; GW6 75' Ronald Araújo→Jeremie Frimpong CARD-RISK; GW6 66' Florian Wirtz→Trey Nyoni CHASING; GW7 79' Víctor Muñoz→Joe Gomez TACTICAL; GW7 79' Alexander Isak→Lewis Koumas TACTICAL; GW7 52' Jeremie Frimpong→Rio Ngumoha INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW7 46' Ronald Araújo→Jeremie Frimpong HALF-TIME; GW7 32' Dominik Szoboszlai→Trey Nyoni INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW8 88' Miloš Kerkez→Kostas Tsimikas LATE; GW8 77' Alexander Isak→Lewis Koumas GAME-STATE; GW8 77' Bradley Barcola→Rio Ngumoha GAME-STATE; GW8 65' Florian Wirtz→Trey Nyoni INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']

### First-choice players and absences (F14) — generated 2026-10-27 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Alisson | start weight 14 | OK | a | — | — |
| CB | Jérémy Jacquet | start weight 14 | OK | a 100% | Miloš Kerkez (DEF, not a CB by heat map) | — |
| CB | Virgil van Dijk | start weight 14 | OK | a | Miloš Kerkez (DEF, not a CB by heat map) | — |
| xGI #1 | Alexander Isak | xGI 4.41 | OK | a 100% | Florian Wirtz | — |
| xGI #2 | Cody Gakpo | xGI 2.94 | OK | a 100% | Florian Wirtz | — |
| Penalties #1 (FPL) | Szoboszlai | FPL order | **OUT** | i 0% — Hamstring injury - Unknown return date | Isak | opposing defenders' negative set-piece pairing removed; own pairings built on him dropped |
| Direct FK #1 (FPL) | Szoboszlai | FPL order | **OUT** | i 0% — Hamstring injury - Unknown return date | Wirtz | opposing defenders' negative set-piece pairing removed; own pairings built on him dropped |
| Corners (observed) | Dominik Szoboszlai | 23 corners taken | **OUT** | i 0% — Hamstring injury - Unknown return date | Konstantinos Tsimikas | opposing defenders' negative corner pairing removed; own corner pairings built on him dropped |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 A Newcastle United: all started · GW2 H Nottingham Forest: all started · GW3 A Ipswich Town: all started · GW4 H Fulham: Cody Gakpo (did not start) · GW5 A Bournemouth: all started · GW6 H Manchester City: Alexander Isak (Thigh Injury), Cody Gakpo (Ankle Injury) · GW7 A Brentford: Cody Gakpo (did not start) · GW8 H Brighton & Hove Albion: all started

### Next fixtures (all competitions)
- Wed 28 Oct 20:00 UTC · EFL Cup R4 · H v Chelsea
- Sun 01 Nov 16:30 UTC · Premier League R9 · H v Arsenal
- Wed 04 Nov 17:45 UTC · UEFA Champions League R4 · A v Fenerbahçe
- Sun 08 Nov 14:00 UTC · Premier League R10 · A v Crystal Palace
- Sun 22 Nov 16:30 UTC · Premier League R11 · H v Manchester United
- Wed 25 Nov 20:00 UTC · UEFA Champions League R5 · A v Club Brugge KV

### FPL availability flags (players with league minutes this season)
Frimpong — Hamstring injury - Unknown return date (0%); Wirtz — Ankle injury - 75% chance of playing (75%); Szoboszlai — Hamstring injury - Unknown return date (0%); Munoz — Knee injury - 25% chance of playing (25%)
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
### Corner takers observed (LiveScore Block L)
- Dominik Szoboszlai: 23 corners (13 left, 10 right, 3 short)
- Konstantinos Tsimikas: 17 corners (6 left, 11 right, 3 short)
- Alexis Mac Allister: 12 corners (5 left, 7 right, 5 short)
- Florian Wirtz: 10 corners (7 left, 3 right, 2 short)
- Luke Chambers: 1 corners (0 left, 1 right)
- Milos Kerkez: 1 corners (0 left, 1 right)
