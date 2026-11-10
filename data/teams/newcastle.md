# Newcastle United — data doc
*Feeder-written (2026-11-10 07:41 UTC); do not edit. Narrative: `profiles/teams/newcastle.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-10 07:41 UTC)
**Manager:** Matthias Jaissle · **Venue:** St James' Park · **SofaScore:** https://www.sofascore.com/football/team/newcastle-united/39 · **FPL code:** NEW
**Table:** 12th, 12 pts (3W 3D 4L, GF 13 GA 16) · Home 17th (1-2-2, 6:7) · Away 7th (2-1-2, 7:9)
**Standing context (F15):** 28 league games left · points v 4th -6, v 5th -4, v 17th (last safe) +3, v 18th +4 · goal difference -3
**Suspension watch (D7, all players of the club):** N.Gonzalez — 🟨 2 from a ban (3/5); Schär — 🟨 2 from a ban (3/5); J.Murphy — 🟨 2 from a ban (3/5); Wissa — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 10 league matches):** goals after 75′ — for 3/13 (23%), against 4/16 (25%) · scored first 5, conceded first 5 (50% of matches), goalless 0 · points from losing positions 1 of 15 (5 matches behind at some point) · points from winning positions 11 of 15 (5 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Botman (DEF) 11.3/90, hit 5/7; Hall (DEF) 8.8/90, hit 5/10; Thiaw (DEF) 8.8/90, hit 3/9; Schär (DEF) 14.6/90, hit 2/5; L.Miley (MID) 11.9/90, hit 2/8; N.Gonzalez (MID) 9.5/90, hit 2/8
**Manager tenure (F13, SofaScore):** Matthias Jaissle since 05 Aug 2026 · 12 matches in charge, all competitions (5W 2D 5L) · 10 league matches this season · contract to 30 Jun 2030 · previous club Al-Ahli · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Sunderland — last 4: Mar 2026 Premier League Newcastle United 1–2 Sunderland (yellows 1–6, xG 1.29–2.44); Dec 2025 Premier League Sunderland 1–0 Newcastle United (yellows 5–4, xG 0.30–0.24); Jan 2024 FA Cup Sunderland 0–3 Newcastle United (yellows 4–2, no xG); Mar 2016 Premier League Newcastle United 1–1 Sunderland (yellows 4–1, no xG) · 27 yellows in 4
**Archetype (F5):** used **HP** — derived HP [DERIVED] · signals, last 6 league matches: possession 52.3%, PPDA 7.9 (Understat, 4 matches; lower = harder press), opponent offsides forced 2.0/match (line height), fast breaks 1.0/match (season), both sides' xG 2.82/match (openness) · note: possession 52.3 v 52; computed from 4 of 6 GWs (no PPDA/possession for GW9, GW10). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 10 (permanent 9, loan 0, free 0, loan returns 1) · out 13 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 10 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 11.53 | 18 | Big chances against | 22 | 8 |
| xGOT | 10.39 | 17 | Box shots against | 100 | 15 |
| xA | 7.24 | 15 | Corners against | 52 | 14 |
| Shots | 122 | 13 | Crosses faced | 188 | 14 |
| SoT | 34 | 17 | Dribbled past | 78 | 13 |
| Big chances | 19 | 17 | Errors→shot | 12 | 16 |
| Shots in box | 73 | 16 | GK goals prevented | 2.37 | 3 |
| Corners | 43 | 12 | Clearances | 324 | 1 |
| Crosses | 162 | 16 | Tackles | 130 | 18 |
| Fast breaks | 10 | 13 | Interceptions | 70 | 18 |
| FK shots | 2 | 16 | Def. contributions | 579 | 6 |
| Possession % | 50.30 | 8 | Aerial % | 54.83 | 3 |
| Pass % | 81.54 | 12 | Duel % | 48.77 | 14 |
| Long balls | 363 | 7 | Fouls | 121 | 13 |
| Dribbles | 67 | 14 | Yellows | 27 | 18 |
| Shots against | 165 | 17 | Km covered | 1158 | 8 |
| SoT against | 51 | 14 | Sprints | 1198 | 3 |
Per match: xG 1.15 · xGOT 1.04 · shots 12.2 · shots against 16.5 · big chances 1.9 for / 2.2 against · corners 4.3 / 5.2 · crosses 16.2 / 18.8 · possession 50.3%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | H | Hull City | 2–1 | 1.44/1.38 | 1.59/1.16 | 56 | 12/22 | 5/4 | 9/12 | 2/11 | 2/1 | 4/7 | 16/3 v 33/6 | 1/2 |
| 6 | A | Coventry City | 1–4 | 1.84/2.22 | 1.47/1.66 | 67 | 19/9 | 6/6 | 11/6 | 6/3 | 3/2 | 6/2 | 17/3 v 9/2 | 2/5 |
| 7 | H | Aston Villa | 0–1 | 0.99/0.92 | 1.57/2.09 | 50 | 16/15 | 1/3 | 11/11 | 9/8 | 0/3 | 4/5 | 29/5 v 10/2 | 0/5 |
| 8 | A | Crystal Palace | 2–0 | 0.95/1.30 | 1.59/2.20 | 47 | 10/17 | 2/4 | 7/9 | 4/5 | 2/2 | 4/7 | 14/3 v 20/3 | 4/1 |
| 9 | H | Everton | 0–1 | 1.29/— | 2.34/— | 52 | 17/16 | 2/5 | 7/11 | 6/1 | 2/4 | 4/5 | 24/7 v 22/7 | 2/0 |
| 10 | A | Fulham | 1–1 | 1.14/— | 0.70/— | 42 | 9/11 | 5/5 | 6/7 | 1/1 | 3/0 | 3/3 | 11/3 v 14/3 | 3/1 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | H | Hull City | 2–1 | 4-2-3-1 | 4/10 | 1/5 | 0/0 | 523/382 | 43/58 | Dedić (Knock Injury), Elanga (Knock Injury), Burn (Ankle Injury), Jaouen (Ankle Injury), Ramsey (Thigh Injury), Joelinton (Muscle Injury), González (Head Injury), Osula (Knock Injury) | Hughes (Groin Injury), Gyabi (Groin Injury), Morita (Groin Injury), Ansah (Back Injury), Butland (Elbow Injury), Mendy (Concussion), Targett (Ankle Injury; doubtful) | Tony Harrington |
| 6 | A | Coventry City | 1–4 | 4-2-3-1 | 10/3 | 1/1 | 0/0 | 548/264 | 59/67 | Elanga (Knock Injury), Jaouen (Hamstring Injury) | Awoniyi (ban (red)), Amenda (Calf Injury), Wright (Muscle Injury), Eccles (Knock Injury), Woolfenden (Knee Injury) | John Brooks |
| 7 | H | Aston Villa | 0–1 | 4-2-3-1 | 14/11 | 6/2 | 0/0 | 407/431 | 62/48 | Elanga (Knock Injury), Jaouen (Hamstring Injury), Ramsey (Thigh Injury), Livramento (Knock Injury) | Onana (Cruciate Ligament Injury), Maatsen (Ankle Injury), Ruggeri (Hamstring Injury), Hemmings (Knock Injury; doubtful) | Jarred Gillett |
| 8 | A | Crystal Palace | 2–0 | 4-2-3-1 | 10/12 | 3/3 | 0/0 | 352/385 | 67/50 | Jaouen (Hamstring Injury), Livramento (Knock Injury) | Riad (Knee Injury), Tomiyasu (Calf Injury), Larsen (Knock Injury; doubtful), Timber (Knock Injury; doubtful) | Paul Tierney |
| 9 | H | Everton | 0–1 | 4-2-3-1 | 13/9 | 4/2 | 1/0 | 428/396 | 70/61 | Jaouen (Hamstring Injury), Livramento (Knock Injury), Miley (Knock Injury; doubtful), Fernández-Pardo (Illness; doubtful) | — | John Brooks |
| 10 | A | Fulham | 1–1 | 4-2-3-1 | 13/9 | 2/0 | 0/0 | 380/526 | 36/67 | Ramsey (ban (cards)), Jaouen (Hamstring Injury), Joelinton (Knock Injury) | Cairney (Knee Injury) | Robert Jones |
Per match: fouls 12.1 / 10.9 · yellows 2.80 / 2.10 · reds 1 / 0 (season) · offsides forced 1.8, committed 2.1 · crosses attempted 16.2 / faced 18.8. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 1.20 for / 1.97 against per match · Away (5): xG 1.11 / 1.39. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW10 A v Fulham 1–1 (Sat 07 Nov 15:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Lukáš Horníček | G | 90 | 6.7 | 0.00 | 0.00 | 0 | 0 | 1 | 0 | 57 |
| Amar Dedić | D | 90 | 6.8 | 0.00 | 0.06 | 1 | 0 | 10 | 2 | 57 |
| Malick Thiaw | D | 85 | 7 | 0.00 | 0.00 | 0 | 0 | 8 | 0 | 61 |
| Dan Burn | D | 90 | 7.1 | 0.00 | 0.00 | 0 | 0 | 11 | 0 | 74 |
| Lewis Hall | D | 90 | 7.3 | 0.24 | 0.00 | 0 | 1 | 12 | 2 | 76 |
| Sean Steur | M | 74 | 6.7 | 0.06 | 0.01 | 0 | 1 | 3 | 0 | 45 |
| Nico González | M | 61 | 6.6 | 0.00 | 0.00 | 0 | 0 | 1 | 0 | 28 |
| Jacob Murphy | M | 90 | 8.2 | 0.02 | 0.17 | 2 | 1 | 4 | 4 | 40 |
| Yoane Wissa | M | 61 | 6.6 | 0.04 | 0.05 | 1 | 1 | 1 | 1 | 17 |
| Harvey Barnes | M | 90 | 6.5 | 0.66 | 0.00 | 0 | 3 | 2 | 2 | 35 |
| William Osula | F | 85 | 6.5 | 0.00 | 0.03 | 2 | 0 | 0 | 0 | 22 |
Subs used: Joe Willock (29'), Lewis Miley (29'), Matías Fernández-Pardo (16'), Fabian Schär (13'), Anthony Elanga (13')
Goals: 80' Jacob Murphy [own]; 83' Rodrigo Muniz [opp]
Substitutions (own): 61' Lewis Miley for Nico González; 61' Joe Willock for Yoane Wissa; 74' Matías Fernández-Pardo for Sean Steur; 85' Anthony Elanga for William Osula; 85' Fabian Schär for Malick Thiaw [injury]
Cards: -5' booking with no player named — staff card (yellow, own; not in SofaScore's card count, no FPL effect); 90' Amar Dedić (yellow, own); 90' Fabian Schär (yellow, own)
**Baseline XI change vs GW9 (4-2-3-1 → 4-2-3-1):** in — Jacob Murphy, Malick Thiaw, Sean Steur, Yoane Wissa; out — Anthony Elanga, Fabian Schär, Joe Willock, Joelinton.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
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
| 9 | H Everton | 49' | AGAINST | Thierno Barry | — | [no Understat] | — |
| 10 | A Fulham | 80' | FOR | Jacob Murphy | — | [no Understat] | — |
| 10 | A Fulham | 83' | AGAINST | Rodrigo Muniz | — | [no Understat] | — |
Scored 13: open play 10, corner 1, set piece 1, [no Understat] 1 · Conceded 16: open play 10, penalty 2, own goal 2, [no Understat] 2. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW8 FOR v Crystal Palace 47' William Osula (assist Jacob Murphy, key pass Amar Dedic): G O O O A A A L - William Osula volleys the ball into the back of the net with the left. A great finish! · before: 47' The cross by Jacob Murphy from Newcastle successfully finds a teammate in the box. ‹ 46' Anan Khalaili is penalised for pushing Lewis Hall. ‹ 46' Daniel Burn relieves the pressure with a clearance
- GW8 FOR v Crystal Palace 58' Harvey Barnes (assist Amar Dedic, key pass Jacob Murphy): G O O O A A A L - Harvey Barnes scores with the right foot! · before: 58' The cross by Amar Dedic from Newcastle successfully finds a teammate in the box. ‹ 58' Jaydee Canvot makes the tackle and wins possession for his team ‹ 57' Joelinton wins an air challenge against Yeremy Pino
- GW9 AG v Everton 49' Thierno Barry: GOAL! It's an easy finish as Thierno Barry from Everton taps the ball into an open goal with the right foot! · before: 49' Good effort by Tyrique George as he directs a shot on target, but the keeper saves it ‹ 49' Kiernan Dewsbury-Hall creates a scoring opportunity for his teammate ‹ 49' Everton with a potentially dangerous attack.
- GW10 FOR v Fulham 80' Jacob Murphy: G O O O A A A L - Jacob Murphy from Newcastle scores from outside the box with the left foot! · before: 80' Due to technical problems, we are unable to deliver game updates at the moment. ‹ 79' Goal kick for Newcastle. ‹ 78' Joseph Willock shoots from outside the box, but Bernd Leno has it under control
- GW10 AG v Fulham 83' Rodrigo Muniz: G O O O O O A A L - Rodrigo Muniz finds the net with the right foot! · before: 83' Alex Iwobi creates a scoring opportunity for his teammate ‹ 82' David Affengruber makes the tackle and wins possession for his team ‹ 82' Jacob Murphy wins an air challenge against Antonee Robinson

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW5 H v Hull City 67' Mohamed Ali Cho: Lewis Miley error leading to the goal [CONFIRMED — SofaScore error flag]
  · GW5 other flags: Lukáš Horníček errorLeadToAShot 1; Lewis Hall errorLeadToAShot 1
- GW6 A v Coventry City 6' Jack Rudoni [pen]: Lukáš Horníček conceded the penalty [CONFIRMED — SofaScore]
- GW6 A v Coventry City 48' Sidiki Cherif: no structured culprit — reports only
- GW6 A v Coventry City 81' Ellis Simms: no structured culprit — reports only
- GW6 A v Coventry City 86' Stephen Mfuni: no structured culprit — reports only
  · GW6 error leading to a goal (SofaScore, match level — 4 conceded, the goal is not identified): Joelinton [CONFIRMED — SofaScore error flag]
  · GW6 other flags: Sven Botman errorLeadToAShot 1
- GW7 H v Aston Villa 36' Johan Manzambi: no structured culprit — reports only
- GW9 H v Everton 49' Thierno Barry: Lukáš Horníček error leading to the goal [CONFIRMED — SofaScore error flag]
  · GW9 other flags: Harvey Barnes errorLeadToAShot 1
- GW10 A v Fulham 83' Rodrigo Muniz: no structured culprit — reports only

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

**Corners (E10 data layer):** observed takers GW1–10 [CONFIRMED — LiveScore Block L, 43 corners; side L/R as LiveScore records it; foot from SofaScore]: Lewis Hall 23 (2L/21R, 6 short, left foot); Jacob Murphy 8 (7L/1R, 1 short, right foot); Harvey Barnes 7 (7L/0R, right foot); Anthony Elanga 3 (3L/0R, right foot). First contact on corners that ended in a shot (Understat) — for: Yoane Wissa 3 (2 headed) — 1 goal, Lewis Hall 2, Nick Woltemade 1 (1 headed), Joelinton 1 (1 headed) · against (who beat them): Alexander Isak 2 (2 headed), Joe Gelhardt 2, Darío Osorio 2, Jan Paul van Hecke 1 (1 headed), Semi Ajayi 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 39.2 (rank 14 of 20, 1 = highest line) · block length 21.4 (rank 12, 1 = most compact) · width 62.1. Per match: GW5 H v Hull City 4-2-3-1: back line 37, front 57, length 20, width 64 (56% poss); GW6 A v Coventry City 4-2-3-1: back line 42, front 67, length 26, width 69 (67% poss); GW7 H v Aston Villa 4-2-3-1: back line 45, front 68, length 23, width 59 (50% poss); GW8 A v Crystal Palace 4-2-3-1: back line 43, front 62, length 18, width 55 (47% poss); GW9 H v Everton 4-2-3-1: back line 44, front 57, length 13, width 57 (52% poss); GW10 A v Fulham 4-2-3-1: back line 38, front 58, length 19, width 64 (42% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 4 league match(es) v LB-coded sides — xG 1.30/match and 1.5 pts/match v 1.05 and 1.0 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW5 H v Hull City 2–1, xG 1.44, box shots 9, poss 56%; GW6 A v Coventry City 1–4, xG 1.84, box shots 11, poss 67%; GW7 H v Aston Villa 0–1, xG 0.99, box shots 11, poss 50%; GW8 A v Crystal Palace 2–0, xG 0.95, box shots 7, poss 47%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Elanga 2, Hall 1, Woltemade 1** · FPL editorial order: Hall #1, Elanga #2, J.Murphy #3
- Direct free-kick shooters: **Osula 1, Dedic 1** · FPL order: Hall #1, Schär #2, Dedić #3
- Penalties taken: **Wissa 1** · FPL order: Wissa #1, Osula #2
- Set-piece deliverers (assisted 'SetPiece' shots): **Hall 3, Thiaw 2, Schär 2**
- Corner targets (headed shots from corners): **Wissa 2, Woltemade 1, Joelinton 1** · corner shots 7
- **DISAGREEMENT:** observed corner taker Anthony Elanga (2) v FPL #1 Hall — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Jacob Murphy 3 (0.62/90, percentile 96, 435 min); William Osula 2 (0.51/90, percentile 89, 354 min); Nico González 3 (0.48/90, percentile 88, 562 min); Anthony Elanga 1 (0.27/90, percentile 78, 329 min); Sean Steur 1 (0.27/90, percentile 78, 330 min); Yoane Wissa 2 (0.25/90, percentile 75, 709 min) · club total 20 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 318 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 9.61, field tilt 29.5, possession 40%, box entries 7, direct speed 3.26, SCA 24; GW2: PPDA 19.63, field tilt 34.2, possession 42.5%, box entries 10, direct speed 2.17, SCA 22; GW3: PPDA 6.53, field tilt 50.6, possession 57.2%, box entries 8, direct speed 2.41, SCA 16; GW4: PPDA 9.94, field tilt 53.2, possession 49.4%, box entries 7, direct speed 1.63, SCA 14; GW5: PPDA 11.67, field tilt 45.9, possession 55.5%, box entries 6, direct speed 2.01, SCA 20; GW6: PPDA 6.65, field tilt 63.3, possession 66.7%, box entries 22, direct speed 2.3, SCA 38; GW7: PPDA 7.44, field tilt 58.9, possession 50.2%, box entries 12, direct speed 2.49, SCA 30; GW8: PPDA 9.16, field tilt 47.8, possession 46.9%, box entries 9, direct speed 3.34, SCA 17; GW9: PPDA 13.81, field tilt 49.4, possession 51.6%, box entries 12, direct speed 2.15, SCA 34; GW10: PPDA 11.53, field tilt 34.5, possession 42.3%, box entries 12, direct speed 2.04, SCA 16

**Zone 14 (C13, SofaScore heat-map points, 10 league matches):** for 24.2/match (rank 16 of 20) · conceded 28.4/match (rank 10 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 6.4/match · allowed 6.1/match · PPDA 9.6. Per match for/allowed: GW3 8/3; GW4 5/9; GW5 4/7; GW6 7/1; GW7 11/8; GW8 5/10 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: Lukáš Horníček (16, 3/3)
- DEF: Lewis Hall (16, 3/3), Amar Dedić (13, 3/3), Malick Thiaw (10, 1/3), Dan Burn (9, 3/3)
- MID: Harvey Barnes (16, 3/3), Nico González (14, 3/3), Joe Willock (11, 2/3), Yoane Wissa (10, 1/3), Lewis Miley (7, 0/3)
- FWD: William Osula (10, 3/3)
- Contested slots: M Lewis Miley 7 v Anthony Elanga 6 · Excluded (FPL flag): Jacob Murphy — Has joined FC Kaiserslautern on loan for the rest of the season; Joelinton — Unspecified injury - Unknown return date
- Absent last match (E12, SofaScore list): Ramsey (ban (cards)), Jaouen (Hamstring Injury), Joelinton (Knock Injury)
- Substitutions this season (C3): GW8 77' Joe Willock→Jacob Ramsey GAME-STATE; GW8 77' William Osula→Yoane Wissa GAME-STATE; GW9 87' Amar Dedić→Bazoumana Touré LATE; GW9 76' Anthony Elanga→Jacob Murphy CHASING; GW9 75' Joelinton→Jacob Ramsey CHASING; GW9 64' Nico González→Sean Steur CHASING; GW9 64' Joe Willock→Yoane Wissa CHASING; GW10 85' William Osula→Anthony Elanga LATE; GW10 85' Malick Thiaw→Fabian Schär INJURY [CONFIRMED: SofaScore flag + LiveScore 'knock']; GW10 74' Sean Steur→Matías Fernández-Pardo TACTICAL; GW10 61' Nico González→Lewis Miley TACTICAL; GW10 61' Yoane Wissa→Joe Willock TACTICAL

### First-choice players and absences (F14) — generated 2026-11-10 07:41 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Lukáš Horníček | start weight 16 | OK | a | — | — |
| CB | Malick Thiaw | start weight 10 | OK | a | Sven Botman | — |
| CB | Dan Burn | start weight 9 | OK | a 100% | Sven Botman | — |
| xGI #1 | Yoane Wissa | xGI 3.59 | OK | a | Joe Willock | — |
| xGI #2 | Harvey Barnes | xGI 3.19 | OK | a | Joe Willock | — |
| Penalties #1 (FPL) | Wissa | FPL order | OK | a | Osula | — |
| Direct FK #1 (FPL) | Hall | FPL order | OK | a | Schär | — |
| Corners (observed) | Lewis Hall | 23 corners taken | OK | a | Jacob Murphy | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Liverpool FC: Dan Burn (Lack of Fitness) · GW2 A Tottenham Hotspur: Dan Burn (Ankle Injury) · GW3 H Bournemouth: Dan Burn (Ankle Injury) · GW4 A Leeds United: Dan Burn (Ankle Injury) · GW5 H Hull City: Dan Burn (Ankle Injury) · GW6 A Coventry City: Dan Burn (did not start) · GW7 H Aston Villa: Dan Burn (did not start) · GW8 A Crystal Palace: Malick Thiaw (did not start), Yoane Wissa (did not start) · GW9 H Everton: Malick Thiaw (did not start), Yoane Wissa (did not start) · GW10 A Fulham: all started

### Next fixtures (all competitions)
- Sat 21 Nov 17:30 UTC · Premier League R11 · H v Arsenal
- Sun 29 Nov 14:05 UTC · Premier League R12 · A v Brighton & Hove Albion
- Wed 02 Dec 20:15 UTC · Premier League R13 · H v Manchester United
- Sun 06 Dec 14:00 UTC · Premier League R14 · H v Sunderland
- Sat 12 Dec 15:00 UTC · Premier League R15 · A v Ipswich Town
- Sat 19 Dec 12:30 UTC · Premier League R16 · A v Brentford

### FPL availability flags (players with league minutes this season)
Joelinton — Unspecified injury - Unknown return date (0%); Woltemade — Has joined Juventus on loan for the rest of the season (0%)
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
- GW9 H Everton 0–1 · xG 1.29–2.34 · poss 52% · 4-2-3-1 · scorers: none
- GW10 A Fulham 1–1 · xG 1.14–0.70 · poss 42% · 4-2-3-1 · scorers: Jacob Murphy 80'
### Corner takers observed (LiveScore Block L)
- Lewis Hall: 23 corners (2 left, 21 right, 6 short)
- Jacob Murphy: 8 corners (7 left, 1 right, 1 short)
- Harvey Barnes: 7 corners (7 left, 0 right)
- Anthony Elanga: 3 corners (3 left, 0 right)
- Matias Fernandez-Pardo: 2 corners (2 left, 0 right, 1 short)
