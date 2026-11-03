# Everton — data doc
*Feeder-written (2026-11-03 07:42 UTC); do not edit. Narrative: `profiles/teams/everton.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-03 07:42 UTC)
**Manager:** David Moyes · **Venue:** Hill Dickinson Stadium · **SofaScore:** https://www.sofascore.com/football/team/everton/48 · **FPL code:** EVE
**Table:** 7th, 13 pts (3W 4D 2L, GF 9 GA 9) · Home 9th (2-1-1, 5:4) · Away 7th (1-3-1, 4:5)
**Standing context (F15):** 29 league games left · points v 4th -3, v 5th -2, v 17th (last safe) +6, v 18th +6 · goal difference +0
**Suspension watch (D7, all players of the club):** Garner — 🟨 2 from a ban (3/5); Armstrong — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 9 league matches):** goals after 75′ — for 3/9 (33%), against 2/9 (22%) · scored first 3, conceded first 5 (56% of matches), goalless 1 · points from losing positions 3 of 15 (5 matches behind at some point) · points from winning positions 10 of 12 (4 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Tarkowski (DEF) 10.4/90, hit 5/9; Branthwaite (DEF) 10.0/90, hit 4/8; Garner (MID) 11.6/90, hit 3/9; Armstrong (MID) 8.6/90, hit 2/9; Mykolenko (DEF) 7.2/90, hit 2/8; O'Brien (DEF) 8.7/90, hit 1/5
**Manager tenure (F13, SofaScore):** David Moyes since 11 Jan 2025 · 72 matches in charge, all competitions (27W 21D 24L) · 9 league matches this season · contract to — · previous club West Ham United · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Liverpool FC — last 4: Apr 2026 Premier League Everton 1–2 Liverpool FC (yellows 2–0, xG 0.79–1.45); Sep 2025 Premier League Liverpool FC 2–1 Everton (yellows 2–3, xG 0.90–0.70); Apr 2025 Premier League Liverpool FC 1–0 Everton (yellows 2–2, xG 1.47–0.67); Feb 2025 Premier League Everton 2–2 Liverpool FC (yellows 4–4, reds 1–1, xG 0.95–0.62) · 19 yellows in 4 | v Manchester United — last 4: Sep 2026 Premier League Everton 2–2 Manchester United (yellows 3–3, xG 1.01–0.69); Feb 2026 Premier League Everton 0–1 Manchester United (yellows 2–3, xG 0.63–1.27); Nov 2025 Premier League Manchester United 0–1 Everton (yellows 2–0, reds 0–1, xG 1.71–0.21); Feb 2025 Premier League Everton 2–2 Manchester United (yellows 4–1, xG 1.91–0.41) · 18 yellows in 4
**Archetype (F5):** used **TR** — derived TR [DERIVED] · signals, last 6 league matches: possession 48.7%, PPDA 14.5 (Understat, 5 matches; lower = harder press), opponent offsides forced 0.7/match (line height), fast breaks 0.6/match (season), both sides' xG 2.77/match (openness) · note: possession 48.7 v 47.5; computed from 5 of 6 GWs (no PPDA/possession for GW9). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 8 (permanent 6, loan 1, free 0, loan returns 1) · out 12 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 9 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 12.40 | 12 | Big chances against | 23 | 11 |
| xGOT | 11.46 | 10 | Box shots against | 82 | 12 |
| xA | 7.62 | 11 | Corners against | 52 | 18 |
| Shots | 125 | 11 | Crosses faced | 166 | 13 |
| SoT | 43 | 6 | Dribbled past | 60 | 5 |
| Big chances | 28 | 4 | Errors→shot | 5 | 5 |
| Shots in box | 88 | 8 | GK goals prevented | 1.31 | 6 |
| Corners | 44 | 8 | Clearances | 233 | 12 |
| Crosses | 168 | 10 | Tackles | 139 | 12 |
| Fast breaks | 5 | 17 | Interceptions | 77 | 12 |
| FK shots | 3 | 8 | Def. contributions | 501 | 10 |
| Possession % | 46.67 | 14 | Aerial % | 53.12 | 4 |
| Pass % | 83.27 | 8 | Duel % | 53.77 | 1 |
| Long balls | 271 | 14 | Fouls | 74 | 1 |
| Dribbles | 57 | 15 | Yellows | 17 | 7 |
| Shots against | 133 | 14 | Km covered | 1023 | 12 |
| SoT against | 36 | 10 | Sprints | 900 | 17 |
Per match: xG 1.38 · xGOT 1.27 · shots 13.9 · shots against 14.8 · big chances 3.1 for / 2.6 against · corners 4.9 / 5.8 · crosses 18.7 / 18.4 · possession 46.666666666667%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | A | Tottenham Hotspur | 0–0 | 1.11/1.60 | 0.69/0.74 | 38 | 12/14 | 3/2 | 9/8 | 6/8 | 2/1 | 6/5 | 17/4 v 23/5 | 2/1 |
| 5 | H | Ipswich Town | 1–0 | 2.24/2.59 | 1.44/1.10 | 52 | 21/13 | 2/4 | 13/9 | 8/4 | 5/1 | 4/4 | 16/4 v 13/3 | 0/1 |
| 6 | A | Hull City | 2–2 | 1.68/2.97 | 1.33/1.53 | 65 | 15/9 | 7/5 | 11/9 | 3/2 | 8/2 | 6/7 | 22/5 v 23/3 | 1/4 |
| 7 | H | Chelsea | 0–2 | 0.43/0.57 | 1.47/1.61 | 47 | 6/18 | 5/7 | 6/10 | 1/5 | 2/3 | 5/7 | 20/3 v 14/3 | 1/4 |
| 8 | A | Arsenal | 0–2 | 0.63/0.72 | 1.96/2.29 | 42 | 8/20 | 3/4 | 6/12 | 2/10 | 2/3 | 3/12 | 16/2 v 23/5 | 0/1 |
| 9 | A | Newcastle United | 1–0 | 2.34/— | 1.29/— | 48 | 16/17 | 5/2 | 11/7 | 1/6 | 4/2 | 5/4 | 22/7 v 24/7 | 0/2 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | A | Tottenham Hotspur | 0–0 | 4-1-4-1 | 8/14 | 2/0 | 0/0 | 381/644 | 37/78 | Nørgaard (Muscle Injury) | Richarlison (coach decision), Kulusevski (Knee Injury), Mudryk (Ankle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Darren England |
| 5 | H | Ipswich Town | 1–0 | 4-2-3-1 | 6/12 | 2/3 | 0/1 | 513/472 | 63/53 | Nørgaard (Muscle Injury), Röhl (Knock Injury; doubtful) | Taylor (Knee Injury) | Stuart Attwell |
| 6 | A | Hull City | 2–2 | 4-2-3-1 | 4/15 | 0/2 | 0/0 | 595/306 | 63/51 | Mykolenko (Knock Injury; doubtful) | Hughes (Groin Injury), Gyabi (Groin Injury), Matazo (Cruciate Ligament Injury), Ansah (Back Injury), Butland (Elbow Injury), Targett (Ankle Injury) | Michael Salisbury |
| 7 | H | Chelsea | 0–2 | 4-2-3-1 | 8/15 | 3/4 | 0/0 | 408/463 | 56/55 | — | Emegha (Hamstring Injury), Gittens (Ankle Injury), James (Knee Injury) | Paul Tierney |
| 8 | A | Arsenal | 0–2 | 4-2-3-1 | 13/11 | 3/1 | 0/0 | 372/518 | 48/65 | — | Saka (Muscle Injury), Tzolis (Hamstring Injury), Saliba (Back Injury) | Tony Harrington |
| 9 | A | Newcastle United | 1–0 | 4-2-3-1 | 9/13 | 2/4 | 0/1 | 396/428 | 61/70 | — | Jaouen (Hamstring Injury), Livramento (Knock Injury), Miley (Knock Injury; doubtful), Fernández-Pardo (Illness; doubtful) | John Brooks |
Per match: fouls 8.2 / 13.0 · yellows 1.89 / 2.33 · reds 0 / 2 (season) · offsides forced 0.6, committed 2.1 · crosses attempted 18.7 / faced 18.4. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 1.20 for / 1.39 against per match · Away (5): xG 1.52 / 1.49. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW9 A v Newcastle United 1–0 (Mon 02 Nov 20:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Pickford | G | 90 | 7 | 0.00 | 0.00 | 0 | 0 | 3 | 0 | 51 |
| Jake O'Brien | D | 90 | 7.5 | 0.20 | 0.08 | 1 | 2 | 5 | 5 | 58 |
| James Tarkowski | D | 90 | 7.4 | 0.00 | 0.00 | 1 | 0 | 9 | 0 | 48 |
| Jarrad Branthwaite | D | 82 | 8.2 | 0.07 | 0.08 | 1 | 1 | 7 | 0 | 57 |
| Vitaliy Mykolenko | D | 90 | 7.4 | 0.00 | 0.04 | 0 | 0 | 7 | 1 | 55 |
| Harrison Armstrong | M | 90 | 7.3 | 0.35 | 0.04 | 2 | 1 | 2 | 0 | 42 |
| James Garner | M | 90 | 7.5 | 0.21 | 0.10 | 1 | 3 | 6 | 2 | 67 |
| Merlin Röhl | M | 90 | 6.8 | 0.05 | 0.02 | 0 | 1 | 2 | 3 | 42 |
| Kiernan Dewsbury-Hall | M | 90 | 7.8 | 0.15 | 0.28 | 3 | 3 | 3 | 7 | 77 |
| Tyrique George | M | 89 | 7.2 | 0.12 | 0.11 | 1 | 2 | 3 | 4 | 48 |
| Thierno Barry | F | 80 | 7.5 | 1.29 | 0.21 | 2 | 3 | 1 | 0 | 19 |
Subs used: Brennan Johnson (10'), Michael Keane (8'), Hayden Hackney (8')
Goals: 49' Thierno Barry [own]
Substitutions (own): 80' Brennan Johnson for Thierno Barry; 82' Michael Keane for Jarrad Branthwaite; 90' Hayden Hackney for Tyrique George
Cards: manager/staff booking: David Moyes 73' [LiveScore] (own; no FPL effect); 32' Dan Burn (yellow, opp); 52' Tyrique George (yellow, own); 90' Brennan Johnson (yellow, own); 90' Fabian Schär (yellow, opp); 90' Jacob Ramsey (yellowRed, opp); 90' Jacob Ramsey (yellow, opp)
**Baseline XI change vs GW8 (4-2-3-1 → 4-2-3-1):** in — Jarrad Branthwaite; out — Brennan Johnson.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 5 | H Ipswich Town | 11' | FOR | Thierno Barry | James Tarkowski | open play | 0.35 |
| 6 | A Hull City | 48' | AGAINST | Joe Gelhardt | Sorba Thomas | open play | 0.55 |
| 6 | A Hull City | 55' | FOR | Kiernan Dewsbury-Hall | Ainsley Maitland-Niles | corner | 0.34 |
| 6 | A Hull City | 68' | FOR | Thierno Barry | Kiernan Dewsbury-Hall | open play | 0.33 |
| 6 | A Hull City | 74' | AGAINST | Mohamed Belloumi | Elliot Stroud | open play | 0.09 |
| 7 | H Chelsea | 46' | AGAINST | Pedro Neto | — | open play | 0.42 |
| 7 | H Chelsea | 90' | AGAINST | Pedro Neto | — | set piece | 0.08 |
| 8 | A Arsenal | 7' | AGAINST | Ezri Konsa | Viktor Gyökeres | [unmatched] | — |
| 8 | A Arsenal | 68' | AGAINST | Gabriel Magalhães | Ben White | [unmatched] | — |
| 9 | A Newcastle United | 49' | FOR | Thierno Barry | — | [no Understat] | — |
Scored 9: open play 5, corner 2, set piece 1, [no Understat] 1 · Conceded 9: open play 6, [unmatched] 2, set piece 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW7 AG v Chelsea 46' Pedro Neto: G O O O O O A A L - Pedro Neto finds the net with the left foot! · before: 46' Jorrel Hato creates a scoring opportunity for his teammate ‹ 46' Harrison Armstrong wins an air challenge against Morgan Rogers ‹ 46' The second half is underway.
- GW7 AG v Chelsea 90' Pedro Neto: G O O O A A A L - Pedro Neto reacts first on the loose ball and puts it away with the left! · before: 90' Jordan Henderson takes the free-kick but it is blocked by the wall ‹ 89' Christian Noergaard pulls a player from the opposite team by the shirt and is booked. ‹ 89' Christian Noergaard from Everton goes a bit too far there as he pulls down Cole Palmer
- GW8 AG v Arsenal 7' Ezri Konsa (assist Viktor Gyoekeres): G O O O A A A L - Ezri Konsa scores with the right foot! · before: 7' Gabriel from Arsenal sees his header hit the crossbar after the keeper parries the ball. ‹ 7' Martin Oedegaard from Arsenal swings in the corner from the right. ‹ 7' Vitaliy Mykolenko from Everton intercepts a cross aimed towards the box.
- GW8 AG v Arsenal 68' Gabriel Magalhães (assist Ben White, key pass Bruno Guimaraes): G O O O A A A L - Gabriel from Arsenal heads the ball home! · before: 68' Ben White creates a scoring opportunity for his teammate ‹ 68' Jake O'Brien from Everton intercepts a cross aimed towards the box. ‹ 68' Declan Rice swings in the ball from a corner on the left, but it is nowhere near a teammate
- GW9 FOR v Newcastle United 49' Thierno Barry: GOAL! It's an easy finish as Thierno Barry from Everton taps the ball into an open goal with the right foot! · before: 49' Good effort by Tyrique George as he directs a shot on target, but the keeper saves it ‹ 49' Kiernan Dewsbury-Hall creates a scoring opportunity for his teammate ‹ 49' Everton with a potentially dangerous attack.

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW6 A v Hull City 48' Joe Gelhardt: no structured culprit — reports only
- GW6 A v Hull City 74' Mohamed Belloumi: no structured culprit — reports only
  · GW6 error leading to a goal (SofaScore, match level — 2 conceded, the goal is not identified): Ainsley Maitland-Niles [CONFIRMED — SofaScore error flag]
  · GW6 other flags: James Tarkowski clearanceOffLine 1
- GW7 H v Chelsea 46' Pedro Neto: no structured culprit — reports only
- GW7 H v Chelsea 90' Pedro Neto: no structured culprit — reports only
  · GW7 other flags: Harrison Armstrong clearanceOffLine 1
- GW8 A v Arsenal 7' Ezri Konsa: no structured culprit — reports only
- GW8 A v Arsenal 68' Gabriel Magalhães: no structured culprit — reports only
  · GW8 error leading to a goal (SofaScore, match level — 2 conceded, the goal is not identified): Vitaliy Mykolenko [CONFIRMED — SofaScore error flag]

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 83 | 9.71 | 5 | 90 | 9.53 | 7 |
| corner | 15 | 2.06 | 2 | 20 | 2.56 | 1 |
| set piece | 9 | 0.77 | 1 | 5 | 0.51 | 1 |
| direct FK | 2 | 0.10 | 0 | 1 | 0.06 | 0 |
Totals per match: xG 1.58 (npxG 1.58) for, xGA 1.58 (np 1.58) against · dead-ball share of xG 23% for, 25% against · penalties won 0, conceded 0 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 15 shots, xG 2.06, 2 goals, headed 5: 6-yard box, central 2 shots, xG 0.91, 1 goals; 6-yard box, right 1 shots, xG 0.31, 0 goals; penalty area, central 2 shots, xG 0.29, 0 goals · against — 20 shots conceded, xG 2.56, 1 goals, headed 9: 6-yard box, central 10 shots, xG 2.33, 1 goals; outside box, central 3 shots, xG 0.07, 0 goals; penalty area, central 1 shots, xG 0.05, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 48 · corner shots conceded 20 (headed 9), xG 2.56, goals 1 · xG per corner faced 0.053 (rank 7 of 20, 1 = weakest) · weak zone: six-yard box (2.33 xG, 91% of theirs v 65% league) · signal: **neutral** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–9 [CONFIRMED — LiveScore Block L, 44 corners; side L/R as LiveScore records it; foot from SofaScore]: Kiernan Dewsbury-Hall 20 (0L/20R, 4 short, left foot); James Garner 20 (16L/4R, 3 short, right foot); Hayden Hackney 4 (4L/0R, right foot). First contact on corners that ended in a shot (Understat) — for: Kiernan Dewsbury-Hall 5 (1 headed) — 1 goal, Thierno Barry 2 (2 headed), Jarrad Branthwaite 2 (1 headed), Tyrique George 2, Michael Keane 1 (1 headed) · against (who beat them): Evanilson 2 (2 headed), Ezri Konsa Ngoyo 2 (1 headed) — 1 goal, António Silva 1 (1 headed), Nobel Mendy 1 (1 headed), Maxence Lacroix 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 39.3 (rank 16 of 20, 1 = highest line) · block length 21.0 (rank 12, 1 = most compact) · width 67.5. Per match: GW4 A v Tottenham Hotspur 4-1-4-1: back line 39, front 55, length 16, width 65 (38% poss); GW5 H v Ipswich Town 4-2-3-1: back line 39, front 58, length 19, width 70 (52% poss); GW6 A v Hull City 4-2-3-1: back line 42, front 62, length 20, width 69 (65% poss); GW7 H v Chelsea 4-2-3-1: back line 43, front 64, length 21, width 68 (47% poss); GW8 A v Arsenal 4-2-3-1: back line 32, front 54, length 23, width 66 (42% poss); GW9 A v Newcastle United 4-2-3-1: back line 41, front 63, length 22, width 64 (48% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 3 league match(es) v LB-coded sides — xG 1.68/match and 2.3 pts/match v 1.23 and 1.0 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW1 H v Crystal Palace 2–0, xG 1.12, box shots 11, poss 42%; GW5 H v Ipswich Town 1–0, xG 2.24, box shots 13, poss 52%; GW6 A v Hull City 2–2, xG 1.68, box shots 11, poss 65%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Grealish 2, Garner 2, George 1** · FPL editorial order: Garner #1, Dewsbury-Hall #2, Hackney #3
- Direct free-kick shooters: **Garner 2** · FPL order: Garner #1
- Penalties taken: **—** · FPL order: Barry #1, Garner #2
- Set-piece deliverers (assisted 'SetPiece' shots): **Dewsbury-Hall 2, Tarkowski 2, Garner 2**
- Corner targets (headed shots from corners): **Barry 2, Branthwaite 1, Keane 1, Dewsbury-Hall 1** · corner shots 15
- **DISAGREEMENT:** observed corner taker Jack Grealish (2) v FPL #1 Garner — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Kiernan Dewsbury-Hall 4 (0.45/90, percentile 87, 804 min) · club total 10 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 306 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 13.7, field tilt 51.2, possession 42.9%, box entries 13, direct speed 1.9, SCA 27; GW2: PPDA 9.03, field tilt 47.4, possession 41.8%, box entries 9, direct speed 3.55, SCA 25; GW3: PPDA 13.19, field tilt 59.2, possession 45.8%, box entries 12, direct speed 2.06, SCA 36; GW4: PPDA 17.73, field tilt 30.5, possession 38%, box entries 8, direct speed 2.27, SCA 23; GW5: PPDA 12.58, field tilt 59.9, possession 51.8%, box entries 14, direct speed 2.09, SCA 41; GW6: PPDA 9.08, field tilt 61.6, possession 64.7%, box entries 18, direct speed 2.34, SCA 27; GW7: PPDA 18.42, field tilt 51.1, possession 47.5%, box entries 10, direct speed 2.39, SCA 10; GW8: PPDA 14.5, field tilt 34.9, possession 41.6%, box entries 7, direct speed 1.97, SCA 14

**Zone 14 (C13, SofaScore heat-map points, 9 league matches):** for 27.4/match (rank 12 of 20) · conceded 36.2/match (rank 4 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 6.4/match · allowed 8.6/match · PPDA 14.8. Per match for/allowed: GW3 7/7; GW4 8/7; GW5 7/5; GW6 8/10; GW7 3/6; GW8 4/18 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 9 league matches, weights last-3 ×3 / older ×1
- GK: Jordan Pickford (15, 3/3)
- DEF: James Tarkowski (15, 3/3), Vitaliy Mykolenko (14, 3/3), Merlin Röhl (12, 3/3), Jarrad Branthwaite (12, 2/3)
- MID: Harrison Armstrong (15, 3/3), Kiernan Dewsbury-Hall (15, 3/3), James Garner (14, 3/3), Tyrique George (10, 2/3), Ainsley Maitland-Niles (6, 1/3)
- FWD: Thierno Barry (15, 3/3)
- Contested slots: M Ainsley Maitland-Niles 6 v Jack Grealish 5 · Excluded (FPL flag): none
- Absent last match (E12, SofaScore list): —
- Substitutions this season (C3): GW6 78' Ainsley Maitland-Niles→Jake O'Brien TACTICAL; GW6 78' Harrison Armstrong→Hayden Hackney TACTICAL; GW6 66' Brennan Johnson→Tyrique George TACTICAL; GW7 85' Harrison Armstrong→Christian Nørgaard CARD-RISK; GW7 85' Jack Grealish→Brennan Johnson LATE; GW7 55' Ainsley Maitland-Niles→Tyrique George CHASING; GW8 86' Kiernan Dewsbury-Hall→Carlos Alcaraz LATE; GW8 74' Vitaliy Mykolenko→Hayden Hackney INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW8 72' Brennan Johnson→Tyler Dibling CHASING; GW9 90' Tyrique George→Hayden Hackney CARD-RISK; GW9 82' Jarrad Branthwaite→Michael Keane INJURY [ONE SOURCE: LiveScore 'knock'; SofaScore marked it regular; FPL shows him available]; GW9 80' Thierno Barry→Brennan Johnson TACTICAL

### First-choice players and absences (F14) — generated 2026-11-03 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Jordan Pickford | start weight 15 | OK | a | — | — |
| CB | James Tarkowski | start weight 15 | OK | a | Michael Keane | — |
| CB | Jarrad Branthwaite | start weight 12 | OK | a 100% | Michael Keane | — |
| xGI #1 | Thierno Barry | xGI 6.75 | OK | a | Harrison Armstrong | — |
| xGI #2 | Kiernan Dewsbury-Hall | xGI 2.88 | OK | a | Harrison Armstrong | — |
| Penalties #1 (FPL) | Barry | FPL order | OK | a | Garner | — |
| Direct FK #1 (FPL) | Garner | FPL order | OK | a 100% | — | — |
| Corners (observed) | Kiernan Dewsbury-Hall | 20 corners taken | OK | a | James Garner | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Crystal Palace: all started · GW2 A Bournemouth: all started · GW3 H Manchester United: all started · GW4 A Tottenham Hotspur: all started · GW5 H Ipswich Town: all started · GW6 A Hull City: all started · GW7 H Chelsea: all started · GW8 A Arsenal: Jarrad Branthwaite (did not start) · GW9 A Newcastle United: all started

### Next fixtures (all competitions)
- Fri 06 Nov 20:00 UTC · Premier League R10 · H v Coventry City
- Mon 23 Nov 20:00 UTC · Premier League R11 · A v Brentford
- Sun 29 Nov 12:00 UTC · Premier League R12 · H v Liverpool FC
- Wed 02 Dec 20:15 UTC · Premier League R13 · A v Aston Villa
- Sun 06 Dec 14:00 UTC · Premier League R14 · H v Fulham
- Sun 13 Dec 14:00 UTC · Premier League R15 · A v Brighton & Hove Albion

### FPL availability flags (players with league minutes this season)
Beto — Has joined Fiorentina permanently (0%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 H Crystal Palace 2–0 · xG 1.12–1.96 · poss 42% · 4-2-3-1 · scorers: Kiernan Dewsbury-Hall 42', Thierno Barry 53'
- GW2 A Bournemouth 1–1 · xG 1.84–2.16 · poss 41% · 4-2-3-1 · scorers: James Tarkowski 90'
- GW3 H Manchester United 2–2 · xG 1.01–0.69 · poss 45% · 4-2-3-1 · scorers: Tyrique George 83', Ainsley Maitland-Niles 90'
- GW4 A Tottenham Hotspur 0–0 · xG 1.11–0.69 · poss 38% · 4-1-4-1 · scorers: none
- GW5 H Ipswich Town 1–0 · xG 2.24–1.44 · poss 52% · 4-2-3-1 · scorers: Thierno Barry 11'
- GW6 A Hull City 2–2 · xG 1.68–1.33 · poss 65% · 4-2-3-1 · scorers: Kiernan Dewsbury-Hall 55', Thierno Barry 68'
- GW7 H Chelsea 0–2 · xG 0.43–1.47 · poss 47% · 4-2-3-1 · scorers: none
- GW8 A Arsenal 0–2 · xG 0.63–1.96 · poss 42% · 4-2-3-1 · scorers: none
- GW9 A Newcastle United 1–0 · xG 2.34–1.29 · poss 48% · 4-2-3-1 · scorers: Thierno Barry 49'
### Corner takers observed (LiveScore Block L)
- Kiernan Dewsbury-Hall: 20 corners (0 left, 20 right, 4 short)
- James Garner: 20 corners (16 left, 4 right, 3 short)
- Hayden Hackney: 4 corners (4 left, 0 right)
