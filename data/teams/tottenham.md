# Tottenham Hotspur — data doc
*Feeder-written (2026-11-10 07:41 UTC); do not edit. Narrative: `profiles/teams/tottenham.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-10 07:41 UTC)
**Manager:** Roberto De Zerbi · **Venue:** Tottenham Hotspur Stadium · **SofaScore:** https://www.sofascore.com/football/team/tottenham-hotspur/33 · **FPL code:** TOT
**Table:** 11th, 12 pts (3W 3D 4L, GF 10 GA 11) · Home 10th (2-1-2, 7:6) · Away 12th (1-2-2, 3:5)
**Standing context (F15):** 28 league games left · points v 4th -6, v 5th -4, v 17th (last safe) +3, v 18th +4 · goal difference -1
**Suspension watch (D7, all players of the club):** Van de Ven — 🟨 2 from a ban (3/5); Gallagher — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 10 league matches):** goals after 75′ — for 6/10 (60%), against 2/11 (18%) · scored first 3, conceded first 5 (50% of matches), goalless 2 · points from losing positions 1 of 15 (5 matches behind at some point) · points from winning positions 9 of 9 (3 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Van Hecke (DEF) 8.5/90, hit 4/10; Tonali (MID) 9.2/90, hit 3/10; Bentancur (MID) 15.7/90, hit 2/7; Fernandes (MID) 11.1/90, hit 2/10; Gallagher (MID) 12.5/90, hit 1/8; Gray (MID) 8.0/90, hit 1/9
**Manager tenure (F13, SofaScore):** Roberto De Zerbi since 31 Mar 2026 · 18 matches in charge, all competitions (7W 5D 6L) · 10 league matches this season · contract to 30 Jun 2031 · previous club Olympique de Marseille · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Arsenal — last 4: Feb 2026 Premier League Tottenham Hotspur 1–4 Arsenal (yellows 2–1, xG 0.76–2.07); Nov 2025 Premier League Arsenal 4–1 Tottenham Hotspur (yellows 1–3, xG 1.93–0.07); Jan 2025 Premier League Arsenal 2–1 Tottenham Hotspur (yellows 3–1, xG 1.45–0.78); Sep 2024 Premier League Tottenham Hotspur 0–1 Arsenal (yellows 5–3, xG 0.71–0.74) · 19 yellows in 4 | v Chelsea — last 4: Oct 2026 Premier League Chelsea 0–2 Tottenham Hotspur (yellows 4–3, reds 1–0, xG 0.47–0.74); May 2026 Premier League Chelsea 2–1 Tottenham Hotspur (yellows 4–3, xG 0.63–1.27); Nov 2025 Premier League Tottenham Hotspur 0–1 Chelsea (yellows 4–2, xG 0.12–3.68); Apr 2025 Premier League Chelsea 1–0 Tottenham Hotspur (yellows 5–5, xG 1.10–0.87) · 30 yellows in 4
**Archetype (F5):** used **HP** — derived HP [DERIVED] · signals, last 6 league matches: possession 64.8%, PPDA 7.2 (Understat, 4 matches; lower = harder press), opponent offsides forced 1.7/match (line height), fast breaks 0.4/match (season), both sides' xG 2.38/match (openness) · note: computed from 4 of 6 GWs (no PPDA/possession for GW9, GW10). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 18 (permanent 9, loan 2, free 0, loan returns 7) · out 19 · flags: Martin Dúbravka arrived 01 Jul, 0 league starts since — role security low (FPL-owned ≥ 1% or tracked) — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 10 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 12.41 | 17 | Big chances against | 18 | 4 |
| xGOT | 12.43 | 12 | Box shots against | 87 | 8 |
| xA | 9.60 | 8 | Corners against | 41 | 5 |
| Shots | 155 | 5 | Crosses faced | 151 | 4 |
| SoT | 44 | 10 | Dribbled past | 70 | 9 |
| Big chances | 23 | 11 | Errors→shot | 12 | 16 |
| Shots in box | 97 | 8 | GK goals prevented | -1.90 | 15 |
| Corners | 75 | 1 | Clearances | 204 | 18 |
| Crosses | 237 | 1 | Tackles | 175 | 6 |
| Fast breaks | 4 | 20 | Interceptions | 75 | 17 |
| FK shots | 6 | 3 | Def. contributions | 489 | 18 |
| Possession % | 62.80 | 2 | Aerial % | 50.76 | 7 |
| Pass % | 88.16 | 2 | Duel % | 49.36 | 11 |
| Long balls | 248 | 20 | Fouls | 135 | 17 |
| Dribbles | 108 | 2 | Yellows | 16 | 5 |
| Shots against | 125 | 8 | Km covered | 1141 | 12 |
| SoT against | 35 | 5 | Sprints | 1086 | 11 |
Per match: xG 1.24 · xGOT 1.24 · shots 15.5 · shots against 12.5 · big chances 2.3 for / 1.8 against · corners 7.5 / 4.1 · crosses 23.7 / 15.1 · possession 62.8%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | H | Aston Villa | 2–3 | 1.56/1.74 | 1.16/1.76 | 64 | 20/15 | 7/6 | 12/9 | 4/3 | 4/2 | 11/1 | 30/6 v 6/0 | 2/5 |
| 6 | A | Manchester United | 1–1 | 1.62/2.03 | 0.80/0.87 | 50 | 12/12 | 3/4 | 8/8 | 6/3 | 4/1 | 4/4 | 18/3 v 9/2 | 2/2 |
| 7 | H | Coventry City | 3–1 | 0.86/0.98 | 0.77/1.14 | 65 | 16/12 | 5/1 | 10/11 | 4/4 | 0/1 | 4/4 | 25/4 v 21/6 | 1/6 |
| 8 | A | Chelsea | 2–0 | 0.74/0.98 | 0.47/0.46 | 69 | 15/7 | 4/4 | 8/6 | 7/2 | 1/1 | 6/4 | 15/3 v 12/1 | 2/1 |
| 9 | H | Crystal Palace | 2–0 | 3.47/— | 0.14/— | 79 | 34/2 | 9/1 | 24/1 | 13/1 | 6/0 | 19/0 | 39/10 v 2/0 | 1/2 |
| 10 | A | Leeds United | 0–1 | 0.72/— | 1.96/— | 62 | 7/16 | 4/4 | 5/11 | 0/4 | 1/4 | 4/6 | 24/6 v 30/5 | 2/1 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | H | Aston Villa | 2–3 | 4-2-3-1 | 9/13 | 1/2 | 0/0 | 581/336 | 64/33 | Richarlison (coach decision), Mudryk (Ankle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Onana (Cruciate Ligament Injury), Madjo (Knock Injury), Maatsen (Ankle Injury), Goretzka (Knee Injury), Torres (Hamstring Injury), Bizot (Back Injury; doubtful) | Samuel Barrott |
| 6 | A | Manchester United | 1–1 | 4-2-3-1 | 16/13 | 3/4 | 1/0 | 464/467 | 48/55 | Richarlison (coach decision), Mudryk (Ankle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Šeško (Shin Injury), Ugarte (Cruciate Ligament Injury), Ligt (Back Injury), Dorgu (Hamstring Injury), Heaton (Abdominal Injury), Mazraoui (Back Injury; doubtful) | Stuart Attwell |
| 7 | H | Coventry City | 3–1 | 3-1-4-2 | 15/14 | 1/3 | 0/0 | 566/290 | 58/42 | Bentancur (ban (red)), Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Porro (Hamstring Injury), Sávio (Muscle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury), Udogie (Physical Discomfort; doubtful) | Amenda (Calf Injury), Wright (Muscle Injury), Eccles (Knock Injury), Woolfenden (Knee Injury) | Andy Madley |
| 8 | A | Chelsea | 2–0 | 4-2-3-1 | 14/14 | 3/4 | 0/1 | 654/288 | 58/37 | Bentancur (ban (red)), Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Sávio (Muscle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury), Udogie (Physical Discomfort; doubtful), Adarabioyo (Physical Discomfort; doubtful) | Martínez (Broken Jaw), Chavarría (Knock Injury), James (Knee Injury), Pedro (Muscle Injury; doubtful) | Chris Kavanagh |
| 9 | H | Crystal Palace | 2–0 | 4-2-3-1 | 8/10 | 1/1 | 0/1 | 815/223 | 103/26 | Bentancur (ban (red)), Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Sávio (Muscle Injury), Adarabioyo (Physical Discomfort), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Riad (Knee Injury), Sarr (Groin Injury), Tomiyasu (Calf Injury) | Michael Oliver |
| 10 | A | Leeds United | 0–1 | 4-3-3 | 16/11 | 3/2 | 0/0 | 531/311 | 61/54 | Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Sávio (Muscle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Joseph (Knee Injury), Stach (Foot Injury; doubtful) | John Brooks |
Per match: fouls 13.5 / 13.1 · yellows 1.60 / 2.30 · reds 1 / 2 (season) · offsides forced 1.7, committed 2.4 · crosses attempted 23.7 / faced 15.1. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 1.54 for / 0.78 against per match · Away (5): xG 0.94 / 1.60. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW10 A v Leeds United 0–1 (Sat 07 Nov 12:30 UTC) — formation 4-3-3
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Antonín Kinský | G | 90 | 6.8 | 0.00 | 0.00 | 0 | 0 | 2 | 0 | 56 |
| Pedro Porro | D | 65 | 6.3 | 0.00 | 0.02 | 1 | 0 | 3 | 4 | 69 |
| Jan Paul van Hecke | D | 90 | 8.2 | 0.07 | 0.03 | 0 | 1 | 10 | 1 | 91 |
| Micky van de Ven | D | 90 | 6.6 | 0.00 | 0.01 | 0 | 0 | 9 | 0 | 87 |
| Andy Robertson | D | 90 | 6.5 | 0.00 | 0.13 | 1 | 0 | 5 | 3 | 92 |
| Sandro Tonali | M | 90 | 6.1 | 0.00 | 0.03 | 0 | 0 | 1 | 1 | 50 |
| Mateus Fernandes | M | 65 | 7 | 0.00 | 0.03 | 0 | 0 | 6 | 1 | 66 |
| Archie Gray | M | 90 | 6.7 | 0.07 | 0.02 | 2 | 1 | 2 | 1 | 40 |
| Mohammed Kudus | F | 83 | 6.2 | 0.04 | 0.04 | 1 | 1 | 1 | 7 | 50 |
| Omar Marmoush | F | 65 | 6.7 | 0.16 | 0.00 | 0 | 2 | 2 | 0 | 20 |
| Mathys Tel | F | 43 | 6.5 | 0.00 | 0.07 | 1 | 0 | 1 | 0 | 17 |
Subs used: Dominic Solanke (47'), Conor Gallagher (25'), Dejan Kulusevski (25'), Rodrigo Bentancur (25'), Luca Williams-Barnett (12')
Goals: 79' Noah Okafor [opp]
Substitutions (own): 43' Dominic Solanke for Mathys Tel [injury]; 65' Rodrigo Bentancur for Mateus Fernandes; 65' Dejan Kulusevski for Omar Marmoush; 65' Conor Gallagher for Pedro Porro; 83' Luca Williams-Barnett for Mohammed Kudus
Cards: manager/staff booking: Roberto De Zerbi 51' [LiveScore] (own; no FPL effect); 15' Micky van de Ven (yellow, own); 22' Sean Longstaff (yellow, opp); 51' Pedro Porro (yellow, own); 80' Noah Okafor (yellow, opp); 88' Sandro Tonali (yellow, own)
**Baseline XI change vs GW9 (4-2-3-1 → 4-3-3):** in — Pedro Porro; out — Dominic Solanke.

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
| 10 | A Leeds United | 79' | AGAINST | Noah Okafor | — | [no Understat] | — |
Scored 10: open play 6, [no Understat] 2, set piece 1, own goal 1 · Conceded 11: open play 8, corner 2, [no Understat] 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW8 AG v Chelsea 77' Mike Penders [OG]: OWN GOAL - Mike Penders sends the ball into his own net! · before: 77' Mateus Fernandes from Tottenham swings in the corner from the left. ‹ 76' Jordan Henderson successfully blocks the shot ‹ 76' A shot by Mateus Fernandes is blocked.
- GW8 FOR v Chelsea 87' Mathys Tel: G O O O A A A L - Mathys Tel from Tottenham scores from outside the box with the right foot! · before: 87' Mathys Tel makes the tackle and wins possession for his team ‹ 86' Antonin Kinsky relieves the pressure with a clearance ‹ 86' Jan Paul van Hecke wins an air challenge against Morgan Rogers
- GW9 FOR v Crystal Palace 25' Archie Gray (assist Mohammed Kudus): — no commentary line — · before: 24' Corner, Tottenham Hotspur. Conceded by Daichi Kamada. ‹ 23' Attempt missed. Mohammed Kudus (Tottenham Hotspur) right footed shot from the right side of ‹ 22' Attempt blocked. Mathys Tel (Tottenham Hotspur) right footed shot from outside the box is b
- GW9 FOR v Crystal Palace 73' Jan Paul van Hecke: — no commentary line — · before: 71' Attempt saved. Andy Robertson (Tottenham Hotspur) left footed shot from the left side of th ‹ 71' Corner, Tottenham Hotspur. Conceded by Dean Henderson. ‹ 70' Attempt blocked. Mathys Tel (Tottenham Hotspur) right footed shot from the left side of the
- GW10 AG v Leeds United 79' Noah Okafor: G O O O O O A A L - Noah Okafor finds the net with the right foot! · before: 79' Rodrigo Bentancur relieves the pressure with a clearance ‹ 78' Safe hands from Antonin Kinsky as he comes out and claims the ball ‹ 78' Rodrigo Bentancur from Tottenham intercepts a cross aimed towards the box.

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW5 H v Aston Villa 45' Johan Manzambi: no structured culprit — reports only
- GW5 H v Aston Villa 67' Nicolas Jackson: no structured culprit — reports only
- GW5 H v Aston Villa 79' Emiliano Buendía: no structured culprit — reports only
  · GW5 error leading to a goal (SofaScore, match level — 3 conceded, the goal is not identified): Andy Robertson [CONFIRMED — SofaScore error flag]
  · GW5 other flags: Jan Paul van Hecke lastManTackle 1; Mateus Fernandes errorLeadToAShot 1
- GW6 A v Manchester United 73' Bryan Mbeumo: no structured culprit — reports only
- GW7 H v Coventry City 49' Jack Rudoni: no structured culprit — reports only
  · GW7 other flags: Micky van de Ven lastManTackle 1
- GW10 A v Leeds United 79' Noah Okafor: no structured culprit — reports only
  · GW10 other flags: Dominic Solanke clearanceOffLine 1; Conor Gallagher errorLeadToAShot 1; Micky van de Ven errorLeadToAShot 1

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

**Corners (E10 data layer):** observed takers GW1–10 [CONFIRMED — LiveScore Block L, 56 corners; side L/R as LiveScore records it; foot from SofaScore]: Mateus Fernandes 11 (11L/0R, 3 short, right foot); Savio 10 (1L/9R, 3 short, left foot); Mathys Tel 7 (7L/0R, 3 short, right foot); Mohammed Kudus 7 (0L/7R, 3 short, left foot). First contact on corners that ended in a shot (Understat) — for: Sandro Tonali 4, Jan Paul van Hecke 3 (2 headed), Micky van de Ven 3 (2 headed), Mohammed Kudus 3, Dominic Solanke 2 (2 headed) · against (who beat them): Yoane Wissa 2 (1 headed) — 1 goal, Murillo 2, Nathan Collins 1 (1 headed), Dango Ouattara 1 (1 headed), Kristoffer Ajer 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 45.3 (rank 2 of 20, 1 = highest line) · block length 18.5 (rank 3, 1 = most compact) · width 63.4. Per match: GW5 H v Aston Villa 4-2-3-1: back line 49, front 65, length 16, width 51 (64% poss); GW6 A v Manchester United 4-2-3-1: back line 42, front 68, length 26, width 63 (50% poss); GW7 H v Coventry City 3-1-4-2: back line 48, front 58, length 10, width 66 (65% poss); GW8 A v Chelsea 4-2-3-1: back line 36, front 64, length 28, width 67 (69% poss); GW9 H v Crystal Palace 4-2-3-1: back line 57, front 66, length 9, width 62 (79% poss); GW10 A v Leeds United 4-3-3: back line 43, front 59, length 16, width 64 (62% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 3 league match(es) v LB-coded sides — xG 1.96/match and 2.0 pts/match v 0.93 and 0.9 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW5 H v Aston Villa 2–3, xG 1.56, box shots 12, poss 64%; GW7 H v Coventry City 3–1, xG 0.86, box shots 10, poss 65%; GW9 H v Crystal Palace 2–0, xG 3.47, box shots 24, poss 79%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Sávio 3, Robertson 2, Fernandes 2** · FPL editorial order: Pedro Porro #1, Sávio #2, Tel #3
- Direct free-kick shooters: **Tel 2, Marmoush 1, Maddison 1** · FPL order: Pedro Porro #1, Xavi #2, Tel #3
- Penalties taken: **—** · FPL order: Solanke #1, Marmoush #2, Kudus #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Robertson 2, Porro 1**
- Corner targets (headed shots from corners): **Hecke 2, Ven 2, Solanke 2, Tel 1** · corner shots 23
- **DISAGREEMENT:** observed corner taker Sávio (3) v FPL #1 Pedro Porro — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Sandro Tonali 6 (0.61/90, percentile 96, 879 min); Conor Gallagher 2 (0.57/90, percentile 93, 317 min); Pedro Porro 2 (0.54/90, percentile 91, 334 min); Sávio 1 (0.27/90, percentile 77, 331 min); Andy Robertson 2 (0.27/90, percentile 77, 668 min) · club total 16 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 318 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 7.42, field tilt 55.1, possession 58.8%, box entries 13, direct speed 1.95, SCA 18; GW2: PPDA 9.4, field tilt 65.8, possession 57.5%, box entries 15, direct speed 2.14, SCA 33; GW3: PPDA 9.26, field tilt 58.4, possession 58.5%, box entries 10, direct speed 1.91, SCA 19; GW4: PPDA 8, field tilt 69.5, possession 62%, box entries 13, direct speed 1.5, SCA 28; GW5: PPDA 5.79, field tilt 75.2, possession 63.6%, box entries 17, direct speed 1.84, SCA 39; GW6: PPDA 7.75, field tilt 53.9, possession 50.4%, box entries 14, direct speed 2.16, SCA 21; GW7: PPDA 6.44, field tilt 68.1, possession 65.4%, box entries 15, direct speed 2.11, SCA 31; GW8: PPDA 6.91, field tilt 60.4, possession 68%, box entries 13, direct speed 2.32, SCA 29; GW9: PPDA 5.06, field tilt 95.4, possession 79.1%, box entries 33, direct speed 1.73, SCA 62; GW10: PPDA 8.12, field tilt 60, possession 60.6%, box entries 9, direct speed 2.46, SCA 14

**Zone 14 (C13, SofaScore heat-map points, 10 league matches):** for 46.2/match (rank 1 of 20) · conceded 23.7/match (rank 16 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 7.0/match · allowed 8.1/match · PPDA 7.8. Per match for/allowed: GW3 3/6; GW4 7/8; GW5 12/4; GW6 9/8; GW7 5/11; GW8 6/7 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: Antonín Kinský (16, 3/3)
- DEF: Jan Paul van Hecke (16, 3/3), Micky van de Ven (14, 3/3), Andy Robertson (14, 3/3), Archie Gray (14, 3/3)
- MID: Sandro Tonali (16, 3/3), Mateus Fernandes (12, 3/3), Mohammed Kudus (11, 3/3), Pedro Porro (6, 1/3), James Maddison (4, 1/3)
- FWD: Omar Marmoush (14, 3/3)
- Contested slots: M James Maddison 4 v Sávio 4 · Excluded (FPL flag): Mathys Tel — Ankle injury - 75% chance of playing
- Absent last match (E12, SofaScore list): Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Sávio (Muscle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury)
- Substitutions this season (C3): GW8 65' Omar Marmoush→Dominic Solanke TACTICAL; GW8 51' James Maddison→Conor Gallagher INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW9 88' Mathys Tel→Luca Williams-Barnett LATE; GW9 77' Omar Marmoush→Dejan Kulusevski GAME-STATE; GW9 77' Andy Robertson→Destiny Udogie GAME-STATE; GW9 66' Dominic Solanke→Conor Gallagher TACTICAL; GW9 46' Archie Gray→Pedro Porro HALF-TIME; GW10 83' Mohammed Kudus→Luca Williams-Barnett CHASING; GW10 65' Mateus Fernandes→Rodrigo Bentancur TACTICAL; GW10 65' Omar Marmoush→Dejan Kulusevski TACTICAL; GW10 65' Pedro Porro→Conor Gallagher CARD-RISK; GW10 43' Mathys Tel→Dominic Solanke INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']

### First-choice players and absences (F14) — generated 2026-11-10 07:41 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Antonín Kinský | start weight 16 | OK | a | — | — |
| CB | Jan Paul van Hecke | start weight 16 | OK | a 100% | Marcos Senesi | — |
| CB | Micky van de Ven | start weight 14 | OK | a 100% | Marcos Senesi | — |
| xGI #1 | Jan Paul van Hecke | xGI 2.44 | OK | a 100% | Dominic Solanke | — |
| xGI #2 | Mohammed Kudus | xGI 2.13 | OK | a 100% | Dominic Solanke | — |
| Penalties #1 (FPL) | Solanke | FPL order | OK | a | Marmoush | — |
| Direct FK #1 (FPL) | Pedro Porro | FPL order | OK | a 100% | Tel | — |
| Corners (observed) | Mateus Fernandes | 11 corners taken | OK | a | Savio | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 A Brentford: Micky van de Ven (Physical Discomfort), Mohammed Kudus (did not start) · GW2 H Newcastle United: Mohammed Kudus (did not start) · GW3 A Nottingham Forest: Mohammed Kudus (did not start) · GW4 H Everton: Mohammed Kudus (did not start) · GW5 H Aston Villa: Mohammed Kudus (did not start) · GW6 A Manchester United: Micky van de Ven (did not start) · GW7 H Coventry City: all started · GW8 A Chelsea: all started · GW9 H Crystal Palace: all started · GW10 A Leeds United: all started

### Next fixtures (all competitions)
- Sat 21 Nov 15:00 UTC · Premier League R11 · H v Ipswich Town
- Sun 29 Nov 14:05 UTC · Premier League R12 · A v Sunderland
- Thu 03 Dec 20:00 UTC · Premier League R13 · H v Fulham
- Sun 06 Dec 16:30 UTC · Premier League R14 · H v Arsenal
- Mon 14 Dec 20:00 UTC · Premier League R15 · A v Hull City
- Sat 19 Dec 17:30 UTC · Premier League R16 · A v Liverpool FC

### FPL availability flags (players with league minutes this season)
Sávio — Muscular injury - Expected back 21 Nov (0%); Tel — Ankle injury - 75% chance of playing (75%); Bergvall — Knee injury - Unknown return date (0%); Moore — Has joined FC Köln on loan for the rest of the season (0%); Richarlison — not included in squad. (0%); Mudryk — Ankle injury - Unknown return date (0%)
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
- GW10 A Leeds United 0–1 · xG 0.72–1.96 · poss 62% · 4-3-3 · scorers: none
### Corner takers observed (LiveScore Block L)
- Mateus Fernandes: 11 corners (11 left, 0 right, 3 short)
- Savio: 10 corners (1 left, 9 right, 3 short)
- Mathys Tel: 7 corners (7 left, 0 right, 3 short)
- Mohammed Kudus: 7 corners (0 left, 7 right, 3 short)
- Sandro Tonali: 5 corners (3 left, 2 right, 1 short)
- Omar Marmoush: 5 corners (5 left, 0 right, 1 short)
- Andrew Robertson: 4 corners (0 left, 4 right, 1 short)
- Pedro Porro: 3 corners (0 left, 3 right, 1 short)
- James Maddison: 3 corners (3 left, 0 right, 2 short)
- Dejan Kulusevski: 1 corners (0 left, 1 right)
