# Manchester City — data doc
*Feeder-written (2026-10-27 07:42 UTC); do not edit. Narrative: `profiles/teams/man-city.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-10-27 07:42 UTC)
**Manager:** Enzo Maresca · **Venue:** Etihad Stadium · **SofaScore:** https://www.sofascore.com/football/team/manchester-city/17 · **FPL code:** MCI
**Table:** 1st, 21 pts (7W 0D 1L, GF 20 GA 9) · Home 2nd (4-0-0, 11:6) · Away 2nd (3-0-1, 9:3)
**Standing context (F15):** 30 league games left · points v 4th +6, v 5th +8, v 17th (last safe) +14, v 18th +15 · goal difference +11
**Suspension watch (D7, all players of the club):** nobody within 2 yellows of a ban, nobody suspended [FPL]
**Goal timing & game state (F17, 8 league matches):** goals after 75′ — for 5/20 (25%), against 1/9 (11%) · scored first 6, conceded first 2 (25% of matches), goalless 0 · points from losing positions 3 of 6 (2 matches behind at some point) · points from winning positions 21 of 21 (7 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Anderson (MID) 11.6/90, hit 2/8; Ndiaye (MID) 8.6/90, hit 2/8; Khusanov (DEF) 8.2/90, hit 1/5; Matheus N. (DEF) 6.9/90, hit 1/5
**Manager tenure (F13, SofaScore):** Enzo Maresca since 01 Jul 2026 · 13 matches in charge, all competitions (10W 0D 3L) · 8 league matches this season · contract to 30 Jun 2029 · previous club Chelsea · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Manchester United — last 4: Sep 2026 Premier League Manchester United 0–1 Manchester City (yellows 1–2, reds 0–1, xG 1.00–1.10); Jan 2026 Premier League Manchester United 2–0 Manchester City (yellows 2–3, xG 2.27–0.45); Sep 2025 Premier League Manchester City 3–0 Manchester United (yellows 0–0, xG 2.63–1.52); Apr 2025 Premier League Manchester United 0–0 Manchester City (yellows 3–2, xG 0.91–0.49) · 13 yellows in 4
**Archetype (F5):** used **PM** — derived PM [DERIVED] · signals, last 6 league matches: possession 62.8%, PPDA 9.2 (Understat, 6 matches; lower = harder press), opponent offsides forced 2.3/match (line height), fast breaks 1.2/match (season), both sides' xG 3.60/match (openness) · note: PPDA 9.2 v HP cut 9.1. Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap).
**Squad changes (F20, since 01 Jun 2026):** in 17 (permanent 10, loan 0, free 0, loan returns 7) · out 19 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 8 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 16.69 | 1 | Big chances against | 21 | 11 |
| xGOT | 17.14 | 1 | Box shots against | 57 | 4 |
| xA | 13.12 | 1 | Corners against | 33 | 4 |
| Shots | 117 | 6 | Crosses faced | 118 | 2 |
| SoT | 44 | 1 | Dribbled past | 57 | 9 |
| Big chances | 30 | 2 | Errors→shot | 5 | 6 |
| Shots in box | 87 | 2 | GK goals prevented | 0.53 | 8 |
| Corners | 46 | 4 | Clearances | 144 | 20 |
| Crosses | 145 | 10 | Tackles | 100 | 18 |
| Fast breaks | 10 | 10 | Interceptions | 59 | 16 |
| FK shots | 2 | 11 | Def. contributions | 321 | 20 |
| Possession % | 64.38 | 1 | Aerial % | 53.81 | 3 |
| Pass % | 89.32 | 1 | Duel % | 50.66 | 8 |
| Long balls | 244 | 12 | Fouls | 92 | 11 |
| Dribbles | 93 | 1 | Yellows | 13 | 5 |
| Shots against | 88 | 5 | Km covered | 896 | 19 |
| SoT against | 31 | 7 | Sprints | 768 | 20 |
Per match: xG 2.09 · xGOT 2.14 · shots 14.6 · shots against 11.0 · big chances 3.8 for / 2.6 against · corners 5.8 / 4.1 · crosses 18.1 / 14.8 · possession 64.375%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Coventry City | 1–0 | 2.12/2.20 | 1.37/1.49 | 78 | 15/12 | 4/3 | 14/8 | 6/3 | 3/3 | 4/5 | 19/5 v 15/5 | 2/5 |
| 4 | A | Manchester United | 1–0 | 1.10/1.14 | 1/0.94 | 45 | 6/16 | 2/3 | 2/6 | 3/4 | 2/1 | 7/6 | 14/3 v 27/6 | 4/1 |
| 5 | H | Sunderland | 5–3 | 2.82/2.67 | 3.57/3.38 | 55 | 16/17 | 6/9 | 12/14 | 5/3 | 3/8 | 6/5 | 19/4 v 17/5 | 0/0 |
| 6 | A | Liverpool FC | 3–0 | 1.28/1.59 | 0.94/0.76 | 65 | 15/13 | 4/6 | 8/6 | 4/4 | 3/0 | 6/5 | 12/2 v 13/2 | 2/2 |
| 7 | H | Ipswich Town | 3–2 | 3.35/4.01 | 1.86/1.37 | 70 | 19/8 | 6/3 | 15/7 | 6/1 | 6/3 | 2/3 | 20/8 v 15/5 | 5/2 |
| 8 | A | Aston Villa | 1–2 | 1.56/2.29 | 0.61/0.65 | 64 | 15/8 | 7/2 | 12/6 | 4/3 | 4/2 | 7/4 | 22/9 v 5/0 | 1/2 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Coventry City | 1–0 | 4-2-3-1 | 7/17 | 1/2 | 0/0 | 819/220 | 71/42 | Doku (Calf Injury), O'Reilly (Back Injury; doubtful) | Mfuni (club decision), Wright (Muscle Injury), Kesler-Hayden (Hamstring Injury), Woolfenden (Knee Injury) | Paul Tierney |
| 4 | A | Manchester United | 1–0 | 4-2-3-1 | 10/17 | 2/1 | 1/0 | 403/487 | 38/54 | — | Diallo (Muscle Injury), Baleba (Ankle Injury), Ugarte (Cruciate Ligament Injury), Heaton (Abdominal Injury), Shaw (Physical Discomfort; doubtful) | Michael Oliver |
| 5 | H | Sunderland | 5–3 | 4-2-3-1 | 14/14 | 0/1 | 0/0 | 475/388 | 40/47 | Foden (ban (red)) | Mandava (ban (cards)), Diarra (Hamstring Injury), Mundle (Knee Injury) | Robert Jones |
| 6 | A | Liverpool FC | 3–0 | 4-2-3-1 | 14/19 | 2/4 | 0/1 | 562/301 | 48/41 | Foden (ban (red)) | Isak (Thigh Injury), Gakpo (Ankle Injury), Bradley (Knee Injury), Szoboszlai (Hamstring Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury) | Chris Kavanagh |
| 7 | H | Ipswich Town | 3–2 | 4-2-3-1 | 8/16 | 1/2 | 0/0 | 753/319 | 85/39 | — | — | Farai Hallam |
| 8 | A | Aston Villa | 1–2 | 4-2-3-1 | 17/21 | 4/4 | 0/0 | 543/314 | 48/26 | Semenyo (Leg Injury), Nunes (Physical Discomfort; doubtful) | Wan-Bissaka (Hamstring Injury), Onana (Cruciate Ligament Injury), Ruggeri (Hamstring Injury) | Peter Bankes |
Per match: fouls 11.5 / 15.4 · yellows 1.62 / 2.12 · reds 1 / 1 (season) · offsides forced 2.2, committed 1.8 · crosses attempted 18.1 / faced 14.8. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 2.63 for / 1.86 against per match · Away (4): xG 1.54 / 0.80. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW8 A v Aston Villa 1–2 (Sat 24 Oct 11:30 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Gianluigi Donnarumma | G | 90 | 4.8 | 0.00 | 0.00 | 0 | 0 | 1 | 0 | 19 |
| Abdukodir Khusanov | D | 90 | 7.5 | 0.02 | 0.06 | 0 | 1 | 16 | 2 | 93 |
| Marc Guéhi | D | 45 | 5.8 | 0.00 | 0.00 | 0 | 0 | 4 | 0 | 38 |
| Rúben Dias | D | 90 | 6.4 | 0.00 | 0.02 | 0 | 0 | 5 | 0 | 91 |
| Joško Gvardiol | D | 90 | 6.5 | 0.45 | 0.04 | 2 | 3 | 8 | 0 | 68 |
| Elliot Anderson | M | 90 | 7.5 | 0.00 | 0.25 | 3 | 0 | 4 | 2 | 93 |
| Enzo Fernández | M | 90 | 7.1 | 0.04 | 0.36 | 2 | 1 | 0 | 5 | 97 |
| Iliman Ndiaye | M | 69 | 7.5 | 0.06 | 0.37 | 1 | 2 | 0 | 3 | 55 |
| Rayan Cherki | M | 45 | 6.1 | 0.39 | 0.04 | 2 | 1 | 0 | 1 | 29 |
| Jérémy Doku | M | 90 | 7.5 | 0.15 | 0.44 | 2 | 3 | 0 | 3 | 74 |
| Erling Haaland | F | 90 | 7.9 | 0.40 | 0.00 | 0 | 3 | 2 | 0 | 15 |
Subs used: Rico Lewis (45'), Phil Foden (45'), Ryan McAidoo (21')
Goals: 6' Nicolas Jackson (assist John McGinn) [opp]; 52' Erling Haaland (assist Iliman Ndiaye) [own]; 60' Nicolas Jackson (assist Ibrahim Mbaye) [opp]
Substitutions (own): 46' Phil Foden for Rayan Cherki; 46' Rico Lewis for Marc Guéhi; 69' Ryan McAidoo for Iliman Ndiaye
Cards: 32' Marc Guéhi (yellow, own); 38' Rayan Cherki (yellow, own); 54' Johan Manzambi (yellow, opp); 55' Matty Cash (yellow, opp); 74' Elliot Anderson (yellow, own); 76' Ryan McAidoo (yellow, own); 83' Brian Madjo (yellow, opp); 90' Emiliano Buendía (yellow, opp)
**Baseline XI change vs GW7 (4-2-3-1 → 4-2-3-1):** in — Abdukodir Khusanov, Elliot Anderson, Enzo Fernández, Joško Gvardiol, Rayan Cherki; out — Ayyoub Bouaddi, Mateo Kovačić, Matheus Nunes, Nico O'Reilly, Phil Foden.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 3 | H Coventry City | 26' | FOR | Erling Haaland | Antoine Semenyo | open play | 0.37 |
| 4 | A Manchester United | 60' | FOR | Erling Haaland | — | open play | 0.58 |
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
Scored 20: open play 16, corner 2, direct FK 1, set piece 1 · Conceded 9: open play 7, own goal 1, penalty 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW6 FOR v Liverpool FC 65' Erling Haaland: G O O O A A A L - Erling Haaland reacts first on the loose ball and puts it away with the left! · before: 65' Alexis Mac Allister successfully blocks the shot ‹ 65' A shot by Jeremy Doku is blocked. ‹ 62' SENT OFF! - After a tactical foul, Ryan Gravenberch gets his second yellow card.
- GW6 FOR v Liverpool FC 68' Jérémy Doku (assist Elliot Anderson): G O O O A A A L - Jeremy Doku scores with the right foot! · before: 67' The referee signals a free kick as Josko Gvardiol from Manchester City trips Ronald Araujo ‹ 67' Ronald Araujo relieves the pressure with a clearance ‹ 66' Nico O'Reilly is leaving the field to be replaced by Josko Gvardiol in a tactical substitut
- GW6 FOR v Liverpool FC 78' Rayan Cherki (assist Josko Gvardiol, key pass Elliot Anderson): G O O O A A A L - Rayan Cherki scores with the right foot! · before: 78' Josko Gvardiol creates a scoring opportunity for his teammate ‹ 76' Antoine Semenyo is penalised for pushing Milos Kerkez. ‹ 75' Goal kick for Liverpool.
- GW7 FOR v Ipswich Town 19' Phil Foden (assist Jeremy Doku, key pass Mateo Kovacic): G O O O A A A L - Phil Foden scores with the left foot! · before: 19' Jeremy Doku creates a scoring opportunity for his teammate ‹ 18' Leif Davis from Ipswich intercepts a cross aimed towards the box. ‹ 18' Christian Walton makes a crucial save!
- GW7 AG v Ipswich Town 21' Daizen Maeda (assist Abdoul Ouattara): G O O O A A A L - Daizen Maeda scores with the left foot! · before: 21' Marc Guehi could cost his team a goal after a defensive blunder. ‹ 21' Abdoul Ouattara creates a scoring opportunity for his teammate ‹ 21' Ayyoub Bouaddi relieves the pressure with a clearance
- GW7 FOR v Ipswich Town 34' Erling Haaland (assist Mateo Kovacic): G O O O A A A L - Erling Haaland from Manchester City heads the ball home! · before: 34' Mateo Kovacic creates a scoring opportunity for his teammate ‹ 34' Mateo Kovacic creates a scoring opportunity for his teammate ‹ 34' Jacob Greaves successfully blocks the shot
- GW7 FOR v Ipswich Town 69' Erling Haaland (assist Iliman Ndiaye): G O O O A A A L - Erling Haaland scores with the left foot! · before: 69' Iliman Ndiaye creates a scoring opportunity for his teammate ‹ 69' Florentino makes the tackle and wins possession for his team ‹ 68' Gianluigi Donnarumma from Manchester City intercepts a cross aimed towards the box.
- GW7 AG v Ipswich Town 90' Zian Flemming [pen]: G O O O A A A L - Zian Flemming from Ipswich puts it away from the penalty spot in the middle with the right foot. Gianluigi Donnarumma jumped on the  · before: 90' After VAR check, the referee changed the call and decided to award a penalty for Ipswich! ‹ 89' VAR - PENALTY! - The referee has stopped the play. VAR check in progress, a potential penal ‹ 88' PENALTY - Marc Guehi from Manchester City concedes a penalty for tripping Abdul Fatawu.
- GW8 AG v Aston Villa 6' Nicolas Jackson (assist John McGinn): G O O O A A A L - Nicolas Jackson scores with the right foot! · before: 6' Boubacar Kamara relieves the pressure with a clearance ‹ 6' Josko Gvardiol relieves the pressure with a clearance ‹ 6' Erling Haaland successfully blocks the shot
- GW8 FOR v Aston Villa 52' Erling Haaland (assist Iliman Ndiaye): G O O O A A A L - Erling Haaland from Manchester City heads the ball home! · before: 52' The cross by Iliman Ndiaye from Manchester City successfully finds a teammate in the box. ‹ 52' Obstruction as Boubacar Kamara cuts off the run of Iliman Ndiaye. A free-kick is awarded. ‹ 52' Phil Foden relieves the pressure with a clearance
- GW8 AG v Aston Villa 60' Nicolas Jackson (assist Ibrahim Mbaye): G O O O A A A L - Nicolas Jackson scores with the right foot! · before: 60' The cross by Ibrahim Mbaye from Aston Villa successfully finds a teammate in the box. ‹ 60' Pau Torres relieves the pressure with a clearance ‹ 60' Abdukodir Khusanov relieves the pressure with a clearance

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

**Corners (E10 data layer):** observed takers GW1–8 [CONFIRMED — LiveScore Block L, 62 corners; side L/R as LiveScore records it; foot from SofaScore]: Enzo Fernandez 23 (19L/4R, 7 short, right foot); Rayan Cherki 15 (6L/9R, 9 short, both foot); Elliot Anderson 12 (10L/2R, 1 short, right foot); Phil Foden 11 (2L/9R, 1 short, left foot). First contact on corners that ended in a shot (Understat) — for: Elliot Anderson 5, Marc Guehi 3 (2 headed) — 1 goal, Erling Haaland 3, Nico O&#039;Reilly 2 (2 headed), Rúben Dias 2 (1 headed) · against (who beat them): Bobby Thomas 3 (3 headed), Harry Maguire 1 (1 headed), Kevin Danso 1 (1 headed), Trai Hume 1 (1 headed), Alexis Mac Allister 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 43.6 (rank 4 of 20, 1 = highest line) · block length 18.9 (rank 3, 1 = most compact) · width 65.0. Per match: GW3 H v Coventry City 4-2-3-1: back line 44, front 61, length 17, width 61 (78% poss); GW4 A v Manchester United 4-2-3-1: back line 33, front 58, length 25, width 64 (45% poss); GW5 H v Sunderland 4-2-3-1: back line 41, front 64, length 23, width 61 (55% poss); GW6 A v Liverpool FC 4-2-3-1: back line 38, front 54, length 15, width 71 (65% poss); GW7 H v Ipswich Town 4-2-3-1: back line 48, front 66, length 18, width 69 (70% poss); GW8 A v Aston Villa 4-2-3-1: back line 45, front 65, length 20, width 65 (64% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 3 league match(es) v LB-coded sides — xG 2.56/match and 3.0 pts/match v 1.80 and 2.4 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW2 A v Crystal Palace 4–1, xG 2.21, box shots 13, poss 72%; GW3 H v Coventry City 1–0, xG 2.12, box shots 14, poss 78%; GW7 H v Ipswich Town 3–2, xG 3.35, box shots 15, poss 70%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Cherki 4, Foden 2, Guehi 2** · FPL editorial order: Cherki #1, Foden #2, Enzo #3
- Direct free-kick shooters: **Fernández 2** · FPL order: Cherki #1, Foden #2, Enzo #3
- Penalties taken: **—** · FPL order: Haaland #1, Semenyo #2, Doku #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Cherki 2, Fernández 1, Foden 1**
- Corner targets (headed shots from corners): **O&#039;Reilly 2, Guehi 2, Dias 1, Gvardiol 1** · corner shots 23

**Through-ball suppliers (Block P, PL/Opta, season):** Jérémy Doku 6 (2.50/90, percentile 100, 216 min); Rayan Cherki 8 (1.64/90, percentile 99, 440 min); Phil Foden 5 (1.32/90, percentile 99, 341 min); Antoine Semenyo 3 (0.49/90, percentile 88, 553 min); Enzo Fernández 2 (0.37/90, percentile 82, 483 min); Josko Gvardiol 2 (0.31/90, percentile 78, 578 min); Nico O'Reilly 1 (0.31/90, percentile 78, 292 min) · club total 34 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 289 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 8.21, field tilt 80.1, possession 65.7%, box entries 19, direct speed 1.7, SCA 26; GW2: PPDA 7.35, field tilt 77.1, possession 71.9%, box entries 19, direct speed 1.29, SCA 36; GW3: PPDA 5.93, field tilt 71.6, possession 77.2%, box entries 12, direct speed 1.49, SCA 30; GW4: PPDA 13.25, field tilt 29.8, possession 45%, box entries 8, direct speed 1.93, SCA 12; GW5: PPDA 11.58, field tilt 59.3, possession 55.2%, box entries 12, direct speed 1.98, SCA 32; GW6: PPDA 9.48, field tilt 64.7, possession 64.6%, box entries 13, direct speed 1.98, SCA 30; GW7: PPDA 9.75, field tilt 76.8, possession 69.5%, box entries 21, direct speed 1.23, SCA 37; GW8: PPDA 8.32, field tilt 79.6, possession 62.7%, box entries 31, direct speed 1.57, SCA 30

**Zone 14 (C13, SofaScore heat-map points, 8 league matches):** for 40.6/match (rank 2 of 20) · conceded 19.9/match (rank 19 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 9.9/match · allowed 4.5/match · PPDA 8.8. Per match for/allowed: GW3 6/2; GW4 2/12; GW5 12/9; GW6 11/3; GW7 12/2; GW8 11/4 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 8 league matches, weights last-3 ×3 / older ×1
- GK: Gianluigi Donnarumma (14, 3/3)
- DEF: Rúben Dias (14, 3/3), Joško Gvardiol (8, 1/3), Abdukodir Khusanov (6, 1/3), Rico Lewis (1, 0/3)
- MID: Marc Guéhi (14, 3/3), Iliman Ndiaye (11, 3/3), Rayan Cherki (10, 2/3), Enzo Fernández (9, 2/3), Matheus Nunes (8, 2/3)
- FWD: Erling Haaland (14, 3/3)
- Contested slots: M Matheus Nunes 8 v Nico O'Reilly 8 · Excluded (FPL flag): Elliot Anderson — Unspecified injury - 75% chance of playing
- Absent last match (E12, SofaScore list): Semenyo (Leg Injury), Nunes (Physical Discomfort; doubtful)
- Substitutions this season (C3): GW6 80' Enzo Fernández→Ayyoub Bouaddi GAME-STATE; GW6 80' Erling Haaland→Allan GAME-STATE; GW6 66' Nico O'Reilly→Joško Gvardiol CARD-RISK; GW6 56' Iliman Ndiaye→Jérémy Doku TACTICAL; GW7 77' Jérémy Doku→Antoine Semenyo GAME-STATE; GW7 77' Phil Foden→Elliot Anderson GAME-STATE; GW7 76' Matheus Nunes→Abdukodir Khusanov INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW7 61' Nico O'Reilly→Joško Gvardiol TACTICAL; GW7 50' Mateo Kovačić→Enzo Fernández INJURY [CONFIRMED: SofaScore flag + LiveScore 'knock']; GW8 69' Iliman Ndiaye→Ryan McAidoo CHASING; GW8 46' Rayan Cherki→Phil Foden HALF-TIME; GW8 46' Marc Guéhi→Rico Lewis HALF-TIME

### First-choice players and absences (F14) — generated 2026-10-27 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Gianluigi Donnarumma | start weight 14 | OK | a | — | — |
| CB | Rúben Dias | start weight 14 | OK | a | Joško Gvardiol (DEF, not a CB by heat map) | — |
| xGI #1 | Erling Haaland | xGI 6.85 | OK | a 100% | Rayan Cherki | — |
| xGI #2 | Phil Foden | xGI 3.86 | OK | a 100% | Rayan Cherki | — |
| Penalties #1 (FPL) | Haaland | FPL order | OK | a 100% | Doku | — |
| Direct FK #1 (FPL) | Cherki | FPL order | OK | a | Foden | — |
| Corners (observed) | Enzo Fernandez | 23 corners taken | OK | a | Rayan Cherki | — |
⚠ only 1 centre-back(s) identified from heat maps — check the baseline DEF list by hand.
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Bournemouth: all started · GW2 A Crystal Palace: all started · GW3 H Coventry City: Phil Foden (did not start) · GW4 A Manchester United: all started · GW5 H Sunderland: Phil Foden (ban (red)) · GW6 A Liverpool FC: Phil Foden (ban (red)) · GW7 H Ipswich Town: all started · GW8 A Aston Villa: Phil Foden (did not start)

### Next fixtures (all competitions)
- Wed 28 Oct 19:30 UTC · EFL Cup R4 · H v Brighton & Hove Albion
- Sat 31 Oct 15:00 UTC · Premier League R9 · H v Brighton & Hove Albion
- Wed 04 Nov 20:00 UTC · UEFA Champions League R4 · A v RB Leipzig
- Sat 07 Nov 17:30 UTC · Premier League R10 · A v Nottingham Forest
- Sat 21 Nov 12:30 UTC · Premier League R11 · H v Fulham
- Tue 24 Nov 20:00 UTC · UEFA Champions League R5 · H v SSC Napoli

### FPL availability flags (players with league minutes this season)
Matheus N. — Unspecified injury - 75% chance of playing (75%); Semenyo — Knee injury - Unknown return date (0%)
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
### Corner takers observed (LiveScore Block L)
- Enzo Fernandez: 23 corners (19 left, 4 right, 7 short)
- Rayan Cherki: 15 corners (6 left, 9 right, 9 short)
- Elliot Anderson: 12 corners (10 left, 2 right, 1 short)
- Phil Foden: 11 corners (2 left, 9 right, 1 short)
- Iliman Ndiaye: 1 corners (0 left, 1 right, 1 short)
