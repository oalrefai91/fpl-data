# Everton — data doc
*Feeder-written (2026-11-10 07:41 UTC); do not edit. Narrative: `profiles/teams/everton.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-10 07:41 UTC)
**Manager:** David Moyes · **Venue:** Hill Dickinson Stadium · **SofaScore:** https://www.sofascore.com/football/team/everton/48 · **FPL code:** EVE
**Table:** 6th, 16 pts (4W 4D 2L, GF 12 GA 10) · Home 6th (3-1-1, 8:5) · Away 8th (1-3-1, 4:5)
**Standing context (F15):** 28 league games left · points v 4th -2, v 5th +0, v 17th (last safe) +7, v 18th +8 · goal difference +2
**Suspension watch (D7, all players of the club):** Garner — 🟨 2 from a ban (3/5); Armstrong — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 10 league matches):** goals after 75′ — for 4/12 (33%), against 2/10 (20%) · scored first 3, conceded first 6 (60% of matches), goalless 1 · points from losing positions 6 of 18 (6 matches behind at some point) · points from winning positions 13 of 15 (5 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Branthwaite (DEF) 10.1/90, hit 5/9; Tarkowski (DEF) 9.8/90, hit 5/10; Garner (MID) 11.5/90, hit 3/10; Mykolenko (DEF) 7.6/90, hit 3/9; Armstrong (MID) 8.9/90, hit 2/10; O'Brien (DEF) 8.4/90, hit 1/6
**Manager tenure (F13, SofaScore):** David Moyes since 11 Jan 2025 · 72 matches in charge, all competitions (27W 21D 24L) · 10 league matches this season · contract to — · previous club West Ham United · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Liverpool FC — last 4: Apr 2026 Premier League Everton 1–2 Liverpool FC (yellows 2–0, xG 0.79–1.45); Sep 2025 Premier League Liverpool FC 2–1 Everton (yellows 2–3, xG 0.90–0.70); Apr 2025 Premier League Liverpool FC 1–0 Everton (yellows 2–2, xG 1.47–0.67); Feb 2025 Premier League Everton 2–2 Liverpool FC (yellows 4–4, reds 1–1, xG 0.95–0.62) · 19 yellows in 4 | v Manchester United — last 4: Sep 2026 Premier League Everton 2–2 Manchester United (yellows 3–3, xG 1.01–0.69); Feb 2026 Premier League Everton 0–1 Manchester United (yellows 2–3, xG 0.63–1.27); Nov 2025 Premier League Manchester United 0–1 Everton (yellows 2–0, reds 0–1, xG 1.71–0.21); Feb 2025 Premier League Everton 2–2 Manchester United (yellows 4–1, xG 1.91–0.41) · 18 yellows in 4
**Archetype (F5):** used **TR** — derived TR [DERIVED] · signals, last 6 league matches: possession 50.7%, PPDA 12.9 (Understat, 4 matches; lower = harder press), opponent offsides forced 0.3/match (line height), fast breaks 0.6/match (season), both sides' xG 2.91/match (openness) · note: possession 50.7 v 52; computed from 4 of 6 GWs (no PPDA/possession for GW9, GW10). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 8 (permanent 6, loan 1, free 0, loan returns 1) · out 12 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 10 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 13.82 | 12 | Big chances against | 26 | 11 |
| xGOT | 13.56 | 9 | Box shots against | 90 | 13 |
| xA | 9.10 | 10 | Corners against | 54 | 18 |
| Shots | 140 | 8 | Crosses faced | 179 | 13 |
| SoT | 50 | 5 | Dribbled past | 68 | 7 |
| Big chances | 33 | 4 | Errors→shot | 5 | 5 |
| Shots in box | 101 | 7 | GK goals prevented | 1.05 | 7 |
| Corners | 46 | 10 | Clearances | 266 | 10 |
| Crosses | 188 | 7 | Tackles | 160 | 10 |
| Fast breaks | 6 | 17 | Interceptions | 86 | 10 |
| FK shots | 3 | 10 | Def. contributions | 567 | 7 |
| Possession % | 47 | 13 | Aerial % | 54.87 | 2 |
| Pass % | 83.06 | 9 | Duel % | 54.06 | 1 |
| Long balls | 294 | 14 | Fouls | 84 | 1 |
| Dribbles | 68 | 13 | Yellows | 18 | 6 |
| Shots against | 148 | 13 | Km covered | 1139 | 13 |
| SoT against | 40 | 10 | Sprints | 1030 | 18 |
Per match: xG 1.38 · xGOT 1.36 · shots 14.0 · shots against 14.8 · big chances 3.3 for / 2.6 against · corners 4.6 / 5.4 · crosses 18.8 / 17.9 · possession 47.0%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | H | Ipswich Town | 1–0 | 2.24/2.59 | 1.44/1.10 | 52 | 21/13 | 2/4 | 13/9 | 8/4 | 5/1 | 4/4 | 16/4 v 13/3 | 0/1 |
| 6 | A | Hull City | 2–2 | 1.68/2.97 | 1.33/1.53 | 65 | 15/9 | 7/5 | 11/9 | 3/2 | 8/2 | 6/7 | 22/5 v 23/3 | 1/4 |
| 7 | H | Chelsea | 0–2 | 0.43/0.57 | 1.47/1.61 | 47 | 6/18 | 5/7 | 6/10 | 1/5 | 2/3 | 5/7 | 20/3 v 14/3 | 1/4 |
| 8 | A | Arsenal | 0–2 | 0.63/0.72 | 1.96/2.29 | 42 | 8/20 | 3/4 | 6/12 | 2/10 | 2/3 | 3/12 | 16/2 v 23/5 | 0/1 |
| 9 | A | Newcastle United | 1–0 | 2.34/— | 1.29/— | 48 | 16/17 | 5/2 | 11/7 | 1/6 | 4/2 | 5/4 | 22/7 v 24/7 | 0/2 |
| 10 | H | Coventry City | 3–1 | 1.43/— | 1.21/— | 50 | 15/15 | 7/4 | 13/8 | 3/3 | 5/3 | 2/2 | 20/6 v 13/3 | 0/1 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | H | Ipswich Town | 1–0 | 4-2-3-1 | 6/12 | 2/3 | 0/1 | 513/472 | 63/53 | Nørgaard (Muscle Injury), Röhl (Knock Injury; doubtful) | Taylor (Knee Injury) | Stuart Attwell |
| 6 | A | Hull City | 2–2 | 4-2-3-1 | 4/15 | 0/2 | 0/0 | 595/306 | 63/51 | Mykolenko (Knock Injury; doubtful) | Hughes (Groin Injury), Gyabi (Groin Injury), Matazo (Cruciate Ligament Injury), Ansah (Back Injury), Butland (Elbow Injury), Targett (Ankle Injury) | Michael Salisbury |
| 7 | H | Chelsea | 0–2 | 4-2-3-1 | 8/15 | 3/4 | 0/0 | 408/463 | 56/55 | — | Emegha (Hamstring Injury), Gittens (Ankle Injury), James (Knee Injury) | Paul Tierney |
| 8 | A | Arsenal | 0–2 | 4-2-3-1 | 13/11 | 3/1 | 0/0 | 372/518 | 48/65 | — | Saka (Muscle Injury), Tzolis (Hamstring Injury), Saliba (Back Injury) | Tony Harrington |
| 9 | A | Newcastle United | 1–0 | 4-2-3-1 | 9/13 | 2/4 | 0/1 | 396/428 | 61/70 | — | Jaouen (Hamstring Injury), Livramento (Knock Injury), Miley (Knock Injury; doubtful), Fernández-Pardo (Illness; doubtful) | John Brooks |
| 10 | H | Coventry City | 3–1 | 4-2-3-1 | 10/6 | 1/1 | 0/0 | 438/451 | 43/56 | Grealish (club decision) | Amenda (Calf Injury), Thomas (Leg Injury), Wright (Muscle Injury), Eccles (Knock Injury), Woolfenden (Knee Injury), Onyeka (Strain Injury; doubtful) | Stuart Attwell |
Per match: fouls 8.4 / 12.3 · yellows 1.80 / 2.20 · reds 0 / 2 (season) · offsides forced 0.5, committed 2.0 · crosses attempted 18.8 / faced 17.9. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 1.25 for / 1.35 against per match · Away (5): xG 1.52 / 1.49. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW10 H v Coventry City 3–1 (Fri 06 Nov 20:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Pickford | G | 90 | 6.9 | 0.00 | 0.01 | 0 | 0 | 2 | 0 | 49 |
| Merlin Röhl | D | 73 | 7.3 | 0.00 | 0.12 | 2 | 0 | 5 | 4 | 44 |
| James Tarkowski | D | 90 | 6.5 | 0.00 | 0.00 | 0 | 0 | 4 | 0 | 39 |
| Jarrad Branthwaite | D | 89 | 7.7 | 0.00 | 0.10 | 1 | 0 | 11 | 1 | 69 |
| Vitaliy Mykolenko | D | 90 | 7.7 | 0.14 | 0.19 | 2 | 1 | 11 | 4 | 78 |
| Harrison Armstrong | M | 73 | 6.8 | 0.04 | 0.01 | 0 | 1 | 5 | 0 | 48 |
| James Garner | M | 90 | 6.7 | 0.00 | 0.05 | 0 | 0 | 7 | 2 | 77 |
| Tyler Dibling | M | 73 | 7.2 | 0.04 | 0.28 | 1 | 1 | 6 | 1 | 35 |
| Kiernan Dewsbury-Hall | M | 90 | 7.9 | 0.18 | 0.11 | 1 | 2 | 6 | 3 | 66 |
| Tyrique George | M | 89 | 7.3 | 0.07 | 0.51 | 2 | 3 | 5 | 4 | 66 |
| Thierno Barry | F | 90 | 8.6 | 0.92 | 0.10 | 1 | 6 | 2 | 0 | 36 |
Subs used: Jake O'Brien (17'), Hayden Hackney (17'), Brennan Johnson (17'), Michael Keane (8'), Carlos Alcaraz (1')
Goals: 52' Yann Gboho [opp]; 56' Thierno Barry (assist Vitaliy Mykolenko) [own]; 61' Thierno Barry [own]; 81' Kiernan Dewsbury-Hall (assist Thierno Barry) [own]
Substitutions (own): 73' Brennan Johnson for Tyler Dibling; 73' Hayden Hackney for Harrison Armstrong; 73' Jake O'Brien for Merlin Röhl; 89' Michael Keane for Jarrad Branthwaite; 90' Carlos Alcaraz for Tyrique George
Cards: 88' Caleb Yirenkyi (yellow, opp); 88' Jarrad Branthwaite (yellow, own)
**Baseline XI change vs GW9 (4-2-3-1 → 4-2-3-1):** in — Tyler Dibling; out — Jake O'Brien.

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
| 10 | H Coventry City | 52' | AGAINST | Yann Gboho | — | [no Understat] | — |
| 10 | H Coventry City | 56' | FOR | Thierno Barry | Vitaliy Mykolenko | [no Understat] | — |
| 10 | H Coventry City | 61' | FOR | Thierno Barry | — | [no Understat] | — |
| 10 | H Coventry City | 81' | FOR | Kiernan Dewsbury-Hall | Thierno Barry | [no Understat] | — |
Scored 12: open play 5, [no Understat] 4, corner 2, set piece 1 · Conceded 10: open play 6, [unmatched] 2, set piece 1, [no Understat] 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW8 AG v Arsenal 7' Ezri Konsa (assist Viktor Gyoekeres): G O O O A A A L - Ezri Konsa scores with the right foot! · before: 7' Gabriel from Arsenal sees his header hit the crossbar after the keeper parries the ball. ‹ 7' Martin Oedegaard from Arsenal swings in the corner from the right. ‹ 7' Vitaliy Mykolenko from Everton intercepts a cross aimed towards the box.
- GW8 AG v Arsenal 68' Gabriel Magalhães (assist Ben White, key pass Bruno Guimaraes): G O O O A A A L - Gabriel from Arsenal heads the ball home! · before: 68' Ben White creates a scoring opportunity for his teammate ‹ 68' Jake O'Brien from Everton intercepts a cross aimed towards the box. ‹ 68' Declan Rice swings in the ball from a corner on the left, but it is nowhere near a teammate
- GW9 FOR v Newcastle United 49' Thierno Barry: GOAL! It's an easy finish as Thierno Barry from Everton taps the ball into an open goal with the right foot! · before: 49' Good effort by Tyrique George as he directs a shot on target, but the keeper saves it ‹ 49' Kiernan Dewsbury-Hall creates a scoring opportunity for his teammate ‹ 49' Everton with a potentially dangerous attack.
- GW10 AG v Coventry City 52' Yann Gboho: G O O O O O A A L - Yann Gboho finds the net with the right foot! · before: 52' Tatsuhiro Sakamoto wins an air challenge against Vitaliy Mykolenko ‹ 51' Thierno Barry is penalised for pushing Victor Torp. ‹ 51' Merlin Roehl wins an air challenge against Jay Dasilva
- GW10 FOR v Coventry City 56' Thierno Barry (assist Vitaliy Mykolenko): G O O O A A A L - Thierno Barry from Everton heads the ball home! · before: 56' The cross by Vitaliy Mykolenko from Everton successfully finds a teammate in the box. ‹ 56' Jay Dasilva from Coventry intercepts a cross aimed towards the box. ‹ 56' A chance presents itself to Tyrique George from Everton but his header goes wide
- GW10 FOR v Coventry City 61' Thierno Barry: G O O O O O A A L - Thierno Barry finds the net with the left foot! · before: 61' Ethan Pinnock relieves the pressure with a clearance ‹ 61' The cross by Tyrique George from Everton successfully finds a teammate in the box. ‹ 60' Ethan Pinnock successfully blocks the shot
- GW10 FOR v Coventry City 81' Kiernan Dewsbury-Hall (assist Thierno Barry, key pass Vitaliy Mykolenko): G O O O A A A L - Kiernan Dewsbury-Hall scores with the left foot! · before: 80' Brandon Thomas-Asante relieves the pressure with a clearance ‹ 80' Everton with a potentially dangerous attack. ‹ 80' Vitaliy Mykolenko relieves the pressure with a clearance

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
- GW10 H v Coventry City 52' Yann Gboho: no structured culprit — reports only

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

**Corners (E10 data layer):** observed takers GW1–10 [CONFIRMED — LiveScore Block L, 46 corners; side L/R as LiveScore records it; foot from SofaScore]: James Garner 22 (18L/4R, 4 short, right foot); Kiernan Dewsbury-Hall 20 (0L/20R, 4 short, left foot); Hayden Hackney 4 (4L/0R, right foot). First contact on corners that ended in a shot (Understat) — for: Kiernan Dewsbury-Hall 5 (1 headed) — 1 goal, Thierno Barry 2 (2 headed), Jarrad Branthwaite 2 (1 headed), Tyrique George 2, Michael Keane 1 (1 headed) · against (who beat them): Evanilson 2 (2 headed), Ezri Konsa Ngoyo 2 (1 headed) — 1 goal, António Silva 1 (1 headed), Nobel Mendy 1 (1 headed), Maxence Lacroix 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 39.1 (rank 15 of 20, 1 = highest line) · block length 21.1 (rank 10, 1 = most compact) · width 67.6. Per match: GW5 H v Ipswich Town 4-2-3-1: back line 39, front 58, length 19, width 70 (52% poss); GW6 A v Hull City 4-2-3-1: back line 42, front 62, length 20, width 69 (65% poss); GW7 H v Chelsea 4-2-3-1: back line 43, front 64, length 21, width 68 (47% poss); GW8 A v Arsenal 4-2-3-1: back line 32, front 54, length 23, width 66 (42% poss); GW9 A v Newcastle United 4-2-3-1: back line 41, front 63, length 22, width 64 (48% poss); GW10 H v Coventry City 4-2-3-1: back line 38, front 60, length 22, width 68 (50% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 4 league match(es) v LB-coded sides — xG 1.62/match and 2.5 pts/match v 1.23 and 1.0 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW1 H v Crystal Palace 2–0, xG 1.12, box shots 11, poss 42%; GW5 H v Ipswich Town 1–0, xG 2.24, box shots 13, poss 52%; GW6 A v Hull City 2–2, xG 1.68, box shots 11, poss 65%; GW10 H v Coventry City 3–1, xG 1.43, box shots 13, poss 50%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Grealish 2, Garner 2, George 1** · FPL editorial order: Garner #1, Dewsbury-Hall #2, Hackney #3
- Direct free-kick shooters: **Garner 2** · FPL order: Garner #1
- Penalties taken: **—** · FPL order: Barry #1, Garner #2
- Set-piece deliverers (assisted 'SetPiece' shots): **Dewsbury-Hall 2, Tarkowski 2, Garner 2**
- Corner targets (headed shots from corners): **Barry 2, Branthwaite 1, Keane 1, Dewsbury-Hall 1** · corner shots 15
- **DISAGREEMENT:** observed corner taker Jack Grealish (2) v FPL #1 Garner — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Kiernan Dewsbury-Hall 4 (0.40/90, percentile 86, 894 min); Merlin Röhl 2 (0.30/90, percentile 81, 594 min) · club total 14 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 318 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 13.7, field tilt 51.2, possession 42.9%, box entries 13, direct speed 1.9, SCA 27; GW2: PPDA 9.03, field tilt 47.4, possession 41.8%, box entries 9, direct speed 3.55, SCA 25; GW3: PPDA 13.19, field tilt 59.2, possession 45.8%, box entries 12, direct speed 2.06, SCA 36; GW4: PPDA 17.73, field tilt 30.5, possession 38%, box entries 8, direct speed 2.27, SCA 23; GW5: PPDA 12.58, field tilt 59.9, possession 51.8%, box entries 14, direct speed 2.09, SCA 41; GW6: PPDA 9.08, field tilt 61.6, possession 64.7%, box entries 18, direct speed 2.34, SCA 27; GW7: PPDA 18.42, field tilt 51.1, possession 47.5%, box entries 10, direct speed 2.39, SCA 10; GW8: PPDA 14.5, field tilt 34.9, possession 41.6%, box entries 7, direct speed 1.97, SCA 14; GW9: PPDA 14.36, field tilt 50.6, possession 48.4%, box entries 13, direct speed 2.27, SCA 32; GW10: PPDA 11.17, field tilt 48.6, possession 49.5%, box entries 12, direct speed 2.26, SCA 28

**Zone 14 (C13, SofaScore heat-map points, 10 league matches):** for 27.2/match (rank 12 of 20) · conceded 35.4/match (rank 5 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 6.4/match · allowed 8.6/match · PPDA 14.8. Per match for/allowed: GW3 7/7; GW4 8/7; GW5 7/5; GW6 8/10; GW7 3/6; GW8 4/18 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: Jordan Pickford (16, 3/3)
- DEF: James Tarkowski (16, 3/3), Vitaliy Mykolenko (15, 3/3), Merlin Röhl (13, 3/3), Jarrad Branthwaite (13, 2/3)
- MID: Harrison Armstrong (16, 3/3), Kiernan Dewsbury-Hall (16, 3/3), James Garner (15, 3/3), Tyrique George (13, 3/3), Ainsley Maitland-Niles (4, 0/3)
- FWD: Thierno Barry (16, 3/3)
- Contested slots: M Ainsley Maitland-Niles 4 v Jack Grealish 3 · Excluded (FPL flag): none
- Absent last match (E12, SofaScore list): Grealish (club decision)
- Substitutions this season (C3): GW7 55' Ainsley Maitland-Niles→Tyrique George CHASING; GW8 86' Kiernan Dewsbury-Hall→Carlos Alcaraz LATE; GW8 74' Vitaliy Mykolenko→Hayden Hackney INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW8 72' Brennan Johnson→Tyler Dibling CHASING; GW9 90' Tyrique George→Hayden Hackney CARD-RISK; GW9 82' Jarrad Branthwaite→Michael Keane INJURY [ONE SOURCE: LiveScore 'knock'; SofaScore marked it regular; FPL shows him available]; GW9 80' Thierno Barry→Brennan Johnson TACTICAL; GW10 90' Tyrique George→Carlos Alcaraz LATE; GW10 89' Jarrad Branthwaite→Michael Keane CARD-RISK; GW10 73' Tyler Dibling→Brennan Johnson TACTICAL; GW10 73' Harrison Armstrong→Hayden Hackney TACTICAL; GW10 73' Merlin Röhl→Jake O'Brien TACTICAL

### First-choice players and absences (F14) — generated 2026-11-10 07:41 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Jordan Pickford | start weight 16 | OK | a | — | — |
| CB | James Tarkowski | start weight 16 | OK | a | Michael Keane | — |
| CB | Jarrad Branthwaite | start weight 13 | OK | a 100% | Michael Keane | — |
| xGI #1 | Thierno Barry | xGI 7.77 | OK | a | Tyrique George | — |
| xGI #2 | Kiernan Dewsbury-Hall | xGI 3.17 | OK | a | Tyrique George | — |
| Penalties #1 (FPL) | Barry | FPL order | OK | a | Garner | — |
| Direct FK #1 (FPL) | Garner | FPL order | OK | a 100% | — | — |
| Corners (observed) | James Garner | 22 corners taken | OK | a 100% | Kiernan Dewsbury-Hall | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Crystal Palace: all started · GW2 A Bournemouth: all started · GW3 H Manchester United: all started · GW4 A Tottenham Hotspur: all started · GW5 H Ipswich Town: all started · GW6 A Hull City: all started · GW7 H Chelsea: all started · GW8 A Arsenal: Jarrad Branthwaite (did not start) · GW9 A Newcastle United: all started · GW10 H Coventry City: all started

### Next fixtures (all competitions)
- Mon 23 Nov 20:00 UTC · Premier League R11 · A v Brentford
- Sun 29 Nov 12:00 UTC · Premier League R12 · H v Liverpool FC
- Wed 02 Dec 20:15 UTC · Premier League R13 · A v Aston Villa
- Sun 06 Dec 14:00 UTC · Premier League R14 · H v Fulham
- Sun 13 Dec 14:00 UTC · Premier League R15 · A v Brighton & Hove Albion
- Thu 17 Dec 20:00 UTC · EFL Cup R27 · A v Fleetwood Town

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
- GW10 H Coventry City 3–1 · xG 1.43–1.21 · poss 50% · 4-2-3-1 · scorers: Thierno Barry 56', Thierno Barry 61', Kiernan Dewsbury-Hall 81'
### Corner takers observed (LiveScore Block L)
- James Garner: 22 corners (18 left, 4 right, 4 short)
- Kiernan Dewsbury-Hall: 20 corners (0 left, 20 right, 4 short)
- Hayden Hackney: 4 corners (4 left, 0 right)
