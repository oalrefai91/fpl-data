# Leeds United — data doc
*Feeder-written (2026-11-10 07:41 UTC); do not edit. Narrative: `profiles/teams/leeds.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-10 07:41 UTC)
**Manager:** Daniel Farke · **Venue:** Elland Road · **SofaScore:** https://www.sofascore.com/football/team/leeds-united/34 · **FPL code:** LEE
**Table:** 9th, 14 pts (3W 5D 2L, GF 10 GA 8) · Home 7th (2-3-0, 7:3) · Away 11th (1-2-2, 3:5)
**Standing context (F15):** 28 league games left · points v 4th -4, v 5th -2, v 17th (last safe) +5, v 18th +6 · goal difference +2
**Suspension watch (D7, all players of the club):** Bogle — 🟨 2 from a ban (3/5); Ampadu — 🟨 **ONE FROM A BAN** (4/5 before GW19); Calvert-Lewin — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 10 league matches):** goals after 75′ — for 3/10 (30%), against 2/8 (25%) · scored first 5, conceded first 3 (30% of matches), goalless 2 · points from losing positions 2 of 12 (4 matches behind at some point) · points from winning positions 10 of 15 (5 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Muharemović (DEF) 11.2/90, hit 7/10; Ampadu (MID) 11.4/90, hit 4/10; Stach (MID) 10.0/90, hit 3/9; Elvedi (DEF) 8.5/90, hit 3/8; Justin (DEF) 8.0/90, hit 3/10; Bijol (DEF) 13.6/90, hit 2/5
**Manager tenure (F13, SofaScore):** Daniel Farke since 04 Jul 2023 · 158 matches in charge, all competitions (79W 43D 36L) · 10 league matches this season · contract to 30 Jun 2027 · previous club Borussia M'gladbach · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Manchester United — last 4: Oct 2026 Premier League Leeds United 1–1 Manchester United (yellows 2–2, xG 1.41–0.92); Apr 2026 Premier League Manchester United 1–2 Leeds United (yellows 3–2, reds 1–0, xG 1.27–2.57); Jan 2026 Premier League Leeds United 1–1 Manchester United (yellows 0–1, xG 0.90–1.59); Feb 2023 Premier League Leeds United 0–2 Manchester United (yellows 2–1, xG 1.81–1.12) · 13 yellows in 4 | v Nottingham Forest — last 4: Aug 2026 EFL Cup Nottingham Forest 0–2 Leeds United (yellows 4–3, xG 1.21–2.58); Aug 2026 Premier League Nottingham Forest 0–1 Leeds United (yellows 2–1, xG 0.66–0.47); Feb 2026 Premier League Leeds United 3–1 Nottingham Forest (yellows 1–1, xG 2.50–1.33); Nov 2025 Premier League Nottingham Forest 3–1 Leeds United (yellows 2–1, xG 2.55–0.74) · 15 yellows in 4
**Archetype (F5):** used **HP** — derived HP [DERIVED] · signals, last 6 league matches: possession 49.7%, PPDA 7.8 (Understat, 4 matches; lower = harder press), opponent offsides forced 2.7/match (line height), fast breaks 0.5/match (season), both sides' xG 2.32/match (openness) · note: computed from 4 of 6 GWs (no PPDA/possession for GW9, GW10). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 13 (permanent 5, loan 2, free 0, loan returns 6) · out 14 · flags: Joël Piroe: still in an FPL set-piece order — use #2 or observation — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 10 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 13.18 | 16 | Big chances against | 20 | 6 |
| xGOT | 12.72 | 11 | Box shots against | 74 | 5 |
| xA | 6.03 | 18 | Corners against | 41 | 5 |
| Shots | 120 | 15 | Crosses faced | 191 | 15 |
| SoT | 37 | 13 | Dribbled past | 66 | 5 |
| Big chances | 21 | 15 | Errors→shot | 4 | 3 |
| Shots in box | 78 | 14 | GK goals prevented | 4.36 | 1 |
| Corners | 43 | 12 | Clearances | 311 | 3 |
| Crosses | 204 | 4 | Tackles | 165 | 9 |
| Fast breaks | 5 | 19 | Interceptions | 95 | 8 |
| FK shots | 6 | 3 | Def. contributions | 608 | 3 |
| Possession % | 47.20 | 12 | Aerial % | 52.63 | 5 |
| Pass % | 78.32 | 15 | Duel % | 52.50 | 4 |
| Long balls | 327 | 8 | Fouls | 129 | 16 |
| Dribbles | 73 | 9 | Yellows | 19 | 7 |
| Shots against | 132 | 10 | Km covered | 1173 | 4 |
| SoT against | 43 | 11 | Sprints | 1162 | 6 |
Per match: xG 1.32 · xGOT 1.27 · shots 12.0 · shots against 13.2 · big chances 2.1 for / 2.0 against · corners 4.3 / 4.1 · crosses 20.4 / 19.1 · possession 47.2%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | H | Crystal Palace | 0–0 | 1.31/1.09 | 1.06/1.13 | 51 | 13/12 | 2/4 | 9/4 | 6/3 | 1/2 | 4/3 | 17/4 v 10/1 | 2/2 |
| 6 | A | Arsenal | 1–2 | 0.62/1.20 | 2.33/2.32 | 42 | 11/13 | 5/6 | 7/8 | 3/3 | 2/4 | 4/2 | 23/6 v 15/7 | 7/4 |
| 7 | H | Manchester United | 1–1 | 1.41/1.43 | 0.92/1.08 | 61 | 12/13 | 5/3 | 10/6 | 1/6 | 2/2 | 2/3 | 29/4 v 10/2 | 3/2 |
| 8 | A | Sunderland | 0–0 | 0.76/1.07 | 0.83/1.03 | 50 | 11/15 | 4/4 | 7/8 | 3/7 | 2/1 | 5/4 | 22/6 v 20/3 | 3/0 |
| 9 | A | Bournemouth | 0–2 | 0.71/— | 1.29/— | 56 | 10/11 | 1/5 | 3/5 | 2/3 | 1/2 | 4/4 | 21/5 v 10/2 | 0/1 |
| 10 | H | Tottenham Hotspur | 1–0 | 1.96/— | 0.72/— | 38 | 16/7 | 4/4 | 11/5 | 4/0 | 4/1 | 6/4 | 30/5 v 24/6 | 1/2 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | H | Crystal Palace | 0–0 | 3-4-2-1 | 10/12 | 2/3 | 0/0 | 424/424 | 58/55 | Wilson (Muscle Injury), Rodon (Hamstring Injury), Joseph (Knee Injury) | Disasi (ban (red)), Riad (Knee Injury), Henderson (Foot Injury), Mateta (Hamstring Injury) | Adam Herczeg |
| 6 | A | Arsenal | 1–2 | 3-4-2-1 | 20/12 | 4/1 | 0/0 | 356/512 | 54/54 | Rodon (Hamstring Injury), Joseph (Knee Injury), James (Back Injury; doubtful) | Tzolis (Hamstring Injury), Saliba (Back Injury) | Paul Tierney |
| 7 | H | Manchester United | 1–1 | 3-4-2-1 | 16/5 | 2/2 | 0/0 | 532/354 | 73/59 | Rodon (Hamstring Injury), Joseph (Knee Injury), James (Back Injury; doubtful) | Šeško (Shin Injury), Ugarte (Cruciate Ligament Injury), Dorgu (Hamstring Injury), Heaton (Abdominal Injury), Mainoo (Knock Injury; doubtful), Shaw (Knock Injury; doubtful) | Darren England |
| 8 | A | Sunderland | 0–0 | 3-4-2-1 | 14/10 | 2/1 | 0/0 | 368/379 | 68/65 | Rodon (Hamstring Injury), Joseph (Knee Injury) | Danso (ban (red)), Mundle (Knee Injury), Meunier (Hamstring Injury; doubtful) | Stuart Attwell |
| 9 | A | Bournemouth | 0–2 | 3-4-2-1 | 15/12 | 2/2 | 0/0 | 520/420 | 64/63 | Joseph (Knee Injury) | Scott (Muscle Injury), Tóth (Hamstring Injury), Araujo (Thigh Injury) | Michael Salisbury |
| 10 | H | Tottenham Hotspur | 1–0 | 3-4-2-1 | 11/16 | 2/3 | 0/0 | 311/531 | 54/61 | Joseph (Knee Injury), Stach (Foot Injury; doubtful) | Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Sávio (Muscle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | John Brooks |
Per match: fouls 12.9 / 12.1 · yellows 1.90 / 2.30 · reds 0 / 0 (season) · offsides forced 2.6, committed 2.0 · crosses attempted 20.4 / faced 19.1. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 1.64 for / 1.05 against per match · Away (5): xG 1.01 / 1.46. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW10 H v Tottenham Hotspur 1–0 (Sat 07 Nov 12:30 UTC) — formation 3-4-2-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| James Trafford | G | 90 | 8.7 | 0.00 | 0.00 | 0 | 0 | 5 | 0 | 44 |
| James Justin | D | 90 | 7.2 | 0.00 | 0.11 | 0 | 0 | 10 | 2 | 56 |
| Nico Elvedi | D | 90 | 7.4 | 0.27 | 0.01 | 0 | 1 | 14 | 0 | 48 |
| Tarik Muharemović | D | 90 | 7.8 | 0.00 | 0.01 | 0 | 0 | 14 | 0 | 70 |
| Jayden Bogle | M | 89 | 6.9 | 0.11 | 0.21 | 3 | 3 | 1 | 6 | 44 |
| Ethan Ampadu | M | 90 | 7 | 0.14 | 0.03 | 1 | 3 | 5 | 0 | 58 |
| Ao Tanaka | M | 77 | 6.8 | 0.33 | 0.01 | 0 | 2 | 8 | 2 | 46 |
| Gabriel Gudmundsson | M | 45 | 7.2 | 0.00 | 0.05 | 0 | 0 | 5 | 5 | 35 |
| Sean Longstaff | F | 89 | 6.9 | 0.08 | 0.15 | 2 | 1 | 5 | 9 | 44 |
| Lukas Nmecha | F | 77 | 6.9 | 0.16 | 0.03 | 1 | 2 | 1 | 2 | 22 |
| Dominic Calvert-Lewin | F | 90 | 6.8 | 0.34 | 0.24 | 2 | 3 | 0 | 0 | 30 |
Subs used: Melvin Bard (45'), Harry Wilson (13'), Noah Okafor (13'), Joe Rodon (1'), Ilia Gruev (1')
Goals: 79' Noah Okafor [own]
Substitutions (own): 46' Melvin Bard for Gabriel Gudmundsson; 77' Noah Okafor for Lukas Nmecha; 77' Harry Wilson for Ao Tanaka; 90' Ilia Gruev for Sean Longstaff; 90' Joe Rodon for Jayden Bogle
Cards: manager/staff booking: Roberto De Zerbi 51' [LiveScore] (opp; no FPL effect); 15' Micky van de Ven (yellow, opp); 22' Sean Longstaff (yellow, own); 51' Pedro Porro (yellow, opp); 80' Noah Okafor (yellow, own); 88' Sandro Tonali (yellow, opp)
**Baseline XI change vs GW9 (3-4-2-1 → 3-4-2-1):** in — Lukas Nmecha, Sean Longstaff; out — Daniel James, Harry Wilson.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 6 | A Arsenal | 55' | FOR | James Justin | Gabriel Gudmundsson | open play | 0.25 |
| 6 | A Arsenal | 62' | AGAINST | Riccardo Calafiori | Ben White | open play | 0.58 |
| 6 | A Arsenal | 70' | AGAINST | Bruno Guimarães | Declan Rice | open play | 0.06 |
| 7 | H Manchester United | 35' | AGAINST | Bryan Mbeumo | Youri Tielemans | open play | 0.41 |
| 7 | H Manchester United | 51' | FOR | Dominic Calvert-Lewin | Tarik Muharemović | corner | 0.56 |
| 9 | A Bournemouth | 31' | AGAINST | Evanilson | Justin Kluivert | [no Understat] | — |
| 9 | A Bournemouth | 90' | AGAINST | Amine Adli | Eli Junior Kroupi | [no Understat] | — |
| 10 | H Tottenham Hotspur | 79' | FOR | Noah Okafor | — | [no Understat] | — |
Scored 10: open play 5, corner 2, direct FK 1, own goal 1, [no Understat] 1 · Conceded 8: open play 5, [no Understat] 2, corner 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW9 AG v Bournemouth 31' Evanilson (assist Justin Kluivert): — no commentary line — · before: 30' Evanilson (Bournemouth) wins a free kick in the defensive half. ‹ 30' Foul by Daniel James (Leeds United). ‹ 29' Foul by James Hill (Bournemouth).
- GW9 AG v Bournemouth 90+4' Amine Adli (assist Junior Kroupi): — no commentary line — · before: 90+3' Amine Adli (Bournemouth) wins a free kick in the defensive half. ‹ 90+3' Foul by Jean-Mattéo Bahoya (Leeds United). ‹ 90+1' Attempt saved. Álvaro Rodríguez (Bournemouth) left footed shot from outside the box is sa
- GW10 FOR v Tottenham Hotspur 79' Noah Okafor: G O O O O O A A L - Noah Okafor finds the net with the right foot! · before: 79' Rodrigo Bentancur relieves the pressure with a clearance ‹ 78' Safe hands from Antonin Kinsky as he comes out and claims the ball ‹ 78' Rodrigo Bentancur from Tottenham intercepts a cross aimed towards the box.

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW6 A v Arsenal 62' Riccardo Calafiori: no structured culprit — reports only
- GW6 A v Arsenal 70' Bruno Guimarães: no structured culprit — reports only
  · GW6 other flags: Nico Elvedi lastManTackle 1; Ao Tanaka errorLeadToAShot 1; James Trafford errorLeadToAShot 1
- GW7 H v Manchester United 35' Bryan Mbeumo: no structured culprit — reports only
- GW9 A v Bournemouth 31' Evanilson: no structured culprit — reports only
- GW9 A v Bournemouth 90' Amine Adli: no structured culprit — reports only
  · GW9 error leading to a goal (SofaScore, match level — 2 conceded, the goal is not identified): Sean Longstaff, James Trafford [CONFIRMED — SofaScore error flag]

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 71 | 8.03 | 5 | 87 | 8.42 | 5 |
| corner | 15 | 3.09 | 2 | 15 | 1.39 | 1 |
| set piece | 5 | 0.45 | 0 | 10 | 0.98 | 0 |
| direct FK | 4 | 0.19 | 1 | 3 | 0.23 | 0 |
Totals per match: xG 1.47 (npxG 1.47) for, xGA 1.38 (np 1.38) against · dead-ball share of xG 32% for, 24% against · penalties won 0, conceded 0 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 15 shots, xG 3.09, 2 goals, headed 5: 6-yard box, central 2 shots, xG 1.51, 1 goals; penalty area, central 7 shots, xG 1.36, 1 goals; penalty area, right 3 shots, xG 0.15, 0 goals · against — 15 shots conceded, xG 1.39, 1 goals, headed 8: penalty area, central 8 shots, xG 0.75, 0 goals; 6-yard box, central 3 shots, xG 0.50, 1 goals; penalty area, right 2 shots, xG 0.09, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 33 · corner shots conceded 15 (headed 8), xG 1.39, goals 1 · xG per corner faced 0.042 (rank 14 of 20, 1 = weakest) · weak zone: penalty-spot band (0.83 xG, 60% of theirs v 26% league) · signal: **neutral** [DERIVED] · scheme: **ZONAL** — beaten by an out-swinger to the six-yard channel `[CONFIRMED]` (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–10 [CONFIRMED — LiveScore Block L, 39 corners; side L/R as LiveScore records it; foot from SofaScore]: Anton Stach 26 (17L/9R, both foot); Harry Wilson 6 (1L/5R, left foot); Sean Longstaff 6 (6L/0R, right foot); Daniel James 1 (1L/0R, 1 short, right foot). First contact on corners that ended in a shot (Understat) — for: Tarik Muharemovic 3 (3 headed), Jayden Bogle 3 — 1 goal, Dominic Calvert-Lewin 2 (1 headed) — 1 goal, Ao Tanaka 2, Noah Okafor 2 · against (who beat them): Nathan Collins 2 (2 headed), Luke O&#039;Nien 2 (1 headed), Nikola Milenkovic 1 (1 headed), Igor Jesus 1 (1 headed), Thiago 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 38.4 (rank 18 of 20, 1 = highest line) · block length 22.4 (rank 14, 1 = most compact) · width 67.0. Per match: GW5 H v Crystal Palace 3-4-2-1: back line 41, front 57, length 16, width 71 (51% poss); GW6 A v Arsenal 3-4-2-1: back line 38, front 58, length 21, width 69 (42% poss); GW7 H v Manchester United 3-4-2-1: back line 41, front 66, length 25, width 67 (61% poss); GW8 A v Sunderland 3-4-2-1: back line 38, front 63, length 25, width 69 (50% poss); GW9 A v Bournemouth 3-4-2-1: back line 37, front 59, length 22, width 70 (56% poss); GW10 H v Tottenham Hotspur 3-4-2-1: back line 39, front 69, length 30, width 69 (38% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 2 league match(es) v LB-coded sides — xG 1.04/match and 1.0 pts/match v 1.40 and 1.5 against the rest → **struggles — chance creation drops** (threshold: xG v LB at least 90% of the rest). GW5 H v Crystal Palace 0–0, xG 1.31, box shots 9, poss 51%; GW8 A v Sunderland 0–0, xG 0.76, box shots 7, poss 50%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Stach 5, Elvedi 1, Tanaka 1** · FPL editorial order: Stach #1, Wilson #2, Longstaff #3
- Direct free-kick shooters: **Stach 4** · FPL order: Stach #1, Wilson #2, Longstaff #3
- Penalties taken: **—** · FPL order: Calvert-Lewin #1, Nmecha #2, Piroe #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Stach 2, Wilson 1**
- Corner targets (headed shots from corners): **Muharemovic 3, Calvert-Lewin 1, Justin 1** · corner shots 15

**Through-ball suppliers (Block P, PL/Opta, season):** Anton Stach 2 (0.27/90, percentile 77, 677 min) · club total 8 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 318 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 6.83, field tilt 43.6, possession 44.2%, box entries 5, direct speed 2.49, SCA 20; GW2: PPDA 11.73, field tilt 41.1, possession 47.1%, box entries 7, direct speed 2.56, SCA 24; GW3: PPDA 11.61, field tilt 33.9, possession 33.7%, box entries 7, direct speed 2.89, SCA 18; GW4: PPDA 11.54, field tilt 46.8, possession 50.6%, box entries 14, direct speed 2.29, SCA 28; GW5: PPDA 9, field tilt 40.1, possession 50.9%, box entries 6, direct speed 2.29, SCA 21; GW6: PPDA 10.03, field tilt 29.2, possession 41.8%, box entries 6, direct speed 2.72, SCA 18; GW7: PPDA 7.91, field tilt 59.9, possession 61.1%, box entries 7, direct speed 2.15, SCA 24; GW8: PPDA 8.33, field tilt 50.2, possession 49.3%, box entries 8, direct speed 2.43, SCA 20; GW9: PPDA 9.67, field tilt 55.8, possession 56.4%, box entries 9, direct speed 2.29, SCA 18; GW10: PPDA 9.55, field tilt 40, possession 39.4%, box entries 10, direct speed 3.05, SCA 30

**Zone 14 (C13, SofaScore heat-map points, 10 league matches):** for 28.1/match (rank 9 of 20) · conceded 31.3/match (rank 8 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 3.9/match · allowed 5.8/match · PPDA 9.0. Per match for/allowed: GW3 8/6; GW4 9/5; GW5 0/4; GW6 1/11; GW7 5/4; GW8 5/5 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 3-4-2-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: James Trafford (16, 3/3)
- DEF: Tarik Muharemović (16, 3/3), Nico Elvedi (11, 2/3), Jaka Bijol (5, 1/3)
- MID: James Justin (16, 3/3), Jayden Bogle (16, 3/3), Ethan Ampadu (16, 3/3), Ao Tanaka (14, 3/3), Sean Longstaff (3, 1/3)
- FWD: Dominic Calvert-Lewin (16, 3/3)
- Contested slots: none · Excluded (FPL flag): Gabriel Gudmundsson — Hamstring injury - 75% chance of playing; Anton Stach — Foot injury - 50% chance of playing
- Absent last match (E12, SofaScore list): Joseph (Knee Injury), Stach (Foot Injury; doubtful)
- Substitutions this season (C3): GW8 66' Harry Wilson→Anton Stach TACTICAL; GW8 65' Brenden Aaronson→Noah Okafor TACTICAL; GW9 84' Harry Wilson→Brenden Aaronson CHASING; GW9 84' James Justin→Jean-Mattéo Bahoya CHASING; GW9 65' Daniel James→Lukas Nmecha CHASING; GW9 65' Ao Tanaka→Anton Stach CHASING; GW9 65' Gabriel Gudmundsson→Sean Longstaff CHASING; GW10 90' Sean Longstaff→Ilia Gruev CARD-RISK; GW10 90' Jayden Bogle→Joe Rodon LATE; GW10 77' Lukas Nmecha→Noah Okafor TACTICAL; GW10 77' Ao Tanaka→Harry Wilson TACTICAL; GW10 46' Gabriel Gudmundsson→Melvin Bard HALF-TIME

### First-choice players and absences (F14) — generated 2026-11-10 07:41 UTC
First choice = starter baseline (GK, 3 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | James Trafford | start weight 16 | OK | a | — | — |
| CB | Tarik Muharemović | start weight 16 | OK | a | Joe Rodon | — |
| CB | Nico Elvedi | start weight 11 | OK | a 100% | Joe Rodon | — |
| CB | Jaka Bijol | start weight 5 | OK | a | Joe Rodon | — |
| xGI #1 | Dominic Calvert-Lewin | xGI 4.64 | OK | a 100% | Anton Stach | — |
| xGI #2 | Jayden Bogle | xGI 2.58 | OK | a | Anton Stach | — |
| Penalties #1 (FPL) | Calvert-Lewin | FPL order | OK | a 100% | Nmecha | — |
| Direct FK #1 (FPL) | Stach | FPL order | DOUBT | d 50% — Foot injury - 50% chance of playing | Wilson | — |
| Corners (observed) | Anton Stach | 26 corners taken | DOUBT | d 50% — Foot injury - 50% chance of playing | Harry Wilson | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 A Nottingham Forest: Nico Elvedi (did not start) · GW2 H Brentford: Nico Elvedi (did not start) · GW3 A Brighton & Hove Albion: Jaka Bijol (did not start) · GW4 H Newcastle United: Jaka Bijol (did not start) · GW5 H Crystal Palace: Jaka Bijol (did not start) · GW6 A Arsenal: Jaka Bijol (did not start) · GW7 H Manchester United: Jaka Bijol (did not start) · GW8 A Sunderland: Nico Elvedi (did not start) · GW9 A Bournemouth: Jaka Bijol (did not start) · GW10 H Tottenham Hotspur: Jaka Bijol (did not start)

### Next fixtures (all competitions)
- Sat 21 Nov 15:00 UTC · Premier League R11 · A v Chelsea
- Sat 28 Nov 15:00 UTC · Premier League R12 · H v Coventry City
- Wed 02 Dec 19:30 UTC · Premier League R13 · A v Manchester City
- Sat 05 Dec 15:00 UTC · Premier League R14 · H v Ipswich Town
- Sat 12 Dec 15:00 UTC · Premier League R15 · A v Liverpool FC
- Sat 19 Dec 15:00 UTC · Premier League R16 · H v Fulham

### FPL availability flags (players with league minutes this season)
Gudmundsson — Hamstring injury - 75% chance of playing (75%); Stach — Foot injury - 50% chance of playing (50%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 A Nottingham Forest 1–0 · xG 0.47–0.66 · poss 44% · 3-4-2-1 · scorers: Anton Stach 88'
- GW2 H Brentford 1–1 · xG 1.46–1.67 · poss 47% · 3-4-2-1 · scorers: Dominic Calvert-Lewin 79'
- GW3 A Brighton & Hove Albion 1–1 · xG 2.49–2.19 · poss 33% · 3-5-2 · scorers: Jayden Bogle 15'
- GW4 H Newcastle United 4–1 · xG 2.08–0.88 · poss 50% · 3-5-2 · scorers: Lewis Miley 32', Jayden Bogle 34', Dominic Calvert-Lewin 45', Noah Okafor 59'
- GW5 H Crystal Palace 0–0 · xG 1.31–1.06 · poss 51% · 3-4-2-1 · scorers: none
- GW6 A Arsenal 1–2 · xG 0.62–2.33 · poss 42% · 3-4-2-1 · scorers: James Justin 55'
- GW7 H Manchester United 1–1 · xG 1.41–0.92 · poss 61% · 3-4-2-1 · scorers: Dominic Calvert-Lewin 51'
- GW8 A Sunderland 0–0 · xG 0.76–0.83 · poss 50% · 3-4-2-1 · scorers: none
- GW9 A Bournemouth 0–2 · xG 0.71–1.29 · poss 56% · 3-4-2-1 · scorers: none
- GW10 H Tottenham Hotspur 1–0 · xG 1.96–0.72 · poss 38% · 3-4-2-1 · scorers: Noah Okafor 79'
### Corner takers observed (LiveScore Block L)
- Anton Stach: 26 corners (17 left, 9 right)
- Harry Wilson: 6 corners (1 left, 5 right)
- Sean Longstaff: 6 corners (6 left, 0 right)
- Daniel James: 1 corners (1 left, 0 right, 1 short)
