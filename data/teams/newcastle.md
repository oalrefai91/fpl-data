# Newcastle United — data doc
*Feeder-written (2026-11-24 07:45 UTC); do not edit. Narrative: `profiles/teams/newcastle.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-24 07:45 UTC)
**Manager:** Matthias Jaissle · **Venue:** St James' Park · **SofaScore:** https://www.sofascore.com/football/team/newcastle-united/39 · **FPL code:** NEW
**Table:** 13th, 13 pts (3W 4D 4L, GF 15 GA 18) · Home 15th (1-3-2, 8:9) · Away 8th (2-1-2, 7:9)
**Standing context (F15):** 27 league games left · points v 4th -8, v 5th -5, v 17th (last safe) +4, v 18th +4 · goal difference -3
**Suspension watch (D7, all players of the club):** N.Gonzalez — 🟨 2 from a ban (3/5); Schär — 🟨 2 from a ban (3/5); J.Murphy — 🟨 2 from a ban (3/5); Wissa — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 11 league matches):** goals after 75′ — for 3/15 (20%), against 5/18 (28%) · scored first 5, conceded first 6 (55% of matches), goalless 0 · points from losing positions 2 of 18 (6 matches behind at some point) · points from winning positions 12 of 18 (6 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Botman (DEF) 11.4/90, hit 5/8; Hall (DEF) 8.4/90, hit 5/11; Thiaw (DEF) 8.6/90, hit 3/10; Schär (DEF) 14.6/90, hit 2/5; L.Miley (MID) 11.4/90, hit 2/9; Burn (DEF) 9.7/90, hit 2/6
**Manager tenure (F13, SofaScore):** Matthias Jaissle since 05 Aug 2026 · 12 matches in charge, all competitions (5W 2D 5L) · 11 league matches this season · contract to 30 Jun 2030 · previous club Al-Ahli · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Sunderland — last 4: Mar 2026 Premier League Newcastle United 1–2 Sunderland (yellows 1–6, xG 1.29–2.36); Dec 2025 Premier League Sunderland 1–0 Newcastle United (yellows 5–4, xG 0.30–0.24); Jan 2024 FA Cup Sunderland 0–3 Newcastle United (yellows 4–2, no xG); Mar 2016 Premier League Newcastle United 1–1 Sunderland (yellows 4–1, no xG) · 27 yellows in 4
**Archetype (F5):** used **HP** — derived HP [DERIVED] · signals, last 6 league matches: possession 48.7%, PPDA 6.9 (Understat, 3 matches; lower = harder press), opponent offsides forced 2.3/match (line height), fast breaks 1.2/match (season), both sides' xG 2.85/match (openness) · note: possession 48.7 v 47.5; computed from 3 of 6 GWs (no PPDA/possession for GW9, GW10, GW11). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 10 (permanent 9, loan 0, free 0, loan returns 1) · out 13 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 11 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 13.24 | 18 | Big chances against | 26 | 9 |
| xGOT | 11.68 | 15 | Box shots against | 110 | 15 |
| xA | 7.66 | 15 | Corners against | 55 | 14 |
| Shots | 134 | 15 | Crosses faced | 203 | 13 |
| SoT | 37 | 17 | Dribbled past | 85 | 13 |
| Big chances | 22 | 16 | Errors→shot | 14 | 18 |
| Shots in box | 78 | 17 | GK goals prevented | 1.79 | 6 |
| Corners | 49 | 10 | Clearances | 347 | 1 |
| Crosses | 176 | 15 | Tackles | 145 | 18 |
| Fast breaks | 13 | 8 | Interceptions | 77 | 18 |
| FK shots | 2 | 17 | Def. contributions | 625 | 8 |
| Possession % | 48.82 | 9 | Aerial % | 54.90 | 2 |
| Pass % | 81.06 | 12 | Duel % | 48.61 | 15 |
| Long balls | 377 | 7 | Fouls | 141 | 15 |
| Dribbles | 71 | 14 | Yellows | 30 | 19 |
| Shots against | 178 | 18 | Km covered | 1280 | 7 |
| SoT against | 55 | 15 | Sprints | 1329 | 2 |
Per match: xG 1.20 · xGOT 1.06 · shots 12.2 · shots against 16.2 · big chances 2.0 for / 2.4 against · corners 4.5 / 5.0 · crosses 16.0 / 18.5 · possession 48.8%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | A | Coventry City | 1–4 | 1.84/2.22 | 1.47/1.66 | 67 | 19/9 | 6/6 | 11/6 | 6/3 | 3/2 | 6/2 | 17/3 v 9/2 | 2/5 |
| 7 | H | Aston Villa | 0–1 | 0.99/0.92 | 1.57/2.09 | 50 | 16/15 | 1/3 | 11/11 | 9/8 | 0/3 | 4/5 | 29/5 v 10/2 | 0/5 |
| 8 | A | Crystal Palace | 2–0 | 0.95/1.30 | 1.59/2.20 | 47 | 10/17 | 2/4 | 7/9 | 4/5 | 2/2 | 4/7 | 14/3 v 20/3 | 4/1 |
| 9 | H | Everton | 0–1 | 1.29/— | 2.34/— | 52 | 17/16 | 2/5 | 7/11 | 6/1 | 2/4 | 4/5 | 24/7 v 22/7 | 2/0 |
| 10 | A | Fulham | 1–1 | 1.14/— | 0.70/— | 42 | 9/11 | 5/5 | 6/7 | 1/1 | 3/0 | 3/3 | 11/3 v 14/3 | 3/1 |
| 11 | H | Arsenal | 2–2 | 1.71/— | 1.49/— | 34 | 12/13 | 3/4 | 5/10 | 4/1 | 3/4 | 6/3 | 14/2 v 15/1 | 3/3 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | A | Coventry City | 1–4 | 4-2-3-1 | 10/3 | 1/1 | 0/0 | 548/264 | 59/67 | Elanga (Knock Injury), Jaouen (Hamstring Injury) | Awoniyi (ban (red)), Amenda (Calf Injury), Wright (Muscle Injury), Eccles (Knock Injury), Woolfenden (Knee Injury) | John Brooks |
| 7 | H | Aston Villa | 0–1 | 4-2-3-1 | 14/11 | 6/2 | 0/0 | 407/431 | 62/48 | Elanga (Knock Injury), Jaouen (Hamstring Injury), Ramsey (Thigh Injury), Livramento (Knock Injury) | Onana (Cruciate Ligament Injury), Maatsen (Ankle Injury), Ruggeri (Hamstring Injury), Hemmings (Knock Injury; doubtful) | Jarred Gillett |
| 8 | A | Crystal Palace | 2–0 | 4-2-3-1 | 10/12 | 3/3 | 0/0 | 352/385 | 67/50 | Jaouen (Hamstring Injury), Livramento (Knock Injury) | Riad (Knee Injury), Tomiyasu (Calf Injury), Larsen (Knock Injury; doubtful), Timber (Knock Injury; doubtful) | Paul Tierney |
| 9 | H | Everton | 0–1 | 4-2-3-1 | 13/9 | 4/2 | 1/0 | 428/396 | 70/61 | Jaouen (Hamstring Injury), Livramento (Knock Injury), Miley (Knock Injury; doubtful), Fernández-Pardo (Illness; doubtful) | — | John Brooks |
| 10 | A | Fulham | 1–1 | 4-2-3-1 | 13/9 | 2/0 | 0/0 | 380/526 | 36/67 | Ramsey (ban (cards)), Jaouen (Hamstring Injury), Joelinton (Knock Injury) | Cairney (Knee Injury) | Robert Jones |
| 11 | H | Arsenal | 2–2 | 4-2-3-1 | 20/7 | 3/3 | 0/0 | 262/529 | 31/61 | Jaouen (Hamstring Injury), Joelinton (Knock Injury) | Dowman (ban (red)), Saka (Muscle Injury), Zubimendi (Hamstring Injury) | Chris Kavanagh |
Per match: fouls 12.8 / 10.5 · yellows 2.82 / 2.18 · reds 1 / 0 (season) · offsides forced 1.9, committed 2.2 · crosses attempted 16.0 / faced 18.5. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (6): xG 1.29 for / 1.89 against per match · Away (5): xG 1.11 / 1.39. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW11 H v Arsenal 2–2 (Sat 21 Nov 17:30 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Lukáš Horníček | G | 90 | 6.4 | 0.00 | 0.00 | 1 | 0 | 1 | 0 | 47 |
| Amar Dedić | D | 45 | 6.1 | 0.00 | 0.00 | 0 | 0 | 3 | 0 | 14 |
| Malick Thiaw | D | 90 | 7.2 | 0.28 | 0.00 | 0 | 1 | 7 | 0 | 45 |
| Dan Burn | D | 90 | 6.4 | 0.09 | 0.00 | 1 | 1 | 12 | 1 | 46 |
| Lewis Hall | D | 89 | 6 | 0.00 | 0.06 | 1 | 0 | 4 | 5 | 47 |
| Sean Steur | M | 45 | 6.4 | 0.00 | 0.00 | 0 | 0 | 1 | 0 | 18 |
| Lewis Miley | M | 90 | 6.5 | 0.03 | 0.03 | 0 | 1 | 4 | 1 | 31 |
| Jacob Murphy | M | 45 | 6.5 | 0.03 | 0.00 | 0 | 2 | 2 | 0 | 10 |
| Joe Willock | M | 83 | 6.3 | 0.87 | 0.02 | 2 | 4 | 2 | 0 | 41 |
| Harvey Barnes | M | 90 | 7.7 | 0.28 | 0.11 | 2 | 2 | 1 | 2 | 36 |
| William Osula | F | 90 | 6.6 | 0.00 | 0.16 | 3 | 0 | 2 | 0 | 27 |
Subs used: Tino Livramento (45'), Jacob Ramsey (45'), Anthony Elanga (45'), Yoane Wissa (17'), Sven Botman (8')
Goals: 33' Eberechi Eze (assist Kai Havertz) [opp]; 49' Harvey Barnes (assist William Osula) [own]; 62' Malick Thiaw (assist Joe Willock) [own]; 78' Noni Madueke (assist Martin Ødegaard) [opp]
Substitutions (own): 46' Anthony Elanga for Jacob Murphy; 46' Tino Livramento for Amar Dedić; 46' Jacob Ramsey for Sean Steur; 83' Yoane Wissa for Joe Willock; 90' Sven Botman for Lewis Hall [injury]
Cards: 23' Amar Dedić (yellow, own); 56' Declan Rice (yellow, opp); 58' Harvey Barnes (yellow, own); 81' Noni Madueke (yellow, opp); 81' Dan Burn (yellow, own); 90' Viktor Gyökeres (yellow, opp)
**Baseline XI change vs GW10 (4-2-3-1 → 4-2-3-1):** in — Joe Willock, Lewis Miley; out — Nico González, Yoane Wissa.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
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
| 11 | H Arsenal | 33' | AGAINST | Eberechi Eze | Kai Havertz | [no Understat] | — |
| 11 | H Arsenal | 49' | FOR | Harvey Barnes | William Osula | [no Understat] | — |
| 11 | H Arsenal | 62' | FOR | Malick Thiaw | Joe Willock | [no Understat] | — |
| 11 | H Arsenal | 78' | AGAINST | Noni Madueke | Martin Ødegaard | [no Understat] | — |
Scored 15: open play 10, [no Understat] 3, corner 1, set piece 1 · Conceded 18: open play 10, [no Understat] 4, penalty 2, own goal 2. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW9 AG v Everton 49' Thierno Barry: GOAL! It's an easy finish as Thierno Barry from Everton taps the ball into an open goal with the right foot! · before: 49' Good effort by Tyrique George as he directs a shot on target, but the keeper saves it ‹ 49' Kiernan Dewsbury-Hall creates a scoring opportunity for his teammate ‹ 49' Everton with a potentially dangerous attack.
- GW10 FOR v Fulham 80' Jacob Murphy: G O O O A A A L - Jacob Murphy from Newcastle scores from outside the box with the left foot! · before: 80' Due to technical problems, we are unable to deliver game updates at the moment. ‹ 79' Goal kick for Newcastle. ‹ 78' Joseph Willock shoots from outside the box, but Bernd Leno has it under control
- GW10 AG v Fulham 83' Rodrigo Muniz: G O O O O O A A L - Rodrigo Muniz finds the net with the right foot! · before: 83' Alex Iwobi creates a scoring opportunity for his teammate ‹ 82' David Affengruber makes the tackle and wins possession for his team ‹ 82' Jacob Murphy wins an air challenge against Antonee Robinson
- GW11 AG v Arsenal 33' Eberechi Eze (assist Kai Havertz): — no commentary line — · before: 32' Jacob Murphy (Newcastle United) wins a free kick in the defensive half. ‹ 32' Foul by Eberechi Eze (Arsenal). ‹ 30' Foul by Joe Willock (Newcastle United).
- GW11 FOR v Arsenal 49' Harvey Barnes (assist William Osula): — no commentary line — · before: 48' Delay over. They are ready to continue. ‹ 47' Delay in match because of an injury David Raya (Arsenal). ‹ 46' Foul by Joe Willock (Newcastle United).
- GW11 FOR v Arsenal 62' Malick Thiaw (assist Joe Willock): — no commentary line — · before: 61' Foul by William Osula (Newcastle United). ‹ 61' David Raya (Arsenal) wins a free kick in the defensive half. ‹ 61' Corner, Newcastle United. Conceded by Gabriel Magalhães.
- GW11 AG v Arsenal 78' Noni Madueke (assist Martin Ødegaard): — no commentary line — · before: 77' Offside, Arsenal. Christos Tzolis is caught offside. ‹ 75' Offside, Newcastle United. Jacob Ramsey is caught offside. ‹ 74' Corner, Newcastle United. Conceded by Kai Havertz.

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
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
- GW11 H v Arsenal 33' Eberechi Eze: no structured culprit — reports only
- GW11 H v Arsenal 78' Noni Madueke: Jacob Ramsey [DERIVED — LiveScore: 'fside, Newcastle United. Jacob Ramsey is caught offside.']
  · GW11 error leading to a goal (SofaScore, match level — 2 conceded, the goal is not identified): Lewis Hall [CONFIRMED — SofaScore error flag]
  · GW11 other flags: Amar Dedić errorLeadToAShot 1; Lewis Hall errorLeadToAShot 1

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

**Corners (E10 data layer):** observed takers GW1–11 [CONFIRMED — LiveScore Block L, 43 corners; side L/R as LiveScore records it; foot from SofaScore]: Lewis Hall 23 (2L/21R, 6 short, left foot); Jacob Murphy 8 (7L/1R, 1 short, right foot); Harvey Barnes 7 (7L/0R, right foot); Anthony Elanga 3 (3L/0R, right foot). First contact on corners that ended in a shot (Understat) — for: Yoane Wissa 3 (2 headed) — 1 goal, Lewis Hall 2, Nick Woltemade 1 (1 headed), Joelinton 1 (1 headed) · against (who beat them): Alexander Isak 2 (2 headed), Joe Gelhardt 2, Darío Osorio 2, Jan Paul van Hecke 1 (1 headed), Semi Ajayi 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 38.9 (rank 14 of 20, 1 = highest line) · block length 21.2 (rank 11, 1 = most compact) · width 61.9. Per match: GW6 A v Coventry City 4-2-3-1: back line 42, front 67, length 26, width 69 (67% poss); GW7 H v Aston Villa 4-2-3-1: back line 45, front 68, length 23, width 59 (50% poss); GW8 A v Crystal Palace 4-2-3-1: back line 43, front 62, length 18, width 55 (47% poss); GW9 H v Everton 4-2-3-1: back line 44, front 57, length 13, width 57 (52% poss); GW10 A v Fulham 4-2-3-1: back line 38, front 58, length 19, width 64 (42% poss); GW11 H v Arsenal 4-2-3-1: back line 36, front 55, length 19, width 59 (34% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 3 league match(es) v LB-coded sides — xG 1.41/match and 2.0 pts/match v 1.13 and 0.9 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW5 H v Hull City 2–1, xG 1.44, box shots 9, poss 56%; GW6 A v Coventry City 1–4, xG 1.84, box shots 11, poss 67%; GW8 A v Crystal Palace 2–0, xG 0.95, box shots 7, poss 47%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Elanga 2, Hall 1, Woltemade 1** · FPL editorial order: Hall #1, Elanga #2, J.Murphy #3
- Direct free-kick shooters: **Osula 1, Dedic 1** · FPL order: Hall #1, Schär #2, Dedić #3
- Penalties taken: **Wissa 1** · FPL order: Wissa #1, Osula #2
- Set-piece deliverers (assisted 'SetPiece' shots): **Hall 3, Thiaw 2, Schär 2**
- Corner targets (headed shots from corners): **Wissa 2, Woltemade 1, Joelinton 1** · corner shots 7
- **DISAGREEMENT:** observed corner taker Anthony Elanga (2) v FPL #1 Hall — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Jacob Murphy 3 (0.56/90, percentile 94, 480 min); Nico González 3 (0.48/90, percentile 90, 562 min); William Osula 2 (0.41/90, percentile 86, 444 min); Joe Willock 2 (0.27/90, percentile 77, 655 min) · club total 21 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 334 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 9.61, field tilt 29.5, possession 40%, box entries 7, direct speed 3.26, SCA 24; GW2: PPDA 19.63, field tilt 34.2, possession 42.5%, box entries 10, direct speed 2.17, SCA 22; GW3: PPDA 6.53, field tilt 50.6, possession 57.2%, box entries 8, direct speed 2.41, SCA 16; GW4: PPDA 9.94, field tilt 53.2, possession 49.4%, box entries 7, direct speed 1.63, SCA 14; GW5: PPDA 11.67, field tilt 45.9, possession 55.5%, box entries 6, direct speed 2.01, SCA 20; GW6: PPDA 6.65, field tilt 63.3, possession 66.7%, box entries 22, direct speed 2.3, SCA 38; GW7: PPDA 7.44, field tilt 58.9, possession 50.2%, box entries 12, direct speed 2.49, SCA 30; GW8: PPDA 9.16, field tilt 47.8, possession 46.9%, box entries 9, direct speed 3.34, SCA 17; GW9: PPDA 13.81, field tilt 49.4, possession 51.6%, box entries 12, direct speed 2.15, SCA 34; GW10: PPDA 11.53, field tilt 34.5, possession 42.3%, box entries 12, direct speed 2.04, SCA 16

**Zone 14 (C13, SofaScore heat-map points, 11 league matches):** for 23.8/match (rank 16 of 20) · conceded 27.6/match (rank 12 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 6.4/match · allowed 6.1/match · PPDA 9.6. Per match for/allowed: GW3 8/3; GW4 5/9; GW5 4/7; GW6 7/1; GW7 11/8; GW8 5/10 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: Lukáš Horníček (16, 3/3)
- DEF: Amar Dedić (13, 3/3), Malick Thiaw (12, 2/3), Dan Burn (10, 3/3), Sven Botman (6, 0/3)
- MID: Harvey Barnes (16, 3/3), Joe Willock (12, 2/3), Nico González (12, 2/3), Lewis Miley (9, 1/3), Sean Steur (7, 2/3)
- FWD: William Osula (10, 3/3)
- Contested slots: F William Osula 10 v Yoane Wissa 9 · Excluded (FPL flag): Lewis Hall — Unspecified injury - 75% chance of playing; Jacob Murphy — Has joined FC Kaiserslautern on loan for the rest of the season
- Absent last match (E12, SofaScore list): Jaouen (Hamstring Injury), Joelinton (Knock Injury)
- Substitutions this season (C3): GW9 64' Nico González→Sean Steur CHASING; GW9 64' Joe Willock→Yoane Wissa CHASING; GW10 85' William Osula→Anthony Elanga LATE; GW10 85' Malick Thiaw→Fabian Schär INJURY [CONFIRMED: SofaScore flag + LiveScore 'knock']; GW10 74' Sean Steur→Matías Fernández-Pardo TACTICAL; GW10 61' Nico González→Lewis Miley TACTICAL; GW10 61' Yoane Wissa→Joe Willock TACTICAL; GW11 90' Lewis Hall→Sven Botman INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW11 83' Joe Willock→Yoane Wissa TACTICAL; GW11 46' Jacob Murphy→Anthony Elanga HALF-TIME; GW11 46' Amar Dedić→Tino Livramento HALF-TIME; GW11 46' Sean Steur→Jacob Ramsey HALF-TIME

### First-choice players and absences (F14) — generated 2026-11-24 07:45 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Lukáš Horníček | start weight 16 | OK | a | — | — |
| CB | Malick Thiaw | start weight 12 | OK | a | Sven Botman | — |
| CB | Dan Burn | start weight 10 | OK | a 100% | Sven Botman | — |
| xGI #1 | Yoane Wissa | xGI 3.59 | OK | a | Joe Willock | — |
| xGI #2 | Harvey Barnes | xGI 3.59 | OK | a | Joe Willock | — |
| Penalties #1 (FPL) | Wissa | FPL order | OK | a | Osula | — |
| Direct FK #1 (FPL) | Hall | FPL order | DOUBT | d 75% — Unspecified injury - 75% chance of playing | Schär | — |
| Corners (observed) | Lewis Hall | 23 corners taken | DOUBT | d 75% — Unspecified injury - 75% chance of playing | Jacob Murphy | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Liverpool FC: Dan Burn (Lack of Fitness) · GW2 A Tottenham Hotspur: Dan Burn (Ankle Injury) · GW3 H Bournemouth: Dan Burn (Ankle Injury) · GW4 A Leeds United: Dan Burn (Ankle Injury) · GW5 H Hull City: Dan Burn (Ankle Injury) · GW6 A Coventry City: Dan Burn (did not start) · GW7 H Aston Villa: Dan Burn (did not start) · GW8 A Crystal Palace: Malick Thiaw (did not start), Yoane Wissa (did not start) · GW9 H Everton: Malick Thiaw (did not start), Yoane Wissa (did not start) · GW10 A Fulham: all started · GW11 H Arsenal: Yoane Wissa (did not start)

### Next fixtures (all competitions)
- Sun 29 Nov 14:05 UTC · Premier League R12 · A v Brighton & Hove Albion
- Wed 02 Dec 20:15 UTC · Premier League R13 · H v Manchester United
- Sun 06 Dec 14:00 UTC · Premier League R14 · H v Sunderland
- Sat 12 Dec 15:00 UTC · Premier League R15 · A v Ipswich Town
- Sat 19 Dec 12:30 UTC · Premier League R16 · A v Brentford
- Sat 26 Dec 20:00 UTC · Premier League R17 · H v Manchester City

### FPL availability flags (players with league minutes this season)
Hall — Unspecified injury - 75% chance of playing (75%); Joelinton — Unspecified injury - Unknown return date (0%); Woltemade — Has joined Juventus on loan for the rest of the season (0%)
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
- GW11 H Arsenal 2–2 · xG 1.71–1.49 · poss 34% · 4-2-3-1 · scorers: Harvey Barnes 49', Malick Thiaw 62'
### Corner takers observed (LiveScore Block L)
- Lewis Hall: 23 corners (2 left, 21 right, 6 short)
- Jacob Murphy: 8 corners (7 left, 1 right, 1 short)
- Harvey Barnes: 7 corners (7 left, 0 right)
- Anthony Elanga: 3 corners (3 left, 0 right)
- Matias Fernandez-Pardo: 2 corners (2 left, 0 right, 1 short)
