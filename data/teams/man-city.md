# Manchester City — data doc
*Feeder-written (2026-11-10 07:41 UTC); do not edit. Narrative: `profiles/teams/man-city.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-10 07:41 UTC)
**Manager:** Enzo Maresca · **Venue:** Etihad Stadium · **SofaScore:** https://www.sofascore.com/football/team/manchester-city/17 · **FPL code:** MCI
**Table:** 3rd, 21 pts (7W 0D 3L, GF 21 GA 13) · Home 3rd (4-0-1, 11:7) · Away 4th (3-0-2, 10:6)
**Standing context (F15):** 28 league games left · points v 4th +3, v 5th +5, v 17th (last safe) +12, v 18th +13 · goal difference +8
**Suspension watch (D7, all players of the club):** nobody within 2 yellows of a ban, nobody suspended [FPL]
**Goal timing & game state (F17, 10 league matches):** goals after 75′ — for 5/21 (24%), against 1/13 (8%) · scored first 6, conceded first 4 (40% of matches), goalless 0 · points from losing positions 3 of 12 (4 matches behind at some point) · points from winning positions 21 of 21 (7 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Anderson (MID) 11.7/90, hit 3/10; Ndiaye (MID) 8.1/90, hit 2/10; Khusanov (DEF) 8.0/90, hit 2/7; Matheus N. (DEF) 6.8/90, hit 1/7
**Manager tenure (F13, SofaScore):** Enzo Maresca since 01 Jul 2026 · 16 matches in charge, all competitions (12W 0D 4L) · 10 league matches this season · contract to 30 Jun 2029 · previous club Chelsea · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Manchester United — last 4: Sep 2026 Premier League Manchester United 0–1 Manchester City (yellows 1–2, reds 0–1, xG 1.00–1.10); Jan 2026 Premier League Manchester United 2–0 Manchester City (yellows 2–3, xG 2.27–0.45); Sep 2025 Premier League Manchester City 3–0 Manchester United (yellows 0–0, xG 2.63–1.52); Apr 2025 Premier League Manchester United 0–0 Manchester City (yellows 3–2, xG 0.91–0.49) · 13 yellows in 4
**Archetype (F5):** used **PM** — last week's PM HELD by the margin rule (Q-86) — derived HP is inside the borderline band · signals, last 6 league matches: possession 65.7%, PPDA 9.3 (Understat, 4 matches; lower = harder press), opponent offsides forced 2.0/match (line height), fast breaks 1.2/match (season), both sides' xG 3.57/match (openness) · note: PPDA 9.3 v HP cut 9.3; computed from 4 of 6 GWs (no PPDA/possession for GW9, GW10). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 17 (permanent 10, loan 0, free 0, loan returns 7) · out 19 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 10 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 20.08 | 1 | Big chances against | 26 | 11 |
| xGOT | 19.01 | 3 | Box shots against | 70 | 4 |
| xA | 15.93 | 1 | Corners against | 38 | 1 |
| Shots | 150 | 6 | Crosses faced | 137 | 2 |
| SoT | 54 | 2 | Dribbled past | 66 | 5 |
| Big chances | 38 | 1 | Errors→shot | 6 | 7 |
| Shots in box | 116 | 1 | GK goals prevented | -0.83 | 13 |
| Corners | 61 | 3 | Clearances | 177 | 20 |
| Crosses | 192 | 6 | Tackles | 132 | 17 |
| Fast breaks | 12 | 8 | Interceptions | 65 | 20 |
| FK shots | 2 | 16 | Def. contributions | 396 | 20 |
| Possession % | 65.50 | 1 | Aerial % | 54.22 | 4 |
| Pass % | 88.74 | 1 | Duel % | 51.60 | 6 |
| Long balls | 305 | 11 | Fouls | 108 | 6 |
| Dribbles | 119 | 1 | Yellows | 13 | 2 |
| Shots against | 106 | 3 | Km covered | 1126 | 18 |
| SoT against | 39 | 8 | Sprints | 1031 | 17 |
Per match: xG 2.01 · xGOT 1.90 · shots 15.0 · shots against 10.6 · big chances 3.8 for / 2.6 against · corners 6.1 / 3.8 · crosses 19.2 / 13.7 · possession 65.5%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | H | Sunderland | 5–3 | 2.82/2.67 | 3.57/3.38 | 55 | 16/17 | 6/9 | 12/14 | 5/3 | 3/8 | 6/5 | 19/4 v 17/5 | 0/0 |
| 6 | A | Liverpool FC | 3–0 | 1.28/1.59 | 0.94/0.76 | 65 | 15/13 | 4/6 | 8/6 | 4/4 | 3/0 | 6/5 | 12/2 v 13/2 | 2/2 |
| 7 | H | Ipswich Town | 3–2 | 3.35/4.01 | 1.86/1.37 | 70 | 19/8 | 6/3 | 15/7 | 6/1 | 6/3 | 2/3 | 20/8 v 15/5 | 5/2 |
| 8 | A | Aston Villa | 1–2 | 1.56/2.29 | 0.61/0.65 | 64 | 15/8 | 7/2 | 12/6 | 4/3 | 4/2 | 7/4 | 22/9 v 5/0 | 1/2 |
| 9 | H | Brighton & Hove Albion | 0–1 | 1.64/— | 1/— | 62 | 21/7 | 6/3 | 19/6 | 8/1 | 5/4 | 8/2 | 24/10 v 7/2 | 2/2 |
| 10 | A | Nottingham Forest | 1–3 | 1.76/— | 1.06/— | 78 | 12/11 | 4/5 | 10/7 | 4/3 | 3/1 | 7/3 | 23/7 v 12/2 | 2/0 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | H | Sunderland | 5–3 | 4-2-3-1 | 14/14 | 0/1 | 0/0 | 475/388 | 40/47 | Foden (ban (red)) | Mandava (ban (cards)), Diarra (Hamstring Injury), Mundle (Knee Injury) | Robert Jones |
| 6 | A | Liverpool FC | 3–0 | 4-2-3-1 | 14/19 | 2/4 | 0/1 | 562/301 | 48/41 | Foden (ban (red)) | Isak (Thigh Injury), Gakpo (Ankle Injury), Bradley (Knee Injury), Szoboszlai (Hamstring Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury) | Chris Kavanagh |
| 7 | H | Ipswich Town | 3–2 | 4-2-3-1 | 8/16 | 1/2 | 0/0 | 753/319 | 85/39 | — | — | Farai Hallam |
| 8 | A | Aston Villa | 1–2 | 4-2-3-1 | 17/21 | 4/4 | 0/0 | 543/314 | 48/26 | Semenyo (Leg Injury), Nunes (Physical Discomfort; doubtful) | Wan-Bissaka (Hamstring Injury), Onana (Cruciate Ligament Injury), Ruggeri (Hamstring Injury) | Peter Bankes |
| 9 | H | Brighton & Hove Albion | 0–1 | 4-3-3 | 9/13 | 0/3 | 0/0 | 611/373 | 63/36 | Semenyo (Leg Injury) | Ferguson (Ankle Injury), Azeez (Muscle Injury), Kadıoğlu (Hip Injury), Mitoma (Hamstring Injury), Struijk (Lack of Fitness), Tzimas (Cruciate Ligament Injury), Yohanna (Knock Injury) | Craig Pawson |
| 10 | A | Nottingham Forest | 1–3 | 4-2-3-1 | 7/13 | 0/4 | 0/0 | 771/208 | 79/38 | Semenyo (Leg Injury) | Domínguez (Knock Injury), Savona (Knee Injury) | Samuel Barrott |
Per match: fouls 10.8 / 14.9 · yellows 1.30 / 2.40 · reds 1 / 1 (season) · offsides forced 2.2, committed 1.6 · crosses attempted 19.2 / faced 13.7. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 2.44 for / 1.69 against per match · Away (5): xG 1.58 / 0.85. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW10 A v Nottingham Forest 1–3 (Sat 07 Nov 17:30 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Gianluigi Donnarumma | G | 90 | 5.6 | 0.00 | 0.00 | 0 | 0 | 2 | 0 | 35 |
| Abdukodir Khusanov | D | 90 | 6.8 | 0.00 | 0.19 | 1 | 0 | 4 | 2 | 112 |
| Rúben Dias | D | 90 | 6.4 | 0.00 | 0.02 | 0 | 0 | 4 | 0 | 138 |
| Marc Guéhi | D | 45 | 6.8 | 0.00 | 0.34 | 2 | 0 | 1 | 1 | 63 |
| Joško Gvardiol | D | 45 | 5.7 | 0.00 | 0.00 | 0 | 0 | 4 | 0 | 27 |
| Enzo Fernández | M | 78 | 6.2 | 0.58 | 0.08 | 1 | 2 | 2 | 7 | 87 |
| Elliot Anderson | M | 90 | 7.5 | 0.09 | 0.24 | 0 | 1 | 4 | 0 | 126 |
| Iliman Ndiaye | M | 90 | 6.8 | 0.00 | 0.09 | 2 | 0 | 1 | 5 | 70 |
| Rayan Cherki | M | 90 | 7.6 | 0.16 | 0.05 | 2 | 1 | 2 | 2 | 85 |
| Jérémy Doku | M | 90 | 6.3 | 0.16 | 0.05 | 0 | 1 | 1 | 3 | 68 |
| Erling Haaland | F | 90 | 6.7 | 0.50 | 0.02 | 0 | 4 | 0 | 0 | 18 |
Subs used: Matheus Nunes (45'), Nico O'Reilly (45'), Phil Foden (12')
Goals: 6' Jair [opp]; 18' Liam Delap (assist Xaver Schlager) [opp]; 52' Rayan Cherki [own]; 73' Liam Delap (assist Morgan Gibbs-White) [opp]
Substitutions (own): 46' Matheus Nunes for Marc Guéhi; 46' Nico O'Reilly for Joško Gvardiol; 78' Phil Foden for Enzo Fernández
Cards: 64' James McAtee (yellow, opp); 69' Dan Ndoye (yellow, opp); 90' Igor Jesus (yellow, opp); 90' Luca Netz (yellow, opp)
**Baseline XI change vs GW9 (4-3-3 → 4-2-3-1):** in — Marc Guéhi, Rayan Cherki; out — Ayyoub Bouaddi, Matheus Nunes.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 5 | H Sunderland | 9' | FOR | Enzo Fernández | — | direct FK | 0.06 |
| 5 | H Sunderland | 12' | AGAINST | Brian Brobbey | Enzo Le Fée | open play | 0.47 |
| 5 | H Sunderland | 29' | FOR | Rayan Cherki | Antoine Semenyo | open play | 0.11 |
| 5 | H Sunderland | 33' | AGAINST | Brian Brobbey | Thomas Meunier | open play | 0.52 |
| 5 | H Sunderland | 43' | FOR | Antoine Semenyo | Marc Guéhi | corner | 0.07 |
| 5 | H Sunderland | 57' | FOR | Antoine Semenyo | — | open play | 0.07 |
| 5 | H Sunderland | 59' | AGAINST | Brian Brobbey | Nilson Angulo | open play | 0.93 |
| 5 | H Sunderland | 81' | FOR | Erling Haaland | Joško Gvardiol | open play | 0.75 |
| 6 | A Liverpool FC | 65' | FOR | Erling Haaland | — | open play | 0.09 |
| 6 | A Liverpool FC | 68' | FOR | Jérémy Doku | Elliot Anderson | open play | 0.06 |
| 6 | A Liverpool FC | 78' | FOR | Rayan Cherki | Joško Gvardiol | open play | 0.75 |
| 7 | H Ipswich Town | 19' | FOR | Phil Foden | Jérémy Doku | open play | 0.64 |
| 7 | H Ipswich Town | 21' | AGAINST | Daizen Maeda | Abdoul Ouattara | open play | 0.17 |
| 7 | H Ipswich Town | 34' | FOR | Erling Haaland | Mateo Kovačić | open play | 0.34 |
| 7 | H Ipswich Town | 69' | FOR | Erling Haaland | Iliman Ndiaye | open play | 0.65 |
| 7 | H Ipswich Town | 90' | AGAINST | Zian Flemming | — | penalty | 0.76 |
| 8 | A Aston Villa | 6' | AGAINST | Nicolas Jackson | John McGinn | open play | 0.12 |
| 8 | A Aston Villa | 52' | FOR | Erling Haaland | Iliman Ndiaye | set piece | 0.53 |
| 8 | A Aston Villa | 60' | AGAINST | Nicolas Jackson | Ibrahim Mbaye | open play | 0.08 |
| 9 | H Brighton & Hove Albion | 11' | AGAINST | Yasin Ayari | Maxim De Cuyper | [no Understat] | — |
| 10 | A Nottingham Forest | 6' | AGAINST | Jair | — | [no Understat] | — |
| 10 | A Nottingham Forest | 18' | AGAINST | Liam Delap | Xaver Schlager | [no Understat] | — |
| 10 | A Nottingham Forest | 52' | FOR | Rayan Cherki | — | [no Understat] | — |
| 10 | A Nottingham Forest | 73' | AGAINST | Liam Delap | Morgan Gibbs-White | [no Understat] | — |
Scored 21: open play 16, corner 2, direct FK 1, set piece 1, [no Understat] 1 · Conceded 13: open play 7, [no Understat] 4, own goal 1, penalty 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW8 AG v Aston Villa 6' Nicolas Jackson (assist John McGinn): G O O O A A A L - Nicolas Jackson scores with the right foot! · before: 6' Boubacar Kamara relieves the pressure with a clearance ‹ 6' Josko Gvardiol relieves the pressure with a clearance ‹ 6' Erling Haaland successfully blocks the shot
- GW8 FOR v Aston Villa 52' Erling Haaland (assist Iliman Ndiaye): G O O O A A A L - Erling Haaland from Manchester City heads the ball home! · before: 52' The cross by Iliman Ndiaye from Manchester City successfully finds a teammate in the box. ‹ 52' Obstruction as Boubacar Kamara cuts off the run of Iliman Ndiaye. A free-kick is awarded. ‹ 52' Phil Foden relieves the pressure with a clearance
- GW8 AG v Aston Villa 60' Nicolas Jackson (assist Ibrahim Mbaye): G O O O A A A L - Nicolas Jackson scores with the right foot! · before: 60' The cross by Ibrahim Mbaye from Aston Villa successfully finds a teammate in the box. ‹ 60' Pau Torres relieves the pressure with a clearance ‹ 60' Abdukodir Khusanov relieves the pressure with a clearance
- GW9 AG v Brighton & Hove Albion 11' Yasin Ayari (assist Maxim De Cuyper, key pass Diego Gomez): G O O O A A A L - Yasin Ayari scores with the left foot! · before: 11' The cross by Diego Gomez from Brighton successfully finds a teammate in the box. ‹ 11' Brighton with a potentially dangerous attack. ‹ 10' The referee signals a free kick as Elliot Anderson from Manchester City trips Yasin Ayari
- GW10 AG v Nottingham Forest 6' Jair Cunha: G O O O O O A A L - Jair Cunha finds the net with the left foot! · before: 6' Nottingham Forest with a potentially dangerous attack. ‹ 6' Jair Cunha makes the tackle and wins possession for his team ‹ 5' Elliot Anderson relieves the pressure with a clearance
- GW10 AG v Nottingham Forest 18' Liam Delap (assist Xaver Schlager): G O O O A A A L - Liam Delap scores with the right foot! · before: 18' Nottingham Forest start a counter attack. ‹ 18' Nikola Milenkovic relieves the pressure with a clearance ‹ 17' Neco Williams relieves the pressure with a clearance
- GW10 FOR v Nottingham Forest 52' Rayan Cherki: G O O O A A A L - Rayan Cherki volleys the ball into the back of the net with the left foot. · before: 52' Ryan Yates relieves the pressure with a clearance ‹ 52' Jair Cunha from Nottingham Forest intercepts a cross aimed towards the box. ‹ 52' The referee signals a free kick as Murillo from Nottingham Forest trips Enzo Fernandez
- GW10 AG v Nottingham Forest 73' Liam Delap (assist Morgan Gibbs-White): G O O O A A A L - Liam Delap scores with the left foot! · before: 73' Morgan Gibbs-White creates a scoring opportunity for his teammate ‹ 73' Nottingham Forest start a counter attack. ‹ 73' Jair Cunha from Nottingham Forest intercepts a cross aimed towards the box.

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW5 H v Sunderland 12' Brian Brobbey: no structured culprit — reports only
- GW5 H v Sunderland 33' Brian Brobbey: no structured culprit — reports only
- GW5 H v Sunderland 59' Brian Brobbey: no structured culprit — reports only
  · GW5 other flags: Joško Gvardiol clearanceOffLine 1
- GW7 H v Ipswich Town 21' Daizen Maeda: no structured culprit — reports only
- GW7 H v Ipswich Town 90' Zian Flemming [pen]: Marc Guéhi conceded the penalty [CONFIRMED — SofaScore]
- GW8 A v Aston Villa 6' Nicolas Jackson: no structured culprit — reports only
- GW8 A v Aston Villa 60' Nicolas Jackson: no structured culprit — reports only
  · GW8 error leading to a goal (SofaScore, match level — 2 conceded, the goal is not identified): Gianluigi Donnarumma, Marc Guéhi [CONFIRMED — SofaScore error flag]
  · GW8 other flags: Abdukodir Khusanov lastManTackle 1
- GW9 H v Brighton & Hove Albion 11' Yasin Ayari: Matheus Nunes error leading to the goal [CONFIRMED — SofaScore error flag]
- GW10 A v Nottingham Forest 6' Jair: no structured culprit — reports only
- GW10 A v Nottingham Forest 18' Liam Delap: no structured culprit — reports only
- GW10 A v Nottingham Forest 73' Liam Delap: no structured culprit — reports only
  · GW10 error leading to a goal (SofaScore, match level — 3 conceded, the goal is not identified): Joško Gvardiol [CONFIRMED — SofaScore error flag]
  · GW10 other flags: Enzo Fernández errorLeadToAShot 1

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 86 | 15.62 | 16 | 59 | 7.83 | 7 |
| corner | 23 | 2.08 | 2 | 14 | 0.92 | 0 |
| set piece | 7 | 1.13 | 1 | 10 | 0.45 | 0 |
| direct FK | 2 | 0.11 | 1 | 4 | 0.26 | 0 |
| penalty | 0 | 0.00 | 0 | 1 | 0.76 | 1 |
Totals per match: xG 2.37 (npxG 2.37) for, xGA 1.28 (np 1.18) against · dead-ball share of xG 18% for, 23% against · penalties won 0, conceded 1 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 23 shots, xG 2.08, 2 goals, headed 6: 6-yard box, central 3 shots, xG 1.01, 0 goals; penalty area, central 7 shots, xG 0.51, 2 goals; penalty area, left 5 shots, xG 0.23, 0 goals · against — 14 shots conceded, xG 0.92, 0 goals, headed 9: penalty area, central 8 shots, xG 0.45, 0 goals; 6-yard box, central 3 shots, xG 0.39, 0 goals; penalty area, right 2 shots, xG 0.06, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 33 · corner shots conceded 14 (headed 9), xG 0.92, goals 0 · xG per corner faced 0.028 (rank 17 of 20, 1 = weakest) · weak zone: penalty-spot band (0.45 xG, 49% of theirs v 26% league) · signal: **STRONG — no corner pairing against them** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–10 [CONFIRMED — LiveScore Block L, 80 corners; side L/R as LiveScore records it; foot from SofaScore]: Enzo Fernandez 33 (29L/4R, 7 short, right foot); Rayan Cherki 17 (6L/11R, 10 short, both foot); Elliot Anderson 16 (10L/6R, 1 short, right foot); Phil Foden 13 (3L/10R, 1 short, left foot). First contact on corners that ended in a shot (Understat) — for: Elliot Anderson 5, Marc Guehi 3 (2 headed) — 1 goal, Erling Haaland 3, Nico O&#039;Reilly 2 (2 headed), Rúben Dias 2 (1 headed) · against (who beat them): Bobby Thomas 3 (3 headed), Harry Maguire 1 (1 headed), Kevin Danso 1 (1 headed), Trai Hume 1 (1 headed), Alexis Mac Allister 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 43.9 (rank 4 of 20, 1 = highest line) · block length 20.6 (rank 8, 1 = most compact) · width 65.1. Per match: GW5 H v Sunderland 4-2-3-1: back line 41, front 64, length 23, width 61 (55% poss); GW6 A v Liverpool FC 4-2-3-1: back line 38, front 54, length 15, width 71 (65% poss); GW7 H v Ipswich Town 4-2-3-1: back line 48, front 66, length 18, width 69 (70% poss); GW8 A v Aston Villa 4-2-3-1: back line 45, front 65, length 20, width 65 (64% poss); GW9 H v Brighton & Hove Albion 4-3-3: back line 45, front 73, length 28, width 61 (62% poss); GW10 A v Nottingham Forest 4-2-3-1: back line 45, front 72, length 27, width 70 (78% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 5 league match(es) v LB-coded sides — xG 2.41/match and 2.4 pts/match v 1.61 and 1.8 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW2 A v Crystal Palace 4–1, xG 2.21, box shots 13, poss 72%; GW3 H v Coventry City 1–0, xG 2.12, box shots 14, poss 78%; GW5 H v Sunderland 5–3, xG 2.82, box shots 12, poss 55%; GW7 H v Ipswich Town 3–2, xG 3.35, box shots 15, poss 70%; GW8 A v Aston Villa 1–2, xG 1.56, box shots 12, poss 64%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Cherki 4, Foden 2, Guehi 2** · FPL editorial order: Cherki #1, Foden #2, Enzo #3
- Direct free-kick shooters: **Fernández 2** · FPL order: Cherki #1, Foden #2, Enzo #3
- Penalties taken: **—** · FPL order: Haaland #1, Semenyo #2, Doku #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Cherki 2, Fernández 1, Foden 1**
- Corner targets (headed shots from corners): **O&#039;Reilly 2, Guehi 2, Dias 1, Gvardiol 1** · corner shots 23

**Through-ball suppliers (Block P, PL/Opta, season):** Jérémy Doku 6 (1.36/90, percentile 100, 396 min); Rayan Cherki 8 (1.27/90, percentile 99, 565 min); Phil Foden 5 (1.24/90, percentile 99, 364 min); Antoine Semenyo 3 (0.49/90, percentile 88, 553 min); Enzo Fernández 3 (0.43/90, percentile 86, 625 min); Josko Gvardiol 2 (0.26/90, percentile 76, 702 min); Nico O'Reilly 1 (0.25/90, percentile 75, 363 min) · club total 36 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 318 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 8.21, field tilt 80.1, possession 65.7%, box entries 19, direct speed 1.7, SCA 26; GW2: PPDA 7.35, field tilt 77.1, possession 71.9%, box entries 19, direct speed 1.29, SCA 36; GW3: PPDA 5.93, field tilt 71.6, possession 77.2%, box entries 12, direct speed 1.49, SCA 30; GW4: PPDA 13.25, field tilt 29.8, possession 45%, box entries 8, direct speed 1.93, SCA 12; GW5: PPDA 11.58, field tilt 59.3, possession 55.2%, box entries 12, direct speed 1.98, SCA 32; GW6: PPDA 9.48, field tilt 64.7, possession 64.6%, box entries 13, direct speed 1.98, SCA 30; GW7: PPDA 9.75, field tilt 76.8, possession 69.5%, box entries 21, direct speed 1.23, SCA 37; GW8: PPDA 8.32, field tilt 79.6, possession 62.7%, box entries 31, direct speed 1.57, SCA 30; GW9: PPDA 10.12, field tilt 76.5, possession 62%, box entries 27, direct speed 1.89, SCA 41; GW10: PPDA 9.88, field tilt 74.4, possession 77.5%, box entries 16, direct speed 1.53, SCA 24

**Zone 14 (C13, SofaScore heat-map points, 10 league matches):** for 38.3/match (rank 4 of 20) · conceded 19.7/match (rank 19 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 9.9/match · allowed 4.5/match · PPDA 8.8. Per match for/allowed: GW3 6/2; GW4 2/12; GW5 12/9; GW6 11/3; GW7 12/2; GW8 11/4 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: Gianluigi Donnarumma (16, 3/3)
- DEF: Rúben Dias (16, 3/3), Abdukodir Khusanov (12, 3/3), Rico Lewis (1, 0/3)
- MID: Elliot Anderson (15, 3/3), Enzo Fernández (13, 3/3), Iliman Ndiaye (13, 3/3), Rayan Cherki (11, 2/3), Matheus Nunes (7, 1/3)
- FWD: Erling Haaland (16, 3/3)
- Contested slots: M Matheus Nunes 7 v Antoine Semenyo 6 · Excluded (FPL flag): Joško Gvardiol — Unspecified injury - 75% chance of playing; Marc Guéhi — Unspecified injury - 75% chance of playing
- Absent last match (E12, SofaScore list): Semenyo (Leg Injury)
- Substitutions this season (C3): GW7 61' Nico O'Reilly→Joško Gvardiol TACTICAL; GW7 50' Mateo Kovačić→Enzo Fernández INJURY [CONFIRMED: SofaScore flag + LiveScore 'knock']; GW8 69' Iliman Ndiaye→Ryan McAidoo CHASING; GW8 46' Rayan Cherki→Phil Foden HALF-TIME; GW8 46' Marc Guéhi→Rico Lewis HALF-TIME; GW9 79' Joško Gvardiol→Phil Foden CHASING; GW9 79' Iliman Ndiaye→Allan CHASING; GW9 64' Enzo Fernández→Nico O'Reilly CHASING; GW9 55' Ayyoub Bouaddi→Rayan Cherki CHASING; GW10 78' Enzo Fernández→Phil Foden CHASING; GW10 46' Marc Guéhi→Matheus Nunes HALF-TIME; GW10 46' Joško Gvardiol→Nico O'Reilly HALF-TIME

### First-choice players and absences (F14) — generated 2026-11-10 07:41 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Gianluigi Donnarumma | start weight 16 | OK | a | — | — |
| CB | Rúben Dias | start weight 16 | OK | a | Joško Gvardiol (DEF, not a CB by heat map) | — |
| CB | Abdukodir Khusanov | start weight 12 | OK | a | Joško Gvardiol (DEF, not a CB by heat map) | — |
| xGI #1 | Erling Haaland | xGI 7.92 | OK | a 100% | Rayan Cherki | — |
| xGI #2 | Phil Foden | xGI 3.93 | OK | a 100% | Rayan Cherki | — |
| Penalties #1 (FPL) | Haaland | FPL order | OK | a 100% | Doku | — |
| Direct FK #1 (FPL) | Cherki | FPL order | OK | a | Foden | — |
| Corners (observed) | Enzo Fernandez | 33 corners taken | OK | a | Rayan Cherki | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Bournemouth: all started · GW2 A Crystal Palace: all started · GW3 H Coventry City: Phil Foden (did not start) · GW4 A Manchester United: Abdukodir Khusanov (did not start) · GW5 H Sunderland: Abdukodir Khusanov (did not start), Phil Foden (ban (red)) · GW6 A Liverpool FC: Abdukodir Khusanov (did not start), Phil Foden (ban (red)) · GW7 H Ipswich Town: Abdukodir Khusanov (did not start) · GW8 A Aston Villa: Phil Foden (did not start) · GW9 H Brighton & Hove Albion: Phil Foden (did not start) · GW10 A Nottingham Forest: Phil Foden (did not start)

### Next fixtures (all competitions)
- Sat 21 Nov 12:30 UTC · Premier League R11 · H v Fulham
- Tue 24 Nov 20:00 UTC · UEFA Champions League R5 · H v SSC Napoli
- Sun 29 Nov 16:30 UTC · Premier League R12 · A v Arsenal
- Wed 02 Dec 19:30 UTC · Premier League R13 · H v Leeds United
- Sat 05 Dec 20:00 UTC · Premier League R14 · A v Brentford
- Tue 08 Dec 20:00 UTC · UEFA Champions League R6 · A v FC Barcelona

### FPL availability flags (players with league minutes this season)
Guéhi — Unspecified injury - 75% chance of playing (75%); Gvardiol — Unspecified injury - 75% chance of playing (75%); Semenyo — Knee injury - Unknown return date (0%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 H Bournemouth 2–1 · xG 2.25–0.65 · poss 66% · 4-2-3-1 · scorers: Marc Guéhi 84', Joško Gvardiol 90'
- GW2 A Crystal Palace 4–1 · xG 2.21–0.66 · poss 72% · 4-2-3-1 · scorers: Erling Haaland 17', Rayan Cherki 54', Rayan Cherki 59', Erling Haaland 84'
- GW3 H Coventry City 1–0 · xG 2.12–1.37 · poss 78% · 4-2-3-1 · scorers: Erling Haaland 26'
- GW4 A Manchester United 1–0 · xG 1.10–1 · poss 45% · 4-2-3-1 · scorers: Erling Haaland 60'
- GW5 H Sunderland 5–3 · xG 2.82–3.57 · poss 55% · 4-2-3-1 · scorers: Enzo Fernández 9', Rayan Cherki 29', Antoine Semenyo 43', Antoine Semenyo 57', Erling Haaland 81'
- GW6 A Liverpool FC 3–0 · xG 1.28–0.94 · poss 65% · 4-2-3-1 · scorers: Erling Haaland 65', Jérémy Doku 68', Rayan Cherki 78'
- GW7 H Ipswich Town 3–2 · xG 3.35–1.86 · poss 70% · 4-2-3-1 · scorers: Phil Foden 19', Erling Haaland 34', Erling Haaland 69'
- GW8 A Aston Villa 1–2 · xG 1.56–0.61 · poss 64% · 4-2-3-1 · scorers: Erling Haaland 52'
- GW9 H Brighton & Hove Albion 0–1 · xG 1.64–1 · poss 62% · 4-3-3 · scorers: none
- GW10 A Nottingham Forest 1–3 · xG 1.76–1.06 · poss 78% · 4-2-3-1 · scorers: Rayan Cherki 52'
### Corner takers observed (LiveScore Block L)
- Enzo Fernandez: 33 corners (29 left, 4 right, 7 short)
- Rayan Cherki: 17 corners (6 left, 11 right, 10 short)
- Elliot Anderson: 16 corners (10 left, 6 right, 1 short)
- Phil Foden: 13 corners (3 left, 10 right, 1 short)
- Iliman Ndiaye: 1 corners (0 left, 1 right, 1 short)
