# Nottingham Forest — data doc
*Feeder-written (2026-11-24 07:45 UTC); do not edit. Narrative: `profiles/teams/nottm-forest.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-24 07:45 UTC)
**Manager:** Oliver Glasner · **Venue:** City Ground · **SofaScore:** https://www.sofascore.com/football/team/nottingham-forest/14 · **FPL code:** NFO
**Table:** 17th, 9 pts (2W 3D 6L, GF 9 GA 15) · Home 19th (1-1-3, 3:4) · Away 13th (1-2-3, 6:11)
**Standing context (F15):** 27 league games left · points v 4th -12, v 5th -9, v 17th (last safe) +0, v 18th +0 · goal difference -6
**Suspension watch (D7, all players of the club):** Delap — 🟨 2 from a ban (3/5); Murillo — 🟨 **ONE FROM A BAN** (4/5 before GW19); Aina — 🟨 2 from a ban (3/5); McAtee — 🟨 **ONE FROM A BAN** (4/5 before GW19) [FPL]
**Goal timing & game state (F17, 11 league matches):** goals after 75′ — for 1/9 (11%), against 4/15 (27%) · scored first 5, conceded first 5 (45% of matches), goalless 1 · points from losing positions 0 of 18 (6 matches behind at some point) · points from winning positions 8 of 15 (5 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Murillo (DEF) 9.8/90, hit 7/11; Schlager (MID) 12.4/90, hit 5/11; McAtee (MID) 11.6/90, hit 5/11; Milenković (DEF) 9.0/90, hit 2/7; N.Williams (DEF) 5.9/90, hit 2/11; Diomande (DEF) 8.7/90, hit 1/5
**Manager tenure (F13, SofaScore):** Oliver Glasner since 06 Jul 2026 · 10 matches in charge, all competitions (1W 3D 6L) · 11 league matches this season · contract to 30 Jun 2029 · previous club Crystal Palace · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Leeds United — last 4: Aug 2026 EFL Cup Nottingham Forest 0–2 Leeds United (yellows 4–3, xG 1.21–2.58); Aug 2026 Premier League Nottingham Forest 0–1 Leeds United (yellows 2–1, xG 0.66–0.47); Feb 2026 Premier League Leeds United 3–1 Nottingham Forest (yellows 1–1, xG 2.83–1.33); Nov 2025 Premier League Nottingham Forest 3–1 Leeds United (yellows 2–1, xG 2.55–0.74) · 15 yellows in 4
**Archetype (F5):** used **LB** — derived LB [DERIVED] (hand-set code agrees) · signals, last 6 league matches: possession 43.8%, PPDA 15.1 (Understat, 3 matches; lower = harder press), opponent offsides forced 1.3/match (line height), fast breaks 2.0/match (season), both sides' xG 3.26/match (openness) · note: computed from 3 of 6 GWs (no PPDA/possession for GW9, GW10, GW11). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 11 (permanent 6, loan 0, free 0, loan returns 5) · out 17 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 11 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 17.69 | 6 | Big chances against | 22 | 6 |
| xGOT | 9.72 | 20 | Box shots against | 79 | 4 |
| xA | 11.14 | 8 | Corners against | 50 | 8 |
| Shots | 181 | 4 | Crosses faced | 184 | 8 |
| SoT | 37 | 17 | Dribbled past | 92 | 17 |
| Big chances | 29 | 6 | Errors→shot | 4 | 1 |
| Shots in box | 112 | 5 | GK goals prevented | -2.05 | 14 |
| Corners | 49 | 10 | Clearances | 289 | 10 |
| Crosses | 198 | 8 | Tackles | 204 | 2 |
| Fast breaks | 22 | 2 | Interceptions | 88 | 14 |
| FK shots | 6 | 4 | Def. contributions | 612 | 10 |
| Possession % | 45.36 | 16 | Aerial % | 49.86 | 10 |
| Pass % | 77.78 | 18 | Duel % | 49.02 | 13 |
| Long balls | 453 | 2 | Fouls | 155 | 19 |
| Dribbles | 78 | 10 | Yellows | 27 | 15 |
| Shots against | 119 | 2 | Km covered | 1263 | 10 |
| SoT against | 38 | 3 | Sprints | 1206 | 10 |
Per match: xG 1.61 · xGOT 0.88 · shots 16.5 · shots against 10.8 · big chances 2.6 for / 2.0 against · corners 4.5 / 4.5 · crosses 18.0 / 16.7 · possession 45.4%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | A | Crystal Palace | 1–3 | 3.34/3.80 | 2.41/2.43 | 57 | 24/13 | 6/7 | 16/11 | 8/2 | 8/5 | 8/5 | 29/10 v 15/6 | 2/1 |
| 7 | H | Arsenal | 0–1 | 0.90/0.75 | 1.14/0.92 | 26 | 14/9 | 2/1 | 8/7 | 6/3 | 0/1 | 8/6 | 14/1 v 27/7 | 1/2 |
| 8 | A | Ipswich Town | 1–1 | 2.29/2.76 | 0.46/0.86 | 51 | 17/7 | 5/3 | 15/3 | 1/0 | 4/1 | 5/0 | 22/5 v 6/1 | 2/1 |
| 9 | A | Brentford | 0–2 | 0.86/— | 0.46/— | 58 | 15/7 | 1/1 | 9/3 | 6/1 | 1/1 | 4/3 | 18/4 v 10/2 | 1/1 |
| 10 | H | Manchester City | 3–1 | 1.06/— | 1.76/— | 22 | 11/12 | 5/4 | 7/10 | 3/4 | 1/3 | 3/7 | 12/2 v 23/7 | 0/2 |
| 11 | A | Bournemouth | 0–2 | 1.99/— | 2.89/— | 49 | 18/19 | 1/7 | 9/12 | 8/5 | 2/5 | 4/6 | 12/4 v 12/1 | 2/0 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | A | Crystal Palace | 1–3 | 3-4-2-1 | 10/11 | 2/2 | 0/0 | 498/386 | 50/47 | Jesus (Calf Injury), Savona (Knee Injury) | Disasi (ban (red)), Riad (Knee Injury), Henderson (Foot Injury), Mateta (Hamstring Injury) | Peter Bankes |
| 7 | H | Arsenal | 0–1 | 3-4-2-1 | 14/8 | 1/1 | 0/0 | 224/634 | 33/76 | Jesus (Calf Injury), Savona (Knee Injury), Gibbs-White (Knock Injury; doubtful) | Tzolis (Hamstring Injury), Hincapié (Ankle Injury) | Michael Oliver |
| 8 | A | Ipswich Town | 1–1 | 3-4-2-1 | 11/9 | 1/1 | 0/0 | 480/486 | 60/58 | Jesus (Calf Injury), Savona (Knee Injury) | Lukić (Groin Injury) | Thomas Bramall |
| 9 | A | Brentford | 0–2 | 3-4-2-1 | 17/6 | 3/1 | 0/0 | 489/346 | 69/47 | Jesus (Calf Injury), Domínguez (Knock Injury), Savona (Knee Injury) | Yarmoliuk (ban (red)), Carvalho (Knock Injury), Furo (Knee Surgery), Henry (Muscle Injury) | Darren England |
| 10 | H | Manchester City | 3–1 | 3-4-2-1 | 13/7 | 4/0 | 0/0 | 208/771 | 38/79 | Domínguez (Knock Injury), Savona (Knee Injury) | Semenyo (Leg Injury) | Samuel Barrott |
| 11 | A | Bournemouth | 0–2 | 3-4-2-1 | 15/13 | 3/1 | 0/0 | 440/454 | 73/51 | Odoi (Groin Injury), Domínguez (Knock Injury) | Tóth (Hamstring Injury), Sánchez (Ankle Injury), Araujo (Thigh Injury) | Adam Herczeg |
Per match: fouls 14.1 / 10.5 · yellows 2.45 / 1.36 · reds 0 / 0 (season) · offsides forced 1.5, committed 1.6 · crosses attempted 18.0 / faced 16.7. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 0.93 for / 1.02 against per match · Away (6): xG 2.18 / 1.47. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW11 A v Bournemouth 0–2 (Sat 21 Nov 15:00 UTC) — formation 3-4-2-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Matz Sels | G | 90 | 7.8 | 0.00 | 0.04 | 0 | 0 | 2 | 0 | 48 |
| Jair | D | 90 | 7.2 | 0.00 | 0.03 | 0 | 0 | 9 | 0 | 73 |
| Nikola Milenković | D | 90 | 6.9 | 0.00 | 0.03 | 1 | 0 | 9 | 0 | 59 |
| Murillo | D | 90 | 7 | 0.03 | 0.01 | 0 | 1 | 6 | 1 | 76 |
| Daniel Muñoz | M | 82 | 6.2 | 0.00 | 0.05 | 2 | 0 | 3 | 3 | 54 |
| James McAtee | M | 72 | 6.3 | 0.36 | 0.18 | 2 | 3 | 5 | 0 | 54 |
| Ryan Yates | M | 45 | 6.8 | 0.00 | 0.01 | 1 | 0 | 4 | 0 | 24 |
| Neco Williams | M | 72 | 7.2 | 0.06 | 0.01 | 0 | 2 | 8 | 1 | 42 |
| Dan Ndoye | F | 45 | 6.1 | 0.03 | 0.00 | 0 | 1 | 1 | 0 | 19 |
| Morgan Gibbs-White | F | 90 | 7.9 | 0.23 | 0.25 | 4 | 2 | 4 | 5 | 63 |
| Liam Delap | F | 90 | 5.6 | 0.05 | 0.24 | 1 | 1 | 0 | 0 | 39 |
Subs used: Xaver Schlager (45'), Igor Jesus (45'), Luca Netz (18'), Chris Wood (18'), Ola Aina (8')
Goals: 19' Evanilson (assist James Hill) [opp]; 45' Justin Kluivert (assist Marcus Tavernier) [opp]
Substitutions (own): 46' Xaver Schlager for Ryan Yates; 46' Igor Jesus for Dan Ndoye; 72' Luca Netz for Neco Williams; 72' Chris Wood for James McAtee; 82' Ola Aina for Daniel Muñoz
Cards: 45' Liam Delap (yellow, own); 57' Daniel Muñoz (yellow, own); 87' Alex Scott (yellow, opp); 90' Murillo (yellow, own)
**Baseline XI change vs GW10 (3-4-2-1 → 3-4-2-1):** in — Dan Ndoye; out — Xaver Schlager.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 6 | A Crystal Palace | 3' | FOR | Dan Ndoye | — | open play | 0.28 |
| 6 | A Crystal Palace | 41' | AGAINST | Daichi Kamada | Quinten Timber | open play | 0.54 |
| 6 | A Crystal Palace | 45' | AGAINST | Jefferson Lerma | Adam Wharton | corner | 0.48 |
| 6 | A Crystal Palace | 59' | AGAINST | Yéremy Pino | — | open play | 0.40 |
| 7 | H Arsenal | 80' | AGAINST | Noni Madueke | Declan Rice | open play | 0.04 |
| 8 | A Ipswich Town | 13' | FOR | Neco Williams | Daniel Muñoz | open play | 0.44 |
| 8 | A Ipswich Town | 41' | AGAINST | Julio Enciso | — | open play | 0.27 |
| 9 | A Brentford | 30' | AGAINST | Nikola Milenković | — | own goal | — |
| 9 | A Brentford | 76' | AGAINST | Igor Thiago | Jaidon Anthony | [no Understat] | — |
| 10 | H Manchester City | 6' | FOR | Jair | — | [no Understat] | — |
| 10 | H Manchester City | 18' | FOR | Liam Delap | Xaver Schlager | [no Understat] | — |
| 10 | H Manchester City | 52' | AGAINST | Rayan Cherki | — | [no Understat] | — |
| 10 | H Manchester City | 73' | FOR | Liam Delap | Morgan Gibbs-White | [no Understat] | — |
| 11 | A Bournemouth | 19' | AGAINST | Evanilson | James Hill | [no Understat] | — |
| 11 | A Bournemouth | 45' | AGAINST | Justin Kluivert | Marcus Tavernier | [no Understat] | — |
Scored 9: open play 5, [no Understat] 3, penalty 1 · Conceded 15: open play 7, [no Understat] 4, direct FK 1, [unmatched] 1, corner 1, own goal 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW9 FOR v Brentford 30' Nikola Milenković [OG]: OWN GOAL - Nikola Milenkovic sends the ball into his own net! · before: 30' Nikola Milenkovic from Nottingham Forest intercepts a cross aimed towards the box. ‹ 29' Kevin Schade makes the tackle and wins possession for his team ‹ 28' Neco Williams makes the tackle and wins possession for his team
- GW9 AG v Brentford 76' Igor Thiago (assist Jaidon Anthony, key pass Aaron Hickey): GOAL! - Igor Thiago score from a shot with the right foot, that takes a deflection. · before: 76' Jaidon Anthony creates a scoring opportunity for his teammate ‹ 75' Keane Lewis-Potter is penalised for pushing Arnaud Kalimuendo-Muinga. ‹ 75' Neco Williams relieves the pressure with a clearance
- GW10 FOR v Manchester City 6' Jair Cunha: G O O O O O A A L - Jair Cunha finds the net with the left foot! · before: 6' Nottingham Forest with a potentially dangerous attack. ‹ 6' Jair Cunha makes the tackle and wins possession for his team ‹ 5' Elliot Anderson relieves the pressure with a clearance
- GW10 FOR v Manchester City 18' Liam Delap (assist Xaver Schlager): G O O O A A A L - Liam Delap scores with the right foot! · before: 18' Nottingham Forest start a counter attack. ‹ 18' Nikola Milenkovic relieves the pressure with a clearance ‹ 17' Neco Williams relieves the pressure with a clearance
- GW10 AG v Manchester City 52' Rayan Cherki: G O O O A A A L - Rayan Cherki volleys the ball into the back of the net with the left foot. · before: 52' Ryan Yates relieves the pressure with a clearance ‹ 52' Jair Cunha from Nottingham Forest intercepts a cross aimed towards the box. ‹ 52' The referee signals a free kick as Murillo from Nottingham Forest trips Enzo Fernandez
- GW10 FOR v Manchester City 73' Liam Delap (assist Morgan Gibbs-White): G O O O A A A L - Liam Delap scores with the left foot! · before: 73' Morgan Gibbs-White creates a scoring opportunity for his teammate ‹ 73' Nottingham Forest start a counter attack. ‹ 73' Jair Cunha from Nottingham Forest intercepts a cross aimed towards the box.
- GW11 AG v Bournemouth 19' Evanilson (assist James Hill): — no commentary line — · before: 18' Corner, Bournemouth. Conceded by Neco Williams. ‹ 17' Foul by Neco Williams (Nottingham Forest). ‹ 17' Adam Smith (Bournemouth) wins a free kick in the defensive half.
- GW11 AG v Bournemouth 45+3' Justin Kluivert (assist Marcus Tavernier): — no commentary line — · before: 45+1' Attempt missed. Marcus Tavernier (Bournemouth) left footed shot from outside the box is c ‹ 45+1' Justin Kluivert (Bournemouth) wins a free kick in the attacking half. ‹ 45+1' Foul by Nikola Milenkovic (Nottingham Forest).

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW6 A v Crystal Palace 41' Daichi Kamada: no structured culprit — reports only
- GW6 A v Crystal Palace 45' Jefferson Lerma: no structured culprit — reports only
- GW6 A v Crystal Palace 59' Yéremy Pino: no structured culprit — reports only
- GW7 H v Arsenal 80' Noni Madueke: no structured culprit — reports only
  · GW7 other flags: Ousmane Diomande lastManTackle 1
- GW8 A v Ipswich Town 41' Julio Enciso: Nikola Milenković error leading to the goal [CONFIRMED — SofaScore error flag]
- GW9 A v Brentford 30' Nikola Milenković [OG]: Nikola Milenković own goal [CONFIRMED — SofaScore]
- GW9 A v Brentford 76' Igor Thiago: no structured culprit — reports only
- GW10 H v Manchester City 52' Rayan Cherki: no structured culprit — reports only
  · GW10 other flags: Jair clearanceOffLine 1
- GW11 A v Bournemouth 19' Evanilson: no structured culprit — reports only
- GW11 A v Bournemouth 45' Justin Kluivert: no structured culprit — reports only
  · GW11 error leading to a goal (SofaScore, match level — 2 conceded, the goal is not identified): James McAtee [CONFIRMED — SofaScore error flag]
  · GW11 other flags: Daniel Muñoz errorLeadToAShot 2; Murillo errorLeadToAShot 1

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 100 | 12.96 | 5 | 59 | 6.44 | 7 |
| corner | 19 | 1.20 | 0 | 11 | 2.21 | 2 |
| set piece | 12 | 0.56 | 0 | 7 | 0.27 | 0 |
| direct FK | 5 | 0.33 | 0 | 5 | 0.30 | 1 |
| penalty | 1 | 0.76 | 1 | 0 | 0.00 | 0 |
Totals per match: xG 1.98 (npxG 1.88) for, xGA 1.15 (np 1.15) against · dead-ball share of xG 18% for, 30% against · penalties won 1, conceded 0 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 19 shots, xG 1.20, 0 goals, headed 9: penalty area, central 11 shots, xG 0.82, 0 goals; 6-yard box, central 3 shots, xG 0.23, 0 goals; penalty area, right 2 shots, xG 0.08, 0 goals · against — 11 shots conceded, xG 2.21, 2 goals, headed 9: 6-yard box, central 4 shots, xG 1.55, 1 goals; penalty area, central 5 shots, xG 0.57, 1 goals; 6-yard box, left 1 shots, xG 0.05, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 34 · corner shots conceded 11 (headed 9), xG 2.21, goals 2 · xG per corner faced 0.065 (rank 4 of 20, 1 = weakest) · weak zone: six-yard box (1.60 xG, 72% of theirs v 65% league) · signal: **WEAK — positive pairing for opposing aerial targets** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–11 [CONFIRMED — LiveScore Block L, 45 corners; side L/R as LiveScore records it; foot from SofaScore]: James McAtee 20 (0L/20R, 1 short, left foot); Neco Williams 19 (19L/0R, right foot); Luca Netz 2 (0L/2R, left foot); Xaver Schlager 2 (0L/2R, left foot). First contact on corners that ended in a shot (Understat) — for: Murillo 8 (4 headed), Xaver Schlager 4, Ousmane Diomande 2 (1 headed), Nikola Milenkovic 1 (1 headed), Igor Jesus 1 (1 headed) · against (who beat them): Jefferson Lerma 2 (2 headed) — 1 goal, Jan Paul van Hecke 2 (1 headed), Gabriel 2 (1 headed), Alexander Isak 1 (1 headed), Micky van de Ven 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 39.0 (rank 13 of 20, 1 = highest line) · block length 23.4 (rank 18, 1 = most compact) · width 62.2. Per match: GW6 A v Crystal Palace 3-4-2-1: back line 43, front 68, length 26, width 66 (57% poss); GW7 H v Arsenal 3-4-2-1: back line 35, front 66, length 30, width 64 (26% poss); GW8 A v Ipswich Town 3-4-2-1: back line 41, front 64, length 23, width 70 (51% poss); GW9 A v Brentford 3-4-2-1: back line 43, front 68, length 24, width 60 (58% poss); GW10 H v Manchester City 3-4-2-1: back line 32, front 59, length 28, width 55 (22% poss); GW11 A v Bournemouth 3-4-2-1: back line 41, front 64, length 23, width 62 (49% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 3 league match(es) v LB-coded sides — xG 2.24/match and 0.3 pts/match v 1.37 and 1.0 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW5 H v Coventry City 0–1, xG 1.10, box shots 12, poss 62%; GW6 A v Crystal Palace 1–3, xG 3.34, box shots 16, poss 57%; GW8 A v Ipswich Town 1–1, xG 2.29, box shots 15, poss 51%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Williams 6, McAtee 5, Delap 1** · FPL editorial order: McAtee #1, N.Williams #2, Gibbs-White #3
- Direct free-kick shooters: **Gibbs-White 2, McAtee 2, Williams 1** · FPL order: Gibbs-White #1, Murillo #2, N.Williams #3
- Penalties taken: **Gibbs-White 1** · FPL order: Gibbs-White #1, Wood #2, Delap #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Gibbs-White 6, Aina 1, Murillo 1**
- Corner targets (headed shots from corners): **Murillo 4, Milenkovic 1, Jesus 1, Diomande 1** · corner shots 19
- **DISAGREEMENT:** observed corner taker Neco Williams (6) v FPL #1 McAtee — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Morgan Gibbs-White 5 (0.50/90, percentile 91, 900 min); James McAtee 5 (0.49/90, percentile 91, 910 min); Igor Jesus 1 (0.30/90, percentile 79, 304 min) · club total 19 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 334 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 10.19, field tilt 56.4, possession 55.8%, box entries 12, direct speed 3.11, SCA 23; GW2: PPDA 20.04, field tilt 27.2, possession 31.7%, box entries 10, direct speed 4.01, SCA 24; GW3: PPDA 7.26, field tilt 41.6, possession 41.5%, box entries 6, direct speed 3.26, SCA 24; GW4: PPDA 8.85, field tilt 49.4, possession 46.6%, box entries 14, direct speed 2.86, SCA 44; GW5: PPDA 9.38, field tilt 73.6, possession 62.6%, box entries 17, direct speed 2.14, SCA 47; GW6: PPDA 9.47, field tilt 62.1, possession 56.5%, box entries 21, direct speed 2.37, SCA 42; GW7: PPDA 18.4, field tilt 23.7, possession 26.7%, box entries 6, direct speed 2.61, SCA 28; GW8: PPDA 12.16, field tilt 53.5, possession 50.6%, box entries 8, direct speed 2.67, SCA 33; GW9: PPDA 7.68, field tilt 69.6, possession 58.7%, box entries 10, direct speed 2.06, SCA 26; GW10: PPDA 14.3, field tilt 25.6, possession 22.5%, box entries 9, direct speed 4.65, SCA 17

**Zone 14 (C13, SofaScore heat-map points, 11 league matches):** for 32.9/match (rank 6 of 20) · conceded 26.4/match (rank 15 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 7.1/match · allowed 4.9/match · PPDA 13.2. Per match for/allowed: GW3 6/3; GW4 9/8; GW5 9/2; GW6 9/6; GW7 6/10; GW8 6/4 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 3-4-2-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: Matz Sels (16, 3/3)
- DEF: Murillo (16, 3/3), Jair (14, 3/3), Nikola Milenković (12, 3/3)
- MID: James McAtee (16, 3/3), Neco Williams (16, 3/3), Xaver Schlager (13, 2/3), Ola Aina (7, 1/3), Ryan Yates (6, 2/3)
- FWD: Morgan Gibbs-White (15, 3/3)
- Contested slots: D Nikola Milenković 12 v Daniel Muñoz 11; F Morgan Gibbs-White 15 v Liam Delap 15 · Excluded (FPL flag): Nicolás Domínguez — Muscular injury - Expected back 30 Dec
- Absent last match (E12, SofaScore list): Odoi (Groin Injury), Domínguez (Knock Injury)
- Substitutions this season (C3): GW9 65' Liam Delap→Chris Wood CHASING; GW9 46' Xaver Schlager→Ryan Yates HALF-TIME; GW9 46' Ola Aina→Daniel Muñoz HALF-TIME; GW10 87' Liam Delap→Igor Jesus LATE; GW10 79' Ryan Yates→Ibrahim Sangaré GAME-STATE; GW10 65' Daniel Muñoz→Luca Netz TACTICAL; GW10 65' James McAtee→Dan Ndoye CARD-RISK; GW11 82' Daniel Muñoz→Ola Aina CARD-RISK; GW11 72' Neco Williams→Luca Netz CHASING; GW11 72' James McAtee→Chris Wood CHASING; GW11 46' Ryan Yates→Xaver Schlager HALF-TIME; GW11 46' Dan Ndoye→Igor Jesus HALF-TIME

### First-choice players and absences (F14) — generated 2026-11-24 07:45 UTC
First choice = starter baseline (GK, 3 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Matz Sels | start weight 16 | OK | a | — | — |
| CB | Murillo | start weight 16 | OK | a 100% | Ousmane Diomande | — |
| CB | Jair | start weight 14 | OK | a 100% | Ousmane Diomande | — |
| CB | Nikola Milenković | start weight 12 | OK | a 100% | Ousmane Diomande | — |
| xGI #1 | Morgan Gibbs-White | xGI 5.37 | OK | a 100% | Dan Ndoye | — |
| xGI #2 | Liam Delap | xGI 3.76 | OK | a | Dan Ndoye | — |
| Penalties #1 (FPL) | Gibbs-White | FPL order | OK | a 100% | Wood | — |
| Direct FK #1 (FPL) | Gibbs-White | FPL order | OK | a 100% | Murillo | — |
| Corners (observed) | James McAtee | 20 corners taken | OK | a | Neco Williams | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Leeds United: Liam Delap (not signed yet) · GW2 A Liverpool FC: Liam Delap (did not start) · GW3 H Tottenham Hotspur: all started · GW4 A Aston Villa: Jair (did not start), Nikola Milenković (did not start) · GW5 H Coventry City: Nikola Milenković (Hamstring Injury) · GW6 A Crystal Palace: Jair (did not start), Nikola Milenković (did not start) · GW7 H Arsenal: Nikola Milenković (did not start), Morgan Gibbs-White (Knock Injury) · GW8 A Ipswich Town: all started · GW9 A Brentford: all started · GW10 H Manchester City: all started · GW11 A Bournemouth: all started

### Next fixtures (all competitions)
- Fri 27 Nov 20:00 UTC · Premier League R12 · H v Chelsea
- Wed 02 Dec 19:30 UTC · Premier League R13 · A v Hull City
- Sat 05 Dec 17:30 UTC · Premier League R14 · H v Brighton & Hove Albion
- Sun 13 Dec 14:00 UTC · Premier League R15 · A v Sunderland
- Sun 20 Dec 14:00 UTC · Premier League R16 · H v Everton
- Sun 27 Dec 16:30 UTC · Premier League R17 · A v Manchester United

### FPL availability flags (players with league minutes this season)
Hudson-Odoi — Unspecified injury - Unknown return date (0%); Dominguez — Muscular injury - Expected back 30 Dec (0%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 H Leeds United 0–1 · xG 0.66–0.47 · poss 56% · 3-4-2-1 · scorers: none
- GW2 A Liverpool FC 2–2 · xG 2.30–1.75 · poss 31% · 3-4-2-1 · scorers: Dan Ndoye 24', Morgan Gibbs-White 70'
- GW3 H Tottenham Hotspur 0–0 · xG 0.92–1.06 · poss 41% · 3-4-2-1 · scorers: none
- GW4 A Aston Villa 2–1 · xG 2.28–0.82 · poss 46% · 3-4-2-1 · scorers: Liam Delap 46', Igor Jesus 88'
- GW5 H Coventry City 0–1 · xG 1.10–0.67 · poss 62% · 3-4-2-1 · scorers: none
- GW6 A Crystal Palace 1–3 · xG 3.34–2.41 · poss 57% · 3-4-2-1 · scorers: Dan Ndoye 3'
- GW7 H Arsenal 0–1 · xG 0.90–1.14 · poss 26% · 3-4-2-1 · scorers: none
- GW8 A Ipswich Town 1–1 · xG 2.29–0.46 · poss 51% · 3-4-2-1 · scorers: Neco Williams 13'
- GW9 A Brentford 0–2 · xG 0.86–0.46 · poss 58% · 3-4-2-1 · scorers: none
- GW10 H Manchester City 3–1 · xG 1.06–1.76 · poss 22% · 3-4-2-1 · scorers: Jair 6', Liam Delap 18', Liam Delap 73'
- GW11 A Bournemouth 0–2 · xG 1.99–2.89 · poss 49% · 3-4-2-1 · scorers: none
### Corner takers observed (LiveScore Block L)
- James McAtee: 20 corners (0 left, 20 right, 1 short)
- Neco Williams: 19 corners (19 left, 0 right)
- Luca Netz: 2 corners (0 left, 2 right)
- Xaver Schlager: 2 corners (0 left, 2 right)
- Nicolas Dominguez: 1 corners (1 left, 0 right)
- Morgan Gibbs-White: 1 corners (1 left, 0 right)
