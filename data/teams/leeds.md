# Leeds United — data doc
*Feeder-written (2026-10-27 07:42 UTC); do not edit. Narrative: `profiles/teams/leeds.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-10-27 07:42 UTC)
**Manager:** Daniel Farke · **Venue:** Elland Road · **SofaScore:** https://www.sofascore.com/football/team/leeds-united/34 · **FPL code:** LEE
**Table:** 7th, 11 pts (2W 5D 1L, GF 9 GA 6) · Home 8th (1-3-0, 6:3) · Away 8th (1-2-1, 3:3)
**Standing context (F15):** 30 league games left · points v 4th -4, v 5th -2, v 17th (last safe) +4, v 18th +5 · goal difference +3
**Suspension watch (D7, all players of the club):** Bogle — 🟨 2 from a ban (3/5); Ampadu — 🟨 2 from a ban (3/5); Calvert-Lewin — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 8 league matches):** goals after 75′ — for 2/9 (22%), against 1/6 (17%) · scored first 4, conceded first 2 (25% of matches), goalless 2 · points from losing positions 2 of 9 (3 matches behind at some point) · points from winning positions 7 of 12 (4 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Muharemović (DEF) 10.8/90, hit 5/8; Ampadu (MID) 11.0/90, hit 3/8; Stach (MID) 10.0/90, hit 3/8; Bijol (DEF) 13.6/90, hit 2/5; Justin (DEF) 7.9/90, hit 2/8; Elvedi (DEF) 7.2/90, hit 1/6
**Manager tenure (F13, SofaScore):** Daniel Farke since 04 Jul 2023 · 158 matches in charge, all competitions (79W 43D 36L) · 8 league matches this season · contract to 30 Jun 2027 · previous club Borussia M'gladbach · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Manchester United — last 4: Oct 2026 Premier League Leeds United 1–1 Manchester United (yellows 2–2, xG 1.41–0.92); Apr 2026 Premier League Manchester United 1–2 Leeds United (yellows 3–2, reds 1–0, xG 1.27–2.57); Jan 2026 Premier League Leeds United 1–1 Manchester United (yellows 0–1, xG 0.90–1.59); Feb 2023 Premier League Leeds United 0–2 Manchester United (yellows 2–1, xG 1.81–1.12) · 13 yellows in 4 | v Nottingham Forest — last 4: Aug 2026 EFL Cup Nottingham Forest 0–2 Leeds United (yellows 4–3, xG 1.21–2.58); Aug 2026 Premier League Nottingham Forest 0–1 Leeds United (yellows 2–1, xG 0.66–0.47); Feb 2026 Premier League Leeds United 3–1 Nottingham Forest (yellows 1–1, xG 2.50–1.33); Nov 2025 Premier League Nottingham Forest 3–1 Leeds United (yellows 2–1, xG 2.55–0.74) · 15 yellows in 4
**Archetype (F5):** used **HP** — derived HP [DERIVED] · signals, last 6 league matches: possession 47.8%, PPDA 8.9 (Understat, 6 matches; lower = harder press), opponent offsides forced 3.7/match (line height), fast breaks 0.4/match (season), both sides' xG 2.81/match (openness) · note: PPDA 8.9 v HP cut 9.1; possession 47.8 v 47.5. Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap).
**Squad changes (F20, since 01 Jun 2026):** in 13 (permanent 5, loan 2, free 0, loan returns 6) · out 14 · flags: Joël Piroe: still in an FPL set-piece order — use #2 or observation — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 8 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 10.51 | 13 | Big chances against | 17 | 7 |
| xGOT | 11.05 | 9 | Box shots against | 64 | 6 |
| xA | 4.34 | 20 | Corners against | 33 | 4 |
| Shots | 94 | 15 | Crosses faced | 157 | 17 |
| SoT | 32 | 12 | Dribbled past | 54 | 6 |
| Big chances | 16 | 13 | Errors→shot | 4 | 3 |
| Shots in box | 64 | 13 | GK goals prevented | 1.96 | 2 |
| Corners | 33 | 14 | Clearances | 239 | 4 |
| Crosses | 153 | 7 | Tackles | 126 | 13 |
| Fast breaks | 3 | 17 | Interceptions | 80 | 5 |
| FK shots | 4 | 6 | Def. contributions | 479 | 3 |
| Possession % | 47.25 | 11 | Aerial % | 52.58 | 4 |
| Pass % | 77.83 | 18 | Duel % | 51.41 | 5 |
| Long balls | 259 | 9 | Fouls | 103 | 15 |
| Dribbles | 57 | 12 | Yellows | 15 | 7 |
| Shots against | 114 | 12 | Km covered | 928 | 6 |
| SoT against | 34 | 10 | Sprints | 938 | 6 |
Per match: xG 1.31 · xGOT 1.38 · shots 11.8 · shots against 14.2 · big chances 2.0 for / 2.1 against · corners 4.1 / 4.1 · crosses 19.1 / 19.6 · possession 47.25%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | A | Brighton & Hove Albion | 1–1 | 2.49/3.04 | 2.19/2.27 | 33 | 10/20 | 5/5 | 10/11 | 1/7 | 5/4 | 6/7 | 13/1 v 35/6 | 4/2 |
| 4 | H | Newcastle United | 4–1 | 2.08/2.29 | 0.88/0.80 | 50 | 15/7 | 6/5 | 10/4 | 5/0 | 3/2 | 5/5 | 16/6 v 18/1 | 3/2 |
| 5 | H | Crystal Palace | 0–0 | 1.31/1.09 | 1.06/1.13 | 51 | 13/12 | 2/4 | 9/4 | 6/3 | 1/2 | 4/3 | 17/4 v 10/1 | 2/2 |
| 6 | A | Arsenal | 1–2 | 0.62/1.20 | 2.33/2.32 | 42 | 11/13 | 5/6 | 7/8 | 3/3 | 2/4 | 4/2 | 23/6 v 15/7 | 7/4 |
| 7 | H | Manchester United | 1–1 | 1.41/1.43 | 0.92/1.08 | 61 | 12/13 | 5/3 | 10/6 | 1/6 | 2/2 | 2/3 | 29/4 v 10/2 | 3/2 |
| 8 | A | Sunderland | 0–0 | 0.76/1.07 | 0.83/1.03 | 50 | 11/15 | 4/4 | 7/8 | 3/7 | 2/1 | 5/4 | 22/6 v 20/3 | 3/0 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | A | Brighton & Hove Albion | 1–1 | 3-5-2 | 16/13 | 3/3 | 0/0 | 252/522 | 38/55 | Gruev (Meniscus Injury), Rodon (Hamstring Injury), Joseph (Knee Injury) | Ferguson (Ankle Injury), Azeez (Muscle Injury), Hinshelwood (Knock Injury), Mitoma (Hamstring Injury), Wieffer (Knee Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Rutter (Physical Discomfort; doubtful) | Stuart Attwell |
| 4 | H | Newcastle United | 4–1 | 3-5-2 | 8/13 | 1/2 | 0/0 | 440/433 | 48/51 | Rodon (Hamstring Injury), Joseph (Knee Injury) | Burn (Ankle Injury), Joelinton (Muscle Injury), Osula (Knock Injury), Jaouen (Ankle Injury; doubtful) | Michael Salisbury |
| 5 | H | Crystal Palace | 0–0 | 3-4-2-1 | 10/12 | 2/3 | 0/0 | 424/424 | 58/55 | Wilson (Muscle Injury), Rodon (Hamstring Injury), Joseph (Knee Injury) | Disasi (ban (red)), Riad (Knee Injury), Henderson (Foot Injury), Mateta (Hamstring Injury) | Adam Herczeg |
| 6 | A | Arsenal | 1–2 | 3-4-2-1 | 20/12 | 4/1 | 0/0 | 356/512 | 54/54 | Rodon (Hamstring Injury), Joseph (Knee Injury), James (Back Injury; doubtful) | Tzolis (Hamstring Injury), Saliba (Back Injury) | Paul Tierney |
| 7 | H | Manchester United | 1–1 | 3-4-2-1 | 16/5 | 2/2 | 0/0 | 532/354 | 73/59 | Rodon (Hamstring Injury), Joseph (Knee Injury), James (Back Injury; doubtful) | Šeško (Shin Injury), Ugarte (Cruciate Ligament Injury), Dorgu (Hamstring Injury), Heaton (Abdominal Injury), Mainoo (Knock Injury; doubtful), Shaw (Knock Injury; doubtful) | Darren England |
| 8 | A | Sunderland | 0–0 | 3-4-2-1 | 14/10 | 2/1 | 0/0 | 368/379 | 68/65 | Rodon (Hamstring Injury), Joseph (Knee Injury) | Danso (ban (red)), Mundle (Knee Injury), Meunier (Hamstring Injury; doubtful) | Stuart Attwell |
Per match: fouls 12.9 / 11.6 · yellows 1.88 / 2.25 · reds 0 / 0 (season) · offsides forced 3.1, committed 2.1 · crosses attempted 19.1 / faced 19.6. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 1.56 for / 1.13 against per match · Away (4): xG 1.08 / 1.50. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW8 A v Sunderland 0–0 (Sun 25 Oct 16:30 UTC) — formation 3-4-2-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| James Trafford | G | 90 | 8.4 | 0.00 | 0.01 | 0 | 0 | 3 | 0 | 53 |
| James Justin | D | 90 | 7 | 0.02 | 0.03 | 1 | 1 | 6 | 5 | 46 |
| Jaka Bijol | D | 90 | 7.1 | 0.02 | 0.00 | 0 | 1 | 15 | 0 | 61 |
| Tarik Muharemović | D | 90 | 7.5 | 0.10 | 0.01 | 0 | 1 | 13 | 0 | 75 |
| Jayden Bogle | M | 90 | 7.1 | 0.12 | 0.12 | 1 | 2 | 5 | 4 | 52 |
| Ethan Ampadu | M | 90 | 7.5 | 0.00 | 0.09 | 1 | 0 | 6 | 1 | 67 |
| Ao Tanaka | M | 89 | 7.2 | 0.08 | 0.01 | 1 | 1 | 7 | 0 | 52 |
| Gabriel Gudmundsson | M | 90 | 7.2 | 0.02 | 0.00 | 0 | 1 | 6 | 4 | 57 |
| Harry Wilson | F | 66 | 6.5 | 0.00 | 0.11 | 2 | 0 | 4 | 4 | 41 |
| Brenden Aaronson | F | 65 | 6.2 | 0.00 | 0.00 | 2 | 0 | 1 | 0 | 21 |
| Dominic Calvert-Lewin | F | 85 | 5.9 | 0.00 | 0.01 | 0 | 0 | 0 | 0 | 22 |
Subs used: Noah Okafor (25'), Anton Stach (24'), Lukas Nmecha (11'), Sean Longstaff (1')
Goals: none
Substitutions (own): 65' Noah Okafor for Brenden Aaronson; 66' Anton Stach for Harry Wilson; 85' Lukas Nmecha for Dominic Calvert-Lewin; 89' Sean Longstaff for Ao Tanaka
Cards: 29' Ethan Ampadu (yellow, own); 39' Reinildo Mandava (yellow, opp); 67' Jayden Bogle (yellow, own)
**Baseline XI change vs GW7 (3-4-2-1 → 3-4-2-1):** in — Brenden Aaronson, Harry Wilson, Jaka Bijol; out — Anton Stach, Nico Elvedi, Noah Okafor.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 3 | A Brighton & Hove Albion | 15' | FOR | Jayden Bogle | Ao Tanaka | corner | 0.97 |
| 3 | A Brighton & Hove Albion | 71' | AGAINST | Luka Vušković | Maxim De Cuyper | corner | 0.37 |
| 4 | H Newcastle United | 32' | FOR | Lewis Miley | — | own goal | — |
| 4 | H Newcastle United | 34' | FOR | Jayden Bogle | Dominic Calvert-Lewin | open play | 0.08 |
| 4 | H Newcastle United | 45' | FOR | Dominic Calvert-Lewin | Tarik Muharemović | open play | 0.48 |
| 4 | H Newcastle United | 59' | FOR | Noah Okafor | — | open play | 0.05 |
| 4 | H Newcastle United | 90' | AGAINST | Bazoumana Touré | — | open play | 0.09 |
| 6 | A Arsenal | 55' | FOR | James Justin | Gabriel Gudmundsson | open play | 0.25 |
| 6 | A Arsenal | 62' | AGAINST | Riccardo Calafiori | Ben White | open play | 0.58 |
| 6 | A Arsenal | 70' | AGAINST | Bruno Guimarães | Declan Rice | open play | 0.06 |
| 7 | H Manchester United | 35' | AGAINST | Bryan Mbeumo | Youri Tielemans | open play | 0.41 |
| 7 | H Manchester United | 51' | FOR | Dominic Calvert-Lewin | Tarik Muharemović | corner | 0.56 |
Scored 9: open play 5, corner 2, direct FK 1, own goal 1 · Conceded 6: open play 5, corner 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW6 FOR v Arsenal 55' James Justin (assist Gabriel Gudmundsson, key pass Noah Okafor): G O O O A A A L - James Justin scores with the right foot! · before: 55' Gabriel Gudmundsson creates a scoring opportunity for his teammate ‹ 55' Leeds with a potentially dangerous attack. ‹ 54' Declan Rice makes the tackle and wins possession for his team
- GW6 AG v Arsenal 62' Riccardo Calafiori (assist Ben White, key pass Noni Madueke): G O O O A A A L - Riccardo Calafiori volleys the ball into the back of the net with the left. A great finish! · before: 62' Ben White creates a scoring opportunity for his teammate ‹ 62' The cross by Noni Madueke from Arsenal successfully finds a teammate in the box. ‹ 62' James Justin successfully blocks the shot
- GW6 AG v Arsenal 70' Bruno Guimarães (assist Declan Rice, key pass Martin Oedegaard): G O O O A A A L - Bruno Guimaraes scores with the right foot! · before: 70' Declan Rice creates a scoring opportunity for his teammate ‹ 70' Arsenal with a potentially dangerous attack. ‹ 70' James Justin is penalised for pushing Bruno Guimaraes.
- GW7 AG v Manchester United 35' Bryan Mbeumo (assist Youri Tielemans): G O O O A A A L - Bryan Mbeumo scores with the left foot! · before: 35' The cross by Youri Tielemans from Manchester United successfully finds a teammate in the bo ‹ 35' Dominic Calvert-Lewin from Leeds is ruled offside. ‹ 35' Tarik Muharemovic relieves the pressure with a clearance
- GW7 FOR v Manchester United 51' Dominic Calvert-Lewin (assist Tarik Muharemovic): G O O O A A A L - Dominic Calvert-Lewin scores with the right foot! · before: 51' A chance presents itself to Tarik Muharemovic from Leeds but his header goes wide ‹ 51' Anton Stach from Leeds swings in the corner from the right. ‹ 51' Noussair Mazraoui from Manchester United intercepts a cross aimed towards the box.

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW3 A v Brighton & Hove Albion 71' Luka Vušković: no structured culprit — reports only
- GW4 H v Newcastle United 90' Bazoumana Touré: no structured culprit — reports only
- GW6 A v Arsenal 62' Riccardo Calafiori: no structured culprit — reports only
- GW6 A v Arsenal 70' Bruno Guimarães: no structured culprit — reports only
  · GW6 other flags: Nico Elvedi lastManTackle 1; Ao Tanaka errorLeadToAShot 1; James Trafford errorLeadToAShot 1
- GW7 H v Manchester United 35' Bryan Mbeumo: no structured culprit — reports only

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

**Corners (E10 data layer):** observed takers GW1–8 [CONFIRMED — LiveScore Block L, 33 corners; side L/R as LiveScore records it; foot from SofaScore]: Anton Stach 26 (17L/9R, both foot); Harry Wilson 6 (1L/5R, left foot); Daniel James 1 (1L/0R, 1 short, right foot). First contact on corners that ended in a shot (Understat) — for: Tarik Muharemovic 3 (3 headed), Jayden Bogle 3 — 1 goal, Dominic Calvert-Lewin 2 (1 headed) — 1 goal, Ao Tanaka 2, Noah Okafor 2 · against (who beat them): Nathan Collins 2 (2 headed), Luke O&#039;Nien 2 (1 headed), Nikola Milenkovic 1 (1 headed), Igor Jesus 1 (1 headed), Thiago 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 38.4 (rank 18 of 20, 1 = highest line) · block length 21.5 (rank 12, 1 = most compact) · width 66.4. Per match: GW3 A v Brighton & Hove Albion 3-5-2: back line 36, front 58, length 21, width 65 (33% poss); GW4 H v Newcastle United 3-5-2: back line 37, front 63, length 26, width 66 (50% poss); GW5 H v Crystal Palace 3-4-2-1: back line 41, front 57, length 16, width 71 (51% poss); GW6 A v Arsenal 3-4-2-1: back line 38, front 58, length 21, width 69 (42% poss); GW7 H v Manchester United 3-4-2-1: back line 41, front 66, length 25, width 67 (61% poss); GW8 A v Sunderland 3-4-2-1: back line 38, front 63, length 25, width 69 (50% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 2 league match(es) v LB-coded sides — xG 0.89/match and 2.0 pts/match v 1.47 and 1.2 against the rest → **struggles — chance creation drops** (threshold: xG v LB at least 90% of the rest). GW1 A v Nottingham Forest 1–0, xG 0.47, box shots 6, poss 44%; GW5 H v Crystal Palace 0–0, xG 1.31, box shots 9, poss 51%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Stach 5, Elvedi 1, Tanaka 1** · FPL editorial order: Stach #1, Wilson #2, Longstaff #3
- Direct free-kick shooters: **Stach 4** · FPL order: Stach #1, Wilson #2, Longstaff #3
- Penalties taken: **—** · FPL order: Calvert-Lewin #1, Nmecha #2, Piroe #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Stach 2, Wilson 1**
- Corner targets (headed shots from corners): **Muharemovic 3, Calvert-Lewin 1, Justin 1** · corner shots 15

**Through-ball suppliers (Block P, PL/Opta, season):** Jayden Bogle 2 (0.28/90, percentile 75, 635 min) · club total 7 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 289 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 6.83, field tilt 43.6, possession 44.2%, box entries 5, direct speed 2.49, SCA 20; GW2: PPDA 11.73, field tilt 41.1, possession 47.1%, box entries 7, direct speed 2.56, SCA 24; GW3: PPDA 11.61, field tilt 33.9, possession 33.7%, box entries 7, direct speed 2.89, SCA 18; GW4: PPDA 11.54, field tilt 46.8, possession 50.6%, box entries 14, direct speed 2.29, SCA 28; GW5: PPDA 9, field tilt 40.1, possession 50.9%, box entries 6, direct speed 2.29, SCA 21; GW6: PPDA 10.03, field tilt 29.2, possession 41.8%, box entries 6, direct speed 2.72, SCA 18; GW7: PPDA 7.91, field tilt 59.9, possession 61.1%, box entries 7, direct speed 2.15, SCA 24; GW8: PPDA 8.33, field tilt 50.2, possession 49.3%, box entries 8, direct speed 2.43, SCA 20

**Zone 14 (C13, SofaScore heat-map points, 8 league matches):** for 27.8/match (rank 10 of 20) · conceded 31.5/match (rank 8 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 3.9/match · allowed 5.8/match · PPDA 9.0. Per match for/allowed: GW3 8/6; GW4 9/5; GW5 0/4; GW6 1/11; GW7 5/4; GW8 5/5 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 3-4-2-1, 8 league matches, weights last-3 ×3 / older ×1
- GK: James Trafford (14, 3/3)
- DEF: Tarik Muharemović (14, 3/3), Gabriel Gudmundsson (12, 3/3), Jaka Bijol (5, 1/3)
- MID: James Justin (14, 3/3), Jayden Bogle (14, 3/3), Ethan Ampadu (14, 3/3), Ao Tanaka (12, 3/3), Anton Stach (11, 2/3)
- FWD: Dominic Calvert-Lewin (14, 3/3)
- Contested slots: none · Excluded (FPL flag): Nico Elvedi — Illness - 75% chance of playing
- Absent last match (E12, SofaScore list): Rodon (Hamstring Injury), Joseph (Knee Injury)
- Substitutions this season (C3): GW5 67' Jayden Bogle→Daniel James CARD-RISK; GW6 86' Nico Elvedi→Jaka Bijol LATE; GW6 86' Jayden Bogle→Jean-Mattéo Bahoya LATE; GW6 79' James Justin→Lukas Nmecha CARD-RISK; GW6 71' Noah Okafor→Brenden Aaronson CHASING; GW6 71' Ao Tanaka→Harry Wilson CARD-RISK; GW7 81' Ao Tanaka→Sean Longstaff TACTICAL; GW7 74' Noah Okafor→Lukas Nmecha TACTICAL; GW8 89' Ao Tanaka→Sean Longstaff LATE; GW8 85' Dominic Calvert-Lewin→Lukas Nmecha LATE; GW8 66' Harry Wilson→Anton Stach TACTICAL; GW8 65' Brenden Aaronson→Noah Okafor TACTICAL

### First-choice players and absences (F14) — generated 2026-10-27 07:42 UTC
First choice = starter baseline (GK, 3 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | James Trafford | start weight 14 | OK | a | — | — |
| CB | Tarik Muharemović | start weight 14 | OK | a | Gabriel Gudmundsson (DEF, not a CB by heat map) | — |
| CB | Nico Elvedi | start weight 9 | DOUBT | d 75% — Illness - 75% chance of playing | Gabriel Gudmundsson (DEF, not a CB by heat map) | — |
| CB | Jaka Bijol | start weight 5 | OK | a | Gabriel Gudmundsson (DEF, not a CB by heat map) | — |
| xGI #1 | Dominic Calvert-Lewin | xGI 3.76 | OK | a 100% | Anton Stach | — |
| xGI #2 | Jayden Bogle | xGI 2.23 | OK | a | Anton Stach | — |
| Penalties #1 (FPL) | Calvert-Lewin | FPL order | OK | a 100% | Nmecha | — |
| Direct FK #1 (FPL) | Stach | FPL order | OK | a 100% | Wilson | — |
| Corners (observed) | Anton Stach | 26 corners taken | OK | a 100% | Harry Wilson | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 A Nottingham Forest: Nico Elvedi (did not start) · GW2 H Brentford: Nico Elvedi (did not start) · GW3 A Brighton & Hove Albion: Jaka Bijol (did not start) · GW4 H Newcastle United: Jaka Bijol (did not start) · GW5 H Crystal Palace: Jaka Bijol (did not start) · GW6 A Arsenal: Jaka Bijol (did not start) · GW7 H Manchester United: Jaka Bijol (did not start) · GW8 A Sunderland: Nico Elvedi (did not start)

### Next fixtures (all competitions)
- Sat 31 Oct 15:00 UTC · Premier League R9 · A v Bournemouth
- Sat 07 Nov 12:30 UTC · Premier League R10 · H v Tottenham Hotspur
- Sat 21 Nov 15:00 UTC · Premier League R11 · A v Chelsea
- Sat 28 Nov 15:00 UTC · Premier League R12 · H v Coventry City
- Wed 02 Dec 19:30 UTC · Premier League R13 · A v Manchester City
- Sat 05 Dec 15:00 UTC · Premier League R14 · H v Ipswich Town

### FPL availability flags (players with league minutes this season)
Rodon — Hamstring injury - Expected back 21 Nov (0%); Elvedi — Illness - 75% chance of playing (75%)
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
### Corner takers observed (LiveScore Block L)
- Anton Stach: 26 corners (17 left, 9 right)
- Harry Wilson: 6 corners (1 left, 5 right)
- Daniel James: 1 corners (1 left, 0 right, 1 short)
