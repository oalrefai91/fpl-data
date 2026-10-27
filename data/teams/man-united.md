# Manchester United — data doc
*Feeder-written (2026-10-27 07:42 UTC); do not edit. Narrative: `profiles/teams/man-united.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-10-27 07:42 UTC)
**Manager:** Michael Carrick · **Venue:** Old Trafford · **SofaScore:** https://www.sofascore.com/football/team/manchester-united/35 · **FPL code:** MUN
**Table:** 16th, 7 pts (1W 4D 3L, GF 10 GA 13) · Home 13th (1-1-2, 6:7) · Away 16th (0-3-1, 4:6)
**Standing context (F15):** 30 league games left · points v 4th -8, v 5th -6, v 17th (last safe) +0, v 18th +1 · goal difference -3
**Suspension watch (D7, all players of the club):** Maguire — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 8 league matches):** goals after 75′ — for 3/10 (30%), against 4/13 (31%) · scored first 3, conceded first 5 (62% of matches), goalless 0 · points from losing positions 4 of 15 (5 matches behind at some point) · points from winning positions 6 of 12 (4 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Mainoo (MID) 14.8/90, hit 5/6; Tielemans (MID) 10.4/90, hit 3/8; Yoro (DEF) 11.4/90, hit 2/5; Maguire (DEF) 7.0/90, hit 2/8; Martinez (DEF) 6.4/90, hit 2/7; Andrey Santos (MID) 12.4/90, hit 1/5
**Manager tenure (F13, SofaScore):** Michael Carrick since 22 May 2026 · 13 matches in charge, all competitions (3W 4D 6L) · 8 league matches this season · contract to 30 Jun 2028 · previous club Middlesbrough; earlier stint here 13 Jan 2026–22 May 2026, 21 Nov 2021–03 Dec 2021 (read as interim/caretaker if it ended when this one began) · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Liverpool FC — last 4: May 2026 Premier League Manchester United 3–2 Liverpool FC (yellows 2–2, xG 2.34–0.89); Oct 2025 Premier League Liverpool FC 1–2 Manchester United (yellows 0–2, xG 2.74–1.34); Jan 2025 Premier League Liverpool FC 2–2 Manchester United (yellows 2–4, xG 2.82–1.05); Sep 2024 Premier League Manchester United 0–3 Liverpool FC (yellows 4–1, xG 1.36–1.79) · 17 yellows in 4 | v Manchester City — last 4: Sep 2026 Premier League Manchester United 0–1 Manchester City (yellows 1–2, reds 0–1, xG 1.00–1.10); Jan 2026 Premier League Manchester United 2–0 Manchester City (yellows 2–3, xG 2.27–0.45); Sep 2025 Premier League Manchester City 3–0 Manchester United (yellows 0–0, xG 2.63–1.52); Apr 2025 Premier League Manchester United 0–0 Manchester City (yellows 3–2, xG 0.91–0.49) · 13 yellows in 4 | v Leeds United — last 4: Oct 2026 Premier League Leeds United 1–1 Manchester United (yellows 2–2, xG 1.41–0.92); Apr 2026 Premier League Manchester United 1–2 Leeds United (yellows 3–2, reds 1–0, xG 1.27–2.57); Jan 2026 Premier League Leeds United 1–1 Manchester United (yellows 0–1, xG 0.90–1.59); Feb 2023 Premier League Leeds United 0–2 Manchester United (yellows 2–1, xG 1.81–1.12) · 13 yellows in 4 | v Everton — last 4: Sep 2026 Premier League Everton 2–2 Manchester United (yellows 3–3, xG 1.01–0.69); Feb 2026 Premier League Everton 0–1 Manchester United (yellows 2–3, xG 0.63–1.27); Nov 2025 Premier League Manchester United 0–1 Everton (yellows 2–0, reds 0–1, xG 1.71–0.21); Feb 2025 Premier League Everton 2–2 Manchester United (yellows 4–1, xG 1.91–0.41) · 18 yellows in 4
**Archetype (F5):** used **PM** — derived PM [DERIVED] · signals, last 6 league matches: possession 53.3%, PPDA 13.2 (Understat, 6 matches; lower = harder press), opponent offsides forced 1.7/match (line height), fast breaks 2.1/match (season), both sides' xG 2.52/match (openness) · note: possession 53.3 v 52. Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap).
**Squad changes (F20, since 01 Jun 2026):** in 14 (permanent 8, loan 0, free 0, loan returns 6) · out 8 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 8 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 12.79 | 7 | Big chances against | 25 | 15 |
| xGOT | 9.56 | 10 | Box shots against | 65 | 7 |
| xA | 9.00 | 4 | Corners against | 29 | 1 |
| Shots | 155 | 1 | Crosses faced | 128 | 7 |
| SoT | 40 | 4 | Dribbled past | 62 | 14 |
| Big chances | 18 | 10 | Errors→shot | 4 | 3 |
| Shots in box | 85 | 5 | GK goals prevented | 0.15 | 9 |
| Corners | 48 | 3 | Clearances | 155 | 19 |
| Crosses | 167 | 3 | Tackles | 130 | 10 |
| Fast breaks | 17 | 1 | Interceptions | 91 | 1 |
| FK shots | 3 | 8 | Def. contributions | 398 | 18 |
| Possession % | 56.50 | 6 | Aerial % | 50 | 9 |
| Pass % | 85.95 | 5 | Duel % | 51.17 | 7 |
| Long balls | 264 | 8 | Fouls | 80 | 3 |
| Dribbles | 62 | 4 | Yellows | 16 | 10 |
| Shots against | 87 | 4 | Km covered | 898 | 18 |
| SoT against | 35 | 12 | Sprints | 818 | 17 |
Per match: xG 1.60 · xGOT 1.20 · shots 19.4 · shots against 10.9 · big chances 2.2 for / 3.1 against · corners 6.0 / 3.6 · crosses 20.9 / 16.0 · possession 56.5%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | A | Everton | 2–2 | 0.69/0.87 | 1.01/1.06 | 55 | 14/18 | 3/6 | 6/14 | 6/7 | 1/1 | 3/4 | 11/4 v 21/4 | 3/1 |
| 4 | H | Manchester City | 0–1 | 1/0.94 | 1.10/1.14 | 55 | 16/6 | 3/2 | 6/2 | 4/3 | 1/2 | 6/7 | 27/6 v 14/3 | 1/4 |
| 5 | A | Fulham | 1–1 | 1.60/2.19 | 1.62/1.72 | 58 | 29/12 | 6/6 | 17/11 | 13/1 | 2/3 | 13/3 | 31/7 v 10/3 | 1/2 |
| 6 | H | Tottenham Hotspur | 1–1 | 0.80/0.87 | 1.62/2.03 | 50 | 12/12 | 4/3 | 8/8 | 3/6 | 1/4 | 4/4 | 9/2 v 18/3 | 2/2 |
| 7 | A | Leeds United | 1–1 | 0.92/1.08 | 1.41/1.43 | 39 | 13/12 | 3/5 | 6/10 | 6/1 | 2/2 | 3/2 | 10/2 v 29/4 | 2/3 |
| 8 | H | Bournemouth | 0–3 | 1.17/0.84 | 2.15/2.56 | 63 | 17/10 | 5/4 | 8/9 | 5/1 | 0/6 | 5/4 | 16/3 v 12/4 | 1/0 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | A | Everton | 2–2 | 4-2-3-1 | 11/7 | 3/3 | 0/0 | 527/418 | 47/49 | Diallo (Knock Injury), Baleba (Ankle Injury), Ugarte (Cruciate Ligament Injury) | Nørgaard (Muscle Injury) | John Brooks |
| 4 | H | Manchester City | 0–1 | 4-2-3-1 | 17/10 | 1/2 | 0/1 | 487/403 | 54/38 | Diallo (Muscle Injury), Baleba (Ankle Injury), Ugarte (Cruciate Ligament Injury), Heaton (Abdominal Injury), Shaw (Physical Discomfort; doubtful) | — | Michael Oliver |
| 5 | A | Fulham | 1–1 | 4-2-3-1 | 5/9 | 0/3 | 0/0 | 606/457 | 72/39 | Diallo (Muscle Injury), Šeško (Shin Injury), Ugarte (Cruciate Ligament Injury), Ligt (Back Injury), Heaton (Abdominal Injury) | Tete (Concussion), Cairney (Knee Injury) | Peter Bankes |
| 6 | H | Tottenham Hotspur | 1–1 | 4-2-3-1 | 13/16 | 4/3 | 0/1 | 467/464 | 55/48 | Šeško (Shin Injury), Ugarte (Cruciate Ligament Injury), Ligt (Back Injury), Dorgu (Hamstring Injury), Heaton (Abdominal Injury), Mazraoui (Back Injury; doubtful) | Richarlison (coach decision), Mudryk (Ankle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Stuart Attwell |
| 7 | A | Leeds United | 1–1 | 4-2-3-1 | 5/16 | 2/2 | 0/0 | 354/532 | 59/73 | Šeško (Shin Injury), Ugarte (Cruciate Ligament Injury), Dorgu (Hamstring Injury), Heaton (Abdominal Injury), Mainoo (Knock Injury; doubtful), Shaw (Knock Injury; doubtful) | Rodon (Hamstring Injury), Joseph (Knee Injury), James (Back Injury; doubtful) | Darren England |
| 8 | H | Bournemouth | 0–3 | 4-2-3-1 | 13/17 | 4/1 | 0/0 | 649/374 | 58/62 | Šeško (Shin Injury), Ugarte (Cruciate Ligament Injury), Dorgu (Hamstring Injury), Rashford (Hip Injury; doubtful) | Scott (Muscle Injury), Tóth (Hamstring Injury), Araujo (Thigh Injury) | Jarred Gillett |
Per match: fouls 10.0 / 12.1 · yellows 2.00 / 2.38 · reds 0 / 2 (season) · offsides forced 1.4, committed 1.9 · crosses attempted 20.9 / faced 16.0. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 1.93 for / 1.73 against per match · Away (4): xG 1.26 / 1.26. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW8 H v Bournemouth 0–3 (Sun 25 Oct 14:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Senne Lammens | G | 90 | 5.7 | 0.00 | 0.04 | 1 | 0 | 0 | 0 | 43 |
| Leny Yoro | D | 90 | 6 | 0.18 | 0.19 | 1 | 2 | 5 | 0 | 91 |
| Harry Maguire | D | 90 | 6.6 | 0.00 | 0.05 | 0 | 0 | 5 | 0 | 95 |
| Ayden Heaven | D | 65 | 6.2 | 0.00 | 0.00 | 0 | 0 | 8 | 0 | 73 |
| Diogo Dalot | D | 90 | 6.7 | 0.03 | 0.03 | 1 | 1 | 6 | 7 | 93 |
| Andrey Santos | M | 90 | 6.9 | 0.15 | 0.04 | 1 | 1 | 6 | 0 | 91 |
| Carlos Baleba | M | 72 | 6.6 | 0.05 | 0.02 | 0 | 1 | 4 | 0 | 60 |
| Amad Diallo | M | 78 | 6.8 | 0.02 | 0.09 | 1 | 1 | 1 | 0 | 45 |
| Youri Tielemans | M | 45 | 5.9 | 0.00 | 0.00 | 0 | 0 | 0 | 1 | 26 |
| Mason Mount | M | 90 | 6.9 | 0.08 | 0.15 | 3 | 3 | 3 | 6 | 88 |
| Bryan Mbeumo | F | 90 | 6.4 | 0.26 | 0.04 | 2 | 2 | 0 | 0 | 45 |
Subs used: Matheus Cunha (45'), Lisandro Martínez (25'), Joshua Zirkzee (18'), Shea Lacey (12')
Goals: 38' Rayan (assist Justin Kluivert) [opp]; 43' Marcus Tavernier (assist Adrien Truffert) [opp]; 71' Evanilson (assist Lewis Cook) [opp]
Substitutions (own): 46' Matheus Cunha for Youri Tielemans; 65' Lisandro Martínez for Ayden Heaven; 72' Joshua Zirkzee for Carlos Baleba; 78' Shea Lacey for Amad Diallo
Cards: 22' Andrey Santos (yellow, own); 27' Tyler Adams (yellow, opp); 37' Ayden Heaven (yellow, own); 40' Youri Tielemans (yellow, own); 45' Harry Maguire (yellow, own)
**Baseline XI change vs GW7 (4-2-3-1 → 4-2-3-1):** in — Ayden Heaven, Mason Mount; out — Bruno Fernandes, Lisandro Martínez.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 3 | A Everton | 46' | FOR | Bryan Mbeumo | Kobbie Mainoo | open play | 0.04 |
| 3 | A Everton | 83' | AGAINST | Tyrique George | Hayden Hackney | open play | 0.05 |
| 3 | A Everton | 88' | FOR | Benjamin Šeško | Luke Shaw | open play | 0.41 |
| 3 | A Everton | 90' | AGAINST | Ainsley Maitland-Niles | — | open play | 0.03 |
| 4 | H Manchester City | 60' | AGAINST | Erling Haaland | — | open play | 0.58 |
| 5 | A Fulham | 63' | AGAINST | Lisandro Martínez | — | own goal | — |
| 5 | A Fulham | 89' | FOR | Matheus Cunha | Patrick Dorgu | open play | 0.02 |
| 6 | H Tottenham Hotspur | 73' | FOR | Bryan Mbeumo | Matheus Cunha | open play | 0.09 |
| 6 | H Tottenham Hotspur | 90' | AGAINST | Dominic Solanke | Sandro Tonali | open play | 0.36 |
| 7 | A Leeds United | 35' | FOR | Bryan Mbeumo | Youri Tielemans | open play | 0.41 |
| 7 | A Leeds United | 51' | AGAINST | Dominic Calvert-Lewin | Tarik Muharemović | corner | 0.56 |
| 8 | H Bournemouth | 38' | AGAINST | Rayan | Justin Kluivert | set piece | 0.18 |
| 8 | H Bournemouth | 43' | AGAINST | Marcus Tavernier | Adrien Truffert | open play | 0.55 |
| 8 | H Bournemouth | 71' | AGAINST | Evanilson | Lewis Cook | open play | 0.39 |
Scored 10: open play 8, own goal 1, penalty 1 · Conceded 13: open play 8, corner 2, set piece 2, own goal 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW6 FOR v Tottenham Hotspur 73' Bryan Mbeumo (assist Matheus Cunha, key pass Luke Shaw): G O O O A A A L - Bryan Mbeumo scores with the left foot! · before: 73' Matheus Cunha creates a scoring opportunity for his teammate ‹ 72' Dominic Solanke successfully blocks the shot ‹ 72' A shot by Harry Maguire is blocked.
- GW6 AG v Tottenham Hotspur 90+2' Dominic Solanke (assist Sandro Tonali): G O O O A A A L - Dominic Solanke from Tottenham heads the ball home! · before: 90+2' The cross by Sandro Tonali from Tottenham successfully finds a teammate in the box. ‹ 90+2' Diogo Dalot from Manchester United intercepts a cross aimed towards the box. ‹ 90+2' Diogo Dalot from Manchester United intercepts a cross aimed towards the box.
- GW7 FOR v Leeds United 35' Bryan Mbeumo (assist Youri Tielemans): G O O O A A A L - Bryan Mbeumo scores with the left foot! · before: 35' The cross by Youri Tielemans from Manchester United successfully finds a teammate in the bo ‹ 35' Dominic Calvert-Lewin from Leeds is ruled offside. ‹ 35' Tarik Muharemovic relieves the pressure with a clearance
- GW7 AG v Leeds United 51' Dominic Calvert-Lewin (assist Tarik Muharemovic): G O O O A A A L - Dominic Calvert-Lewin scores with the right foot! · before: 51' A chance presents itself to Tarik Muharemovic from Leeds but his header goes wide ‹ 51' Anton Stach from Leeds swings in the corner from the right. ‹ 51' Noussair Mazraoui from Manchester United intercepts a cross aimed towards the box.
- GW8 AG v Bournemouth 38' Rayan (assist Justin Kluivert): G O O O A A A L - Rayan volleys the ball into the back of the net with the left. A great finish! · before: 38' The cross by Justin Kluivert from Bournemouth successfully finds a teammate in the box. ‹ 37' Ayden Heaven from Manchester United receives a yellow card after a dangerous challenge on a ‹ 37' Dangerous challenge by Ayden Heaven from Manchester United. Evanilson on the receiving end 
- GW8 AG v Bournemouth 43' Marcus Tavernier (assist Adrien Truffert): G O O O A A A L - Marcus Tavernier scores with the left foot! · before: 43' The cross by Marcus Tavernier from Bournemouth successfully finds a teammate in the box. ‹ 42' Adam Smith makes the tackle and wins possession for his team ‹ 41' Lewis Cook from Bournemouth intercepts a cross aimed towards the box.
- GW8 AG v Bournemouth 71' Evanilson (assist Lewis Cook): G O O O A A A L - Evanilson from Bournemouth beats the keeper from outside the box with the right foot! · before: 68' Lisandro Martinez from Manchester United goes a bit too far there as he pulls down Rayan ‹ 68' Lisandro Martinez shoots from outside the box, but Djordje Petrovic has it under control ‹ 67' Bryan Mbeumo wins an air challenge against James Hill

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW3 A v Everton 83' Tyrique George: no structured culprit — reports only
- GW3 A v Everton 90' Ainsley Maitland-Niles: no structured culprit — reports only
  · GW3 other flags: Diogo Dalot errorLeadToAShot 1
- GW4 H v Manchester City 60' Erling Haaland: no structured culprit — reports only
- GW5 A v Fulham 63' Lisandro Martínez [OG]: Lisandro Martínez own goal [CONFIRMED — SofaScore]
- GW6 H v Tottenham Hotspur 90' Dominic Solanke: no structured culprit — reports only
  · GW6 other flags: Harry Maguire errorLeadToAShot 1; Senne Lammens errorLeadToAShot 1; Leny Yoro errorLeadToAShot 1, lastManTackle 1
- GW7 A v Leeds United 51' Dominic Calvert-Lewin: no structured culprit — reports only
  · GW7 other flags: Noussair Mazraoui clearanceOffLine 1
- GW8 H v Bournemouth 38' Rayan: no structured culprit — reports only
- GW8 H v Bournemouth 43' Marcus Tavernier: no structured culprit — reports only
- GW8 H v Bournemouth 71' Evanilson: no structured culprit — reports only
  · GW8 error leading to a goal (SofaScore, match level — 3 conceded, the goal is not identified): Senne Lammens, Leny Yoro [CONFIRMED — SofaScore error flag]

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 117 | 11.22 | 8 | 66 | 9.70 | 8 |
| corner | 31 | 1.37 | 0 | 13 | 2.32 | 2 |
| set piece | 4 | 0.17 | 0 | 9 | 1.52 | 2 |
| direct FK | 3 | 0.12 | 0 | 0 | 0.00 | 0 |
| penalty | 1 | 0.76 | 1 | 0 | 0.00 | 0 |
Totals per match: xG 1.71 (npxG 1.61) for, xGA 1.69 (np 1.69) against · dead-ball share of xG 18% for, 28% against · penalties won 1, conceded 0 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 31 shots, xG 1.37, 0 goals, headed 10: penalty area, central 11 shots, xG 0.69, 0 goals; 6-yard box, central 3 shots, xG 0.25, 0 goals; outside box, central 7 shots, xG 0.18, 0 goals · against — 13 shots conceded, xG 2.32, 2 goals, headed 3: 6-yard box, central 3 shots, xG 1.51, 1 goals; penalty area, central 2 shots, xG 0.59, 1 goals; outside box, central 5 shots, xG 0.13, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 29 · corner shots conceded 13 (headed 3), xG 2.32, goals 2 · xG per corner faced 0.080 (rank 2 of 20, 1 = weakest) · weak zone: six-yard box (1.53 xG, 66% of theirs v 65% league) · signal: **WEAK — positive pairing for opposing aerial targets** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–8 [CONFIRMED — LiveScore Block L, 59 corners; side L/R as LiveScore records it; foot from SofaScore]: Bruno Fernandes 28 (22L/6R, 10 short, right foot); Bryan Mbeumo 16 (0L/16R, 3 short, left foot); Amad Diallo 5 (1L/4R, 1 short, left foot); Mason Mount 5 (3L/2R, right foot). First contact on corners that ended in a shot (Understat) — for: Diogo Dalot 4 (1 headed), Lisandro Martínez 4, Harry Maguire 3 (3 headed), Kobbie Mainoo 3, Matheus Cunha 2 (2 headed) · against (who beat them): Dara O&#039;Shea 1 (1 headed), Tarik Muharemovic 1 (1 headed), Rayan 1 (1 headed), Oliver McBurnie 1, Semi Ajayi 1 — 1 goal. Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 42.4 (rank 7 of 20, 1 = highest line) · block length 20.2 (rank 9, 1 = most compact) · width 66.8. Per match: GW3 A v Everton 4-2-3-1: back line 36, front 56, length 20, width 66 (55% poss); GW4 H v Manchester City 4-2-3-1: back line 45, front 67, length 22, width 70 (55% poss); GW5 A v Fulham 4-2-3-1: back line 47, front 68, length 21, width 69 (58% poss); GW6 H v Tottenham Hotspur 4-2-3-1: back line 38, front 60, length 22, width 63 (50% poss); GW7 A v Leeds United 4-2-3-1: back line 36, front 56, length 19, width 67 (39% poss); GW8 H v Bournemouth 4-2-3-1: back line 40, front 58, length 18, width 67 (63% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 2 league match(es) v LB-coded sides — xG 3.30/match and 1.5 pts/match v 1.03 and 0.7 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW1 A v Hull City 0–2, xG 1.83, box shots 15, poss 72%; GW2 H v Ipswich Town 5–2, xG 4.77, box shots 19, poss 60%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Fernandes 6, Rashford 3, Mbeumo 2** · FPL editorial order: B.Fernandes #1, Mbeumo #2, Mount #3
- Direct free-kick shooters: **Rashford 2, Fernandes 1** · FPL order: B.Fernandes #1, Mbeumo #2, Rashford #3
- Penalties taken: **Fernandes 1** · FPL order: B.Fernandes #1, Mbeumo #2, Tielemans #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Fernandes 2, Dorgu 1**
- Corner targets (headed shots from corners): **Maguire 3, Cunha 2, Heaven 1, Dalot 1** · corner shots 31

**Through-ball suppliers (Block P, PL/Opta, season):** Youri Tielemans 6 (0.91/90, percentile 97, 592 min); Bruno Fernandes 6 (0.86/90, percentile 97, 630 min); Matheus Cunha 3 (0.49/90, percentile 89, 550 min); Leny Yoro 1 (0.34/90, percentile 81, 261 min); Andrey Santos 1 (0.34/90, percentile 81, 263 min) · club total 23 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 289 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 11.72, field tilt 81.2, possession 71.8%, box entries 20, direct speed 2.3, SCA 41; GW2: PPDA 7.76, field tilt 66.3, possession 59.6%, box entries 20, direct speed 1.99, SCA 62; GW3: PPDA 14, field tilt 40.8, possession 54.2%, box entries 15, direct speed 1.65, SCA 26; GW4: PPDA 7.26, field tilt 70.2, possession 55%, box entries 17, direct speed 2.57, SCA 29; GW5: PPDA 17.33, field tilt 71.7, possession 57.5%, box entries 19, direct speed 1.72, SCA 57; GW6: PPDA 7.7, field tilt 46.1, possession 49.6%, box entries 13, direct speed 2.97, SCA 23; GW7: PPDA 17.23, field tilt 40.1, possession 38.9%, box entries 9, direct speed 2.8, SCA 26; GW8: PPDA 10.21, field tilt 63.2, possession 62.2%, box entries 10, direct speed 2.35, SCA 32

**Zone 14 (C13, SofaScore heat-map points, 8 league matches):** for 43.4/match (rank 1 of 20) · conceded 27.1/match (rank 13 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 9.2/match · allowed 4.2/match · PPDA 12.5. Per match for/allowed: GW3 7/7; GW4 12/2; GW5 15/5; GW6 8/9; GW7 4/5; GW8 6/2 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 8 league matches, weights last-3 ×3 / older ×1
- GK: Senne Lammens (14, 3/3)
- DEF: Harry Maguire (14, 3/3), Diogo Dalot (10, 2/3), Lisandro Martínez (10, 2/3), Leny Yoro (9, 3/3)
- MID: Youri Tielemans (14, 3/3), Bryan Mbeumo (14, 3/3), Bruno Fernandes (11, 2/3), Amad Diallo (9, 3/3), Andrey Santos (7, 2/3)
- FWD: Matheus Cunha (8, 1/3)
- Contested slots: M Andrey Santos 7 v Kobbie Mainoo 7 · Excluded (FPL flag): none
- Absent last match (E12, SofaScore list): Šeško (Shin Injury), Ugarte (Cruciate Ligament Injury), Dorgu (Hamstring Injury), Rashford (Hip Injury; doubtful)
- Substitutions this season (C3): GW6 90' Luke Shaw→Ayden Heaven CARD-RISK; GW6 90' Matheus Cunha→Marcus Rashford LATE; GW6 59' Youri Tielemans→Carlos Baleba TACTICAL; GW6 59' Leny Yoro→Diogo Dalot TACTICAL; GW6 59' Amad Diallo→Joshua Zirkzee TACTICAL; GW7 84' Youri Tielemans→Matheus Cunha TACTICAL; GW7 74' Carlos Baleba→Mason Mount TACTICAL; GW7 46' Lisandro Martínez→Noussair Mazraoui HALF-TIME; GW8 78' Amad Diallo→Shea Lacey CHASING; GW8 72' Carlos Baleba→Joshua Zirkzee CHASING; GW8 65' Ayden Heaven→Lisandro Martínez CARD-RISK; GW8 46' Youri Tielemans→Matheus Cunha HALF-TIME

### First-choice players and absences (F14) — generated 2026-10-27 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Senne Lammens | start weight 14 | OK | a | — | — |
| CB | Harry Maguire | start weight 14 | OK | a | Ayden Heaven | — |
| CB | Lisandro Martínez | start weight 10 | OK | a 100% | Ayden Heaven | — |
| xGI #1 | Bryan Mbeumo | xGI 5.16 | OK | a | Matheus Cunha | — |
| xGI #2 | Bruno Fernandes | xGI 4.17 | OK | a | Matheus Cunha | — |
| Penalties #1 (FPL) | B.Fernandes | FPL order | OK | a | Mbeumo | — |
| Direct FK #1 (FPL) | B.Fernandes | FPL order | OK | a | Mbeumo | — |
| Corners (observed) | Bruno Fernandes | 28 corners taken | OK | a | Bryan Mbeumo | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 A Hull City: Lisandro Martínez (did not start) · GW2 H Ipswich Town: all started · GW3 A Everton: all started · GW4 H Manchester City: all started · GW5 A Fulham: all started · GW6 H Tottenham Hotspur: all started · GW7 A Leeds United: all started · GW8 H Bournemouth: Lisandro Martínez (did not start), Bruno Fernandes (did not start)

### Next fixtures (all competitions)
- Sat 31 Oct 12:30 UTC · Premier League R9 · A v Chelsea
- Tue 03 Nov 20:00 UTC · UEFA Champions League R4 · H v AS Roma
- Sun 08 Nov 16:30 UTC · Premier League R10 · H v Aston Villa
- Sun 22 Nov 16:30 UTC · Premier League R11 · A v Liverpool FC
- Wed 25 Nov 20:00 UTC · UEFA Champions League R5 · A v Sporting CP
- Sat 28 Nov 15:00 UTC · Premier League R12 · H v Brentford

### FPL availability flags (players with league minutes this season)
Dorgu — Hamstring injury - Expected back 25 Oct (0%); Shaw — Unspecified injury - Unknown return date (0%); Rashford — Hip injury - 75% chance of playing (75%); Mainoo — Unspecified injury - Expected back 8 Nov (0%); Šeško — Shin injury - Unknown return date (0%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 A Hull City 0–2 · xG 1.83–1.01 · poss 72% · 4-2-3-1 · scorers: none
- GW2 H Ipswich Town 5–2 · xG 4.77–2.06 · poss 60% · 4-2-3-1 · scorers: Bruno Fernandes 40', Jacob Greaves 56', Bruno Fernandes 61', Bruno Fernandes 68', Bryan Mbeumo 82'
- GW3 A Everton 2–2 · xG 0.69–1.01 · poss 55% · 4-2-3-1 · scorers: Bryan Mbeumo 46', Benjamin Šeško 88'
- GW4 H Manchester City 0–1 · xG 1–1.10 · poss 55% · 4-2-3-1 · scorers: none
- GW5 A Fulham 1–1 · xG 1.60–1.62 · poss 58% · 4-2-3-1 · scorers: Matheus Cunha 89'
- GW6 H Tottenham Hotspur 1–1 · xG 0.80–1.62 · poss 50% · 4-2-3-1 · scorers: Bryan Mbeumo 73'
- GW7 A Leeds United 1–1 · xG 0.92–1.41 · poss 39% · 4-2-3-1 · scorers: Bryan Mbeumo 35'
- GW8 H Bournemouth 0–3 · xG 1.17–2.15 · poss 63% · 4-2-3-1 · scorers: none
### Corner takers observed (LiveScore Block L)
- Bruno Fernandes: 28 corners (22 left, 6 right, 10 short)
- Bryan Mbeumo: 16 corners (0 left, 16 right, 3 short)
- Amad Diallo: 5 corners (1 left, 4 right, 1 short)
- Mason Mount: 5 corners (3 left, 2 right)
- Matheus Cunha: 4 corners (4 left, 0 right)
- Shea Lacey: 1 corners (0 left, 1 right)
