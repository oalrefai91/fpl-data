# Ipswich Town — data doc
*Feeder-written (2026-11-24 07:45 UTC); do not edit. Narrative: `profiles/teams/ipswich.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-24 07:45 UTC)
**Manager:** Gary O'Neil · **Venue:** Portman Road Stadium · **SofaScore:** https://www.sofascore.com/football/team/ipswich-town/32 · **FPL code:** IPS
**Table:** 16th, 11 pts (3W 2D 6L, GF 15 GA 22) · Home 13th (2-1-2, 6:7) · Away 16th (1-1-4, 9:15)
**Standing context (F15):** 27 league games left · points v 4th -10, v 5th -7, v 17th (last safe) +2, v 18th +2 · goal difference -7
**Suspension watch (D7, all players of the club):** Diop — 🟨 2 from a ban (3/5); Enciso — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 11 league matches):** goals after 75′ — for 6/15 (40%), against 1/22 (5%) · scored first 3, conceded first 8 (73% of matches), goalless 0 · points from losing positions 8 of 30 (10 matches behind at some point) · points from winning positions 10 of 15 (5 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Palacios (MID) 15.8/90, hit 7/10; Diop (DEF) 8.5/90, hit 5/11; O'Shea (DEF) 9.6/90, hit 4/11; Lukić (MID) 10.2/90, hit 2/7; Florentino (MID) 11.6/90, hit 1/8; Greaves (DEF) 7.3/90, hit 1/6
**Manager tenure (F13, SofaScore):** Gary O'Neil since 01 Jul 2026 · 11 matches in charge, all competitions (4W 2D 5L) · 11 league matches this season · contract to 30 Jun 2029 · previous club RC Strasbourg · interim flag not published by SofaScore
**Archetype (F5):** used **LB** — derived LB [DERIVED] (hand-set code agrees) · signals, last 6 league matches: possession 47.0%, PPDA 12.9 (Understat, 3 matches; lower = harder press), opponent offsides forced 1.7/match (line height), fast breaks 0.9/match (season), both sides' xG 3.23/match (openness) · note: possession 47.0 v 47.5; computed from 3 of 6 GWs (no PPDA/possession for GW9, GW10, GW11). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 17 (permanent 14, loan 0, free 0, loan returns 3) · out 20 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 11 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 13.97 | 17 | Big chances against | 38 | 17 |
| xGOT | 16.51 | 6 | Box shots against | 119 | 18 |
| xA | 7.52 | 16 | Corners against | 59 | 17 |
| Shots | 120 | 19 | Crosses faced | 197 | 12 |
| SoT | 42 | 14 | Dribbled past | 79 | 12 |
| Big chances | 22 | 16 | Errors→shot | 5 | 4 |
| Shots in box | 71 | 19 | GK goals prevented | -2.54 | 18 |
| Corners | 34 | 20 | Clearances | 288 | 11 |
| Crosses | 151 | 19 | Tackles | 174 | 11 |
| Fast breaks | 10 | 15 | Interceptions | 108 | 5 |
| FK shots | 6 | 4 | Def. contributions | 620 | 9 |
| Possession % | 46.09 | 14 | Aerial % | 48.62 | 14 |
| Pass % | 82.16 | 10 | Duel % | 49.00 | 14 |
| Long balls | 311 | 16 | Fouls | 126 | 10 |
| Dribbles | 83 | 5 | Yellows | 21 | 7 |
| Shots against | 176 | 17 | Km covered | 1287 | 5 |
| SoT against | 59 | 16 | Sprints | 1307 | 3 |
Per match: xG 1.27 · xGOT 1.50 · shots 10.9 · shots against 16.0 · big chances 2.0 for / 3.5 against · corners 3.1 / 5.4 · crosses 13.7 / 17.9 · possession 46.1%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | H | Fulham | 2–1 | 1.15/1.26 | 1.81/1.78 | 48 | 11/13 | 5/5 | 7/9 | 1/2 | 2/3 | 2/5 | 19/4 v 14/5 | 1/0 |
| 7 | A | Manchester City | 2–3 | 1.86/1.37 | 3.35/4.01 | 30 | 8/19 | 3/6 | 7/15 | 1/6 | 3/6 | 3/2 | 15/5 v 20/8 | 2/5 |
| 8 | H | Nottingham Forest | 1–1 | 0.46/0.86 | 2.29/2.76 | 49 | 7/17 | 3/5 | 3/15 | 0/1 | 1/4 | 0/5 | 6/1 v 22/5 | 1/2 |
| 9 | A | Hull City | 2–2 | 1.06/— | 0.78/— | 61 | 15/9 | 3/3 | 10/5 | 6/1 | 4/1 | 3/6 | 11/2 v 16/3 | 4/3 |
| 10 | H | Bournemouth | 1–2 | 1.26/— | 2.23/— | 56 | 10/15 | 2/4 | 4/9 | 3/5 | 2/4 | 2/7 | 13/2 v 12/1 | 1/2 |
| 11 | A | Tottenham Hotspur | 0–2 | 0.47/— | 2.65/— | 38 | 11/17 | 3/8 | 5/15 | 8/3 | 0/3 | 6/8 | 14/3 v 19/6 | 1/2 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | H | Fulham | 2–1 | 4-2-3-1 | 8/10 | 2/4 | 0/0 | 454/505 | 66/57 | Issahaku (ban (cards)) | Robinson (Ankle Injury; doubtful) | Lewis Smith |
| 7 | A | Manchester City | 2–3 | 3-4-2-1 | 16/8 | 2/1 | 0/0 | 319/753 | 39/85 | — | — | Farai Hallam |
| 8 | H | Nottingham Forest | 1–1 | 4-2-3-1 | 9/11 | 1/1 | 0/0 | 486/480 | 58/60 | Lukić (Groin Injury) | Jesus (Calf Injury), Savona (Knee Injury) | Thomas Bramall |
| 9 | A | Hull City | 2–2 | 4-2-3-1 | 12/13 | 3/3 | 0/0 | 565/344 | 76/45 | Lukić (Groin Injury; doubtful) | Hughes (Groin Injury), Gyabi (Groin Injury), Matazo (Cruciate Ligament Injury), Ansah (Back Injury), Targett (Ankle Injury) | Thomas Kirk |
| 10 | H | Bournemouth | 1–2 | 4-2-3-1 | 6/20 | 2/3 | 0/0 | 517/401 | 56/71 | — | Tóth (Hamstring Injury), Sánchez (Ankle Injury), Araujo (Thigh Injury) | Simon Hooper |
| 11 | A | Tottenham Hotspur | 0–2 | 4-2-3-1 | 17/17 | 1/4 | 0/0 | 354/591 | 39/68 | — | Tel (Hamstring Injury), Mudryk (Ankle Injury), Adarabioyo (Knock Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Robert Jones |
Per match: fouls 11.5 / 11.4 · yellows 1.91 / 2.36 · reds 1 / 1 (season) · offsides forced 1.7, committed 2.0 · crosses attempted 13.7 / faced 17.9. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 1.08 for / 1.54 against per match · Away (6): xG 1.43 / 2.40. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW11 A v Tottenham Hotspur 0–2 (Sat 21 Nov 15:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Christian Walton | G | 90 | 9.2 | 0.00 | 0.00 | 0 | 0 | 3 | 0 | 49 |
| Darnell Furlong | D | 90 | 6.2 | 0.00 | 0.00 | 0 | 0 | 3 | 0 | 39 |
| Issa Diop | D | 90 | 6.4 | 0.00 | 0.00 | 0 | 0 | 7 | 0 | 51 |
| Dara O'Shea | D | 90 | 7.1 | 0.00 | 0.02 | 1 | 0 | 10 | 1 | 53 |
| Leif Davis | D | 83 | 6.5 | 0.00 | 0.04 | 3 | 0 | 4 | 6 | 48 |
| Exequiel Palacios | M | 56 | 6.7 | 0.02 | 0.02 | 0 | 1 | 5 | 0 | 40 |
| Saša Lukić | M | 90 | 7 | 0.00 | 0.01 | 1 | 0 | 11 | 1 | 50 |
| Abdoul Ouattara | M | 56 | 7.9 | 0.10 | 0.01 | 0 | 1 | 7 | 0 | 24 |
| Julio Enciso | M | 90 | 6.9 | 0.12 | 0.16 | 1 | 4 | 0 | 0 | 53 |
| Daizen Maeda | M | 56 | 6.2 | 0.00 | 0.00 | 0 | 0 | 2 | 0 | 19 |
| Zian Flemming | F | 74 | 6.5 | 0.10 | 0.01 | 2 | 2 | 1 | 0 | 32 |
Subs used: Florentino Luís (34'), Abdul Fatawu Issahaku (34'), Jack Clarke (34'), Emersonn (16'), Jacob Greaves (13')
Goals: 15' Luca Williams-Barnett (assist Pedro Porro) [opp]; 51' Dominic Solanke (assist Luca Williams-Barnett) [opp]
Substitutions (own): 56' Jack Clarke for Daizen Maeda; 56' Abdul Fatawu Issahaku for Abdoul Ouattara; 56' Florentino Luís for Exequiel Palacios; 74' Emersonn for Zian Flemming; 83' Jacob Greaves for Leif Davis [injury]
Cards: manager/staff booking: Gary O'Neil 42' [LiveScore] (own; no FPL effect); 41' James Maddison (yellow, opp); 52' Luca Williams-Barnett (yellow, opp); 79' Mohammed Kudus (yellow, opp); 83' Issa Diop (yellow, own); 90' Mateus Fernandes (yellow, opp)
**Baseline XI change vs GW10 (4-2-3-1 → 4-2-3-1):** in — Darnell Furlong, Saša Lukić, Zian Flemming; out — Emersonn, Florentino Luís, Jaden Philogene-Bidace.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 6 | H Fulham | 55' | AGAINST | Ryan Sessegnon | — | corner | 0.02 |
| 6 | H Fulham | 88' | FOR | Abdoul Ouattara | — | open play | 0.01 |
| 6 | H Fulham | 90' | FOR | Dara O'Shea | Jack Clarke | set piece | 0.55 |
| 7 | A Manchester City | 19' | AGAINST | Phil Foden | Jérémy Doku | open play | 0.64 |
| 7 | A Manchester City | 21' | FOR | Daizen Maeda | Abdoul Ouattara | open play | 0.17 |
| 7 | A Manchester City | 34' | AGAINST | Erling Haaland | Mateo Kovačić | open play | 0.34 |
| 7 | A Manchester City | 69' | AGAINST | Erling Haaland | Iliman Ndiaye | open play | 0.65 |
| 7 | A Manchester City | 90' | FOR | Zian Flemming | — | penalty | 0.76 |
| 8 | H Nottingham Forest | 13' | AGAINST | Neco Williams | Daniel Muñoz | open play | 0.44 |
| 8 | H Nottingham Forest | 41' | FOR | Julio Enciso | — | open play | 0.27 |
| 9 | A Hull City | 22' | FOR | Florentino Luís | Abdoul Ouattara | [no Understat] | — |
| 9 | A Hull City | 58' | AGAINST | Tim Iroegbunam | Oliver McBurnie | [no Understat] | — |
| 9 | A Hull City | 68' | AGAINST | Oliver McBurnie | — | [no Understat] | — |
| 9 | A Hull City | 74' | FOR | Julio Enciso | Azor Matusiwa | [no Understat] | — |
| 10 | H Bournemouth | 5' | AGAINST | Evanilson | — | [no Understat] | — |
| 10 | H Bournemouth | 46' | AGAINST | Leif Davis | — | own goal | — |
| 10 | H Bournemouth | 73' | FOR | Jack Clarke | — | penalty | — |
| 11 | A Tottenham Hotspur | 15' | AGAINST | Luca Williams-Barnett | Pedro Porro | [no Understat] | — |
| 11 | A Tottenham Hotspur | 51' | AGAINST | Dominic Solanke | Luca Williams-Barnett | [no Understat] | — |
Scored 15: open play 10, penalty 2, [no Understat] 2, set piece 1 · Conceded 22: open play 12, [no Understat] 5, own goal 2, direct FK 1, penalty 1, corner 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW9 FOR v Hull City 22' Florentino Luis (assist Abdoul Ouattara): G O O O A A A L - Florentino scores with the right foot! · before: 22' Abdoul Ouattara creates a scoring opportunity for his teammate ‹ 21' Abdoul Ouattara relieves the pressure with a clearance ‹ 21' Safe hands from Konstantinos Tzolakis as he comes out and claims the ball
- GW9 AG v Hull City 58' Tim Iroegbunam (assist Oli McBurnie, key pass Lewie Coyle): G O O O A A A L - Tim Iroegbunam scores with the right foot! · before: 58' Semi Ajayi successfully blocks the shot ‹ 58' A shot by Jaden Philogene-Bidace is blocked. ‹ 58' Nobel Mendy relieves the pressure with a clearance
- GW9 AG v Hull City 68' Oli McBurnie: G O O O A A A L Oli McBurnie curls the direct free kick into the back of the net with the right foot! Wonderful finish · before: 67' The referee signals a free kick as Florentino from Ipswich trips Mohamed Belloumi ‹ 67' Mohamed Belloumi relieves the pressure with a clearance ‹ 67' Dara O'Shea from Ipswich intercepts a cross aimed towards the box.
- GW9 FOR v Hull City 74' Julio Enciso (assist Azor Matusiwa): G O O O A A A L - Julio Enciso from Ipswich beats the keeper from outside the box with the right foot! · before: 74' Nobel Mendy successfully blocks the shot ‹ 74' Daizen Maeda takes the free-kick but it is blocked by the wall ‹ 73' Jack Clarke relieves the pressure with a clearance
- GW10 AG v Bournemouth 5' Evanilson: GOAL! It's an easy finish as Evanilson from Bournemouth taps the ball into an open goal with the right foot! · before: 5' Evanilson makes the tackle and wins possession for his team ‹ 4' Goal kick for Bournemouth. ‹ 3' Antonio Silva relieves the pressure with a clearance
- GW10 FOR v Bournemouth 46' Leif Davis [OG]: OWN GOAL - Leif Davis sends the ball into his own net! · before: 46' Issa Diop successfully blocks the shot ‹ 46' A shot by Ryan Christie is blocked. ‹ 46' Ryan Christie wins an air challenge against Emersonn
- GW10 FOR v Bournemouth 73' Jack Clarke [pen]: G O O O A A A L - Jack Clarke from Ipswich puts it away from the penalty spot with the right foot! Djordje Petrovic chose the wrong side. · before: 73' After VAR check, the referee decided to stay with the initial call - penalty for Ipswich! ‹ 73' VAR - PENALTY! - The referee has stopped the play. VAR check in progress, a potential penal ‹ 72' PENALTY - Lewis Cook from Bournemouth concedes a penalty for tripping Abdoul Ouattara.
- GW11 AG v Tottenham Hotspur 15' Luca Williams-Barnet (assist Pedro Porro): — no commentary line — · before: 14' Corner, Tottenham Hotspur. Conceded by Leif Davis. ‹ 14' Attempt saved. Dominic Solanke (Tottenham Hotspur) header from the centre of the box is sav ‹ 13' Foul by Zian Flemming (Ipswich Town).
- GW11 AG v Tottenham Hotspur 51' Dominic Solanke: — no commentary line — · before: 50' Zian Flemming (Ipswich Town) wins a free kick in the defensive half. ‹ 50' Foul by Conor Gallagher (Tottenham Hotspur). ‹ 49' Corner, Tottenham Hotspur. Conceded by Leif Davis.

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW6 H v Fulham 55' Ryan Sessegnon: no structured culprit — reports only
  · GW6 other flags: Issa Diop clearanceOffLine 1
- GW7 A v Manchester City 19' Phil Foden: no structured culprit — reports only
- GW7 A v Manchester City 34' Erling Haaland: no structured culprit — reports only
- GW7 A v Manchester City 69' Erling Haaland: no structured culprit — reports only
  · GW7 error leading to a goal (SofaScore, match level — 3 conceded, the goal is not identified): Abdoul Ouattara [CONFIRMED — SofaScore error flag]
- GW8 H v Nottingham Forest 13' Neco Williams: Dara O'Shea error leading to the goal [CONFIRMED — SofaScore error flag]
  · GW8 other flags: Issa Diop errorLeadToAShot 1; Florentino Luís errorLeadToAShot 2; Leif Davis clearanceOffLine 1
- GW9 A v Hull City 58' Tim Iroegbunam: no structured culprit — reports only
- GW9 A v Hull City 68' Oliver McBurnie: no structured culprit — reports only
- GW10 H v Bournemouth 5' Evanilson: no structured culprit — reports only
- GW10 H v Bournemouth 46' Leif Davis [OG]: Leif Davis own goal [CONFIRMED — SofaScore]
  · GW10 error leading to a goal (SofaScore, match level — 2 conceded, the goal is not identified): Christian Walton, Abdoul Ouattara [CONFIRMED — SofaScore error flag]
- GW11 A v Tottenham Hotspur 15' Luca Williams-Barnett: no structured culprit — reports only
- GW11 A v Tottenham Hotspur 51' Dominic Solanke: no structured culprit — reports only
  · GW11 other flags: Abdoul Ouattara lastManTackle 1, clearanceOffLine 1

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 71 | 8.58 | 10 | 107 | 16.56 | 12 |
| corner | 7 | 0.49 | 0 | 17 | 1.21 | 1 |
| set piece | 4 | 0.73 | 1 | 5 | 0.29 | 0 |
| direct FK | 2 | 0.11 | 0 | 5 | 0.26 | 1 |
| penalty | 1 | 0.76 | 1 | 1 | 0.76 | 1 |
Totals per match: xG 1.33 (npxG 1.24) for, xGA 2.39 (np 2.29) against · dead-ball share of xG 20% for, 13% against · penalties won 1, conceded 1 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 7 shots, xG 0.49, 0 goals, headed 3: 6-yard box, central 1 shots, xG 0.24, 0 goals; penalty area, central 2 shots, xG 0.12, 0 goals; penalty area, right 1 shots, xG 0.06, 0 goals · against — 17 shots conceded, xG 1.21, 1 goals, headed 7: 6-yard box, central 3 shots, xG 0.51, 0 goals; penalty area, central 7 shots, xG 0.49, 0 goals; outside box, central 4 shots, xG 0.09, 1 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 38 · corner shots conceded 17 (headed 7), xG 1.21, goals 1 · xG per corner faced 0.032 (rank 16 of 20, 1 = weakest) · weak zone: penalty-spot band (0.49 xG, 40% of theirs v 26% league) · signal: **STRONG — no corner pairing against them** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–11 [CONFIRMED — LiveScore Block L, 28 corners; side L/R as LiveScore records it; foot from SofaScore]: Abdul Fatawu 8 (0L/8R, left foot); Sasa Lukic 8 (8L/0R, right foot); Jaden Philogene-Bidace 3 (2L/1R, 2 short, right foot); Exequiel Palacios 3 (2L/1R, 1 short, right foot). First contact on corners that ended in a shot (Understat) — for: Dara O&#039;Shea 1 (1 headed), Jacob Greaves 1 (1 headed), Emersonn 1 (1 headed), Marcelino Núñez 1, Sasa Lukic 1 · against (who beat them): Diogo Dalot 2 (1 headed), Murillo 2 (1 headed), Kobbie Mainoo 2, Nilson Angulo 1 (1 headed), Alexis Mac Allister 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 38.3 (rank 17 of 20, 1 = highest line) · block length 21.3 (rank 12, 1 = most compact) · width 64.7. Per match: GW6 H v Fulham 4-2-3-1: back line 45, front 62, length 17, width 64 (48% poss); GW7 A v Manchester City 3-4-2-1: back line 36, front 57, length 21, width 58 (30% poss); GW8 H v Nottingham Forest 4-2-3-1: back line 36, front 59, length 23, width 66 (49% poss); GW9 A v Hull City 4-2-3-1: back line 37, front 63, length 26, width 63 (61% poss); GW10 H v Bournemouth 4-2-3-1: back line 35, front 61, length 26, width 69 (56% poss); GW11 A v Tottenham Hotspur 4-2-3-1: back line 37, front 59, length 22, width 53 (38% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 4 league match(es) v LB-coded sides — xG 1.25/match and 2.0 pts/match v 1.28 and 0.4 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW1 H v Sunderland 2–1, xG 1.80, box shots 8, poss 38%; GW4 A v Crystal Palace 3–2, xG 1.68, box shots 8, poss 54%; GW8 H v Nottingham Forest 1–1, xG 0.46, box shots 3, poss 49%; GW9 A v Hull City 2–2, xG 1.06, box shots 10, poss 61%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Davis 2, Fatawu 1, Núñez 1** · FPL editorial order: Lukić #1, Fatawu #2, Philogene #3
- Direct free-kick shooters: **Davis 1, Enciso 1** · FPL order: Enciso #1, Davis #2, Clarke #3
- Penalties taken: **Flemming 1** · FPL order: Clarke #1, Flemming #2, Philogene #3
- Set-piece deliverers (assisted 'SetPiece' shots): **O&#039;Shea 2, Clarke 1**
- Corner targets (headed shots from corners): **O&#039;Shea 1, Greaves 1, Emersonn 1** · corner shots 7
- **DISAGREEMENT:** observed corner taker Leif Davis (2) v FPL #1 Lukić — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Julio Enciso 4 (0.39/90, percentile 85, 919 min); Abdul Fatawu Issahaku 2 (0.31/90, percentile 80, 578 min); Jaden Philogene 1 (0.30/90, percentile 79, 298 min); Jack Clarke 1 (0.28/90, percentile 78, 321 min) · club total 12 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 334 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 11.49, field tilt 41, possession 37.4%, box entries 7, direct speed 2.51, SCA 20; GW2: PPDA 13.43, field tilt 33.7, possession 40.4%, box entries 8, direct speed 2.43, SCA 16; GW3: PPDA 14.64, field tilt 42, possession 45.9%, box entries 10, direct speed 3.01, SCA 27; GW4: PPDA 8.37, field tilt 57, possession 53.3%, box entries 12, direct speed 2.8, SCA 20; GW5: PPDA 15.52, field tilt 40.1, possession 48.2%, box entries 7, direct speed 2, SCA 23; GW6: PPDA 12.06, field tilt 60.1, possession 47.6%, box entries 15, direct speed 2.08, SCA 22; GW7: PPDA 13.2, field tilt 23.2, possession 30.5%, box entries 8, direct speed 2.84, SCA 16; GW8: PPDA 13.54, field tilt 46.5, possession 49.4%, box entries 6, direct speed 2.43, SCA 12; GW9: PPDA 9.28, field tilt 52.3, possession 61.1%, box entries 11, direct speed 2.5, SCA 30; GW10: PPDA 9.3, field tilt 51.1, possession 56%, box entries 8, direct speed 1.99, SCA 19

**Zone 14 (C13, SofaScore heat-map points, 11 league matches):** for 30.9/match (rank 7 of 20) · conceded 31.4/match (rank 9 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 4.9/match · allowed 7.8/match · PPDA 12.6. Per match for/allowed: GW3 5/6; GW4 11/9; GW5 5/7; GW6 5/5; GW7 2/12; GW8 4/6 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: Christian Walton (13, 3/3)
- DEF: Issa Diop (16, 3/3), Dara O'Shea (16, 3/3), Abdoul Ouattara (13, 3/3), Jacob Greaves (4, 0/3)
- MID: Julio Enciso (16, 3/3), Exequiel Palacios (14, 3/3), Daizen Maeda (10, 2/3), Florentino Luís (9, 2/3), Saša Lukić (8, 1/3)
- FWD: Emersonn (13, 2/3)
- Contested slots: D Jacob Greaves 4 v Darnell Furlong 3; M Saša Lukić 8 v Abdul Fatawu Issahaku 8 · Excluded (FPL flag): Leif Davis — Calf injury - 75% chance of playing
- Absent last match (E12, SofaScore list): —
- Substitutions this season (C3): GW9 70' Abdul Fatawu Issahaku→Daizen Maeda CHASING; GW9 70' Florentino Luís→Azor Matusiwa CHASING; GW9 69' Jaden Philogene-Bidace→Jack Clarke CHASING; GW10 85' Florentino Luís→Chuba Akpom LATE; GW10 65' Daizen Maeda→Abdul Fatawu Issahaku CHASING; GW10 54' Emersonn→Zian Flemming CHASING; GW10 53' Jaden Philogene-Bidace→Jack Clarke CHASING; GW11 83' Leif Davis→Jacob Greaves INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW11 74' Zian Flemming→Emersonn CHASING; GW11 56' Daizen Maeda→Jack Clarke CHASING; GW11 56' Abdoul Ouattara→Abdul Fatawu Issahaku CHASING; GW11 56' Exequiel Palacios→Florentino Luís CHASING

### First-choice players and absences (F14) — generated 2026-11-24 07:45 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Christian Walton | start weight 13 | OK | a | Kjell Scherpen | — |
| CB | Issa Diop | start weight 16 | OK | a | Jacob Greaves | — |
| CB | Dara O'Shea | start weight 16 | OK | a | Jacob Greaves | — |
| xGI #1 | Julio Enciso | xGI 4.53 | OK | a 100% | Leif Davis | — |
| xGI #2 | Emersonn | xGI 2.91 | OK | a 100% | Leif Davis | — |
| Penalties #1 (FPL) | Clarke | FPL order | OK | a | Flemming | — |
| Direct FK #1 (FPL) | Enciso | FPL order | OK | a 100% | Davis | — |
| Corners (observed) | Abdul Fatawu | 8 corners taken | OK | a 100% | Sasa Lukic | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Sunderland: Christian Walton (did not start) · GW2 A Manchester United: Christian Walton (did not start) · GW3 H Liverpool FC: Christian Walton (did not start) · GW4 A Crystal Palace: Christian Walton (did not start) · GW5 A Everton: all started · GW6 H Fulham: all started · GW7 A Manchester City: all started · GW8 H Nottingham Forest: all started · GW9 A Hull City: all started · GW10 H Bournemouth: all started · GW11 A Tottenham Hotspur: Emersonn (did not start)

### Next fixtures (all competitions)
- Sat 28 Nov 17:30 UTC · Premier League R12 · H v Aston Villa
- Tue 01 Dec 20:00 UTC · Premier League R13 · A v Coventry City
- Sat 05 Dec 15:00 UTC · Premier League R14 · A v Leeds United
- Sat 12 Dec 15:00 UTC · Premier League R15 · H v Newcastle United
- Sun 20 Dec 14:00 UTC · Premier League R16 · A v Brighton & Hove Albion
- Sat 26 Dec 15:00 UTC · Premier League R17 · H v Brentford

### FPL availability flags (players with league minutes this season)
Davis — Calf injury - 75% chance of playing (75%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 H Sunderland 2–1 · xG 1.80–0.66 · poss 38% · 4-2-3-1 · scorers: Emersonn 24', Jack Clarke 90'
- GW2 A Manchester United 2–5 · xG 2.06–4.77 · poss 40% · 4-2-3-1 · scorers: Leif Davis 29', Chuba Akpom 90'
- GW3 H Liverpool FC 0–2 · xG 0.75–0.69 · poss 45% · 4-2-3-1 · scorers: none
- GW4 A Crystal Palace 3–2 · xG 1.68–0.62 · poss 54% · 4-2-3-1 · scorers: Emersonn 23', Leif Davis 45', Zian Flemming 90'
- GW5 A Everton 0–1 · xG 1.44–2.24 · poss 48% · 4-2-3-1 · scorers: none
- GW6 H Fulham 2–1 · xG 1.15–1.81 · poss 48% · 4-2-3-1 · scorers: Abdoul Ouattara 88', Dara O'Shea 90'
- GW7 A Manchester City 2–3 · xG 1.86–3.35 · poss 30% · 3-4-2-1 · scorers: Daizen Maeda 21', Zian Flemming 90'
- GW8 H Nottingham Forest 1–1 · xG 0.46–2.29 · poss 49% · 4-2-3-1 · scorers: Julio Enciso 41'
- GW9 A Hull City 2–2 · xG 1.06–0.78 · poss 61% · 4-2-3-1 · scorers: Florentino Luís 22', Julio Enciso 74'
- GW10 H Bournemouth 1–2 · xG 1.26–2.23 · poss 56% · 4-2-3-1 · scorers: Jack Clarke 73'
- GW11 A Tottenham Hotspur 0–2 · xG 0.47–2.65 · poss 38% · 4-2-3-1 · scorers: none
### Corner takers observed (LiveScore Block L)
- Abdul Fatawu: 8 corners (0 left, 8 right)
- Sasa Lukic: 8 corners (8 left, 0 right)
- Jaden Philogene-Bidace: 3 corners (2 left, 1 right, 2 short)
- Exequiel Palacios: 3 corners (2 left, 1 right, 1 short)
- Leif Davis: 3 corners (0 left, 3 right)
- Jack Clarke: 2 corners (2 left, 0 right, 1 short)
- Marcelino Nunez: 1 corners (1 left, 0 right)
