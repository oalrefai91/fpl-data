# Everton — data doc
*Feeder-written (2026-11-24 07:45 UTC); do not edit. Narrative: `profiles/teams/everton.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-24 07:45 UTC)
**Manager:** David Moyes · **Venue:** Hill Dickinson Stadium · **SofaScore:** https://www.sofascore.com/football/team/everton/48 · **FPL code:** EVE
**Table:** 9th, 16 pts (4W 4D 3L, GF 12 GA 14) · Home 8th (3-1-1, 8:5) · Away 11th (1-3-2, 4:9)
**Standing context (F15):** 27 league games left · points v 4th -5, v 5th -2, v 17th (last safe) +7, v 18th +7 · goal difference -2
**Suspension watch (D7, all players of the club):** Tarkowski — ⛔ SUSPENDED (Suspended until 13 Dec); Mykolenko — 🟨 2 from a ban (3/5); Garner — 🟨 2 from a ban (3/5); Armstrong — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 11 league matches):** goals after 75′ — for 4/12 (33%), against 3/14 (21%) · scored first 3, conceded first 7 (64% of matches), goalless 1 · points from losing positions 6 of 21 (7 matches behind at some point) · points from winning positions 13 of 15 (5 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Branthwaite (DEF) 10.8/90, hit 6/10; Tarkowski (DEF) 9.9/90, hit 5/11; Garner (MID) 12.4/90, hit 4/11; Mykolenko (DEF) 8.0/90, hit 4/10; O'Brien (DEF) 9.1/90, hit 2/7; Armstrong (MID) 8.9/90, hit 2/11
**Manager tenure (F13, SofaScore):** David Moyes since 11 Jan 2025 · 72 matches in charge, all competitions (27W 21D 24L) · 11 league matches this season · contract to — · previous club West Ham United · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Liverpool FC — last 4: Apr 2026 Premier League Everton 1–2 Liverpool FC (yellows 2–0, xG 1.00–1.45); Sep 2025 Premier League Liverpool FC 2–1 Everton (yellows 2–3, xG 0.90–0.70); Apr 2025 Premier League Liverpool FC 1–0 Everton (yellows 2–2, xG 1.47–0.67); Feb 2025 Premier League Everton 2–2 Liverpool FC (yellows 4–4, reds 1–1, xG 0.95–0.62) · 19 yellows in 4 | v Manchester United — last 4: Sep 2026 Premier League Everton 2–2 Manchester United (yellows 3–3, xG 1.01–0.69); Feb 2026 Premier League Everton 0–1 Manchester United (yellows 2–3, xG 0.63–1.27); Nov 2025 Premier League Manchester United 0–1 Everton (yellows 2–0, reds 0–1, xG 1.71–0.21); Feb 2025 Premier League Everton 2–2 Manchester United (yellows 4–1, xG 1.91–0.41) · 18 yellows in 4
**Archetype (F5):** used **TR** — last week's TR HELD by the margin rule (Q-86) — derived LB is inside the borderline band · signals, last 6 league matches: possession 46.7%, PPDA 12.7 (Understat, 3 matches; lower = harder press), opponent offsides forced 0.7/match (line height), fast breaks 0.7/match (season), both sides' xG 2.76/match (openness) · note: possession 46.7 v 47.5; computed from 3 of 6 GWs (no PPDA/possession for GW9, GW10, GW11). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 9 (permanent 7, loan 1, free 0, loan returns 1) · out 12 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 11 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 14.05 | 16 | Big chances against | 29 | 12 |
| xGOT | 14.12 | 12 | Box shots against | 107 | 13 |
| xA | 9.15 | 11 | Corners against | 60 | 18 |
| Shots | 144 | 12 | Crosses faced | 210 | 16 |
| SoT | 52 | 7 | Dribbled past | 73 | 5 |
| Big chances | 34 | 5 | Errors→shot | 6 | 5 |
| Shots in box | 103 | 9 | GK goals prevented | -0.57 | 10 |
| Corners | 49 | 10 | Clearances | 313 | 6 |
| Crosses | 196 | 9 | Tackles | 176 | 9 |
| Fast breaks | 8 | 18 | Interceptions | 101 | 10 |
| FK shots | 3 | 13 | Def. contributions | 655 | 3 |
| Possession % | 45.27 | 17 | Aerial % | 54.32 | 3 |
| Pass % | 82.15 | 11 | Duel % | 54.38 | 1 |
| Long balls | 322 | 14 | Fouls | 93 | 1 |
| Dribbles | 74 | 12 | Yellows | 19 | 5 |
| Shots against | 169 | 15 | Km covered | 1249 | 15 |
| SoT against | 47 | 12 | Sprints | 1125 | 18 |
Per match: xG 1.28 · xGOT 1.28 · shots 13.1 · shots against 15.4 · big chances 3.1 for / 2.6 against · corners 4.5 / 5.5 · crosses 17.8 / 19.1 · possession 45.3%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | A | Hull City | 2–2 | 1.68/2.97 | 1.33/1.53 | 65 | 15/9 | 7/5 | 11/9 | 3/2 | 8/2 | 6/7 | 22/5 v 23/3 | 1/4 |
| 7 | H | Chelsea | 0–2 | 0.43/0.57 | 1.47/1.61 | 47 | 6/18 | 5/7 | 6/10 | 1/5 | 2/3 | 5/7 | 20/3 v 14/3 | 1/4 |
| 8 | A | Arsenal | 0–2 | 0.63/0.72 | 1.96/2.29 | 42 | 8/20 | 3/4 | 6/12 | 2/10 | 2/3 | 3/12 | 16/2 v 23/5 | 0/1 |
| 9 | A | Newcastle United | 1–0 | 2.34/— | 1.29/— | 48 | 16/17 | 5/2 | 11/7 | 1/6 | 4/2 | 5/4 | 22/7 v 24/7 | 0/2 |
| 10 | H | Coventry City | 3–1 | 1.43/— | 1.21/— | 50 | 15/15 | 7/4 | 13/8 | 3/3 | 5/3 | 2/2 | 20/6 v 13/3 | 0/1 |
| 11 | A | Brentford | 0–4 | 0.23/— | 2.57/— | 28 | 4/21 | 2/7 | 2/17 | 1/10 | 1/3 | 3/6 | 8/1 v 31/8 | 2/0 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | A | Hull City | 2–2 | 4-2-3-1 | 4/15 | 0/2 | 0/0 | 595/306 | 63/51 | Mykolenko (Knock Injury; doubtful) | Hughes (Groin Injury), Gyabi (Groin Injury), Matazo (Cruciate Ligament Injury), Ansah (Back Injury), Butland (Elbow Injury), Targett (Ankle Injury) | Michael Salisbury |
| 7 | H | Chelsea | 0–2 | 4-2-3-1 | 8/15 | 3/4 | 0/0 | 408/463 | 56/55 | — | Emegha (Hamstring Injury), Gittens (Ankle Injury), James (Knee Injury) | Paul Tierney |
| 8 | A | Arsenal | 0–2 | 4-2-3-1 | 13/11 | 3/1 | 0/0 | 372/518 | 48/65 | — | Saka (Muscle Injury), Tzolis (Hamstring Injury), Saliba (Back Injury) | Tony Harrington |
| 9 | A | Newcastle United | 1–0 | 4-2-3-1 | 9/13 | 2/4 | 0/1 | 396/428 | 61/70 | — | Jaouen (Hamstring Injury), Livramento (Knock Injury), Miley (Knock Injury; doubtful), Fernández-Pardo (Illness; doubtful) | John Brooks |
| 10 | H | Coventry City | 3–1 | 4-2-3-1 | 10/6 | 1/1 | 0/0 | 438/451 | 43/56 | Grealish (club decision) | Amenda (Calf Injury), Thomas (Leg Injury), Wright (Muscle Injury), Eccles (Knock Injury), Woolfenden (Knee Injury), Onyeka (Strain Injury; doubtful) | Stuart Attwell |
| 11 | A | Brentford | 0–4 | 4-2-3-1 | 9/8 | 1/0 | 1/0 | 303/771 | 35/96 | — | Thiago (ban (red)), Hickey (Hamstring Injury), Milambo (Cruciate Ligament Injury), Dasilva (Hamstring Injury), Furo (Knee Surgery), Collins (Knee Injury), Henry (Muscle Injury) | Craig Pawson |
Per match: fouls 8.5 / 11.9 · yellows 1.73 / 2.00 · reds 1 / 2 (season) · offsides forced 0.6, committed 1.8 · crosses attempted 17.8 / faced 19.1. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 1.25 for / 1.35 against per match · Away (6): xG 1.30 / 1.67. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW11 A v Brentford 0–4 (Mon 23 Nov 20:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Jordan Pickford | G | 90 | 5.2 | 0.00 | 0.00 | 0 | 0 | 2 | 0 | 47 |
| Jake O'Brien | D | 90 | 6.5 | 0.00 | 0.00 | 0 | 0 | 11 | 0 | 39 |
| James Tarkowski | D | 40 | 5.3 | 0.00 | 0.00 | 0 | 0 | 5 | 0 | 19 |
| Jarrad Branthwaite | D | 90 | 7 | 0.00 | 0.00 | 0 | 0 | 17 | 0 | 48 |
| Vitaliy Mykolenko | D | 90 | 5.9 | 0.00 | 0.00 | 0 | 0 | 11 | 0 | 47 |
| Harrison Armstrong | M | 90 | 6.5 | 0.02 | 0.00 | 0 | 1 | 3 | 0 | 32 |
| James Garner | M | 85 | 7.6 | 0.00 | 0.02 | 1 | 0 | 12 | 3 | 58 |
| Merlin Röhl | M | 69 | 7 | 0.00 | 0.00 | 0 | 0 | 8 | 1 | 40 |
| Kiernan Dewsbury-Hall | M | 69 | 6.3 | 0.02 | 0.00 | 0 | 1 | 5 | 3 | 54 |
| Tyrique George | M | 45 | 6.3 | 0.00 | 0.00 | 1 | 0 | 2 | 1 | 16 |
| Thierno Barry | F | 69 | 6.7 | 0.12 | 0.00 | 0 | 1 | 5 | 0 | 26 |
Subs used: Jack Grealish (45'), Michael Keane (21'), Hayden Hackney (21'), Brennan Johnson (21'), Christian Nørgaard (10')
Goals: 23' Keane Lewis-Potter (assist Jaidon Anthony) [opp]; 25' Keane Lewis-Potter [opp]; 67' Vitaly Janelt (assist Jaidon Anthony) [opp]; 90' Fabio Carvalho (assist Mathias Jensen) [opp]
Substitutions (own): 46' Jack Grealish for Tyrique George; 69' Michael Keane for Merlin Röhl; 69' Brennan Johnson for Thierno Barry; 69' Hayden Hackney for Kiernan Dewsbury-Hall; 85' Christian Nørgaard for James Garner
Cards: 24' Vitaliy Mykolenko (yellow, own); 40' James Tarkowski (red, own)
**Baseline XI change vs GW10 (4-2-3-1 → 4-2-3-1):** in — Jake O'Brien; out — Tyler Dibling.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
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
| 11 | A Brentford | 23' | AGAINST | Keane Lewis-Potter | Jaidon Anthony | [no Understat] | — |
| 11 | A Brentford | 25' | AGAINST | Keane Lewis-Potter | — | [no Understat] | — |
| 11 | A Brentford | 67' | AGAINST | Vitaly Janelt | Jaidon Anthony | [no Understat] | — |
| 11 | A Brentford | 90' | AGAINST | Fabio Carvalho | Mathias Jensen | [no Understat] | — |
Scored 12: open play 5, [no Understat] 4, corner 2, set piece 1 · Conceded 14: open play 6, [no Understat] 5, [unmatched] 2, set piece 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW9 FOR v Newcastle United 49' Thierno Barry: GOAL! It's an easy finish as Thierno Barry from Everton taps the ball into an open goal with the right foot! · before: 49' Good effort by Tyrique George as he directs a shot on target, but the keeper saves it ‹ 49' Kiernan Dewsbury-Hall creates a scoring opportunity for his teammate ‹ 49' Everton with a potentially dangerous attack.
- GW10 AG v Coventry City 52' Yann Gboho: G O O O O O A A L - Yann Gboho finds the net with the right foot! · before: 52' Tatsuhiro Sakamoto wins an air challenge against Vitaliy Mykolenko ‹ 51' Thierno Barry is penalised for pushing Victor Torp. ‹ 51' Merlin Roehl wins an air challenge against Jay Dasilva
- GW10 FOR v Coventry City 56' Thierno Barry (assist Vitaliy Mykolenko): G O O O A A A L - Thierno Barry from Everton heads the ball home! · before: 56' The cross by Vitaliy Mykolenko from Everton successfully finds a teammate in the box. ‹ 56' Jay Dasilva from Coventry intercepts a cross aimed towards the box. ‹ 56' A chance presents itself to Tyrique George from Everton but his header goes wide
- GW10 FOR v Coventry City 61' Thierno Barry: G O O O O O A A L - Thierno Barry finds the net with the left foot! · before: 61' Ethan Pinnock relieves the pressure with a clearance ‹ 61' The cross by Tyrique George from Everton successfully finds a teammate in the box. ‹ 60' Ethan Pinnock successfully blocks the shot
- GW10 FOR v Coventry City 81' Kiernan Dewsbury-Hall (assist Thierno Barry, key pass Vitaliy Mykolenko): G O O O A A A L - Kiernan Dewsbury-Hall scores with the left foot! · before: 80' Brandon Thomas-Asante relieves the pressure with a clearance ‹ 80' Everton with a potentially dangerous attack. ‹ 80' Vitaliy Mykolenko relieves the pressure with a clearance
- GW11 AG v Brentford 23' Keane Lewis-Potter (assist Jaidon Anthony): — no commentary line — · before: 19' Attempt missed. Michael Kayode (Brentford) right footed shot from the centre of the box mis ‹ 17' Foul by James Garner (Everton). ‹ 17' Mikkel Damsgaard (Brentford) wins a free kick in the attacking half.
- GW11 AG v Brentford 25' Keane Lewis-Potter: — no commentary line — · before: 24' Foul by Vitalii Mykolenko (Everton). ‹ 24' Dango Ouattara (Brentford) wins a free kick on the right wing. ‹ 24' Vitalii Mykolenko (Everton) is shown the yellow card for a bad foul.
- GW11 AG v Brentford 67' Vitaly Janelt (assist Jaidon Anthony): — no commentary line — · before: 66' Substitution, Brentford. Kevin Schade replaces Dango Ouattara. ‹ 62' Offside, Brentford. Keane Lewis-Potter is caught offside. ‹ 59' Jack Grealish (Everton) wins a free kick on the left wing.
- GW11 AG v Brentford 90' Fábio Carvalho (assist Mathias Jensen): — no commentary line — · before: 90' Fourth official has announced 3 minutes of added time. ‹ 86' Attempt blocked. Fábio Carvalho (Brentford) right footed shot from the centre of the box is ‹ 85' Substitution, Everton. Christian Nørgaard replaces James Garner.

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
- GW11 A v Brentford 23' Keane Lewis-Potter: no structured culprit — reports only
- GW11 A v Brentford 25' Keane Lewis-Potter: no structured culprit — reports only
- GW11 A v Brentford 67' Vitaly Janelt: no structured culprit — reports only
- GW11 A v Brentford 90' Fabio Carvalho: no structured culprit — reports only
  · GW11 other flags: Kiernan Dewsbury-Hall errorLeadToAShot 1

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

**Corners (E10 data layer):** observed takers GW1–11 [CONFIRMED — LiveScore Block L, 46 corners; side L/R as LiveScore records it; foot from SofaScore]: James Garner 22 (18L/4R, 4 short, right foot); Kiernan Dewsbury-Hall 20 (0L/20R, 4 short, left foot); Hayden Hackney 4 (4L/0R, right foot). First contact on corners that ended in a shot (Understat) — for: Kiernan Dewsbury-Hall 5 (1 headed) — 1 goal, Thierno Barry 2 (2 headed), Jarrad Branthwaite 2 (1 headed), Tyrique George 2, Michael Keane 1 (1 headed) · against (who beat them): Evanilson 2 (2 headed), Ezri Konsa Ngoyo 2 (1 headed) — 1 goal, António Silva 1 (1 headed), Nobel Mendy 1 (1 headed), Maxence Lacroix 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 38.2 (rank 19 of 20, 1 = highest line) · block length 21.1 (rank 9, 1 = most compact) · width 66.6. Per match: GW6 A v Hull City 4-2-3-1: back line 42, front 62, length 20, width 69 (65% poss); GW7 H v Chelsea 4-2-3-1: back line 43, front 64, length 21, width 68 (47% poss); GW8 A v Arsenal 4-2-3-1: back line 32, front 54, length 23, width 66 (42% poss); GW9 A v Newcastle United 4-2-3-1: back line 41, front 63, length 22, width 64 (48% poss); GW10 H v Coventry City 4-2-3-1: back line 38, front 60, length 22, width 68 (50% poss); GW11 A v Brentford 4-2-3-1: back line 28, front 50, length 22, width 57 (28% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 4 league match(es) v LB-coded sides — xG 1.62/match and 2.5 pts/match v 1.08 and 0.9 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW1 H v Crystal Palace 2–0, xG 1.12, box shots 11, poss 42%; GW5 H v Ipswich Town 1–0, xG 2.24, box shots 13, poss 52%; GW6 A v Hull City 2–2, xG 1.68, box shots 11, poss 65%; GW10 H v Coventry City 3–1, xG 1.43, box shots 13, poss 50%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Grealish 2, Garner 2, George 1** · FPL editorial order: Garner #1, Dewsbury-Hall #2, Hackney #3
- Direct free-kick shooters: **Garner 2** · FPL order: Garner #1
- Penalties taken: **—** · FPL order: Barry #1, Garner #2
- Set-piece deliverers (assisted 'SetPiece' shots): **Dewsbury-Hall 2, Tarkowski 2, Garner 2**
- Corner targets (headed shots from corners): **Barry 2, Branthwaite 1, Keane 1, Dewsbury-Hall 1** · corner shots 15
- **DISAGREEMENT:** observed corner taker Jack Grealish (2) v FPL #1 Garner — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Kiernan Dewsbury-Hall 4 (0.37/90, percentile 84, 963 min); Merlin Röhl 2 (0.27/90, percentile 76, 663 min); Tyrique George 2 (0.26/90, percentile 75, 684 min) · club total 15 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 334 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 13.7, field tilt 51.2, possession 42.9%, box entries 13, direct speed 1.9, SCA 27; GW2: PPDA 9.03, field tilt 47.4, possession 41.8%, box entries 9, direct speed 3.55, SCA 25; GW3: PPDA 13.19, field tilt 59.2, possession 45.8%, box entries 12, direct speed 2.06, SCA 36; GW4: PPDA 17.73, field tilt 30.5, possession 38%, box entries 8, direct speed 2.27, SCA 23; GW5: PPDA 12.58, field tilt 59.9, possession 51.8%, box entries 14, direct speed 2.09, SCA 41; GW6: PPDA 9.08, field tilt 61.6, possession 64.7%, box entries 18, direct speed 2.34, SCA 27; GW7: PPDA 18.42, field tilt 51.1, possession 47.5%, box entries 10, direct speed 2.39, SCA 10; GW8: PPDA 14.5, field tilt 34.9, possession 41.6%, box entries 7, direct speed 1.97, SCA 14; GW9: PPDA 14.36, field tilt 50.6, possession 48.4%, box entries 13, direct speed 2.27, SCA 32; GW10: PPDA 11.17, field tilt 48.6, possession 49.5%, box entries 12, direct speed 2.26, SCA 28

**Zone 14 (C13, SofaScore heat-map points, 11 league matches):** for 25.5/match (rank 14 of 20) · conceded 38.1/match (rank 2 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 6.4/match · allowed 8.6/match · PPDA 14.8. Per match for/allowed: GW3 7/7; GW4 8/7; GW5 7/5; GW6 8/10; GW7 3/6; GW8 4/18 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: Jordan Pickford (16, 3/3)
- DEF: Jarrad Branthwaite (15, 3/3), Vitaliy Mykolenko (15, 3/3), Merlin Röhl (13, 3/3), Jake O'Brien (7, 2/3)
- MID: Harrison Armstrong (16, 3/3), James Garner (16, 3/3), Kiernan Dewsbury-Hall (16, 3/3), Tyrique George (13, 3/3), Ainsley Maitland-Niles (4, 0/3)
- FWD: Thierno Barry (16, 3/3)
- Contested slots: M Ainsley Maitland-Niles 4 v Jack Grealish 3 · Excluded (FPL flag): James Tarkowski — Suspended until 13 Dec
- Absent last match (E12, SofaScore list): —
- Substitutions this season (C3): GW9 82' Jarrad Branthwaite→Michael Keane INJURY [ONE SOURCE: LiveScore 'knock'; SofaScore marked it regular; FPL shows him available]; GW9 80' Thierno Barry→Brennan Johnson TACTICAL; GW10 90' Tyrique George→Carlos Alcaraz LATE; GW10 89' Jarrad Branthwaite→Michael Keane CARD-RISK; GW10 73' Tyler Dibling→Brennan Johnson TACTICAL; GW10 73' Harrison Armstrong→Hayden Hackney TACTICAL; GW10 73' Merlin Röhl→Jake O'Brien TACTICAL; GW11 85' James Garner→Christian Nørgaard LATE; GW11 69' Merlin Röhl→Michael Keane CHASING; GW11 69' Thierno Barry→Brennan Johnson CHASING; GW11 69' Kiernan Dewsbury-Hall→Hayden Hackney CHASING; GW11 46' Tyrique George→Jack Grealish HALF-TIME

### First-choice players and absences (F14) — generated 2026-11-24 07:45 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Jordan Pickford | start weight 16 | OK | a | — | — |
| CB | James Tarkowski | start weight 16 | **OUT** | s 0% — Suspended until 13 Dec | Michael Keane | +0.5 to attackers facing them (cap +1.0); −0.5 to this club's own defenders |
| CB | Jarrad Branthwaite | start weight 15 | OK | a 100% | Michael Keane | — |
| xGI #1 | Thierno Barry | xGI 7.89 | OK | a | Tyrique George | — |
| xGI #2 | Kiernan Dewsbury-Hall | xGI 3.19 | OK | a | Tyrique George | — |
| Penalties #1 (FPL) | Barry | FPL order | OK | a | Garner | — |
| Direct FK #1 (FPL) | Garner | FPL order | OK | a 100% | — | — |
| Corners (observed) | James Garner | 22 corners taken | OK | a 100% | Kiernan Dewsbury-Hall | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Crystal Palace: all started · GW2 A Bournemouth: all started · GW3 H Manchester United: all started · GW4 A Tottenham Hotspur: all started · GW5 H Ipswich Town: all started · GW6 A Hull City: all started · GW7 H Chelsea: all started · GW8 A Arsenal: Jarrad Branthwaite (did not start) · GW9 A Newcastle United: all started · GW10 H Coventry City: all started · GW11 A Brentford: all started

### Next fixtures (all competitions)
- Sun 29 Nov 12:00 UTC · Premier League R12 · H v Liverpool FC
- Wed 02 Dec 20:15 UTC · Premier League R13 · A v Aston Villa
- Sun 06 Dec 14:00 UTC · Premier League R14 · H v Fulham
- Sun 13 Dec 14:00 UTC · Premier League R15 · A v Brighton & Hove Albion
- Thu 17 Dec 20:00 UTC · EFL Cup R27 · A v Fleetwood Town
- Sun 20 Dec 14:00 UTC · Premier League R16 · A v Nottingham Forest

### FPL availability flags (players with league minutes this season)
Tarkowski — Suspended until 13 Dec (0%); Beto — Has joined Fiorentina permanently (0%)
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
- GW11 A Brentford 0–4 · xG 0.23–2.57 · poss 28% · 4-2-3-1 · scorers: none
### Corner takers observed (LiveScore Block L)
- James Garner: 22 corners (18 left, 4 right, 4 short)
- Kiernan Dewsbury-Hall: 20 corners (0 left, 20 right, 4 short)
- Hayden Hackney: 4 corners (4 left, 0 right)
