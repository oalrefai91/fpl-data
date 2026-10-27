# Newcastle United — data doc
*Feeder-written (2026-10-27 07:42 UTC); do not edit. Narrative: `profiles/teams/newcastle.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-10-27 07:42 UTC)
**Manager:** Matthias Jaissle · **Venue:** St James' Park · **SofaScore:** https://www.sofascore.com/football/team/newcastle-united/39 · **FPL code:** NEW
**Table:** 8th, 11 pts (3W 2D 3L, GF 12 GA 14) · Home 11th (1-2-1, 6:6) · Away 7th (2-0-2, 6:8)
**Standing context (F15):** 30 league games left · points v 4th -4, v 5th -2, v 17th (last safe) +4, v 18th +5 · goal difference -2
**Suspension watch (D7, all players of the club):** N.Gonzalez — 🟨 2 from a ban (3/5); J.Murphy — 🟨 2 from a ban (3/5); Wissa — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 8 league matches):** goals after 75′ — for 2/12 (17%), against 3/14 (21%) · scored first 4, conceded first 4 (50% of matches), goalless 0 · points from losing positions 1 of 12 (4 matches behind at some point) · points from winning positions 10 of 12 (4 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Botman (DEF) 11.3/90, hit 5/7; Hall (DEF) 8.8/90, hit 4/8; Thiaw (DEF) 8.8/90, hit 3/8; L.Miley (MID) 11.4/90, hit 2/7; N.Gonzalez (MID) 10.0/90, hit 2/6
**Manager tenure (F13, SofaScore):** Matthias Jaissle since 05 Aug 2026 · 10 matches in charge, all competitions (5W 2D 3L) · 8 league matches this season · contract to 30 Jun 2030 · previous club Al-Ahli · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Sunderland — last 4: Mar 2026 Premier League Newcastle United 1–2 Sunderland (yellows 1–6, xG 1.29–2.44); Dec 2025 Premier League Sunderland 1–0 Newcastle United (yellows 5–4, xG 0.30–0.24); Jan 2024 FA Cup Sunderland 0–3 Newcastle United (yellows 4–2, no xG); Mar 2016 Premier League Newcastle United 1–1 Sunderland (yellows 4–1, no xG) · 27 yellows in 4
**Archetype (F5):** used **HP** — derived HP [DERIVED] · signals, last 6 league matches: possession 54.7%, PPDA 8.1 (Understat, 6 matches; lower = harder press), opponent offsides forced 1.7/match (line height), fast breaks 1.2/match (season), both sides' xG 2.75/match (openness). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap).
**Squad changes (F20, since 01 Jun 2026):** in 10 (permanent 9, loan 0, free 0, loan returns 1) · out 13 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 8 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 9.10 | 16 | Big chances against | 18 | 10 |
| xGOT | 8.75 | 13 | Box shots against | 82 | 16 |
| xA | 6.20 | 14 | Corners against | 44 | 16 |
| Shots | 96 | 13 | Crosses faced | 152 | 15 |
| SoT | 27 | 17 | Dribbled past | 60 | 12 |
| Big chances | 14 | 16 | Errors→shot | 11 | 19 |
| Shots in box | 60 | 15 | GK goals prevented | 0.76 | 6 |
| Corners | 36 | 12 | Clearances | 258 | 1 |
| Crosses | 127 | 16 | Tackles | 106 | 17 |
| Fast breaks | 10 | 10 | Interceptions | 55 | 20 |
| FK shots | 2 | 11 | Def. contributions | 472 | 5 |
| Possession % | 51.12 | 8 | Aerial % | 57.36 | 2 |
| Pass % | 82.19 | 11 | Duel % | 49.88 | 13 |
| Long balls | 293 | 6 | Fouls | 95 | 12 |
| Dribbles | 60 | 8 | Yellows | 22 | 18 |
| Shots against | 138 | 20 | Km covered | 923 | 7 |
| SoT against | 41 | 17 | Sprints | 983 | 3 |
Per match: xG 1.14 · xGOT 1.09 · shots 12.0 · shots against 17.2 · big chances 1.8 for / 2.2 against · corners 4.5 / 5.5 · crosses 15.9 / 19.0 · possession 51.125%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Bournemouth | 2–2 | 0.71/0.78 | 1.37/1.68 | 58 | 8/17 | 2/5 | 5/9 | 2/7 | 1/2 | 4/3 | 11/2 v 12/2 | 1/1 |
| 4 | A | Leeds United | 1–4 | 0.88/0.80 | 2.08/2.29 | 50 | 7/15 | 5/6 | 4/10 | 0/5 | 2/3 | 5/5 | 18/1 v 16/6 | 2/3 |
| 5 | H | Hull City | 2–1 | 1.44/1.38 | 1.59/1.16 | 56 | 12/22 | 5/4 | 9/12 | 2/11 | 2/1 | 4/7 | 16/3 v 33/6 | 1/2 |
| 6 | A | Coventry City | 1–4 | 1.84/2.22 | 1.47/1.66 | 67 | 19/9 | 6/6 | 11/6 | 6/3 | 3/2 | 6/2 | 17/3 v 9/2 | 2/5 |
| 7 | H | Aston Villa | 0–1 | 0.99/0.92 | 1.57/2.09 | 50 | 16/15 | 1/3 | 11/11 | 9/8 | 0/3 | 4/5 | 29/5 v 10/2 | 0/5 |
| 8 | A | Crystal Palace | 2–0 | 0.95/1.30 | 1.59/2.20 | 47 | 10/17 | 2/4 | 7/9 | 4/5 | 2/2 | 4/7 | 14/3 v 20/3 | 4/1 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Bournemouth | 2–2 | 4-2-3-1 | 19/17 | 2/3 | 0/0 | 459/335 | 38/64 | Burn (Ankle Injury), Joelinton (Muscle Injury), Osula (Knock Injury) | Adli (Calf Injury), Kroupi (Foot Injury), Araujo (Thigh Injury), Milosavljević (Knock Injury) | Robert Jones |
| 4 | A | Leeds United | 1–4 | 4-2-3-1 | 13/8 | 2/1 | 0/0 | 433/440 | 51/48 | Burn (Ankle Injury), Joelinton (Muscle Injury), Osula (Knock Injury), Jaouen (Ankle Injury; doubtful) | Rodon (Hamstring Injury), Joseph (Knee Injury) | Michael Salisbury |
| 5 | H | Hull City | 2–1 | 4-2-3-1 | 4/10 | 1/5 | 0/0 | 523/382 | 43/58 | Dedić (Knock Injury), Elanga (Knock Injury), Burn (Ankle Injury), Jaouen (Ankle Injury), Ramsey (Thigh Injury), Joelinton (Muscle Injury), González (Head Injury), Osula (Knock Injury) | Hughes (Groin Injury), Gyabi (Groin Injury), Morita (Groin Injury), Ansah (Back Injury), Butland (Elbow Injury), Mendy (Concussion), Targett (Ankle Injury; doubtful) | Tony Harrington |
| 6 | A | Coventry City | 1–4 | 4-2-3-1 | 10/3 | 1/1 | 0/0 | 548/264 | 59/67 | Elanga (Knock Injury), Jaouen (Hamstring Injury) | Awoniyi (ban (red)), Amenda (Calf Injury), Wright (Muscle Injury), Eccles (Knock Injury), Woolfenden (Knee Injury) | John Brooks |
| 7 | H | Aston Villa | 0–1 | 4-2-3-1 | 14/11 | 6/2 | 0/0 | 407/431 | 62/48 | Elanga (Knock Injury), Jaouen (Hamstring Injury), Ramsey (Thigh Injury), Livramento (Knock Injury) | Onana (Cruciate Ligament Injury), Maatsen (Ankle Injury), Ruggeri (Hamstring Injury), Hemmings (Knock Injury; doubtful) | Jarred Gillett |
| 8 | A | Crystal Palace | 2–0 | 4-2-3-1 | 10/12 | 3/3 | 0/0 | 352/385 | 67/50 | Jaouen (Hamstring Injury), Livramento (Knock Injury) | Riad (Knee Injury), Tomiyasu (Calf Injury), Larsen (Knock Injury; doubtful), Timber (Knock Injury; doubtful) | Paul Tierney |
Per match: fouls 11.9 / 11.4 · yellows 2.75 / 2.38 · reds 0 / 0 (season) · offsides forced 1.6, committed 2.5 · crosses attempted 15.9 / faced 19.0. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 1.18 for / 1.88 against per match · Away (4): xG 1.10 / 1.56. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW8 A v Crystal Palace 2–0 (Sun 25 Oct 14:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Lukáš Horníček | G | 90 | 8.2 | 0.00 | 0.00 | 0 | 0 | 4 | 0 | 50 |
| Amar Dedić | D | 89 | 7.5 | 0.00 | 0.10 | 1 | 0 | 3 | 1 | 54 |
| Fabian Schär | D | 90 | 7.5 | 0.00 | 0.02 | 1 | 0 | 15 | 0 | 64 |
| Dan Burn | D | 90 | 7.2 | 0.08 | 0.03 | 0 | 1 | 9 | 1 | 54 |
| Lewis Hall | D | 90 | 7.1 | 0.00 | 0.07 | 1 | 0 | 8 | 2 | 70 |
| Nico González | M | 90 | 7.7 | 0.00 | 0.13 | 0 | 0 | 7 | 0 | 61 |
| Joelinton | M | 85 | 6.9 | 0.08 | 0.02 | 1 | 2 | 7 | 0 | 56 |
| Jacob Murphy | M | 90 | 7.6 | 0.00 | 0.28 | 4 | 0 | 5 | 7 | 32 |
| Joe Willock | M | 77 | 6.3 | 0.00 | 0.01 | 1 | 0 | 2 | 0 | 40 |
| Harvey Barnes | M | 77 | 7.4 | 0.27 | 0.01 | 0 | 5 | 1 | 3 | 42 |
| William Osula | F | 77 | 7.3 | 0.52 | 0.00 | 0 | 2 | 2 | 0 | 14 |
Subs used: Jacob Ramsey (13'), Yoane Wissa (13'), Anthony Elanga (13'), Sean Steur (14'), Malick Thiaw (1')
Goals: 47' William Osula (assist Jacob Murphy) [own]; 58' Harvey Barnes (assist Amar Dedić) [own]
Substitutions (own): 77' Anthony Elanga for Harvey Barnes; 77' Jacob Ramsey for Joe Willock; 77' Yoane Wissa for William Osula; 85' Sean Steur for Joelinton; 90' Malick Thiaw for Amar Dedić
Cards: 36' Nico González (yellow, own); 45' Fabian Schär (yellow, own); 75' Yéremy Pino (yellow, opp); 78' Lewis Hall (yellow, own); 79' Anan Khalaili (yellow, opp); 90' Jaydee Canvot (yellow, opp)
**Baseline XI change vs GW7 (4-2-3-1 → 4-2-3-1):** in — Amar Dedić, Dan Burn, Fabian Schär, Jacob Murphy, William Osula; out — Lewis Miley, Malick Thiaw, Matías Fernández-Pardo, Sven Botman, Yoane Wissa.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 3 | H Bournemouth | 9' | AGAINST | Marcus Tavernier | — | open play | 0.63 |
| 3 | H Bournemouth | 35' | AGAINST | Malick Thiaw | — | own goal | — |
| 3 | H Bournemouth | 37' | FOR | Harvey Barnes | Lewis Hall | open play | 0.02 |
| 3 | H Bournemouth | 88' | FOR | Jacob Ramsey | — | set piece | 0.06 |
| 4 | A Leeds United | 32' | AGAINST | Lewis Miley | — | own goal | — |
| 4 | A Leeds United | 34' | AGAINST | Jayden Bogle | Dominic Calvert-Lewin | open play | 0.08 |
| 4 | A Leeds United | 45' | AGAINST | Dominic Calvert-Lewin | Tarik Muharemović | open play | 0.48 |
| 4 | A Leeds United | 59' | AGAINST | Noah Okafor | — | open play | 0.05 |
| 4 | A Leeds United | 90' | FOR | Bazoumana Touré | — | open play | 0.09 |
| 5 | H Hull City | 3' | FOR | Joe Willock | Harvey Barnes | open play | 0.11 |
| 5 | H Hull City | 7' | FOR | Lewis Hall | Harvey Barnes | open play | 0.10 |
| 5 | H Hull City | 67' | AGAINST | Mohamed Ali Cho | Mohamed Belloumi | open play | 0.09 |
| 6 | A Coventry City | 6' | AGAINST | Jack Rudoni | — | penalty | 0.76 |
| 6 | A Coventry City | 48' | AGAINST | Sidiki Cherif | — | open play | 0.07 |
| 6 | A Coventry City | 70' | FOR | Sven Botman | Nico González | open play | 0.02 |
| 6 | A Coventry City | 81' | AGAINST | Ellis Simms | Brandon Thomas-Asante | open play | 0.09 |
| 6 | A Coventry City | 86' | AGAINST | Stephen Mfuni | Jay DaSilva | open play | 0.08 |
| 7 | H Aston Villa | 36' | AGAINST | Johan Manzambi | João Gomes | open play | 0.43 |
| 8 | A Crystal Palace | 47' | FOR | William Osula | Jacob Murphy | open play | 0.51 |
| 8 | A Crystal Palace | 58' | FOR | Harvey Barnes | Amar Dedić | open play | 0.12 |
Scored 12: open play 10, corner 1, set piece 1 · Conceded 14: open play 10, penalty 2, own goal 2. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW6 AG v Coventry City 6' Jack Rudoni [pen]: G O O O A A A L - Jack Rudoni from Coventry puts it away from the penalty spot with the left foot! Lukas Hornicek chose the wrong side. · before: 6' After VAR check, the referee decided to stay with the initial call - penalty for Coventry! ‹ 5' VAR - PENALTY! - The referee has stopped the play. VAR check in progress, a potential penalt ‹ 4' PENALTY - Lukas Hornicek from Newcastle concedes a penalty for tripping Sidiki Cherif.
- GW6 AG v Coventry City 48' Sidiki Cherif: G O O O O O A A L - Sidiki Cherif finds the net with the right foot! · before: 48' Malick Thiaw from Newcastle intercepts a cross aimed towards the box. ‹ 48' A player from Coventry takes a long throw into the opponent's box. ‹ 48' Malick Thiaw from Newcastle intercepts a cross aimed towards the box.
- GW6 FOR v Coventry City 70' Sven Botman (assist Nico Gonzalez): G O O O A A A L - Sven Botman from Newcastle beats the keeper from outside the box with the left foot! · before: 69' Nico Gonzalez is penalised for pushing Jack Rudoni. ‹ 68' Caleb Yirenkyi makes the tackle and wins possession for his team ‹ 68' Goal kick for Newcastle.
- GW6 AG v Coventry City 81' Ellis Simms (assist Brandon Thomas-Asante): G O O O A A A L - Ellis Simms scores with the right foot! · before: 81' Brandon Thomas-Asante makes the tackle and wins possession for his team ‹ 81' Joelinton with a bad execution which leads to a goal for the opponent ‹ 81' Tatsuhiro Sakamoto makes the tackle and wins possession for his team
- GW6 AG v Coventry City 86' Stephen Mfuni (assist Jay Dasilva): G O O O A A A L - Stephen Mfuni scores with the left foot! · before: 86' Lukas Hornicek relieves the pressure with a clearance ‹ 85' Stephen Mfuni sends a header towards goal, but Lukas Hornicek is there to comfortably save  ‹ 85' Victor Torp from Coventry swings in the corner from the left.
- GW7 AG v Aston Villa 36' Johan Manzambi (key pass Alysson Edward): G O O O A A A L - Johan Manzambi from Aston Villa heads the ball home! · before: 36' The cross by Joao Gomes from Aston Villa successfully finds a teammate in the box. ‹ 35' Harvey Barnes from Newcastle is ruled offside. ‹ 35' Matias Fernandez-Pardo relieves the pressure with a clearance
- GW8 FOR v Crystal Palace 47' William Osula (assist Jacob Murphy, key pass Amar Dedic): G O O O A A A L - William Osula volleys the ball into the back of the net with the left. A great finish! · before: 47' The cross by Jacob Murphy from Newcastle successfully finds a teammate in the box. ‹ 46' Anan Khalaili is penalised for pushing Lewis Hall. ‹ 46' Daniel Burn relieves the pressure with a clearance
- GW8 FOR v Crystal Palace 58' Harvey Barnes (assist Amar Dedic, key pass Jacob Murphy): G O O O A A A L - Harvey Barnes scores with the right foot! · before: 58' The cross by Amar Dedic from Newcastle successfully finds a teammate in the box. ‹ 58' Jaydee Canvot makes the tackle and wins possession for his team ‹ 57' Joelinton wins an air challenge against Yeremy Pino

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW3 H v Bournemouth 9' Marcus Tavernier: no structured culprit — reports only
- GW3 H v Bournemouth 35' Malick Thiaw [OG]: Malick Thiaw own goal [CONFIRMED — SofaScore]
  · GW3 other flags: Yoane Wissa errorLeadToAShot 1; Sven Botman errorLeadToAShot 2; Amar Dedić errorLeadToAShot 1
- GW4 A v Leeds United 32' Lewis Miley [OG]: Lewis Miley own goal [CONFIRMED — SofaScore]
- GW4 A v Leeds United 34' Jayden Bogle: no structured culprit — reports only
- GW4 A v Leeds United 45' Dominic Calvert-Lewin: no structured culprit — reports only
- GW4 A v Leeds United 59' Noah Okafor: no structured culprit — reports only
  · GW4 error leading to a goal (SofaScore, match level — 4 conceded, the goal is not identified): Sean Steur [CONFIRMED — SofaScore error flag]
  · GW4 other flags: Sven Botman errorLeadToAShot 1
- GW5 H v Hull City 67' Mohamed Ali Cho: Lewis Miley error leading to the goal [CONFIRMED — SofaScore error flag]
  · GW5 other flags: Lukáš Horníček errorLeadToAShot 1; Lewis Hall errorLeadToAShot 1
- GW6 A v Coventry City 6' Jack Rudoni [pen]: Lukáš Horníček conceded the penalty [CONFIRMED — SofaScore]
- GW6 A v Coventry City 48' Sidiki Cherif: no structured culprit — reports only
- GW6 A v Coventry City 81' Ellis Simms: no structured culprit — reports only
- GW6 A v Coventry City 86' Stephen Mfuni: no structured culprit — reports only
  · GW6 error leading to a goal (SofaScore, match level — 4 conceded, the goal is not identified): Joelinton [CONFIRMED — SofaScore error flag]
  · GW6 other flags: Sven Botman errorLeadToAShot 1
- GW7 H v Aston Villa 36' Johan Manzambi: no structured culprit — reports only

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 76 | 7.89 | 10 | 100 | 9.63 | 10 |
| corner | 7 | 0.75 | 1 | 23 | 2.20 | 0 |
| set piece | 12 | 0.56 | 1 | 9 | 1.79 | 0 |
| direct FK | 2 | 0.09 | 0 | 4 | 0.21 | 0 |
| penalty | 1 | 0.76 | 0 | 2 | 1.52 | 2 |
Totals per match: xG 1.26 (npxG 1.16) for, xGA 1.92 (np 1.73) against · dead-ball share of xG 22% for, 37% against · penalties won 1, conceded 2 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 7 shots, xG 0.75, 1 goals, headed 4: 6-yard box, central 2 shots, xG 0.62, 1 goals; penalty area, central 2 shots, xG 0.06, 0 goals; outside box, left 1 shots, xG 0.03, 0 goals · against — 23 shots conceded, xG 2.20, 0 goals, headed 8: 6-yard box, central 4 shots, xG 1.66, 0 goals; penalty area, central 4 shots, xG 0.19, 0 goals; outside box, left 5 shots, xG 0.10, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 44 · corner shots conceded 23 (headed 8), xG 2.20, goals 0 · xG per corner faced 0.050 (rank 12 of 20, 1 = weakest) · weak zone: six-yard box (1.69 xG, 77% of theirs v 65% league) · signal: **neutral** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–8 [CONFIRMED — LiveScore Block L, 36 corners; side L/R as LiveScore records it; foot from SofaScore]: Lewis Hall 19 (2L/17R, 5 short, left foot); Harvey Barnes 7 (7L/0R, right foot); Jacob Murphy 5 (4L/1R, right foot); Anthony Elanga 3 (3L/0R, right foot). First contact on corners that ended in a shot (Understat) — for: Yoane Wissa 3 (2 headed) — 1 goal, Lewis Hall 2, Nick Woltemade 1 (1 headed), Joelinton 1 (1 headed) · against (who beat them): Alexander Isak 2 (2 headed), Joe Gelhardt 2, Darío Osorio 2, Jan Paul van Hecke 1 (1 headed), Semi Ajayi 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 38.7 (rank 17 of 20, 1 = highest line) · block length 22.7 (rank 16, 1 = most compact) · width 62.5. Per match: GW3 H v Bournemouth 4-2-3-1: back line 37, front 60, length 23, width 64 (58% poss); GW4 A v Leeds United 4-2-3-1: back line 38, front 62, length 24, width 64 (50% poss); GW5 H v Hull City 4-2-3-1: back line 37, front 57, length 20, width 64 (56% poss); GW6 A v Coventry City 4-2-3-1: back line 42, front 67, length 26, width 69 (67% poss); GW7 H v Aston Villa 4-2-3-1: back line 45, front 68, length 23, width 59 (50% poss); GW8 A v Crystal Palace 4-2-3-1: back line 43, front 62, length 18, width 55 (47% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 3 league match(es) v LB-coded sides — xG 1.41/match and 2.0 pts/match v 0.98 and 1.0 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW5 H v Hull City 2–1, xG 1.44, box shots 9, poss 56%; GW6 A v Coventry City 1–4, xG 1.84, box shots 11, poss 67%; GW8 A v Crystal Palace 2–0, xG 0.95, box shots 7, poss 47%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Elanga 2, Hall 1, Woltemade 1** · FPL editorial order: Hall #1, Elanga #2, J.Murphy #3
- Direct free-kick shooters: **Osula 1, Dedic 1** · FPL order: Hall #1, Schär #2, Dedić #3
- Penalties taken: **Wissa 1** · FPL order: Wissa #1, Osula #2
- Set-piece deliverers (assisted 'SetPiece' shots): **Hall 3, Thiaw 2, Schär 2**
- Corner targets (headed shots from corners): **Wissa 2, Woltemade 1, Joelinton 1** · corner shots 7
- **DISAGREEMENT:** observed corner taker Anthony Elanga (2) v FPL #1 Hall — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Jacob Murphy 3 (0.82/90, percentile 96, 331 min); Nico González 3 (0.62/90, percentile 92, 437 min); Sean Steur 1 (0.39/90, percentile 84, 230 min); Yoane Wissa 2 (0.29/90, percentile 76, 622 min) · club total 19 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 289 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 9.61, field tilt 29.5, possession 40%, box entries 7, direct speed 3.26, SCA 24; GW2: PPDA 19.63, field tilt 34.2, possession 42.5%, box entries 10, direct speed 2.17, SCA 22; GW3: PPDA 6.53, field tilt 50.6, possession 57.2%, box entries 8, direct speed 2.41, SCA 16; GW4: PPDA 9.94, field tilt 53.2, possession 49.4%, box entries 7, direct speed 1.63, SCA 14; GW5: PPDA 11.67, field tilt 45.9, possession 55.5%, box entries 6, direct speed 2.01, SCA 20; GW6: PPDA 6.65, field tilt 63.3, possession 66.7%, box entries 22, direct speed 2.3, SCA 38; GW7: PPDA 7.44, field tilt 58.9, possession 50.2%, box entries 12, direct speed 2.49, SCA 30; GW8: PPDA 9.16, field tilt 47.8, possession 46.9%, box entries 9, direct speed 3.34, SCA 17

**Zone 14 (C13, SofaScore heat-map points, 8 league matches):** for 23.8/match (rank 16 of 20) · conceded 30.5/match (rank 9 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 6.4/match · allowed 6.1/match · PPDA 9.6. Per match for/allowed: GW3 8/3; GW4 5/9; GW5 4/7; GW6 7/1; GW7 11/8; GW8 5/10 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 8 league matches, weights last-3 ×3 / older ×1
- GK: Lukáš Horníček (14, 3/3)
- DEF: Lewis Hall (14, 3/3), Malick Thiaw (11, 2/3), Sven Botman (11, 2/3), Amar Dedić (7, 1/3)
- MID: Harvey Barnes (14, 3/3), Nico González (12, 3/3), Joe Willock (12, 3/3), Lewis Miley (11, 2/3), Yoane Wissa (11, 2/3)
- FWD: William Osula (4, 1/3)
- Contested slots: none · Excluded (FPL flag): Matías Fernández-Pardo — Illness - 75% chance of playing
- Absent last match (E12, SofaScore list): Jaouen (Hamstring Injury), Livramento (Knock Injury)
- Substitutions this season (C3): GW6 78' Yoane Wissa→William Osula CHASING; GW6 59' Joe Willock→Joelinton CHASING; GW6 59' Jacob Murphy→Bazoumana Touré CHASING; GW6 59' Lewis Miley→Amar Dedić CHASING; GW7 90' Joelinton→Dan Burn CARD-RISK; GW7 56' Joe Willock→William Osula CHASING; GW7 56' Matías Fernández-Pardo→Bazoumana Touré CHASING; GW8 90' Amar Dedić→Malick Thiaw LATE; GW8 85' Joelinton→Sean Steur LATE; GW8 77' Harvey Barnes→Anthony Elanga GAME-STATE; GW8 77' Joe Willock→Jacob Ramsey GAME-STATE; GW8 77' William Osula→Yoane Wissa GAME-STATE

### First-choice players and absences (F14) — generated 2026-10-27 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Lukáš Horníček | start weight 14 | OK | a | — | — |
| CB | Malick Thiaw | start weight 11 | OK | a | Fabian Schär | — |
| CB | Sven Botman | start weight 11 | OK | a | Fabian Schär | — |
| xGI #1 | Yoane Wissa | xGI 3.10 | OK | a | Joe Willock | — |
| xGI #2 | Harvey Barnes | xGI 2.41 | OK | a | Joe Willock | — |
| Penalties #1 (FPL) | Wissa | FPL order | OK | a | Osula | — |
| Direct FK #1 (FPL) | Hall | FPL order | OK | a | Schär | — |
| Corners (observed) | Lewis Hall | 19 corners taken | OK | a | Harvey Barnes | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Liverpool FC: all started · GW2 A Tottenham Hotspur: all started · GW3 H Bournemouth: all started · GW4 A Leeds United: all started · GW5 H Hull City: all started · GW6 A Coventry City: all started · GW7 H Aston Villa: all started · GW8 A Crystal Palace: Malick Thiaw (did not start), Sven Botman (did not start), Yoane Wissa (did not start)

### Next fixtures (all competitions)
- Thu 29 Oct 19:45 UTC · EFL Cup R4 · A v Everton
- Mon 02 Nov 20:00 UTC · Premier League R9 · H v Everton
- Sat 07 Nov 15:00 UTC · Premier League R10 · A v Fulham
- Sat 21 Nov 17:30 UTC · Premier League R11 · H v Arsenal
- Sun 29 Nov 14:05 UTC · Premier League R12 · A v Brighton & Hove Albion
- Wed 02 Dec 20:15 UTC · Premier League R13 · H v Manchester United

### FPL availability flags (players with league minutes this season)
Livramento — Knee injury - Expected back 7 Nov (0%); Woltemade — Has joined Juventus on loan for the rest of the season (0%); Fernandez-Pardo — Illness - 75% chance of playing (75%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 H Liverpool FC 2–2 · xG 1.58–2.98 · poss 39% · 4-2-3-1 · scorers: Anthony Elanga 5', Joe Willock 57'
- GW2 A Tottenham Hotspur 2–0 · xG 0.72–1.12 · poss 42% · 4-2-3-1 · scorers: Anthony Elanga 62', Yoane Wissa 72'
- GW3 H Bournemouth 2–2 · xG 0.71–1.37 · poss 58% · 4-2-3-1 · scorers: Harvey Barnes 37', Jacob Ramsey 88'
- GW4 A Leeds United 1–4 · xG 0.88–2.08 · poss 50% · 4-2-3-1 · scorers: Bazoumana Touré 90'
- GW5 H Hull City 2–1 · xG 1.44–1.59 · poss 56% · 4-2-3-1 · scorers: Joe Willock 3', Lewis Hall 7'
- GW6 A Coventry City 1–4 · xG 1.84–1.47 · poss 67% · 4-2-3-1 · scorers: Sven Botman 70'
- GW7 H Aston Villa 0–1 · xG 0.99–1.57 · poss 50% · 4-2-3-1 · scorers: none
- GW8 A Crystal Palace 2–0 · xG 0.95–1.59 · poss 47% · 4-2-3-1 · scorers: William Osula 47', Harvey Barnes 58'
### Corner takers observed (LiveScore Block L)
- Lewis Hall: 19 corners (2 left, 17 right, 5 short)
- Harvey Barnes: 7 corners (7 left, 0 right)
- Jacob Murphy: 5 corners (4 left, 1 right)
- Anthony Elanga: 3 corners (3 left, 0 right)
- Matias Fernandez-Pardo: 2 corners (2 left, 0 right, 1 short)
