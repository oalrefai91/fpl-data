# Tottenham Hotspur — data doc
*Feeder-written (2026-11-03 07:42 UTC); do not edit. Narrative: `profiles/teams/tottenham.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-03 07:42 UTC)
**Manager:** Roberto De Zerbi · **Venue:** Tottenham Hotspur Stadium · **SofaScore:** https://www.sofascore.com/football/team/tottenham-hotspur/33 · **FPL code:** TOT
**Table:** 9th, 12 pts (3W 3D 3L, GF 10 GA 10) · Home 8th (2-1-2, 7:6) · Away 9th (1-2-1, 3:4)
**Standing context (F15):** 29 league games left · points v 4th -4, v 5th -3, v 17th (last safe) +5, v 18th +5 · goal difference +0
**Suspension watch (D7, all players of the club):** Gallagher — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 9 league matches):** goals after 75′ — for 6/10 (60%), against 1/10 (10%) · scored first 3, conceded first 4 (44% of matches), goalless 2 · points from losing positions 1 of 12 (4 matches behind at some point) · points from winning positions 9 of 9 (3 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Tonali (MID) 10.1/90, hit 3/9; Van Hecke (DEF) 8.3/90, hit 3/9; Bentancur (MID) 14.6/90, hit 2/6; Gallagher (MID) 12.1/90, hit 1/7; Fernandes (MID) 9.8/90, hit 1/9; Gray (MID) 8.5/90, hit 1/8
**Manager tenure (F13, SofaScore):** Roberto De Zerbi since 31 Mar 2026 · 18 matches in charge, all competitions (7W 5D 6L) · 9 league matches this season · contract to 30 Jun 2031 · previous club Olympique de Marseille · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Arsenal — last 4: Feb 2026 Premier League Tottenham Hotspur 1–4 Arsenal (yellows 2–1, xG 0.76–2.07); Nov 2025 Premier League Arsenal 4–1 Tottenham Hotspur (yellows 1–3, xG 1.93–0.07); Jan 2025 Premier League Arsenal 2–1 Tottenham Hotspur (yellows 3–1, xG 1.45–0.78); Sep 2024 Premier League Tottenham Hotspur 0–1 Arsenal (yellows 5–3, xG 0.71–0.74) · 19 yellows in 4 | v Chelsea — last 4: Oct 2026 Premier League Chelsea 0–2 Tottenham Hotspur (yellows 4–3, reds 1–0, xG 0.47–0.74); May 2026 Premier League Chelsea 2–1 Tottenham Hotspur (yellows 4–3, xG 0.63–1.27); Nov 2025 Premier League Tottenham Hotspur 0–1 Chelsea (yellows 4–2, xG 0.12–3.68); Apr 2025 Premier League Chelsea 1–0 Tottenham Hotspur (yellows 5–5, xG 1.10–0.87) · 30 yellows in 4
**Archetype (F5):** used **HP** — derived HP [DERIVED] · signals, last 6 league matches: possession 64.8%, PPDA 7.1 (Understat, 5 matches; lower = harder press), opponent offsides forced 1.5/match (line height), fast breaks 0.3/match (season), both sides' xG 2.23/match (openness) · note: computed from 5 of 6 GWs (no PPDA/possession for GW9). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 18 (permanent 9, loan 2, free 0, loan returns 7) · out 19 · flags: Martin Dúbravka arrived 01 Jul, 0 league starts since — role security low (FPL-owned ≥ 1% or tracked) — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 9 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 11.69 | 14 | Big chances against | 14 | 2 |
| xGOT | 11.02 | 11 | Box shots against | 76 | 7 |
| xA | 9.06 | 7 | Corners against | 35 | 1 |
| Shots | 148 | 4 | Crosses faced | 121 | 1 |
| SoT | 40 | 8 | Dribbled past | 63 | 10 |
| Big chances | 22 | 9 | Errors→shot | 10 | 16 |
| Shots in box | 92 | 6 | GK goals prevented | -2.11 | 15 |
| Corners | 71 | 1 | Clearances | 171 | 19 |
| Crosses | 213 | 1 | Tackles | 160 | 5 |
| Fast breaks | 3 | 20 | Interceptions | 71 | 13 |
| FK shots | 6 | 3 | Def. contributions | 432 | 18 |
| Possession % | 62.89 | 2 | Aerial % | 51.49 | 6 |
| Pass % | 88.62 | 2 | Duel % | 50.40 | 9 |
| Long balls | 216 | 20 | Fouls | 119 | 17 |
| Dribbles | 103 | 2 | Yellows | 13 | 2 |
| Shots against | 109 | 6 | Km covered | 1022 | 13 |
| SoT against | 31 | 4 | Sprints | 964 | 12 |
Per match: xG 1.30 · xGOT 1.22 · shots 16.4 · shots against 12.1 · big chances 2.4 for / 1.6 against · corners 7.9 / 3.9 · crosses 23.7 / 13.4 · possession 62.888888888889%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | H | Everton | 0–0 | 0.69/0.74 | 1.11/1.60 | 62 | 14/12 | 2/3 | 8/9 | 8/6 | 1/2 | 5/6 | 23/5 v 17/4 | 1/2 |
| 5 | H | Aston Villa | 2–3 | 1.56/1.74 | 1.16/1.76 | 64 | 20/15 | 7/6 | 12/9 | 4/3 | 4/2 | 11/1 | 30/6 v 6/0 | 2/5 |
| 6 | A | Manchester United | 1–1 | 1.62/2.03 | 0.80/0.87 | 50 | 12/12 | 3/4 | 8/8 | 6/3 | 4/1 | 4/4 | 18/3 v 9/2 | 2/2 |
| 7 | H | Coventry City | 3–1 | 0.86/0.98 | 0.77/1.14 | 65 | 16/12 | 5/1 | 10/11 | 4/4 | 0/1 | 4/4 | 25/4 v 21/6 | 1/6 |
| 8 | A | Chelsea | 2–0 | 0.74/0.98 | 0.47/0.46 | 69 | 15/7 | 4/4 | 8/6 | 7/2 | 1/1 | 6/4 | 15/3 v 12/1 | 2/1 |
| 9 | H | Crystal Palace | 2–0 | 3.47/— | 0.14/— | 79 | 34/2 | 9/1 | 24/1 | 13/1 | 6/0 | 19/0 | 39/10 v 2/0 | 1/2 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | H | Everton | 0–0 | 4-2-3-1 | 14/8 | 0/2 | 0/0 | 644/381 | 78/37 | Richarlison (coach decision), Kulusevski (Knee Injury), Mudryk (Ankle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Nørgaard (Muscle Injury) | Darren England |
| 5 | H | Aston Villa | 2–3 | 4-2-3-1 | 9/13 | 1/2 | 0/0 | 581/336 | 64/33 | Richarlison (coach decision), Mudryk (Ankle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Onana (Cruciate Ligament Injury), Madjo (Knock Injury), Maatsen (Ankle Injury), Goretzka (Knee Injury), Torres (Hamstring Injury), Bizot (Back Injury; doubtful) | Samuel Barrott |
| 6 | A | Manchester United | 1–1 | 4-2-3-1 | 16/13 | 3/4 | 1/0 | 464/467 | 48/55 | Richarlison (coach decision), Mudryk (Ankle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Šeško (Shin Injury), Ugarte (Cruciate Ligament Injury), Ligt (Back Injury), Dorgu (Hamstring Injury), Heaton (Abdominal Injury), Mazraoui (Back Injury; doubtful) | Stuart Attwell |
| 7 | H | Coventry City | 3–1 | 3-1-4-2 | 15/14 | 1/3 | 0/0 | 566/290 | 58/42 | Bentancur (ban (red)), Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Porro (Hamstring Injury), Sávio (Muscle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury), Udogie (Physical Discomfort; doubtful) | Amenda (Calf Injury), Wright (Muscle Injury), Eccles (Knock Injury), Woolfenden (Knee Injury) | Andy Madley |
| 8 | A | Chelsea | 2–0 | 4-2-3-1 | 14/14 | 3/4 | 0/1 | 654/288 | 58/37 | Bentancur (ban (red)), Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Sávio (Muscle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury), Udogie (Physical Discomfort; doubtful), Adarabioyo (Physical Discomfort; doubtful) | Martínez (Broken Jaw), Chavarría (Knock Injury), James (Knee Injury), Pedro (Muscle Injury; doubtful) | Chris Kavanagh |
| 9 | H | Crystal Palace | 2–0 | 4-2-3-1 | 8/10 | 1/1 | 0/1 | 815/223 | 103/26 | Bentancur (ban (red)), Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Sávio (Muscle Injury), Adarabioyo (Physical Discomfort), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Riad (Knee Injury), Sarr (Groin Injury), Tomiyasu (Calf Injury) | Michael Oliver |
Per match: fouls 13.2 / 13.3 · yellows 1.44 / 2.33 · reds 1 / 2 (season) · offsides forced 1.7, committed 2.6 · crosses attempted 23.7 / faced 13.4. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 1.54 for / 0.78 against per match · Away (4): xG 1.00 / 1.52. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW9 H v Crystal Palace 2–0 (Sat 31 Oct 17:30 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Antonín Kinský | G | 90 | 6.9 | 0.00 | 0.00 | 0 | 0 | 0 | 0 | 18 |
| Archie Gray | D | 45 | 7.5 | 0.13 | 0.07 | 1 | 1 | 1 | 2 | 60 |
| Jan Paul van Hecke | D | 90 | 9.8 | 0.94 | 0.18 | 3 | 5 | 2 | 0 | 160 |
| Micky van de Ven | D | 90 | 8.2 | 0.00 | 0.10 | 3 | 0 | 3 | 0 | 132 |
| Andy Robertson | D | 77 | 8.6 | 0.10 | 0.77 | 3 | 2 | 3 | 7 | 109 |
| Sandro Tonali | M | 90 | 7.1 | 0.03 | 0.10 | 0 | 1 | 6 | 4 | 92 |
| Mateus Fernandes | M | 90 | 7.9 | 0.08 | 0.49 | 4 | 3 | 4 | 7 | 105 |
| Mohammed Kudus | M | 90 | 6.8 | 0.76 | 0.27 | 3 | 3 | 2 | 12 | 98 |
| Omar Marmoush | M | 77 | 6.7 | 0.14 | 0.15 | 3 | 4 | 0 | 0 | 42 |
| Mathys Tel | M | 88 | 7.4 | 0.27 | 0.15 | 4 | 4 | 3 | 3 | 87 |
| Dominic Solanke | F | 66 | 7.1 | 0.36 | 0.03 | 1 | 4 | 5 | 0 | 24 |
Subs used: Pedro Porro (45'), Conor Gallagher (24'), Destiny Udogie (13'), Dejan Kulusevski (13'), Luca Williams-Barnett (2')
Goals: 25' Archie Gray (assist Mohammed Kudus) [own]; 73' Jan Paul van Hecke [own]
Substitutions (own): 46' Pedro Porro for Archie Gray; 66' Conor Gallagher for Dominic Solanke; 77' Dejan Kulusevski for Omar Marmoush; 77' Destiny Udogie for Andy Robertson; 88' Luca Williams-Barnett for Mathys Tel
Cards: 13' Jean-Philippe Mateta (red, opp); 15' Archie Gray (yellow, own); 53' Óscar Mingueza (yellow, opp)
**Baseline XI change vs GW8 (4-2-3-1 → 4-2-3-1):** in — Dominic Solanke; out — James Maddison.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 5 | H Aston Villa | 45' | AGAINST | Johan Manzambi | Boubacar Kamara | open play | 0.70 |
| 5 | H Aston Villa | 67' | AGAINST | Nicolas Jackson | Johan Manzambi | open play | 0.12 |
| 5 | H Aston Villa | 79' | AGAINST | Emiliano Buendía | John McGinn | open play | 0.02 |
| 5 | H Aston Villa | 86' | FOR | Conor Gallagher | Mohammed Kudus | open play | 0.38 |
| 5 | H Aston Villa | 90' | FOR | Jan Paul van Hecke | Andy Robertson | set piece | 0.36 |
| 6 | A Manchester United | 73' | AGAINST | Bryan Mbeumo | Matheus Cunha | open play | 0.09 |
| 6 | A Manchester United | 90' | FOR | Dominic Solanke | Sandro Tonali | open play | 0.36 |
| 7 | H Coventry City | 14' | FOR | James Maddison | Mohammed Kudus | open play | 0.03 |
| 7 | H Coventry City | 49' | AGAINST | Jack Rudoni | Brandon Thomas-Asante | open play | 0.56 |
| 7 | H Coventry City | 58' | FOR | Omar Marmoush | Andy Robertson | open play | 0.03 |
| 7 | H Coventry City | 90' | FOR | Ben Davies | Dominic Solanke | open play | 0.07 |
| 8 | A Chelsea | 77' | FOR | Mike Penders | — | own goal | — |
| 8 | A Chelsea | 87' | FOR | Mathys Tel | — | open play | 0.03 |
| 9 | H Crystal Palace | 25' | FOR | Archie Gray | Mohammed Kudus | [no Understat] | — |
| 9 | H Crystal Palace | 73' | FOR | Jan Paul van Hecke | — | [no Understat] | — |
Scored 10: open play 6, [no Understat] 2, set piece 1, own goal 1 · Conceded 10: open play 8, corner 2. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW7 FOR v Coventry City 14' James Maddison (assist Mohammed Kudus): G O O O A A A L - James Maddison from Tottenham beats the keeper from outside the box with the right foot! · before: 14' Tottenham with a potentially dangerous attack. ‹ 14' Carl Rushworth from Coventry intercepts a cross aimed towards the box. ‹ 12' Safe hands from Carl Rushworth as he comes out and claims the ball
- GW7 AG v Coventry City 49' Jack Rudoni (assist Brandon Thomas-Asante): G O O O A A A L - Jack Rudoni scores with the right foot! · before: 49' Jack Rudoni goes for goal, but his effort was never close to hitting the target. ‹ 49' The cross by Jack Rudoni from Coventry successfully finds a teammate in the box. ‹ 49' Coventry start a counter attack.
- GW7 FOR v Coventry City 58' Omar Marmoush (assist Andrew Robertson, key pass James Maddison): G O O O A A A L - Omar Marmoush from Tottenham beats the keeper from outside the box with the right foot! · before: 57' Goal kick for Coventry. ‹ 56' Jay Dasilva makes the tackle and wins possession for his team ‹ 56' Goal kick for Coventry.
- GW7 FOR v Coventry City 90+6' Ben Davies (assist Dominic Solanke): G O O O A A A L - Ben Davies from Tottenham beats the keeper from outside the box with the left foot! · before: 90+6' Ethan Pinnock from Coventry intercepts a cross aimed towards the box. ‹ 90+5' Jay Dasilva from Coventry goes a bit too far there as he pulls down Archie Gray ‹ 90+5' Ethan Pinnock wins an air challenge against Dejan Kulusevski
- GW8 AG v Chelsea 77' Mike Penders [OG]: OWN GOAL - Mike Penders sends the ball into his own net! · before: 77' Mateus Fernandes from Tottenham swings in the corner from the left. ‹ 76' Jordan Henderson successfully blocks the shot ‹ 76' A shot by Mateus Fernandes is blocked.
- GW8 FOR v Chelsea 87' Mathys Tel: G O O O A A A L - Mathys Tel from Tottenham scores from outside the box with the right foot! · before: 87' Mathys Tel makes the tackle and wins possession for his team ‹ 86' Antonin Kinsky relieves the pressure with a clearance ‹ 86' Jan Paul van Hecke wins an air challenge against Morgan Rogers
- GW9 FOR v Crystal Palace 25' Archie Gray (assist Mohammed Kudus): — no commentary line — · before: 24' Corner, Tottenham Hotspur. Conceded by Daichi Kamada. ‹ 23' Attempt missed. Mohammed Kudus (Tottenham Hotspur) right footed shot from the right side of ‹ 22' Attempt blocked. Mathys Tel (Tottenham Hotspur) right footed shot from outside the box is b
- GW9 FOR v Crystal Palace 73' Jan Paul van Hecke: — no commentary line — · before: 71' Attempt saved. Andy Robertson (Tottenham Hotspur) left footed shot from the left side of th ‹ 71' Corner, Tottenham Hotspur. Conceded by Dean Henderson. ‹ 70' Attempt blocked. Mathys Tel (Tottenham Hotspur) right footed shot from the left side of the

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW5 H v Aston Villa 45' Johan Manzambi: no structured culprit — reports only
- GW5 H v Aston Villa 67' Nicolas Jackson: no structured culprit — reports only
- GW5 H v Aston Villa 79' Emiliano Buendía: no structured culprit — reports only
  · GW5 error leading to a goal (SofaScore, match level — 3 conceded, the goal is not identified): Andy Robertson [CONFIRMED — SofaScore error flag]
  · GW5 other flags: Jan Paul van Hecke lastManTackle 1; Mateus Fernandes errorLeadToAShot 1
- GW6 A v Manchester United 73' Bryan Mbeumo: no structured culprit — reports only
- GW7 H v Coventry City 49' Jack Rudoni: no structured culprit — reports only
  · GW7 other flags: Micky van de Ven lastManTackle 1

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 82 | 7.04 | 6 | 80 | 8.22 | 8 |
| corner | 23 | 1.70 | 0 | 20 | 2.42 | 2 |
| set piece | 4 | 0.74 | 1 | 5 | 0.27 | 0 |
| direct FK | 6 | 0.36 | 0 | 2 | 0.10 | 0 |
| penalty | 0 | 0.00 | 0 | 1 | 0.76 | 0 |
Totals per match: xG 1.23 (npxG 1.23) for, xGA 1.47 (np 1.38) against · dead-ball share of xG 28% for, 30% against · penalties won 0, conceded 1 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 23 shots, xG 1.70, 0 goals, headed 7: 6-yard box, central 3 shots, xG 0.97, 0 goals; penalty area, left 4 shots, xG 0.19, 0 goals; penalty area, central 3 shots, xG 0.18, 0 goals · against — 20 shots conceded, xG 2.42, 2 goals, headed 7: 6-yard box, central 6 shots, xG 1.93, 2 goals; penalty area, central 4 shots, xG 0.26, 0 goals; penalty area, right 3 shots, xG 0.07, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 35 · corner shots conceded 20 (headed 7), xG 2.42, goals 2 · xG per corner faced 0.069 (rank 3 of 20, 1 = weakest) · weak zone: six-yard box (1.93 xG, 80% of theirs v 65% league) · signal: **WEAK — positive pairing for opposing aerial targets** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–9 [CONFIRMED — LiveScore Block L, 52 corners; side L/R as LiveScore records it; foot from SofaScore]: Mateus Fernandes 10 (10L/0R, 3 short, right foot); Savio 10 (1L/9R, 3 short, left foot); Mathys Tel 7 (7L/0R, 3 short, right foot); Mohammed Kudus 5 (0L/5R, 2 short, left foot). First contact on corners that ended in a shot (Understat) — for: Sandro Tonali 4, Jan Paul van Hecke 3 (2 headed), Micky van de Ven 3 (2 headed), Mohammed Kudus 3, Dominic Solanke 2 (2 headed) · against (who beat them): Yoane Wissa 2 (1 headed) — 1 goal, Murillo 2, Nathan Collins 1 (1 headed), Dango Ouattara 1 (1 headed), Kristoffer Ajer 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 45.6 (rank 1 of 20, 1 = highest line) · block length 18.8 (rank 3, 1 = most compact) · width 63.4. Per match: GW4 H v Everton 4-2-3-1: back line 48, front 62, length 14, width 62 (62% poss); GW5 H v Aston Villa 4-2-3-1: back line 49, front 65, length 16, width 51 (64% poss); GW6 A v Manchester United 4-2-3-1: back line 42, front 68, length 26, width 63 (50% poss); GW7 H v Coventry City 3-1-4-2: back line 48, front 58, length 10, width 66 (65% poss); GW8 A v Chelsea 4-2-3-1: back line 36, front 64, length 28, width 67 (69% poss); GW9 H v Crystal Palace 4-2-3-1: back line 57, front 66, length 9, width 62 (79% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 2 league match(es) v LB-coded sides — xG 2.17/match and 3.0 pts/match v 1.05 and 0.9 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW7 H v Coventry City 3–1, xG 0.86, box shots 10, poss 65%; GW9 H v Crystal Palace 2–0, xG 3.47, box shots 24, poss 79%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Sávio 3, Robertson 2, Fernandes 2** · FPL editorial order: Pedro Porro #1, Sávio #2, Tel #3
- Direct free-kick shooters: **Tel 2, Marmoush 1, Maddison 1** · FPL order: Pedro Porro #1, Xavi #2, Tel #3
- Penalties taken: **—** · FPL order: Solanke #1, Marmoush #2, Kudus #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Robertson 2, Porro 1**
- Corner targets (headed shots from corners): **Hecke 2, Ven 2, Solanke 2, Tel 1** · corner shots 23
- **DISAGREEMENT:** observed corner taker Sávio (3) v FPL #1 Pedro Porro — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Sandro Tonali 6 (0.68/90, percentile 96, 789 min); Pedro Porro 2 (0.67/90, percentile 94, 269 min); Conor Gallagher 2 (0.62/90, percentile 92, 292 min); Andy Robertson 2 (0.31/90, percentile 80, 578 min); Sávio 1 (0.27/90, percentile 75, 331 min) · club total 16 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 306 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 7.42, field tilt 55.1, possession 58.8%, box entries 13, direct speed 1.95, SCA 18; GW2: PPDA 9.4, field tilt 65.8, possession 57.5%, box entries 15, direct speed 2.14, SCA 33; GW3: PPDA 9.26, field tilt 58.4, possession 58.5%, box entries 10, direct speed 1.91, SCA 19; GW4: PPDA 8, field tilt 69.5, possession 62%, box entries 13, direct speed 1.5, SCA 28; GW5: PPDA 5.79, field tilt 75.2, possession 63.6%, box entries 17, direct speed 1.84, SCA 39; GW6: PPDA 7.75, field tilt 53.9, possession 50.4%, box entries 14, direct speed 2.16, SCA 21; GW7: PPDA 6.44, field tilt 68.1, possession 65.4%, box entries 15, direct speed 2.11, SCA 31; GW8: PPDA 6.91, field tilt 60.4, possession 68%, box entries 13, direct speed 2.32, SCA 29

**Zone 14 (C13, SofaScore heat-map points, 9 league matches):** for 48.4/match (rank 1 of 20) · conceded 23.2/match (rank 16 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 7.0/match · allowed 8.1/match · PPDA 7.8. Per match for/allowed: GW3 3/6; GW4 7/8; GW5 12/4; GW6 9/8; GW7 5/11; GW8 6/7 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 9 league matches, weights last-3 ×3 / older ×1
- GK: Antonín Kinský (15, 3/3)
- DEF: Jan Paul van Hecke (15, 3/3), Archie Gray (13, 3/3), Micky van de Ven (13, 3/3), Andy Robertson (13, 3/3)
- MID: Sandro Tonali (15, 3/3), Mohammed Kudus (10, 3/3), Mateus Fernandes (9, 2/3), Mathys Tel (9, 2/3), James Maddison (6, 2/3)
- FWD: Omar Marmoush (13, 3/3)
- Contested slots: none · Excluded (FPL flag): none
- Absent last match (E12, SofaScore list): Bentancur (ban (red)), Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Sávio (Muscle Injury), Adarabioyo (Physical Discomfort), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury)
- Substitutions this season (C3): GW7 69' James Maddison→Conor Gallagher TACTICAL; GW7 69' Andy Robertson→Ben Davies INJURY [CONFIRMED: SofaScore flag + LiveScore 'knock']; GW8 89' Mohammed Kudus→Dejan Kulusevski LATE; GW8 89' Mathys Tel→Ben Davies LATE; GW8 65' Andy Robertson→Pedro Porro TACTICAL; GW8 65' Omar Marmoush→Dominic Solanke TACTICAL; GW8 51' James Maddison→Conor Gallagher INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW9 88' Mathys Tel→Luca Williams-Barnett LATE; GW9 77' Omar Marmoush→Dejan Kulusevski GAME-STATE; GW9 77' Andy Robertson→Destiny Udogie GAME-STATE; GW9 66' Dominic Solanke→Conor Gallagher TACTICAL; GW9 46' Archie Gray→Pedro Porro HALF-TIME

### First-choice players and absences (F14) — generated 2026-11-03 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Antonín Kinský | start weight 15 | OK | a | — | — |
| CB | Jan Paul van Hecke | start weight 15 | OK | a 100% | Marcos Senesi | — |
| CB | Micky van de Ven | start weight 13 | OK | a 100% | Marcos Senesi | — |
| xGI #1 | Jan Paul van Hecke | xGI 2.35 | OK | a 100% | Dominic Solanke | — |
| xGI #2 | Mohammed Kudus | xGI 2.05 | OK | a 100% | Dominic Solanke | — |
| Penalties #1 (FPL) | Solanke | FPL order | OK | a | Marmoush | — |
| Direct FK #1 (FPL) | Pedro Porro | FPL order | OK | a 100% | Tel | — |
| Corners (observed) | Mateus Fernandes | 10 corners taken | OK | a | Savio | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 A Brentford: Micky van de Ven (Physical Discomfort), Mohammed Kudus (did not start) · GW2 H Newcastle United: Mohammed Kudus (did not start) · GW3 A Nottingham Forest: Mohammed Kudus (did not start) · GW4 H Everton: Mohammed Kudus (did not start) · GW5 H Aston Villa: Mohammed Kudus (did not start) · GW6 A Manchester United: Micky van de Ven (did not start) · GW7 H Coventry City: all started · GW8 A Chelsea: all started · GW9 H Crystal Palace: all started

### Next fixtures (all competitions)
- Sat 07 Nov 12:30 UTC · Premier League R10 · A v Leeds United
- Sat 21 Nov 15:00 UTC · Premier League R11 · H v Ipswich Town
- Sun 29 Nov 14:05 UTC · Premier League R12 · A v Sunderland
- Thu 03 Dec 20:00 UTC · Premier League R13 · H v Fulham
- Sun 06 Dec 16:30 UTC · Premier League R14 · H v Arsenal
- Mon 14 Dec 20:00 UTC · Premier League R15 · A v Hull City

### FPL availability flags (players with league minutes this season)
Tosin — Calf injury - Unknown return date (0%); Sávio — Muscular injury - Expected back 21 Nov (0%); Bergvall — Knee injury - Expected back 31 Oct (0%); Moore — Has joined FC Köln on loan for the rest of the season (0%); Richarlison — not included in squad. (0%); Mudryk — Ankle injury - Unknown return date (0%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 A Brentford 0–3 · xG 0.57–3.87 · poss 60% · 4-2-3-1 · scorers: none
- GW2 H Newcastle United 0–2 · xG 1.12–0.72 · poss 58% · 4-2-3-1 · scorers: none
- GW3 A Nottingham Forest 0–0 · xG 1.06–0.92 · poss 59% · 4-2-3-1 · scorers: none
- GW4 H Everton 0–0 · xG 0.69–1.11 · poss 62% · 4-2-3-1 · scorers: none
- GW5 H Aston Villa 2–3 · xG 1.56–1.16 · poss 64% · 4-2-3-1 · scorers: Conor Gallagher 86', Jan Paul van Hecke 90'
- GW6 A Manchester United 1–1 · xG 1.62–0.80 · poss 50% · 4-2-3-1 · scorers: Dominic Solanke 90'
- GW7 H Coventry City 3–1 · xG 0.86–0.77 · poss 65% · 3-1-4-2 · scorers: James Maddison 14', Omar Marmoush 58', Ben Davies 90'
- GW8 A Chelsea 2–0 · xG 0.74–0.47 · poss 69% · 4-2-3-1 · scorers: Mike Penders 77', Mathys Tel 87'
- GW9 H Crystal Palace 2–0 · xG 3.47–0.14 · poss 79% · 4-2-3-1 · scorers: Archie Gray 25', Jan Paul van Hecke 73'
### Corner takers observed (LiveScore Block L)
- Mateus Fernandes: 10 corners (10 left, 0 right, 3 short)
- Savio: 10 corners (1 left, 9 right, 3 short)
- Mathys Tel: 7 corners (7 left, 0 right, 3 short)
- Mohammed Kudus: 5 corners (0 left, 5 right, 2 short)
- Sandro Tonali: 5 corners (3 left, 2 right, 1 short)
- Omar Marmoush: 5 corners (5 left, 0 right, 1 short)
- Andrew Robertson: 4 corners (0 left, 4 right, 1 short)
- Pedro Porro: 3 corners (0 left, 3 right, 1 short)
- James Maddison: 3 corners (3 left, 0 right, 2 short)
