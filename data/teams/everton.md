# Everton — data doc
*Feeder-written (2026-10-27 07:42 UTC); do not edit. Narrative: `profiles/teams/everton.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-10-27 07:42 UTC)
**Manager:** David Moyes · **Venue:** Hill Dickinson Stadium · **SofaScore:** https://www.sofascore.com/football/team/everton/48 · **FPL code:** EVE
**Table:** 11th, 10 pts (2W 4D 2L, GF 8 GA 9) · Home 6th (2-1-1, 5:4) · Away 17th (0-3-1, 3:5)
**Standing context (F15):** 30 league games left · points v 4th -5, v 5th -3, v 17th (last safe) +3, v 18th +4 · goal difference -1
**Suspension watch (D7, all players of the club):** Garner — 🟨 2 from a ban (3/5); Armstrong — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 8 league matches):** goals after 75′ — for 3/8 (38%), against 2/9 (22%) · scored first 2, conceded first 5 (62% of matches), goalless 1 · points from losing positions 3 of 15 (5 matches behind at some point) · points from winning positions 7 of 9 (3 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Tarkowski (DEF) 10.6/90, hit 5/8; Branthwaite (DEF) 10.3/90, hit 4/7; Garner (MID) 11.7/90, hit 3/8; Armstrong (MID) 9.3/90, hit 2/8; Mykolenko (DEF) 7.2/90, hit 2/7
**Manager tenure (F13, SofaScore):** David Moyes since 11 Jan 2025 · 71 matches in charge, all competitions (26W 21D 24L) · 8 league matches this season · contract to — · previous club West Ham United · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Liverpool FC — last 4: Apr 2026 Premier League Everton 1–2 Liverpool FC (yellows 2–0, xG 0.79–1.45); Sep 2025 Premier League Liverpool FC 2–1 Everton (yellows 2–3, xG 0.90–0.70); Apr 2025 Premier League Liverpool FC 1–0 Everton (yellows 2–2, xG 1.47–0.67); Feb 2025 Premier League Everton 2–2 Liverpool FC (yellows 4–4, reds 1–1, xG 0.95–0.62) · 19 yellows in 4 | v Manchester United — last 4: Sep 2026 Premier League Everton 2–2 Manchester United (yellows 3–3, xG 1.01–0.69); Feb 2026 Premier League Everton 0–1 Manchester United (yellows 2–3, xG 0.63–1.27); Nov 2025 Premier League Manchester United 0–1 Everton (yellows 2–0, reds 0–1, xG 1.71–0.21); Feb 2025 Premier League Everton 2–2 Manchester United (yellows 4–1, xG 1.91–0.41) · 18 yellows in 4
**Archetype (F5):** used **TR** — derived TR [DERIVED] · signals, last 6 league matches: possession 48.2%, PPDA 14.3 (Understat, 6 matches; lower = harder press), opponent offsides forced 0.8/match (line height), fast breaks 0.4/match (season), both sides' xG 2.45/match (openness) · note: possession 48.2 v 47.5. Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap).
**Squad changes (F20, since 01 Jun 2026):** in 8 (permanent 6, loan 1, free 0, loan returns 1) · out 12 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 8 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 10.06 | 15 | Big chances against | 21 | 11 |
| xGOT | 9.09 | 12 | Box shots against | 75 | 12 |
| xA | 6.64 | 10 | Corners against | 48 | 19 |
| Shots | 109 | 10 | Crosses faced | 142 | 11 |
| SoT | 38 | 7 | Dribbled past | 59 | 11 |
| Big chances | 24 | 5 | Errors→shot | 5 | 6 |
| Shots in box | 77 | 7 | GK goals prevented | 1.11 | 5 |
| Corners | 39 | 8 | Clearances | 207 | 13 |
| Crosses | 146 | 9 | Tackles | 129 | 11 |
| Fast breaks | 3 | 17 | Interceptions | 71 | 9 |
| FK shots | 2 | 11 | Def. contributions | 453 | 8 |
| Possession % | 46.50 | 12 | Aerial % | 51.20 | 6 |
| Pass % | 83.70 | 7 | Duel % | 52.56 | 2 |
| Long balls | 236 | 14 | Fouls | 65 | 1 |
| Dribbles | 48 | 15 | Yellows | 15 | 7 |
| Shots against | 116 | 13 | Km covered | 908 | 14 |
| SoT against | 34 | 10 | Sprints | 812 | 18 |
Per match: xG 1.26 · xGOT 1.14 · shots 13.6 · shots against 14.5 · big chances 3.0 for / 2.6 against · corners 4.9 / 6.0 · crosses 18.2 / 17.8 · possession 46.5%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Manchester United | 2–2 | 1.01/1.06 | 0.69/0.87 | 45 | 18/14 | 6/3 | 14/6 | 7/6 | 1/1 | 4/3 | 21/4 v 11/4 | 1/3 |
| 4 | A | Tottenham Hotspur | 0–0 | 1.11/1.60 | 0.69/0.74 | 38 | 12/14 | 3/2 | 9/8 | 6/8 | 2/1 | 6/5 | 17/4 v 23/5 | 2/1 |
| 5 | H | Ipswich Town | 1–0 | 2.24/2.59 | 1.44/1.10 | 52 | 21/13 | 2/4 | 13/9 | 8/4 | 5/1 | 4/4 | 16/4 v 13/3 | 0/1 |
| 6 | A | Hull City | 2–2 | 1.68/2.97 | 1.33/1.53 | 65 | 15/9 | 7/5 | 11/9 | 3/2 | 8/2 | 6/7 | 22/5 v 23/3 | 1/4 |
| 7 | H | Chelsea | 0–2 | 0.43/0.57 | 1.47/1.61 | 47 | 6/18 | 5/7 | 6/10 | 1/5 | 2/3 | 5/7 | 20/3 v 14/3 | 1/4 |
| 8 | A | Arsenal | 0–2 | 0.63/0.72 | 1.96/2.29 | 42 | 8/20 | 3/4 | 6/12 | 2/10 | 2/3 | 3/12 | 16/2 v 23/5 | 0/1 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Manchester United | 2–2 | 4-2-3-1 | 7/11 | 3/3 | 0/0 | 418/527 | 49/47 | Nørgaard (Muscle Injury) | Diallo (Knock Injury), Baleba (Ankle Injury), Ugarte (Cruciate Ligament Injury) | John Brooks |
| 4 | A | Tottenham Hotspur | 0–0 | 4-1-4-1 | 8/14 | 2/0 | 0/0 | 381/644 | 37/78 | Nørgaard (Muscle Injury) | Richarlison (coach decision), Kulusevski (Knee Injury), Mudryk (Ankle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | Darren England |
| 5 | H | Ipswich Town | 1–0 | 4-2-3-1 | 6/12 | 2/3 | 0/1 | 513/472 | 63/53 | Nørgaard (Muscle Injury), Röhl (Knock Injury; doubtful) | Taylor (Knee Injury) | Stuart Attwell |
| 6 | A | Hull City | 2–2 | 4-2-3-1 | 4/15 | 0/2 | 0/0 | 595/306 | 63/51 | Mykolenko (Knock Injury; doubtful) | Hughes (Groin Injury), Gyabi (Groin Injury), Matazo (Cruciate Ligament Injury), Ansah (Back Injury), Butland (Elbow Injury), Targett (Ankle Injury) | Michael Salisbury |
| 7 | H | Chelsea | 0–2 | 4-2-3-1 | 8/15 | 3/4 | 0/0 | 408/463 | 56/55 | — | Emegha (Hamstring Injury), Gittens (Ankle Injury), James (Knee Injury) | Paul Tierney |
| 8 | A | Arsenal | 0–2 | 4-2-3-1 | 13/11 | 3/1 | 0/0 | 372/518 | 48/65 | — | Saka (Muscle Injury), Tzolis (Hamstring Injury), Saliba (Back Injury) | Tony Harrington |
Per match: fouls 8.1 / 13.0 · yellows 1.88 / 2.12 · reds 0 / 1 (season) · offsides forced 0.6, committed 2.1 · crosses attempted 18.2 / faced 17.8. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 1.20 for / 1.39 against per match · Away (4): xG 1.31 / 1.54. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW8 A v Arsenal 0–2 (Sat 24 Oct 14:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Pickford | G | 90 | 7.2 | 0.00 | 0.01 | 0 | 0 | 4 | 0 | 57 |
| Merlin Röhl | D | 90 | 6.3 | 0.00 | 0.01 | 0 | 0 | 4 | 3 | 44 |
| James Tarkowski | D | 90 | 7.6 | 0.00 | 0.01 | 0 | 0 | 10 | 0 | 61 |
| Jake O'Brien | D | 90 | 6.9 | 0.00 | 0.00 | 0 | 0 | 13 | 0 | 45 |
| Vitaliy Mykolenko | D | 74 | 6.4 | 0.00 | 0.01 | 0 | 0 | 6 | 1 | 42 |
| Harrison Armstrong | M | 90 | 7.6 | 0.05 | 0.16 | 1 | 1 | 10 | 0 | 55 |
| James Garner | M | 90 | 6.9 | 0.03 | 0.08 | 1 | 1 | 5 | 2 | 57 |
| Brennan Johnson | M | 72 | 6.2 | 0.00 | 0.00 | 0 | 0 | 1 | 1 | 9 |
| Kiernan Dewsbury-Hall | M | 86 | 6.7 | 0.06 | 0.02 | 1 | 1 | 4 | 4 | 47 |
| Tyrique George | M | 90 | 6.9 | 0.03 | 0.23 | 2 | 1 | 3 | 4 | 46 |
| Thierno Barry | F | 90 | 7.7 | 0.38 | 0.01 | 1 | 2 | 6 | 0 | 40 |
Subs used: Tyler Dibling (18'), Hayden Hackney (16'), Carlos Alcaraz (13')
Goals: 7' Ezri Konsa (assist Viktor Gyökeres) [opp]; 68' Gabriel Magalhães (assist Ben White) [opp]
Substitutions (own): 72' Tyler Dibling for Brennan Johnson; 74' Hayden Hackney for Vitaliy Mykolenko [injury]; 86' Carlos Alcaraz for Kiernan Dewsbury-Hall
Cards: -5' booking with no player named — staff card (yellow, own; not in SofaScore's card count, no FPL effect); manager/staff booking: Mikel Arteta 64' [LiveScore] (opp; no FPL effect); 45' Vitaliy Mykolenko (yellow, own); 58' Myles Lewis-Skelly (yellow, opp); 66' James Garner (yellow, own); 79' James Tarkowski (yellow, own)
**Baseline XI change vs GW7 (4-2-3-1 → 4-2-3-1):** in — Brennan Johnson, Jake O'Brien, Tyrique George; out — Ainsley Maitland-Niles, Jack Grealish, Jarrad Branthwaite.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 3 | H Manchester United | 46' | AGAINST | Bryan Mbeumo | Kobbie Mainoo | open play | 0.04 |
| 3 | H Manchester United | 83' | FOR | Tyrique George | Hayden Hackney | open play | 0.05 |
| 3 | H Manchester United | 88' | AGAINST | Benjamin Šeško | Luke Shaw | open play | 0.41 |
| 3 | H Manchester United | 90' | FOR | Ainsley Maitland-Niles | — | open play | 0.03 |
| 5 | H Ipswich Town | 11' | FOR | Thierno Barry | James Tarkowski | open play | 0.35 |
| 6 | A Hull City | 48' | AGAINST | Joe Gelhardt | Sorba Thomas | open play | 0.55 |
| 6 | A Hull City | 55' | FOR | Kiernan Dewsbury-Hall | Ainsley Maitland-Niles | corner | 0.34 |
| 6 | A Hull City | 68' | FOR | Thierno Barry | Kiernan Dewsbury-Hall | open play | 0.33 |
| 6 | A Hull City | 74' | AGAINST | Mohamed Belloumi | Elliot Stroud | open play | 0.09 |
| 7 | H Chelsea | 46' | AGAINST | Pedro Neto | — | open play | 0.42 |
| 7 | H Chelsea | 90' | AGAINST | Pedro Neto | — | set piece | 0.08 |
| 8 | A Arsenal | 7' | AGAINST | Ezri Konsa | Viktor Gyökeres | [unmatched] | — |
| 8 | A Arsenal | 68' | AGAINST | Gabriel Magalhães | Ben White | [unmatched] | — |
Scored 8: open play 5, corner 2, set piece 1 · Conceded 9: open play 6, [unmatched] 2, set piece 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW6 AG v Hull City 48' Joe Gelhardt (assist Sorba Thomas): G O O O A A A L - Joe Gelhardt scores with the left foot! · before: 48' Sorba Thomas creates a scoring opportunity for his teammate ‹ 48' Hull with a potentially dangerous attack. ‹ 48' Nobel Mendy relieves the pressure with a clearance
- GW6 FOR v Hull City 55' Kiernan Dewsbury-Hall (assist Ainsley Maitland-Niles, key pass Jack Grealish): G O O O A A A L - Kiernan Dewsbury-Hall from Everton heads the ball home! · before: 55' The cross by Ainsley Maitland-Niles from Everton successfully finds a teammate in the box. ‹ 55' Kiernan Dewsbury-Hall swings in the ball from a corner on the right, but it is nowhere near ‹ 54' John Egan from Hull intercepts a cross aimed towards the box.
- GW6 FOR v Hull City 68' Thierno Barry (assist Kiernan Dewsbury-Hall): G O O O A A A L - Thierno Barry scores with the right foot! · before: 68' Kiernan Dewsbury-Hall makes the tackle and wins possession for his team ‹ 68' Sorba Thomas could cost his team a goal after a defensive blunder. ‹ 68' Everton with a potentially dangerous attack.
- GW6 AG v Hull City 74' Mohamed Belloumi (assist Elliot Stroud, key pass Sorba Thomas): G O O O A A A L - Mohamed Belloumi scores with the left foot! · before: 74' Elliot Stroud creates a scoring opportunity for his teammate ‹ 74' Hull start a counter attack. ‹ 74' Elliot Stroud relieves the pressure with a clearance
- GW7 AG v Chelsea 46' Pedro Neto: G O O O O O A A L - Pedro Neto finds the net with the left foot! · before: 46' Jorrel Hato creates a scoring opportunity for his teammate ‹ 46' Harrison Armstrong wins an air challenge against Morgan Rogers ‹ 46' The second half is underway.
- GW7 AG v Chelsea 90' Pedro Neto: G O O O A A A L - Pedro Neto reacts first on the loose ball and puts it away with the left! · before: 90' Jordan Henderson takes the free-kick but it is blocked by the wall ‹ 89' Christian Noergaard pulls a player from the opposite team by the shirt and is booked. ‹ 89' Christian Noergaard from Everton goes a bit too far there as he pulls down Cole Palmer
- GW8 AG v Arsenal 7' Ezri Konsa (assist Viktor Gyoekeres): G O O O A A A L - Ezri Konsa scores with the right foot! · before: 7' Gabriel from Arsenal sees his header hit the crossbar after the keeper parries the ball. ‹ 7' Martin Oedegaard from Arsenal swings in the corner from the right. ‹ 7' Vitaliy Mykolenko from Everton intercepts a cross aimed towards the box.
- GW8 AG v Arsenal 68' Gabriel Magalhães (assist Ben White, key pass Bruno Guimaraes): G O O O A A A L - Gabriel from Arsenal heads the ball home! · before: 68' Ben White creates a scoring opportunity for his teammate ‹ 68' Jake O'Brien from Everton intercepts a cross aimed towards the box. ‹ 68' Declan Rice swings in the ball from a corner on the left, but it is nowhere near a teammate

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW3 H v Manchester United 46' Bryan Mbeumo: no structured culprit — reports only
- GW3 H v Manchester United 88' Benjamin Šeško: no structured culprit — reports only
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

**Corners (E10 data layer):** observed takers GW1–8 [CONFIRMED — LiveScore Block L, 39 corners; side L/R as LiveScore records it; foot from SofaScore]: James Garner 18 (14L/4R, 3 short, right foot); Kiernan Dewsbury-Hall 17 (0L/17R, 3 short, left foot); Hayden Hackney 4 (4L/0R, right foot). First contact on corners that ended in a shot (Understat) — for: Kiernan Dewsbury-Hall 5 (1 headed) — 1 goal, Thierno Barry 2 (2 headed), Jarrad Branthwaite 2 (1 headed), Tyrique George 2, Michael Keane 1 (1 headed) · against (who beat them): Evanilson 2 (2 headed), Ezri Konsa Ngoyo 2 (1 headed) — 1 goal, António Silva 1 (1 headed), Nobel Mendy 1 (1 headed), Maxence Lacroix 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 39.0 (rank 16 of 20, 1 = highest line) · block length 20.9 (rank 11, 1 = most compact) · width 67.8. Per match: GW3 H v Manchester United 4-2-3-1: back line 40, front 66, length 26, width 70 (45% poss); GW4 A v Tottenham Hotspur 4-1-4-1: back line 39, front 55, length 16, width 65 (38% poss); GW5 H v Ipswich Town 4-2-3-1: back line 39, front 58, length 19, width 70 (52% poss); GW6 A v Hull City 4-2-3-1: back line 42, front 62, length 20, width 69 (65% poss); GW7 H v Chelsea 4-2-3-1: back line 43, front 64, length 21, width 68 (47% poss); GW8 A v Arsenal 4-2-3-1: back line 32, front 54, length 23, width 66 (42% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 3 league match(es) v LB-coded sides — xG 1.68/match and 2.3 pts/match v 1.00 and 0.6 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW1 H v Crystal Palace 2–0, xG 1.12, box shots 11, poss 42%; GW5 H v Ipswich Town 1–0, xG 2.24, box shots 13, poss 52%; GW6 A v Hull City 2–2, xG 1.68, box shots 11, poss 65%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Grealish 2, Garner 2, George 1** · FPL editorial order: Garner #1, Dewsbury-Hall #2, Hackney #3
- Direct free-kick shooters: **Garner 2** · FPL order: Garner #1
- Penalties taken: **—** · FPL order: Barry #1, Garner #2
- Set-piece deliverers (assisted 'SetPiece' shots): **Dewsbury-Hall 2, Tarkowski 2, Garner 2**
- Corner targets (headed shots from corners): **Barry 2, Branthwaite 1, Keane 1, Dewsbury-Hall 1** · corner shots 15
- **DISAGREEMENT:** observed corner taker Jack Grealish (2) v FPL #1 Garner — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Kiernan Dewsbury-Hall 3 (0.38/90, percentile 83, 714 min) · club total 8 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 289 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 13.7, field tilt 51.2, possession 42.9%, box entries 13, direct speed 1.9, SCA 27; GW2: PPDA 9.03, field tilt 47.4, possession 41.8%, box entries 9, direct speed 3.55, SCA 25; GW3: PPDA 13.19, field tilt 59.2, possession 45.8%, box entries 12, direct speed 2.06, SCA 36; GW4: PPDA 17.73, field tilt 30.5, possession 38%, box entries 8, direct speed 2.27, SCA 23; GW5: PPDA 12.58, field tilt 59.9, possession 51.8%, box entries 14, direct speed 2.09, SCA 41; GW6: PPDA 9.08, field tilt 61.6, possession 64.7%, box entries 18, direct speed 2.34, SCA 27; GW7: PPDA 18.42, field tilt 51.1, possession 47.5%, box entries 10, direct speed 2.39, SCA 10; GW8: PPDA 14.5, field tilt 34.9, possession 41.6%, box entries 7, direct speed 1.97, SCA 14

**Zone 14 (C13, SofaScore heat-map points, 8 league matches):** for 28.8/match (rank 9 of 20) · conceded 36.2/match (rank 3 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 6.4/match · allowed 8.6/match · PPDA 14.8. Per match for/allowed: GW3 7/7; GW4 8/7; GW5 7/5; GW6 8/10; GW7 3/6; GW8 4/18 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 8 league matches, weights last-3 ×3 / older ×1
- GK: Jordan Pickford (14, 3/3)
- DEF: James Tarkowski (14, 3/3), Jarrad Branthwaite (11, 2/3), Merlin Röhl (9, 2/3), Jake O'Brien (3, 1/3)
- MID: Harrison Armstrong (14, 3/3), Kiernan Dewsbury-Hall (14, 3/3), James Garner (13, 3/3), Ainsley Maitland-Niles (8, 2/3), Tyrique George (7, 1/3)
- FWD: Thierno Barry (14, 3/3)
- Contested slots: D Jake O'Brien 3 v Michael Keane 3 · Excluded (FPL flag): Vitaliy Mykolenko — Unspecified injury - 75% chance of playing; Jack Grealish — Illness - 75% chance of playing
- Absent last match (E12, SofaScore list): —
- Substitutions this season (C3): GW5 66' Brennan Johnson→Tyler Dibling TACTICAL; GW6 86' Thierno Barry→Carlos Alcaraz LATE; GW6 86' Jack Grealish→Tyler Dibling LATE; GW6 78' Ainsley Maitland-Niles→Jake O'Brien TACTICAL; GW6 78' Harrison Armstrong→Hayden Hackney TACTICAL; GW6 66' Brennan Johnson→Tyrique George TACTICAL; GW7 85' Harrison Armstrong→Christian Nørgaard CARD-RISK; GW7 85' Jack Grealish→Brennan Johnson LATE; GW7 55' Ainsley Maitland-Niles→Tyrique George CHASING; GW8 86' Kiernan Dewsbury-Hall→Carlos Alcaraz LATE; GW8 74' Vitaliy Mykolenko→Hayden Hackney INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW8 72' Brennan Johnson→Tyler Dibling CHASING

### First-choice players and absences (F14) — generated 2026-10-27 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Jordan Pickford | start weight 14 | OK | a | — | — |
| CB | James Tarkowski | start weight 14 | OK | a | Michael Keane | — |
| CB | Jarrad Branthwaite | start weight 11 | OK | a 100% | Michael Keane | — |
| xGI #1 | Thierno Barry | xGI 5.25 | OK | a | Brennan Johnson | — |
| xGI #2 | Kiernan Dewsbury-Hall | xGI 2.44 | OK | a | Brennan Johnson | — |
| Penalties #1 (FPL) | Barry | FPL order | OK | a | Garner | — |
| Direct FK #1 (FPL) | Garner | FPL order | OK | a 100% | — | — |
| Corners (observed) | James Garner | 18 corners taken | OK | a 100% | Kiernan Dewsbury-Hall | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Crystal Palace: all started · GW2 A Bournemouth: all started · GW3 H Manchester United: all started · GW4 A Tottenham Hotspur: all started · GW5 H Ipswich Town: all started · GW6 A Hull City: all started · GW7 H Chelsea: all started · GW8 A Arsenal: Jarrad Branthwaite (did not start)

### Next fixtures (all competitions)
- Thu 29 Oct 19:45 UTC · EFL Cup R4 · H v Newcastle United
- Mon 02 Nov 20:00 UTC · Premier League R9 · A v Newcastle United
- Fri 06 Nov 20:00 UTC · Premier League R10 · H v Coventry City
- Mon 23 Nov 20:00 UTC · Premier League R11 · A v Brentford
- Sun 29 Nov 12:00 UTC · Premier League R12 · H v Liverpool FC
- Wed 02 Dec 20:15 UTC · Premier League R13 · A v Aston Villa

### FPL availability flags (players with league minutes this season)
Mykolenko — Unspecified injury - 75% chance of playing (75%); Grealish — Illness - 75% chance of playing (75%); Beto — Has joined Fiorentina permanently (0%)
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
### Corner takers observed (LiveScore Block L)
- James Garner: 18 corners (14 left, 4 right, 3 short)
- Kiernan Dewsbury-Hall: 17 corners (0 left, 17 right, 3 short)
- Hayden Hackney: 4 corners (4 left, 0 right)
