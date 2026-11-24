# Arsenal — data doc
*Feeder-written (2026-11-24 07:45 UTC); do not edit. Narrative: `profiles/teams/arsenal.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-24 07:45 UTC)
**Manager:** Mikel Arteta · **Venue:** Emirates Stadium · **SofaScore:** https://www.sofascore.com/football/team/arsenal/42 · **FPL code:** ARS
**Table:** 1st, 28 pts (9W 1D 1L, GF 17 GA 7) · Home 1st (5-0-0, 10:2) · Away 2nd (4-1-1, 7:5)
**Standing context (F15):** 27 league games left · points v 4th +7, v 5th +10, v 17th (last safe) +19, v 18th +19 · goal difference +10
**Suspension watch (D7, all players of the club):** Madueke — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 11 league matches):** goals after 75′ — for 3/17 (18%), against 0/7 (0%) · scored first 8, conceded first 3 (27% of matches), goalless 0 · points from losing positions 7 of 12 (4 matches behind at some point) · points from winning positions 28 of 30 (10 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Gabriel (DEF) 8.8/90, hit 5/11; Konsa (DEF) 8.0/90, hit 4/10; Rice (MID) 9.0/90, hit 2/11
**Manager tenure (F13, SofaScore):** Mikel Arteta since 22 Dec 2019 · 368 matches in charge, all competitions (230W 61D 77L) · 11 league matches this season · contract to 30 Jun 2030 · previous club — · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Tottenham Hotspur — last 4: Feb 2026 Premier League Tottenham Hotspur 1–4 Arsenal (yellows 2–1, xG 0.70–2.07); Nov 2025 Premier League Arsenal 4–1 Tottenham Hotspur (yellows 1–3, xG 1.93–0.07); Jan 2025 Premier League Arsenal 2–1 Tottenham Hotspur (yellows 3–1, xG 1.45–0.78); Sep 2024 Premier League Tottenham Hotspur 0–1 Arsenal (yellows 5–3, xG 0.71–0.74) · 19 yellows in 4 | v Chelsea — last 4: Sep 2026 Premier League Arsenal 2–1 Chelsea (yellows 2–4, xG 2.05–0.39); Mar 2026 Premier League Arsenal 2–1 Chelsea (yellows 1–5, reds 0–1, xG 1.09–1.07); Feb 2026 EFL Cup Arsenal 1–0 Chelsea (yellows 0–3, xG 1.14–1.02); Jan 2026 EFL Cup Chelsea 2–3 Arsenal (yellows 4–4, xG 0.85–2.58) · 23 yellows in 4
**Archetype (F5):** used **PM** — last week's PM HELD by the margin rule (Q-86) — derived HP is inside the borderline band · signals, last 6 league matches: possession 61.2%, PPDA 8.5 (Understat, 3 matches; lower = harder press), opponent offsides forced 2.2/match (line height), fast breaks 1.1/match (season), both sides' xG 2.40/match (openness) · note: PPDA 8.5 v HP cut 8.5; computed from 3 of 6 GWs (no PPDA/possession for GW9, GW10, GW11). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 11 (permanent 6, loan 0, free 0, loan returns 5) · out 12 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 11 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 17.64 | 7 | Big chances against | 15 | 1 |
| xGOT | 16.82 | 5 | Box shots against | 72 | 2 |
| xA | 15.06 | 2 | Corners against | 48 | 7 |
| Shots | 151 | 9 | Crosses faced | 181 | 7 |
| SoT | 52 | 7 | Dribbled past | 47 | 1 |
| Big chances | 28 | 7 | Errors→shot | 14 | 18 |
| Shots in box | 103 | 9 | GK goals prevented | 1.53 | 7 |
| Corners | 59 | 6 | Clearances | 247 | 17 |
| Crosses | 185 | 13 | Tackles | 135 | 19 |
| Fast breaks | 12 | 13 | Interceptions | 73 | 19 |
| FK shots | 3 | 13 | Def. contributions | 490 | 19 |
| Possession % | 60.36 | 4 | Aerial % | 50 | 9 |
| Pass % | 85.90 | 4 | Duel % | 53.17 | 3 |
| Long balls | 285 | 19 | Fouls | 105 | 3 |
| Dribbles | 69 | 15 | Yellows | 17 | 3 |
| Shots against | 122 | 3 | Km covered | 1315 | 1 |
| SoT against | 29 | 1 | Sprints | 1193 | 12 |
Per match: xG 1.60 · xGOT 1.53 · shots 13.7 · shots against 11.1 · big chances 2.5 for / 1.4 against · corners 5.4 / 4.4 · crosses 16.8 / 16.5 · possession 60.4%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | H | Leeds United | 2–1 | 2.33/2.32 | 0.62/1.20 | 58 | 13/11 | 6/5 | 8/7 | 3/3 | 4/2 | 2/4 | 15/7 v 23/6 | 4/7 |
| 7 | A | Nottingham Forest | 1–0 | 1.14/0.92 | 0.90/0.75 | 74 | 9/14 | 1/2 | 7/8 | 3/6 | 1/0 | 6/8 | 27/7 v 14/1 | 2/1 |
| 8 | H | Everton | 2–0 | 1.96/2.29 | 0.63/0.72 | 58 | 20/8 | 4/3 | 12/6 | 10/2 | 3/2 | 12/3 | 23/5 v 16/2 | 1/0 |
| 9 | A | Liverpool FC | 1–0 | 0.98/— | 1.05/— | 44 | 10/17 | 3/0 | 6/14 | 3/9 | 2/1 | 4/7 | 10/4 v 33/5 | 2/3 |
| 10 | H | Hull City | 1–0 | 1.26/— | 0.36/— | 67 | 21/7 | 10/2 | 14/6 | 6/2 | 2/0 | 7/4 | 21/5 v 15/6 | 1/4 |
| 11 | A | Newcastle United | 2–2 | 1.49/— | 1.71/— | 66 | 13/12 | 4/3 | 10/5 | 1/4 | 4/3 | 3/6 | 15/1 v 14/2 | 3/3 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | H | Leeds United | 2–1 | 4-2-3-1 | 12/20 | 1/4 | 0/0 | 512/356 | 54/54 | Tzolis (Hamstring Injury), Saliba (Back Injury) | Rodon (Hamstring Injury), Joseph (Knee Injury), James (Back Injury; doubtful) | Paul Tierney |
| 7 | A | Nottingham Forest | 1–0 | 4-2-3-1 | 8/14 | 1/1 | 0/0 | 634/224 | 76/33 | Tzolis (Hamstring Injury), Hincapié (Ankle Injury) | Jesus (Calf Injury), Savona (Knee Injury), Gibbs-White (Knock Injury; doubtful) | Michael Oliver |
| 8 | H | Everton | 2–0 | 4-2-3-1 | 11/13 | 1/3 | 0/0 | 518/372 | 65/48 | Saka (Muscle Injury), Tzolis (Hamstring Injury), Saliba (Back Injury) | — | Tony Harrington |
| 9 | A | Liverpool FC | 1–0 | 4-2-3-1 | 10/18 | 4/4 | 0/0 | 372/464 | 45/72 | Dowman (ban (red)), Saka (Muscle Injury), Saliba (Back Injury) | Bradley (Knee Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Frimpong (Hamstring Injury) | Andy Madley |
| 10 | H | Hull City | 1–0 | 4-2-3-1 | 6/15 | 0/5 | 0/0 | 590/279 | 57/57 | Dowman (ban (red)), Saka (Muscle Injury) | Crooks (ban (yellows)), Hughes (Groin Injury), Gyabi (Groin Injury), Matazo (Cruciate Ligament Injury), Ansah (Back Injury), Targett (Ankle Injury) | Farai Hallam |
| 11 | A | Newcastle United | 2–2 | 4-2-3-1 | 7/20 | 3/3 | 0/0 | 529/262 | 61/31 | Dowman (ban (red)), Saka (Muscle Injury), Zubimendi (Hamstring Injury) | Jaouen (Hamstring Injury), Joelinton (Knock Injury) | Chris Kavanagh |
Per match: fouls 9.5 / 16.1 · yellows 1.55 / 3.45 · reds 0 / 1 (season) · offsides forced 1.4, committed 3.5 · crosses attempted 16.8 / faced 16.5. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 1.91 for / 0.43 against per match · Away (6): xG 1.36 / 1.18. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW11 A v Newcastle United 2–2 (Sat 21 Nov 17:30 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| David Raya | G | 70 | 6.2 | 0.00 | 0.00 | 0 | 0 | 1 | 0 | 42 |
| Jurriën Timber | D | 90 | 6.4 | 0.00 | 0.03 | 1 | 0 | 2 | 0 | 57 |
| Ezri Konsa | D | 90 | 6.8 | 0.00 | 0.01 | 1 | 0 | 7 | 0 | 67 |
| Gabriel Magalhães | D | 90 | 6.8 | 0.00 | 0.01 | 0 | 0 | 6 | 0 | 85 |
| Riccardo Calafiori | D | 90 | 6.5 | 0.04 | 0.03 | 1 | 1 | 4 | 0 | 68 |
| Declan Rice | M | 90 | 7.3 | 0.02 | 0.44 | 1 | 1 | 2 | 3 | 73 |
| Bruno Guimarães | M | 70 | 6.1 | 0.43 | 0.01 | 0 | 1 | 3 | 1 | 35 |
| Noni Madueke | M | 90 | 8.6 | 0.39 | 0.07 | 1 | 6 | 3 | 2 | 59 |
| Martin Ødegaard | M | 89 | 7 | 0.00 | 0.43 | 2 | 0 | 2 | 6 | 67 |
| Eberechi Eze | M | 70 | 7.1 | 0.53 | 0.01 | 3 | 2 | 1 | 1 | 38 |
| Kai Havertz | F | 89 | 6.7 | 0.06 | 0.32 | 1 | 1 | 3 | 1 | 35 |
Subs used: Kepa Arrizabalaga (20'), Myles Lewis-Skelly (20'), Christos Tzolis (20'), Mikel Merino (1'), Viktor Gyökeres (1')
Goals: 33' Eberechi Eze (assist Kai Havertz) [own]; 49' Harvey Barnes (assist William Osula) [opp]; 62' Malick Thiaw (assist Joe Willock) [opp]; 78' Noni Madueke (assist Martin Ødegaard) [own]
Substitutions (own): 70' Christos Tzolis for Eberechi Eze; 70' Myles Lewis-Skelly for Bruno Guimarães; 70' Kepa Arrizabalaga for David Raya [injury]; 90' Mikel Merino for Martin Ødegaard; 90' Viktor Gyökeres for Kai Havertz
Cards: 23' Amar Dedić (yellow, opp); 56' Declan Rice (yellow, own); 58' Harvey Barnes (yellow, opp); 81' Noni Madueke (yellow, own); 81' Dan Burn (yellow, opp); 90' Viktor Gyökeres (yellow, own)
**Baseline XI change vs GW10 (4-2-3-1 → 4-2-3-1):** in — Eberechi Eze; out — Christos Tzolis.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 6 | H Leeds United | 55' | AGAINST | James Justin | Gabriel Gudmundsson | open play | 0.25 |
| 6 | H Leeds United | 62' | FOR | Riccardo Calafiori | Ben White | open play | 0.58 |
| 6 | H Leeds United | 70' | FOR | Bruno Guimarães | Declan Rice | open play | 0.06 |
| 7 | A Nottingham Forest | 80' | FOR | Noni Madueke | Declan Rice | open play | 0.04 |
| 8 | H Everton | 7' | FOR | Ezri Konsa | Viktor Gyökeres | [unmatched] | — |
| 8 | H Everton | 68' | FOR | Gabriel Magalhães | Ben White | [unmatched] | — |
| 9 | A Liverpool FC | 16' | FOR | Kai Havertz | Declan Rice | [no Understat] | — |
| 10 | H Hull City | 72' | FOR | Martin Ødegaard | — | [no Understat] | — |
| 11 | A Newcastle United | 33' | FOR | Eberechi Eze | Kai Havertz | [no Understat] | — |
| 11 | A Newcastle United | 49' | AGAINST | Harvey Barnes | William Osula | [no Understat] | — |
| 11 | A Newcastle United | 62' | AGAINST | Malick Thiaw | Joe Willock | [no Understat] | — |
| 11 | A Newcastle United | 78' | FOR | Noni Madueke | Martin Ødegaard | [no Understat] | — |
Scored 17: open play 10, [no Understat] 4, [unmatched] 2, penalty 1 · Conceded 7: open play 3, [no Understat] 2, set piece 1, corner 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW9 FOR v Liverpool FC 16' Kai Havertz (assist Declan Rice, key pass Noni Madueke): G O O O A A A L - Kai Havertz scores with the left foot! · before: 16' The cross by Declan Rice from Arsenal successfully finds a teammate in the box. ‹ 16' Goal kick for Liverpool. ‹ 16' Declan Rice from Arsenal tries to score from outside the penalty box, but the shot is nowhe
- GW10 FOR v Hull City 72' Martin Ødegaard: G O O O A A A L - Martin Oedegaard reacts first on the loose ball and puts it away with the right! · before: 72' Good effort by Noni Madueke as he directs a shot on target, but the keeper saves it ‹ 72' Lucas Herrington relieves the pressure with a clearance ‹ 72' Obstruction as Elliot Stroud cuts off the run of Noni Madueke. A free-kick is awarded.
- GW11 FOR v Newcastle United 33' Eberechi Eze (assist Kai Havertz): — no commentary line — · before: 32' Jacob Murphy (Newcastle United) wins a free kick in the defensive half. ‹ 32' Foul by Eberechi Eze (Arsenal). ‹ 30' Foul by Joe Willock (Newcastle United).
- GW11 AG v Newcastle United 49' Harvey Barnes (assist William Osula): — no commentary line — · before: 48' Delay over. They are ready to continue. ‹ 47' Delay in match because of an injury David Raya (Arsenal). ‹ 46' Foul by Joe Willock (Newcastle United).
- GW11 AG v Newcastle United 62' Malick Thiaw (assist Joe Willock): — no commentary line — · before: 61' Foul by William Osula (Newcastle United). ‹ 61' David Raya (Arsenal) wins a free kick in the defensive half. ‹ 61' Corner, Newcastle United. Conceded by Gabriel Magalhães.
- GW11 FOR v Newcastle United 78' Noni Madueke (assist Martin Ødegaard): — no commentary line — · before: 77' Offside, Arsenal. Christos Tzolis is caught offside. ‹ 75' Offside, Newcastle United. Jacob Ramsey is caught offside. ‹ 74' Corner, Newcastle United. Conceded by Kai Havertz.

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW6 H v Leeds United 55' James Justin: no structured culprit — reports only
  · GW6 other flags: Ezri Konsa lastManTackle 1; Declan Rice errorLeadToAShot 1
- GW11 A v Newcastle United 49' Harvey Barnes: no structured culprit — reports only
- GW11 A v Newcastle United 62' Malick Thiaw: no structured culprit — reports only
  · GW11 error leading to a goal (SofaScore, match level — 2 conceded, the goal is not identified): Martin Ødegaard [CONFIRMED — SofaScore error flag]
  · GW11 other flags: Myles Lewis-Skelly errorLeadToAShot 1

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 79 | 10.70 | 11 | 63 | 5.55 | 3 |
| corner | 20 | 2.19 | 1 | 13 | 1.57 | 1 |
| set piece | 5 | 1.26 | 0 | 6 | 0.19 | 1 |
| direct FK | 2 | 0.13 | 0 | 3 | 0.18 | 0 |
| penalty | 1 | 0.76 | 1 | 1 | 0.76 | 0 |
Totals per match: xG 1.88 (npxG 1.79) for, xGA 1.03 (np 0.94) against · dead-ball share of xG 29% for, 33% against · penalties won 1, conceded 1 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 20 shots, xG 2.19, 1 goals, headed 11: 6-yard box, central 8 shots, xG 1.40, 1 goals; penalty area, central 6 shots, xG 0.65, 0 goals; outside box, left 2 shots, xG 0.05, 0 goals · against — 13 shots conceded, xG 1.57, 1 goals, headed 3: 6-yard box, central 3 shots, xG 1.09, 1 goals; penalty area, central 4 shots, xG 0.33, 0 goals; penalty area, right 1 shots, xG 0.07, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 31 · corner shots conceded 13 (headed 3), xG 1.57, goals 1 · xG per corner faced 0.051 (rank 11 of 20, 1 = weakest) · weak zone: six-yard box (1.09 xG, 69% of theirs v 65% league) · signal: **neutral** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–11 [CONFIRMED — LiveScore Block L, 76 corners; side L/R as LiveScore records it; foot from SofaScore]: Declan Rice 34 (34L/0R, 6 short, right foot); Bukayo Saka 19 (0L/19R, 4 short, left foot); Martin Oedegaard 15 (0L/15R, 2 short, left foot); Noni Madueke 7 (0L/7R, 2 short, left foot). First contact on corners that ended in a shot (Understat) — for: Gabriel 4 (3 headed), Riccardo Calafiori 3 (2 headed), Ezri Konsa Ngoyo 3 (2 headed) — 1 goal, Kai Havertz 2 (2 headed), Christos Tzolis 2 · against (who beat them): Murillo 2 (1 headed), Nordi Mukiele 2, Chema Andres 1 (1 headed) — 1 goal, Pascal Struijk 1 (1 headed), Reece James 1. Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 44.2 (rank 3 of 20, 1 = highest line) · block length 20.8 (rank 8, 1 = most compact) · width 63.3. Per match: GW6 H v Leeds United 4-2-3-1: back line 47, front 67, length 21, width 67 (58% poss); GW7 A v Nottingham Forest 4-2-3-1: back line 47, front 67, length 19, width 68 (74% poss); GW8 H v Everton 4-2-3-1: back line 46, front 65, length 19, width 58 (58% poss); GW9 A v Liverpool FC 4-2-3-1: back line 35, front 52, length 16, width 56 (44% poss); GW10 H v Hull City 4-2-3-1: back line 42, front 68, length 26, width 59 (67% poss); GW11 A v Newcastle United 4-2-3-1: back line 44, front 63, length 20, width 63 (66% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 4 league match(es) v LB-coded sides — xG 1.54/match and 3.0 pts/match v 1.65 and 2.3 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW1 H v Coventry City 3–0, xG 1.88, box shots 10, poss 64%; GW4 A v Sunderland 2–0, xG 1.88, box shots 8, poss 57%; GW7 A v Nottingham Forest 1–0, xG 1.14, box shots 7, poss 74%; GW10 H v Hull City 1–0, xG 1.26, box shots 14, poss 67%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Saka 5, Rice 5, White 1** · FPL editorial order: Rice #1, Saka #2, Ødegaard #3
- Direct free-kick shooters: **Eze 1, Odegaard 1** · FPL order: Rice #1, Saka #2, Eze #3
- Penalties taken: **Saka 1** · FPL order: Saka #1, Gyökeres #2, Ødegaard #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Rice 2, Odegaard 1**
- Corner targets (headed shots from corners): **Gabriel 3, Calafiori 2, Havertz 2, Ngoyo 2** · corner shots 20
- **DISAGREEMENT:** observed corner taker Bukayo Saka (5) v FPL #1 Rice — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Martin Ødegaard 14 (1.37/90, percentile 100, 918 min); Viktor Gyökeres 2 (0.99/90, percentile 98, 182 min); Bruno Guimarães 3 (0.59/90, percentile 95, 460 min); Bukayo Saka 3 (0.45/90, percentile 88, 598 min); Mikel Merino 1 (0.44/90, percentile 88, 204 min); Jurriën Timber 2 (0.42/90, percentile 87, 426 min); Myles Lewis-Skelly 2 (0.40/90, percentile 85, 452 min) · club total 34 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 334 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 9.72, field tilt 68.9, possession 64.7%, box entries 21, direct speed 1.71, SCA 40; GW2: PPDA 12.67, field tilt 64.4, possession 61.1%, box entries 13, direct speed 2.2, SCA 13; GW3: PPDA 9.5, field tilt 59.8, possession 54.6%, box entries 21, direct speed 3.05, SCA 32; GW4: PPDA 7.5, field tilt 54.6, possession 56.9%, box entries 15, direct speed 2.08, SCA 20; GW5: PPDA 12.57, field tilt 54.9, possession 60%, box entries 13, direct speed 1.82, SCA 21; GW6: PPDA 9.81, field tilt 70.8, possession 58.2%, box entries 20, direct speed 2.78, SCA 26; GW7: PPDA 7.12, field tilt 76.3, possession 73.3%, box entries 12, direct speed 1.77, SCA 18; GW8: PPDA 8.24, field tilt 65.1, possession 58.4%, box entries 21, direct speed 2.43, SCA 40; GW9: PPDA 11.5, field tilt 38.9, possession 43.6%, box entries 12, direct speed 3.01, SCA 19; GW10: PPDA 13.18, field tilt 76.2, possession 66.8%, box entries 30, direct speed 2.58, SCA 42

**Zone 14 (C13, SofaScore heat-map points, 11 league matches):** for 29.8/match (rank 9 of 20) · conceded 27.5/match (rank 13 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 12.1/match · allowed 4.2/match · PPDA 9.7. Per match for/allowed: GW3 17/5; GW4 5/5; GW5 10/6; GW6 11/1; GW7 10/6; GW8 18/4 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: 
- DEF: Gabriel Magalhães (16, 3/3), Ezri Konsa (15, 3/3), Riccardo Calafiori (15, 3/3), Jurriën Timber (10, 3/3)
- MID: Declan Rice (16, 3/3), Martin Ødegaard (16, 3/3), Bruno Guimarães (11, 3/3), Christos Tzolis (10, 2/3), Eberechi Eze (5, 1/3)
- FWD: Kai Havertz (15, 3/3)
- Contested slots: M Eberechi Eze 5 v Myles Lewis-Skelly 5 · Excluded (FPL flag): David Raya — Shoulder injury - 50% chance of playing; Bukayo Saka — Thigh injury - Expected back 20 Dec
- Absent last match (E12, SofaScore list): Dowman (ban (red)), Saka (Muscle Injury), Zubimendi (Hamstring Injury)
- Substitutions this season (C3): GW9 84' Christos Tzolis→Piero Hincapié TACTICAL; GW9 62' Bruno Guimarães→Myles Lewis-Skelly TACTICAL; GW10 89' Bruno Guimarães→Martín Zubimendi LATE; GW10 69' Riccardo Calafiori→Piero Hincapié TACTICAL; GW10 69' Christos Tzolis→Eberechi Eze TACTICAL; GW10 63' Kai Havertz→Viktor Gyökeres TACTICAL; GW10 63' Declan Rice→Mikel Merino TACTICAL; GW11 90' Martin Ødegaard→Mikel Merino LATE; GW11 90' Kai Havertz→Viktor Gyökeres LATE; GW11 70' Eberechi Eze→Christos Tzolis CHASING; GW11 70' Bruno Guimarães→Myles Lewis-Skelly CHASING; GW11 70' David Raya→Kepa Arrizabalaga INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']

### First-choice players and absences (F14) — generated 2026-11-24 07:45 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | David Raya | start weight 16 | DOUBT | d 50% — Shoulder injury - 50% chance of playing | — | — |
| CB | Gabriel Magalhães | start weight 16 | OK | a | Cristhian Mosquera | — |
| CB | Ezri Konsa | start weight 15 | OK | a 100% | Cristhian Mosquera | — |
| xGI #1 | Martin Ødegaard | xGI 5.27 | OK | a | Kai Havertz | — |
| xGI #2 | Bukayo Saka | xGI 4.85 | **OUT** | i 0% — Thigh injury - Expected back 20 Dec | Kai Havertz | +0.5 to defenders and GK facing them (cap +1.0); P(CS) with his xGI share removed |
| Penalties #1 (FPL) | Saka | FPL order | **OUT** | i 0% — Thigh injury - Expected back 20 Dec | Gyökeres | opposing defenders' negative set-piece pairing removed; own pairings built on him dropped |
| Direct FK #1 (FPL) | Rice | FPL order | OK | a 100% | Eze | — |
| Corners (observed) | Declan Rice | 34 corners taken | OK | a 100% | Bukayo Saka | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Coventry City: Ezri Konsa (did not start) · GW2 A Aston Villa: Ezri Konsa (did not start) · GW3 H Chelsea: all started · GW4 A Sunderland: all started · GW5 A Brighton & Hove Albion: all started · GW6 H Leeds United: all started · GW7 A Nottingham Forest: all started · GW8 H Everton: Bukayo Saka (Muscle Injury) · GW9 A Liverpool FC: Bukayo Saka (Muscle Injury) · GW10 H Hull City: Bukayo Saka (Muscle Injury) · GW11 A Newcastle United: Bukayo Saka (Muscle Injury)

### Next fixtures (all competitions)
- Tue 24 Nov 20:00 UTC · UEFA Champions League R5 · H v Borussia Dortmund
- Sun 29 Nov 16:30 UTC · Premier League R12 · H v Manchester City
- Wed 02 Dec 20:15 UTC · Premier League R13 · A v Brentford
- Sun 06 Dec 16:30 UTC · Premier League R14 · A v Tottenham Hotspur
- Wed 09 Dec 20:00 UTC · UEFA Champions League R6 · H v Real Madrid
- Sun 13 Dec 14:00 UTC · Premier League R15 · H v Bournemouth

### FPL availability flags (players with league minutes this season)
Raya — Shoulder injury - 50% chance of playing (50%); Saka — Thigh injury - Expected back 20 Dec (0%); Zubimendi — Hamstring injury - Unknown return date (0%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 H Coventry City 3–0 · xG 1.88–0.20 · poss 64% · 4-2-3-1 · scorers: Kai Havertz 15', Bukayo Saka 23', Martin Ødegaard 49'
- GW2 A Aston Villa 1–0 · xG 1.04–0.33 · poss 61% · 4-2-3-1 · scorers: Bukayo Saka 59'
- GW3 H Chelsea 2–1 · xG 2.11–0.35 · poss 55% · 4-2-3-1 · scorers: Kai Havertz 25', Martin Ødegaard 50'
- GW4 A Sunderland 2–0 · xG 1.88–1.80 · poss 57% · 4-2-3-1 · scorers: Bruno Guimarães 58', Bukayo Saka 90'
- GW5 A Brighton & Hove Albion 0–3 · xG 1.63–1.31 · poss 60% · 4-2-3-1 · scorers: none
- GW6 H Leeds United 2–1 · xG 2.33–0.62 · poss 58% · 4-2-3-1 · scorers: Riccardo Calafiori 62', Bruno Guimarães 70'
- GW7 A Nottingham Forest 1–0 · xG 1.14–0.90 · poss 74% · 4-2-3-1 · scorers: Noni Madueke 80'
- GW8 H Everton 2–0 · xG 1.96–0.63 · poss 58% · 4-2-3-1 · scorers: Ezri Konsa 7', Gabriel Magalhães 68'
- GW9 A Liverpool FC 1–0 · xG 0.98–1.05 · poss 44% · 4-2-3-1 · scorers: Kai Havertz 16'
- GW10 H Hull City 1–0 · xG 1.26–0.36 · poss 67% · 4-2-3-1 · scorers: Martin Ødegaard 72'
- GW11 A Newcastle United 2–2 · xG 1.49–1.71 · poss 66% · 4-2-3-1 · scorers: Eberechi Eze 33', Noni Madueke 78'
### Corner takers observed (LiveScore Block L)
- Declan Rice: 34 corners (34 left, 0 right, 6 short)
- Bukayo Saka: 19 corners (0 left, 19 right, 4 short)
- Martin Oedegaard: 15 corners (0 left, 15 right, 2 short)
- Noni Madueke: 7 corners (0 left, 7 right, 2 short)
- Max Dowman: 1 corners (0 left, 1 right)
