# Arsenal — data doc
*Feeder-written (2026-10-27 07:42 UTC); do not edit. Narrative: `profiles/teams/arsenal.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-10-27 07:42 UTC)
**Manager:** Mikel Arteta · **Venue:** Emirates Stadium · **SofaScore:** https://www.sofascore.com/football/team/arsenal/42 · **FPL code:** ARS
**Table:** 2nd, 21 pts (7W 0D 1L, GF 13 GA 5) · Home 1st (4-0-0, 9:2) · Away 3rd (3-0-1, 4:3)
**Standing context (F15):** 30 league games left · points v 4th +6, v 5th +8, v 17th (last safe) +14, v 18th +15 · goal difference +8
**Suspension watch (D7, all players of the club):** nobody within 2 yellows of a ban, nobody suspended [FPL]
**Goal timing & game state (F17, 8 league matches):** goals after 75′ — for 2/13 (15%), against 0/5 (0%) · scored first 5, conceded first 3 (38% of matches), goalless 0 · points from losing positions 6 of 9 (3 matches behind at some point) · points from winning positions 21 of 21 (7 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Gabriel (DEF) 9.0/90, hit 4/8; Konsa (DEF) 6.5/90, hit 2/7; Rice (MID) 8.7/90, hit 1/8
**Manager tenure (F13, SofaScore):** Mikel Arteta since 22 Dec 2019 · 365 matches in charge, all competitions (228W 61D 76L) · 8 league matches this season · contract to 30 Jun 2030 · previous club — · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Tottenham Hotspur — last 4: Feb 2026 Premier League Tottenham Hotspur 1–4 Arsenal (yellows 2–1, xG 0.76–2.07); Nov 2025 Premier League Arsenal 4–1 Tottenham Hotspur (yellows 1–3, xG 1.93–0.07); Jan 2025 Premier League Arsenal 2–1 Tottenham Hotspur (yellows 3–1, xG 1.45–0.78); Sep 2024 Premier League Tottenham Hotspur 0–1 Arsenal (yellows 5–3, xG 0.71–0.74) · 19 yellows in 4 | v Chelsea — last 4: Sep 2026 Premier League Arsenal 2–1 Chelsea (yellows 2–4, xG 2.05–0.39); Mar 2026 Premier League Arsenal 2–1 Chelsea (yellows 1–5, reds 0–1, xG 1.09–1.07); Feb 2026 EFL Cup Arsenal 1–0 Chelsea (yellows 0–3, xG 1.14–1.02); Jan 2026 EFL Cup Chelsea 2–3 Arsenal (yellows 4–4, xG 0.85–2.58) · 23 yellows in 4
**Archetype (F5):** used **PM** — derived PM [DERIVED] · signals, last 6 league matches: possession 60.3%, PPDA 9.7 (Understat, 6 matches; lower = harder press), opponent offsides forced 1.5/match (line height), fast breaks 1.5/match (season), both sides' xG 2.78/match (openness) · note: PPDA 9.7 v HP cut 9.1. Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap).
**Squad changes (F20, since 01 Jun 2026):** in 11 (permanent 6, loan 0, free 0, loan returns 5) · out 12 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 8 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 13.91 | 4 | Big chances against | 11 | 1 |
| xGOT | 12.79 | 5 | Box shots against | 47 | 1 |
| xA | 10.75 | 2 | Corners against | 31 | 2 |
| Shots | 107 | 11 | Crosses faced | 119 | 3 |
| SoT | 35 | 9 | Dribbled past | 35 | 1 |
| Big chances | 20 | 9 | Errors→shot | 13 | 20 |
| Shots in box | 73 | 9 | GK goals prevented | 1.52 | 3 |
| Corners | 45 | 5 | Clearances | 159 | 18 |
| Crosses | 139 | 12 | Tackles | 93 | 19 |
| Fast breaks | 12 | 5 | Interceptions | 56 | 18 |
| FK shots | 2 | 11 | Def. contributions | 330 | 19 |
| Possession % | 60.88 | 2 | Aerial % | 50 | 9 |
| Pass % | 87.04 | 3 | Duel % | 52.05 | 3 |
| Long balls | 202 | 19 | Fouls | 82 | 4 |
| Dribbles | 45 | 17 | Yellows | 10 | 2 |
| Shots against | 86 | 3 | Km covered | 955 | 1 |
| SoT against | 24 | 1 | Sprints | 857 | 11 |
Per match: xG 1.74 · xGOT 1.60 · shots 13.4 · shots against 10.8 · big chances 2.5 for / 1.4 against · corners 5.6 / 3.9 · crosses 17.4 / 14.9 · possession 60.875%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Chelsea | 2–1 | 2.11/2.87 | 0.35/0.43 | 55 | 16/13 | 9/5 | 13/5 | 6/2 | 4/1 | 5/3 | 16/4 v 14/1 | 0/3 |
| 4 | A | Sunderland | 2–0 | 1.88/1.99 | 1.80/2.07 | 57 | 11/12 | 5/3 | 8/7 | 2/4 | 3/3 | 2/4 | 7/3 v 16/5 | 2/2 |
| 5 | A | Brighton & Hove Albion | 0–3 | 1.63/1.29 | 1.31/2.25 | 60 | 11/17 | 2/5 | 10/10 | 5/3 | 2/3 | 6/5 | 16/6 v 15/6 | 0/2 |
| 6 | H | Leeds United | 2–1 | 2.33/2.32 | 0.62/1.20 | 58 | 13/11 | 6/5 | 8/7 | 3/3 | 4/2 | 2/4 | 15/7 v 23/6 | 4/7 |
| 7 | A | Nottingham Forest | 1–0 | 1.14/0.92 | 0.90/0.75 | 74 | 9/14 | 1/2 | 7/8 | 3/6 | 1/0 | 6/8 | 27/7 v 14/1 | 2/1 |
| 8 | H | Everton | 2–0 | 1.96/2.29 | 0.63/0.72 | 58 | 20/8 | 4/3 | 12/6 | 10/2 | 3/2 | 12/3 | 23/5 v 16/2 | 1/0 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Chelsea | 2–1 | 4-2-3-1 | 13/16 | 2/4 | 0/0 | 457/379 | 59/46 | Timber (Ankle Injury), Saliba (Back Injury), Mosquera (Knock Injury; doubtful) | Henderson (Wrist Injury), Palestra (Physical Discomfort; doubtful), Caicedo (Knock Injury; doubtful) | Chris Kavanagh |
| 4 | A | Sunderland | 2–0 | 4-2-3-1 | 11/18 | 2/6 | 0/1 | 386/284 | 44/50 | Saliba (Back Injury), Mosquera (Knock Injury; doubtful) | Diarra (Hamstring Injury), Mundle (Knee Injury) | John Brooks |
| 5 | A | Brighton & Hove Albion | 0–3 | 4-2-3-1 | 11/13 | 1/4 | 0/0 | 511/343 | 51/62 | Saliba (Back Injury), White (Groin Injury; doubtful) | Ferguson (Ankle Injury), Azeez (Muscle Injury), Hinshelwood (Knock Injury), Mitoma (Hamstring Injury), Wieffer (Knee Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Yohanna (Knock Injury) | Darren England |
| 6 | H | Leeds United | 2–1 | 4-2-3-1 | 12/20 | 1/4 | 0/0 | 512/356 | 54/54 | Tzolis (Hamstring Injury), Saliba (Back Injury) | Rodon (Hamstring Injury), Joseph (Knee Injury), James (Back Injury; doubtful) | Paul Tierney |
| 7 | A | Nottingham Forest | 1–0 | 4-2-3-1 | 8/14 | 1/1 | 0/0 | 634/224 | 76/33 | Tzolis (Hamstring Injury), Hincapié (Ankle Injury) | Jesus (Calf Injury), Savona (Knee Injury), Gibbs-White (Knock Injury; doubtful) | Michael Oliver |
| 8 | H | Everton | 2–0 | 4-2-3-1 | 11/13 | 1/3 | 0/0 | 518/372 | 65/48 | Saka (Muscle Injury), Tzolis (Hamstring Injury), Saliba (Back Injury) | — | Tony Harrington |
Per match: fouls 10.2 / 15.5 · yellows 1.25 / 3.25 · reds 0 / 1 (season) · offsides forced 1.1, committed 3.5 · crosses attempted 17.4 / faced 14.9. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 2.07 for / 0.45 against per match · Away (4): xG 1.42 / 1.08. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW8 H v Everton 2–0 (Sat 24 Oct 14:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| David Raya | G | 90 | 7.3 | 0.00 | 0.00 | 0 | 0 | 1 | 0 | 35 |
| Ben White | D | 90 | 7.7 | 0.00 | 0.36 | 3 | 0 | 5 | 2 | 69 |
| Ezri Konsa | D | 90 | 8.1 | 0.38 | 0.00 | 0 | 2 | 2 | 0 | 51 |
| Gabriel Magalhães | D | 90 | 9 | 0.54 | 0.02 | 0 | 2 | 14 | 0 | 71 |
| Myles Lewis-Skelly | D | 68 | 7.4 | 0.00 | 0.06 | 1 | 0 | 4 | 2 | 55 |
| Declan Rice | M | 80 | 8.2 | 0.04 | 0.49 | 4 | 1 | 3 | 8 | 70 |
| Mikel Merino | M | 68 | 6.6 | 0.52 | 0.07 | 0 | 5 | 0 | 1 | 41 |
| Noni Madueke | M | 90 | 6.3 | 0.16 | 0.06 | 2 | 3 | 1 | 2 | 49 |
| Martin Ødegaard | M | 90 | 8 | 0.26 | 0.42 | 2 | 5 | 0 | 6 | 116 |
| Eberechi Eze | M | 80 | 6.9 | 0.05 | 0.15 | 1 | 2 | 1 | 2 | 45 |
| Viktor Gyökeres | F | 68 | 6.4 | 0.00 | 0.06 | 3 | 0 | 0 | 0 | 17 |
Subs used: Riccardo Calafiori (22'), Bruno Guimarães (22'), Kai Havertz (22'), Martín Zubimendi (10'), Max Dowman (10')
Goals: 7' Ezri Konsa (assist Viktor Gyökeres) [own]; 68' Gabriel Magalhães (assist Ben White) [own]
Substitutions (own): 68' Riccardo Calafiori for Myles Lewis-Skelly; 68' Kai Havertz for Viktor Gyökeres; 68' Bruno Guimarães for Mikel Merino; 80' Max Dowman for Eberechi Eze; 80' Martín Zubimendi for Declan Rice
Cards: -5' booking with no player named — staff card (yellow, opp; not in SofaScore's card count, no FPL effect); manager/staff booking: Mikel Arteta 64' [LiveScore] (own; no FPL effect); 45' Vitaliy Mykolenko (yellow, opp); 58' Myles Lewis-Skelly (yellow, own); 66' James Garner (yellow, opp); 79' James Tarkowski (yellow, opp)
**Baseline XI change vs GW7 (4-2-3-1 → 4-2-3-1):** in — Mikel Merino, Myles Lewis-Skelly, Noni Madueke, Viktor Gyökeres; out — Bruno Guimarães, Bukayo Saka, Kai Havertz, Riccardo Calafiori.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 3 | H Chelsea | 2' | AGAINST | Morgan Rogers | Jorrel Hato | set piece | 0.04 |
| 3 | H Chelsea | 25' | FOR | Kai Havertz | Declan Rice | open play | 0.04 |
| 3 | H Chelsea | 50' | FOR | Martin Ødegaard | Christos Tzolis | open play | 0.56 |
| 4 | A Sunderland | 58' | FOR | Bruno Guimarães | Declan Rice | open play | 0.03 |
| 4 | A Sunderland | 90' | FOR | Bukayo Saka | — | penalty | 0.76 |
| 5 | A Brighton & Hove Albion | 31' | AGAINST | Pascal Groß | Charalampos Kostoulas | open play | 0.03 |
| 5 | A Brighton & Hove Albion | 45' | AGAINST | Charalampos Kostoulas | Diego Gómez | open play | 0.05 |
| 5 | A Brighton & Hove Albion | 57' | AGAINST | Chema Andrés | Pascal Groß | corner | 0.53 |
| 6 | H Leeds United | 55' | AGAINST | James Justin | Gabriel Gudmundsson | open play | 0.25 |
| 6 | H Leeds United | 62' | FOR | Riccardo Calafiori | Ben White | open play | 0.58 |
| 6 | H Leeds United | 70' | FOR | Bruno Guimarães | Declan Rice | open play | 0.06 |
| 7 | A Nottingham Forest | 80' | FOR | Noni Madueke | Declan Rice | open play | 0.04 |
| 8 | H Everton | 7' | FOR | Ezri Konsa | Viktor Gyökeres | [unmatched] | — |
| 8 | H Everton | 68' | FOR | Gabriel Magalhães | Ben White | [unmatched] | — |
Scored 13: open play 10, [unmatched] 2, penalty 1 · Conceded 5: open play 3, set piece 1, corner 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW6 AG v Leeds United 55' James Justin (assist Gabriel Gudmundsson, key pass Noah Okafor): G O O O A A A L - James Justin scores with the right foot! · before: 55' Gabriel Gudmundsson creates a scoring opportunity for his teammate ‹ 55' Leeds with a potentially dangerous attack. ‹ 54' Declan Rice makes the tackle and wins possession for his team
- GW6 FOR v Leeds United 62' Riccardo Calafiori (assist Ben White, key pass Noni Madueke): G O O O A A A L - Riccardo Calafiori volleys the ball into the back of the net with the left. A great finish! · before: 62' Ben White creates a scoring opportunity for his teammate ‹ 62' The cross by Noni Madueke from Arsenal successfully finds a teammate in the box. ‹ 62' James Justin successfully blocks the shot
- GW6 FOR v Leeds United 70' Bruno Guimarães (assist Declan Rice, key pass Martin Oedegaard): G O O O A A A L - Bruno Guimaraes scores with the right foot! · before: 70' Declan Rice creates a scoring opportunity for his teammate ‹ 70' Arsenal with a potentially dangerous attack. ‹ 70' James Justin is penalised for pushing Bruno Guimaraes.
- GW7 FOR v Nottingham Forest 80' Noni Madueke (assist Declan Rice): GOAL! - Noni Madueke score from a shot with the right foot, that takes a deflection. · before: 80' Jair Cunha from Nottingham Forest intercepts a cross aimed towards the box. ‹ 79' Daniel Munoz from Nottingham Forest intercepts a cross aimed towards the box. ‹ 79' Jair Cunha successfully blocks the shot
- GW8 FOR v Everton 7' Ezri Konsa (assist Viktor Gyoekeres): G O O O A A A L - Ezri Konsa scores with the right foot! · before: 7' Gabriel from Arsenal sees his header hit the crossbar after the keeper parries the ball. ‹ 7' Martin Oedegaard from Arsenal swings in the corner from the right. ‹ 7' Vitaliy Mykolenko from Everton intercepts a cross aimed towards the box.
- GW8 FOR v Everton 68' Gabriel Magalhães (assist Ben White, key pass Bruno Guimaraes): G O O O A A A L - Gabriel from Arsenal heads the ball home! · before: 68' Ben White creates a scoring opportunity for his teammate ‹ 68' Jake O'Brien from Everton intercepts a cross aimed towards the box. ‹ 68' Declan Rice swings in the ball from a corner on the left, but it is nowhere near a teammate

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW3 H v Chelsea 2' Morgan Rogers: no structured culprit — reports only
  · GW3 other flags: Ezri Konsa lastManTackle 1; Bukayo Saka errorLeadToAShot 1; Myles Lewis-Skelly errorLeadToAShot 1
- GW5 A v Brighton & Hove Albion 31' Pascal Groß: no structured culprit — reports only
- GW5 A v Brighton & Hove Albion 45' Charalampos Kostoulas: no structured culprit — reports only
- GW5 A v Brighton & Hove Albion 57' Chema Andrés: no structured culprit — reports only
  · GW5 other flags: David Raya errorLeadToAShot 1, lastManTackle 1; Ezri Konsa errorLeadToAShot 1; Bruno Guimarães errorLeadToAShot 1; Gabriel Magalhães lastManTackle 1; Riccardo Calafiori errorLeadToAShot 1
- GW6 H v Leeds United 55' James Justin: no structured culprit — reports only
  · GW6 other flags: Ezri Konsa lastManTackle 1; Declan Rice errorLeadToAShot 1

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 79 | 10.70 | 11 | 63 | 5.55 | 3 |
| corner | 20 | 2.19 | 1 | 13 | 1.57 | 1 |
| set piece | 5 | 1.26 | 0 | 6 | 0.19 | 1 |
| direct FK | 2 | 0.13 | 0 | 3 | 0.18 | 0 |
| penalty | 1 | 0.76 | 1 | 1 | 0.76 | 0 |
Totals per match: xG 1.88 (npxG 1.79) for, xGA 1.03 (np 0.94) against · dead-ball share of xG 29% for, 33% against · penalties won 1, conceded 1 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 20 shots, xG 2.19, 1 goals, headed 11: 6-yard box, central 8 shots, xG 1.40, 1 goals; penalty area, central 6 shots, xG 0.65, 0 goals; outside box, left 2 shots, xG 0.05, 0 goals · against — 13 shots conceded, xG 1.57, 1 goals, headed 3: 6-yard box, central 3 shots, xG 1.09, 1 goals; penalty area, central 4 shots, xG 0.33, 0 goals; penalty area, right 1 shots, xG 0.07, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 31 · corner shots conceded 13 (headed 3), xG 1.57, goals 1 · xG per corner faced 0.051 (rank 11 of 20, 1 = weakest) · weak zone: six-yard box (1.09 xG, 69% of theirs v 65% league) · signal: **neutral** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–8 [CONFIRMED — LiveScore Block L, 63 corners; side L/R as LiveScore records it; foot from SofaScore]: Declan Rice 30 (30L/0R, 4 short, right foot); Bukayo Saka 19 (0L/19R, 4 short, left foot); Martin Oedegaard 7 (0L/7R); Noni Madueke 6 (0L/6R, 1 short, left foot). First contact on corners that ended in a shot (Understat) — for: Gabriel 4 (3 headed), Riccardo Calafiori 3 (2 headed), Ezri Konsa Ngoyo 3 (2 headed) — 1 goal, Kai Havertz 2 (2 headed), Christos Tzolis 2 · against (who beat them): Murillo 2 (1 headed), Nordi Mukiele 2, Chema Andres 1 (1 headed) — 1 goal, Pascal Struijk 1 (1 headed), Reece James 1. Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 45.7 (rank 2 of 20, 1 = highest line) · block length 20.8 (rank 10, 1 = most compact) · width 64.7. Per match: GW3 H v Chelsea 4-2-3-1: back line 50, front 71, length 22, width 66 (55% poss); GW4 A v Sunderland 4-2-3-1: back line 42, front 66, length 24, width 68 (57% poss); GW5 A v Brighton & Hove Albion 4-2-3-1: back line 41, front 61, length 20, width 61 (60% poss); GW6 H v Leeds United 4-2-3-1: back line 47, front 67, length 21, width 67 (58% poss); GW7 A v Nottingham Forest 4-2-3-1: back line 47, front 67, length 19, width 68 (74% poss); GW8 H v Everton 4-2-3-1: back line 46, front 65, length 19, width 58 (58% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 2 league match(es) v LB-coded sides — xG 1.51/match and 3.0 pts/match v 1.82 and 2.5 against the rest → **struggles — chance creation drops** (threshold: xG v LB at least 90% of the rest). GW1 H v Coventry City 3–0, xG 1.88, box shots 10, poss 64%; GW7 A v Nottingham Forest 1–0, xG 1.14, box shots 7, poss 74%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Saka 5, Rice 5, White 1** · FPL editorial order: Rice #1, Saka #2, Ødegaard #3
- Direct free-kick shooters: **Eze 1, Odegaard 1** · FPL order: Rice #1, Saka #2, Eze #3
- Penalties taken: **Saka 1** · FPL order: Saka #1, Gyökeres #2, Ødegaard #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Rice 2, Odegaard 1**
- Corner targets (headed shots from corners): **Gabriel 3, Calafiori 2, Havertz 2, Ngoyo 2** · corner shots 20
- **DISAGREEMENT:** observed corner taker Bukayo Saka (5) v FPL #1 Rice — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Bruno Guimarães 3 (1.13/90, percentile 98, 239 min); Martin Ødegaard 8 (1.11/90, percentile 98, 651 min); Bukayo Saka 3 (0.45/90, percentile 87, 598 min); Myles Lewis-Skelly 2 (0.45/90, percentile 86, 404 min) · club total 23 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 289 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 9.72, field tilt 68.9, possession 64.7%, box entries 21, direct speed 1.71, SCA 40; GW2: PPDA 12.67, field tilt 64.4, possession 61.1%, box entries 13, direct speed 2.2, SCA 13; GW3: PPDA 9.5, field tilt 59.8, possession 54.6%, box entries 21, direct speed 3.05, SCA 32; GW4: PPDA 7.5, field tilt 54.6, possession 56.9%, box entries 15, direct speed 2.08, SCA 20; GW5: PPDA 12.57, field tilt 54.9, possession 60%, box entries 13, direct speed 1.82, SCA 21; GW6: PPDA 9.81, field tilt 70.8, possession 58.2%, box entries 20, direct speed 2.78, SCA 26; GW7: PPDA 7.12, field tilt 76.3, possession 73.3%, box entries 12, direct speed 1.77, SCA 18; GW8: PPDA 8.24, field tilt 65.1, possession 58.4%, box entries 21, direct speed 2.43, SCA 40

**Zone 14 (C13, SofaScore heat-map points, 8 league matches):** for 31.4/match (rank 7 of 20) · conceded 25.1/match (rank 15 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 12.1/match · allowed 4.2/match · PPDA 9.7. Per match for/allowed: GW3 17/5; GW4 5/5; GW5 10/6; GW6 11/1; GW7 10/6; GW8 18/4 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 8 league matches, weights last-3 ×3 / older ×1
- GK: David Raya (14, 3/3)
- DEF: Gabriel Magalhães (14, 3/3), Ben White (13, 3/3), Ezri Konsa (12, 3/3), Cristhian Mosquera (2, 0/3)
- MID: Declan Rice (14, 3/3), Martin Ødegaard (14, 3/3), Myles Lewis-Skelly (10, 2/3), Eberechi Eze (6, 2/3), Bruno Guimarães (4, 1/3)
- FWD: Kai Havertz (11, 2/3)
- Contested slots: D Cristhian Mosquera 2 v Jurriën Timber 1; M Bruno Guimarães 4 v Mikel Merino 3 · Excluded (FPL flag): Riccardo Calafiori — Hip injury - 75% chance of playing; Bukayo Saka — Thigh injury - Unknown return date; Christos Tzolis — Hamstring injury - Expected back 1 Nov
- Absent last match (E12, SofaScore list): Saka (Muscle Injury), Tzolis (Hamstring Injury), Saliba (Back Injury)
- Substitutions this season (C3): GW6 63' Myles Lewis-Skelly→Bruno Guimarães TACTICAL; GW6 63' Kai Havertz→Viktor Gyökeres TACTICAL; GW6 63' Ben White→Jurriën Timber TACTICAL; GW7 66' Bruno Guimarães→Mikel Merino TACTICAL; GW7 66' Kai Havertz→Viktor Gyökeres TACTICAL; GW7 66' Ben White→Jurriën Timber TACTICAL; GW7 46' Eberechi Eze→Noni Madueke HALF-TIME; GW8 80' Eberechi Eze→Max Dowman GAME-STATE; GW8 80' Declan Rice→Martín Zubimendi GAME-STATE; GW8 68' Myles Lewis-Skelly→Riccardo Calafiori CARD-RISK; GW8 68' Viktor Gyökeres→Kai Havertz GAME-STATE; GW8 68' Mikel Merino→Bruno Guimarães GAME-STATE

### First-choice players and absences (F14) — generated 2026-10-27 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | David Raya | start weight 14 | OK | a | — | — |
| CB | Gabriel Magalhães | start weight 14 | OK | a | Cristhian Mosquera | — |
| CB | Ezri Konsa | start weight 12 | OK | a 100% | Cristhian Mosquera | — |
| xGI #1 | Bukayo Saka | xGI 4.85 | **OUT** | i 0% — Thigh injury - Unknown return date | Kai Havertz | +0.5 to defenders and GK facing them (cap +1.0); P(CS) with his xGI share removed |
| xGI #2 | Martin Ødegaard | xGI 4.15 | OK | a | Kai Havertz | — |
| Penalties #1 (FPL) | Saka | FPL order | **OUT** | i 0% — Thigh injury - Unknown return date | Gyökeres | opposing defenders' negative set-piece pairing removed; own pairings built on him dropped |
| Direct FK #1 (FPL) | Rice | FPL order | OK | a 100% | Eze | — |
| Corners (observed) | Declan Rice | 30 corners taken | OK | a 100% | Bukayo Saka | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Coventry City: Ezri Konsa (did not start) · GW2 A Aston Villa: Ezri Konsa (did not start) · GW3 H Chelsea: all started · GW4 A Sunderland: all started · GW5 A Brighton & Hove Albion: all started · GW6 H Leeds United: all started · GW7 A Nottingham Forest: all started · GW8 H Everton: Bukayo Saka (Muscle Injury)

### Next fixtures (all competitions)
- Tue 27 Oct 20:00 UTC · EFL Cup R4 · A v Fleetwood Town
- Sun 01 Nov 16:30 UTC · Premier League R9 · A v Liverpool FC
- Wed 04 Nov 20:00 UTC · UEFA Champions League R4 · A v SK Slavia Praha
- Sat 07 Nov 15:00 UTC · Premier League R10 · H v Hull City
- Sat 21 Nov 17:30 UTC · Premier League R11 · A v Newcastle United
- Tue 24 Nov 20:00 UTC · UEFA Champions League R5 · H v Borussia Dortmund

### FPL availability flags (players with league minutes this season)
Calafiori — Hip injury - 75% chance of playing (75%); Saka — Thigh injury - Unknown return date (0%); Tzolis — Hamstring injury - Expected back 1 Nov (0%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 H Coventry City 3–0 · xG 1.88–0.20 · poss 64% · 4-2-3-1 · scorers: Kai Havertz 15', Bukayo Saka 23', Martin Ødegaard 49'
- GW2 A Aston Villa 1–0 · xG 1.04–0.33 · poss 61% · 4-2-3-1 · scorers: Bukayo Saka 59'
- GW3 H Chelsea 2–1 · xG 2.11–0.35 · poss 55% · 4-2-3-1 · scorers: Kai Havertz 25', Martin Ødegaard 50'
- GW4 A Sunderland 2–0 · xG 1.88–1.80 · poss 57% · 4-2-3-1 · scorers: Bruno Guimarães 58', Bukayo Saka 90'
- GW5 A Brighton & Hove Albion 0–3 · xG 1.63–1.31 · poss 60% · 4-2-3-1 · scorers: none
- GW6 H Leeds United 2–1 · xG 2.33–0.62 · poss 58% · 4-2-3-1 · scorers: Riccardo Calafiori 62', Bruno Guimarães 70'
- GW7 A Nottingham Forest 1–0 · xG 1.14–0.90 · poss 74% · 4-2-3-1 · scorers: Noni Madueke 80'
- GW8 H Everton 2–0 · xG 1.96–0.63 · poss 58% · 4-2-3-1 · scorers: Ezri Konsa 7', Gabriel Magalhães 68'
### Corner takers observed (LiveScore Block L)
- Declan Rice: 30 corners (30 left, 0 right, 4 short)
- Bukayo Saka: 19 corners (0 left, 19 right, 4 short)
- Martin Oedegaard: 7 corners (0 left, 7 right)
- Noni Madueke: 6 corners (0 left, 6 right, 1 short)
- Max Dowman: 1 corners (0 left, 1 right)
