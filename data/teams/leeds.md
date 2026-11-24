# Leeds United — data doc
*Feeder-written (2026-11-24 07:45 UTC); do not edit. Narrative: `profiles/teams/leeds.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-24 07:45 UTC)
**Manager:** Daniel Farke · **Venue:** Elland Road · **SofaScore:** https://www.sofascore.com/football/team/leeds-united/34 · **FPL code:** LEE
**Table:** 7th, 17 pts (4W 5D 2L, GF 14 GA 9) · Home 10th (2-3-0, 7:3) · Away 5th (2-2-2, 7:6)
**Standing context (F15):** 27 league games left · points v 4th -4, v 5th -1, v 17th (last safe) +8, v 18th +8 · goal difference +5
**Suspension watch (D7, all players of the club):** Bogle — 🟨 **ONE FROM A BAN** (4/5 before GW19); Ampadu — 🟨 **ONE FROM A BAN** (4/5 before GW19); Calvert-Lewin — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 11 league matches):** goals after 75′ — for 4/14 (29%), against 2/9 (22%) · scored first 5, conceded first 4 (36% of matches), goalless 2 · points from losing positions 5 of 15 (5 matches behind at some point) · points from winning positions 13 of 18 (6 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Muharemović (DEF) 10.7/90, hit 7/11; Ampadu (MID) 11.6/90, hit 5/11; Elvedi (DEF) 8.6/90, hit 4/9; Justin (DEF) 8.2/90, hit 4/11; Stach (MID) 9.9/90, hit 3/10; Bijol (DEF) 13.6/90, hit 2/5
**Manager tenure (F13, SofaScore):** Daniel Farke since 04 Jul 2023 · 158 matches in charge, all competitions (79W 43D 36L) · 11 league matches this season · contract to 30 Jun 2027 · previous club Borussia M'gladbach · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Manchester United — last 4: Oct 2026 Premier League Leeds United 1–1 Manchester United (yellows 2–2, xG 1.41–0.92); Apr 2026 Premier League Manchester United 1–2 Leeds United (yellows 3–2, reds 1–0, xG 1.27–2.57); Jan 2026 Premier League Leeds United 1–1 Manchester United (yellows 0–1, xG 0.90–1.59); Feb 2023 Premier League Leeds United 0–2 Manchester United (yellows 2–1, xG 1.81–1.12) · 13 yellows in 4 | v Nottingham Forest — last 4: Aug 2026 EFL Cup Nottingham Forest 0–2 Leeds United (yellows 4–3, xG 1.21–2.58); Aug 2026 Premier League Nottingham Forest 0–1 Leeds United (yellows 2–1, xG 0.66–0.47); Feb 2026 Premier League Leeds United 3–1 Nottingham Forest (yellows 1–1, xG 2.83–1.33); Nov 2025 Premier League Nottingham Forest 3–1 Leeds United (yellows 2–1, xG 2.55–0.74) · 15 yellows in 4
**Archetype (F5):** used **HP** — derived HP [DERIVED] · signals, last 6 league matches: possession 48.3%, PPDA 7.2 (Understat, 3 matches; lower = harder press), opponent offsides forced 2.7/match (line height), fast breaks 0.8/match (season), both sides' xG 2.49/match (openness) · note: possession 48.3 v 47.5; computed from 3 of 6 GWs (no PPDA/possession for GW9, GW10, GW11). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 13 (permanent 5, loan 2, free 0, loan returns 6) · out 14 · flags: Joël Piroe: still in an FPL set-piece order — use #2 or observation — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 11 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 15.95 | 9 | Big chances against | 20 | 4 |
| xGOT | 14.82 | 10 | Box shots against | 81 | 5 |
| xA | 6.98 | 18 | Corners against | 44 | 2 |
| Shots | 141 | 13 | Crosses faced | 206 | 15 |
| SoT | 45 | 11 | Dribbled past | 73 | 5 |
| Big chances | 28 | 7 | Errors→shot | 4 | 1 |
| Shots in box | 91 | 14 | GK goals prevented | 3.87 | 1 |
| Corners | 45 | 13 | Clearances | 329 | 4 |
| Crosses | 220 | 4 | Tackles | 182 | 7 |
| Fast breaks | 9 | 17 | Interceptions | 102 | 9 |
| FK shots | 6 | 4 | Def. contributions | 655 | 3 |
| Possession % | 46.82 | 12 | Aerial % | 51.97 | 6 |
| Pass % | 78.63 | 16 | Duel % | 51.82 | 4 |
| Long balls | 362 | 8 | Fouls | 145 | 16 |
| Dribbles | 82 | 6 | Yellows | 22 | 8 |
| Shots against | 146 | 9 | Km covered | 1297 | 3 |
| SoT against | 46 | 10 | Sprints | 1272 | 7 |
Per match: xG 1.45 · xGOT 1.35 · shots 12.8 · shots against 13.3 · big chances 2.5 for / 1.8 against · corners 4.1 / 4.0 · crosses 20.0 / 18.7 · possession 46.8%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | A | Arsenal | 1–2 | 0.62/1.20 | 2.33/2.32 | 42 | 11/13 | 5/6 | 7/8 | 3/3 | 2/4 | 4/2 | 23/6 v 15/7 | 7/4 |
| 7 | H | Manchester United | 1–1 | 1.41/1.43 | 0.92/1.08 | 61 | 12/13 | 5/3 | 10/6 | 1/6 | 2/2 | 2/3 | 29/4 v 10/2 | 3/2 |
| 8 | A | Sunderland | 0–0 | 0.76/1.07 | 0.83/1.03 | 50 | 11/15 | 4/4 | 7/8 | 3/7 | 2/1 | 5/4 | 22/6 v 20/3 | 3/0 |
| 9 | A | Bournemouth | 0–2 | 0.71/— | 1.29/— | 56 | 10/11 | 1/5 | 3/5 | 2/3 | 1/2 | 4/4 | 21/5 v 10/2 | 0/1 |
| 10 | H | Tottenham Hotspur | 1–0 | 1.96/— | 0.72/— | 38 | 16/7 | 4/4 | 11/5 | 4/0 | 4/1 | 6/4 | 30/5 v 24/6 | 1/2 |
| 11 | A | Chelsea | 4–1 | 2.77/— | 0.64/— | 43 | 21/14 | 8/3 | 13/7 | 4/5 | 7/0 | 2/3 | 16/6 v 15/3 | 2/7 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | A | Arsenal | 1–2 | 3-4-2-1 | 20/12 | 4/1 | 0/0 | 356/512 | 54/54 | Rodon (Hamstring Injury), Joseph (Knee Injury), James (Back Injury; doubtful) | Tzolis (Hamstring Injury), Saliba (Back Injury) | Paul Tierney |
| 7 | H | Manchester United | 1–1 | 3-4-2-1 | 16/5 | 2/2 | 0/0 | 532/354 | 73/59 | Rodon (Hamstring Injury), Joseph (Knee Injury), James (Back Injury; doubtful) | Šeško (Shin Injury), Ugarte (Cruciate Ligament Injury), Dorgu (Hamstring Injury), Heaton (Abdominal Injury), Mainoo (Knock Injury; doubtful), Shaw (Knock Injury; doubtful) | Darren England |
| 8 | A | Sunderland | 0–0 | 3-4-2-1 | 14/10 | 2/1 | 0/0 | 368/379 | 68/65 | Rodon (Hamstring Injury), Joseph (Knee Injury) | Danso (ban (red)), Mundle (Knee Injury), Meunier (Hamstring Injury; doubtful) | Stuart Attwell |
| 9 | A | Bournemouth | 0–2 | 3-4-2-1 | 15/12 | 2/2 | 0/0 | 520/420 | 64/63 | Joseph (Knee Injury) | Scott (Muscle Injury), Tóth (Hamstring Injury), Araujo (Thigh Injury) | Michael Salisbury |
| 10 | H | Tottenham Hotspur | 1–0 | 3-4-2-1 | 11/16 | 2/3 | 0/0 | 311/531 | 54/61 | Joseph (Knee Injury), Stach (Foot Injury; doubtful) | Bergvall (Physical Discomfort), Mudryk (Ankle Injury), Sávio (Muscle Injury), Odobert (Cruciate Ligament Injury), Simons (Cruciate Ligament Injury) | John Brooks |
| 11 | A | Chelsea | 4–1 | 3-4-2-1 | 16/6 | 3/1 | 0/0 | 407/557 | 52/63 | Joseph (Knee Injury) | Pedro (Muscle Injury), Lacroix (Hamstring Injury), James (Knee Injury) | Michael Oliver |
Per match: fouls 13.2 / 11.5 · yellows 2.00 / 2.18 · reds 0 / 0 (season) · offsides forced 2.5, committed 2.5 · crosses attempted 20.0 / faced 18.7. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (5): xG 1.64 for / 1.05 against per match · Away (6): xG 1.30 / 1.32. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW11 A v Chelsea 4–1 (Sat 21 Nov 15:00 UTC) — formation 3-4-2-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| James Trafford | G | 90 | 6.2 | 0.00 | 0.00 | 0 | 0 | 2 | 0 | 31 |
| James Justin | D | 90 | 7.3 | 0.00 | 0.09 | 1 | 0 | 11 | 1 | 64 |
| Nico Elvedi | D | 90 | 7 | 0.05 | 0.16 | 1 | 1 | 10 | 0 | 58 |
| Tarik Muharemović | D | 90 | 7.2 | 0.00 | 0.01 | 0 | 0 | 6 | 0 | 63 |
| Jayden Bogle | M | 86 | 6.7 | 0.06 | 0.17 | 1 | 3 | 3 | 4 | 58 |
| Ethan Ampadu | M | 90 | 7.7 | 0.00 | 0.15 | 1 | 0 | 3 | 2 | 86 |
| Ao Tanaka | M | 86 | 6.5 | 0.54 | 0.01 | 0 | 3 | 4 | 0 | 60 |
| Gabriel Gudmundsson | M | 89 | 6.7 | 0.08 | 0.00 | 0 | 2 | 1 | 2 | 37 |
| Sean Longstaff | F | 89 | 7.2 | 0.06 | 0.21 | 2 | 1 | 3 | 5 | 37 |
| Noah Okafor | F | 73 | 8.6 | 0.27 | 0.06 | 3 | 3 | 1 | 2 | 39 |
| Dominic Calvert-Lewin | F | 90 | 6.9 | 1.40 | 0.03 | 3 | 6 | 0 | 0 | 33 |
Subs used: Brenden Aaronson (17'), Joe Rodon (11'), Anton Stach (11'), Melvin Bard (1'), Harry Wilson (1')
Goals: 25' Emmanuel Emegha (assist Morgan Rogers) [opp]; 28' Noah Okafor (assist Dominic Calvert-Lewin) [own]; 53' Dominic Calvert-Lewin [own, penalty]; 58' Noah Okafor [own]; 90' Brenden Aaronson (assist Harry Wilson) [own]
Substitutions (own): 73' Brenden Aaronson for Noah Okafor; 86' Joe Rodon for Ao Tanaka; 86' Anton Stach for Jayden Bogle; 90' Melvin Bard for Gabriel Gudmundsson; 90' Harry Wilson for Sean Longstaff
Cards: 38' Gabriel Gudmundsson (yellow, own); 47' Roméo Lavia (yellow, opp); 68' Jayden Bogle (yellow, own); 83' Sean Longstaff (yellow, own)
**Baseline XI change vs GW10 (3-4-2-1 → 3-4-2-1):** in — Noah Okafor; out — Lukas Nmecha.

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
| 11 | A Chelsea | 25' | AGAINST | Emmanuel Emegha | Morgan Rogers | [no Understat] | — |
| 11 | A Chelsea | 28' | FOR | Noah Okafor | Dominic Calvert-Lewin | [no Understat] | — |
| 11 | A Chelsea | 53' | FOR | Dominic Calvert-Lewin | — | penalty | — |
| 11 | A Chelsea | 58' | FOR | Noah Okafor | — | [no Understat] | — |
| 11 | A Chelsea | 90' | FOR | Brenden Aaronson | Harry Wilson | [no Understat] | — |
Scored 14: open play 5, [no Understat] 4, corner 2, direct FK 1, own goal 1, penalty 1 · Conceded 9: open play 5, [no Understat] 3, corner 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW9 AG v Bournemouth 31' Evanilson (assist Justin Kluivert): — no commentary line — · before: 30' Evanilson (Bournemouth) wins a free kick in the defensive half. ‹ 30' Foul by Daniel James (Leeds United). ‹ 29' Foul by James Hill (Bournemouth).
- GW9 AG v Bournemouth 90+4' Amine Adli (assist Junior Kroupi): — no commentary line — · before: 90+3' Amine Adli (Bournemouth) wins a free kick in the defensive half. ‹ 90+3' Foul by Jean-Mattéo Bahoya (Leeds United). ‹ 90+1' Attempt saved. Álvaro Rodríguez (Bournemouth) left footed shot from outside the box is sa
- GW10 FOR v Tottenham Hotspur 79' Noah Okafor: G O O O O O A A L - Noah Okafor finds the net with the right foot! · before: 79' Rodrigo Bentancur relieves the pressure with a clearance ‹ 78' Safe hands from Antonin Kinsky as he comes out and claims the ball ‹ 78' Rodrigo Bentancur from Tottenham intercepts a cross aimed towards the box.
- GW11 AG v Chelsea 25' Emanuel Emegha (assist Morgan Rogers): — no commentary line — · before: 23' Attempt saved. Dominic Calvert-Lewin (Leeds United) header from the centre of the box is sa ‹ 22' Substitution, Chelsea. Jordan Henderson replaces Moisés Caicedo because of an injury. ‹ 22' Delay over. They are ready to continue.
- GW11 FOR v Chelsea 28' Noah Okafor (assist Dominic Calvert-Lewin): — no commentary line — · before: 25' Goal! Chelsea 1, Leeds United 0. Emmanuel Emegha (Chelsea) left footed shot from the centre ‹ 23' Attempt saved. Dominic Calvert-Lewin (Leeds United) header from the centre of the box is sa ‹ 22' Substitution, Chelsea. Jordan Henderson replaces Moisés Caicedo because of an injury.
- GW11 FOR v Chelsea 53' Dominic Calvert-Lewin [pen]: — no commentary line — · before: 49' Offside, Leeds United. Dominic Calvert-Lewin is caught offside. ‹ 49' Attempt blocked. Jayden Bogle (Leeds United) right footed shot from outside the box is bloc ‹ 49' Penalty conceded by Morgan Rogers (Chelsea) with a handball in the penalty area.
- GW11 FOR v Chelsea 58' Noah Okafor: — no commentary line — · before: 56' Foul by Dominic Calvert-Lewin (Leeds United). ‹ 56' Wesley Fofana (Chelsea) wins a free kick in the defensive half. ‹ 55' Attempt saved. Morgan Rogers (Chelsea) right footed shot from outside the box is saved in t
- GW11 FOR v Chelsea 90+1' Brenden Aaronson (assist Harry Wilson): — no commentary line — · before: 90' Attempt blocked. Morgan Rogers (Chelsea) right footed shot from outside the box is blocked. ‹ 90' Corner, Chelsea. Conceded by Sean Longstaff. ‹ 90' Attempt blocked. Levi Colwill (Chelsea) left footed shot from the centre of the box is bloc

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW6 A v Arsenal 62' Riccardo Calafiori: no structured culprit — reports only
- GW6 A v Arsenal 70' Bruno Guimarães: no structured culprit — reports only
  · GW6 other flags: Nico Elvedi lastManTackle 1; Ao Tanaka errorLeadToAShot 1; James Trafford errorLeadToAShot 1
- GW7 H v Manchester United 35' Bryan Mbeumo: no structured culprit — reports only
- GW9 A v Bournemouth 31' Evanilson: no structured culprit — reports only
- GW9 A v Bournemouth 90' Amine Adli: no structured culprit — reports only
  · GW9 error leading to a goal (SofaScore, match level — 2 conceded, the goal is not identified): Sean Longstaff, James Trafford [CONFIRMED — SofaScore error flag]
- GW11 A v Chelsea 25' Emmanuel Emegha: no structured culprit — reports only
  · GW11 other flags: James Justin lastManTackle 1

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

**Corners (E10 data layer):** observed takers GW1–11 [CONFIRMED — LiveScore Block L, 39 corners; side L/R as LiveScore records it; foot from SofaScore]: Anton Stach 26 (17L/9R, both foot); Harry Wilson 6 (1L/5R, left foot); Sean Longstaff 6 (6L/0R, right foot); Daniel James 1 (1L/0R, 1 short, right foot). First contact on corners that ended in a shot (Understat) — for: Tarik Muharemovic 3 (3 headed), Jayden Bogle 3 — 1 goal, Dominic Calvert-Lewin 2 (1 headed) — 1 goal, Ao Tanaka 2, Noah Okafor 2 · against (who beat them): Nathan Collins 2 (2 headed), Luke O&#039;Nien 2 (1 headed), Nikola Milenkovic 1 (1 headed), Igor Jesus 1 (1 headed), Thiago 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 38.6 (rank 16 of 20, 1 = highest line) · block length 22.2 (rank 14, 1 = most compact) · width 67.0. Per match: GW6 A v Arsenal 3-4-2-1: back line 38, front 58, length 21, width 69 (42% poss); GW7 H v Manchester United 3-4-2-1: back line 41, front 66, length 25, width 67 (61% poss); GW8 A v Sunderland 3-4-2-1: back line 38, front 63, length 25, width 69 (50% poss); GW9 A v Bournemouth 3-4-2-1: back line 37, front 59, length 22, width 70 (56% poss); GW10 H v Tottenham Hotspur 3-4-2-1: back line 39, front 69, length 30, width 69 (38% poss); GW11 A v Chelsea 3-4-2-1: back line 41, front 62, length 21, width 68 (43% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 3 league match(es) v LB-coded sides — xG 0.85/match and 1.7 pts/match v 1.69 and 1.5 against the rest → **struggles — chance creation drops** (threshold: xG v LB at least 90% of the rest). GW1 A v Nottingham Forest 1–0, xG 0.47, box shots 6, poss 44%; GW5 H v Crystal Palace 0–0, xG 1.31, box shots 9, poss 51%; GW8 A v Sunderland 0–0, xG 0.76, box shots 7, poss 50%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Stach 5, Elvedi 1, Tanaka 1** · FPL editorial order: Stach #1, Wilson #2, Longstaff #3
- Direct free-kick shooters: **Stach 4** · FPL order: Stach #1, Wilson #2, Longstaff #3
- Penalties taken: **—** · FPL order: Calvert-Lewin #1, Nmecha #2, Piroe #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Stach 2, Wilson 1**
- Corner targets (headed shots from corners): **Muharemovic 3, Calvert-Lewin 1, Justin 1** · corner shots 15

**Through-ball suppliers (Block P, PL/Opta, season):** Sean Longstaff 1 (0.40/90, percentile 85, 223 min); Anton Stach 2 (0.26/90, percentile 75, 681 min) · club total 10 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 334 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 6.83, field tilt 43.6, possession 44.2%, box entries 5, direct speed 2.49, SCA 20; GW2: PPDA 11.73, field tilt 41.1, possession 47.1%, box entries 7, direct speed 2.56, SCA 24; GW3: PPDA 11.61, field tilt 33.9, possession 33.7%, box entries 7, direct speed 2.89, SCA 18; GW4: PPDA 11.54, field tilt 46.8, possession 50.6%, box entries 14, direct speed 2.29, SCA 28; GW5: PPDA 9, field tilt 40.1, possession 50.9%, box entries 6, direct speed 2.29, SCA 21; GW6: PPDA 10.03, field tilt 29.2, possession 41.8%, box entries 6, direct speed 2.72, SCA 18; GW7: PPDA 7.91, field tilt 59.9, possession 61.1%, box entries 7, direct speed 2.15, SCA 24; GW8: PPDA 8.33, field tilt 50.2, possession 49.3%, box entries 8, direct speed 2.43, SCA 20; GW9: PPDA 9.67, field tilt 55.8, possession 56.4%, box entries 9, direct speed 2.29, SCA 18; GW10: PPDA 9.55, field tilt 40, possession 39.4%, box entries 10, direct speed 3.05, SCA 30

**Zone 14 (C13, SofaScore heat-map points, 11 league matches):** for 28.5/match (rank 10 of 20) · conceded 31.3/match (rank 10 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 3.9/match · allowed 5.8/match · PPDA 9.0. Per match for/allowed: GW3 8/6; GW4 9/5; GW5 0/4; GW6 1/11; GW7 5/4; GW8 5/5 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 3-4-2-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: James Trafford (16, 3/3)
- DEF: Tarik Muharemović (16, 3/3), Gabriel Gudmundsson (15, 3/3), Nico Elvedi (14, 3/3)
- MID: James Justin (16, 3/3), Jayden Bogle (16, 3/3), Ethan Ampadu (16, 3/3), Ao Tanaka (15, 3/3), Sean Longstaff (6, 2/3), Anton Stach (6, 0/3)
- FWD: Dominic Calvert-Lewin (16, 3/3)
- Contested slots: none · Excluded (FPL flag): none
- Absent last match (E12, SofaScore list): Joseph (Knee Injury)
- Substitutions this season (C3): GW9 65' Ao Tanaka→Anton Stach CHASING; GW9 65' Gabriel Gudmundsson→Sean Longstaff CHASING; GW10 90' Sean Longstaff→Ilia Gruev CARD-RISK; GW10 90' Jayden Bogle→Joe Rodon LATE; GW10 77' Lukas Nmecha→Noah Okafor TACTICAL; GW10 77' Ao Tanaka→Harry Wilson TACTICAL; GW10 46' Gabriel Gudmundsson→Melvin Bard HALF-TIME; GW11 90' Gabriel Gudmundsson→Melvin Bard CARD-RISK; GW11 90' Sean Longstaff→Harry Wilson CARD-RISK; GW11 86' Ao Tanaka→Joe Rodon LATE; GW11 86' Jayden Bogle→Anton Stach CARD-RISK; GW11 73' Noah Okafor→Brenden Aaronson GAME-STATE

### First-choice players and absences (F14) — generated 2026-11-24 07:45 UTC
First choice = starter baseline (GK, 3 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | James Trafford | start weight 16 | OK | a | — | — |
| CB | Tarik Muharemović | start weight 16 | OK | a | Joe Rodon | — |
| CB | Nico Elvedi | start weight 14 | OK | a 100% | Joe Rodon | — |
| CB | Jaka Bijol | start weight 2 | OK | a | Joe Rodon | — |
| xGI #1 | Dominic Calvert-Lewin | xGI 6.07 | OK | a 100% | Anton Stach | — |
| xGI #2 | Jayden Bogle | xGI 2.80 | OK | a | Anton Stach | — |
| Penalties #1 (FPL) | Calvert-Lewin | FPL order | OK | a 100% | Nmecha | — |
| Direct FK #1 (FPL) | Stach | FPL order | OK | a 100% | Wilson | — |
| Corners (observed) | Anton Stach | 26 corners taken | OK | a 100% | Harry Wilson | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 A Nottingham Forest: Nico Elvedi (did not start) · GW2 H Brentford: Nico Elvedi (did not start) · GW3 A Brighton & Hove Albion: Jaka Bijol (did not start) · GW4 H Newcastle United: Jaka Bijol (did not start) · GW5 H Crystal Palace: Jaka Bijol (did not start) · GW6 A Arsenal: Jaka Bijol (did not start) · GW7 H Manchester United: Jaka Bijol (did not start) · GW8 A Sunderland: Nico Elvedi (did not start) · GW9 A Bournemouth: Jaka Bijol (did not start) · GW10 H Tottenham Hotspur: Jaka Bijol (did not start) · GW11 A Chelsea: Jaka Bijol (did not start)

### Next fixtures (all competitions)
- Sat 28 Nov 15:00 UTC · Premier League R12 · H v Coventry City
- Wed 02 Dec 19:30 UTC · Premier League R13 · A v Manchester City
- Sat 05 Dec 15:00 UTC · Premier League R14 · H v Ipswich Town
- Sat 12 Dec 15:00 UTC · Premier League R15 · A v Liverpool FC
- Sat 19 Dec 15:00 UTC · Premier League R16 · H v Fulham
- Sat 26 Dec 12:30 UTC · Premier League R17 · A v Aston Villa

### FPL availability flags (players with league minutes this season)
none flagged
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
- GW11 A Chelsea 4–1 · xG 2.77–0.64 · poss 43% · 3-4-2-1 · scorers: Noah Okafor 28', Dominic Calvert-Lewin 53', Noah Okafor 58', Brenden Aaronson 90'
### Corner takers observed (LiveScore Block L)
- Anton Stach: 26 corners (17 left, 9 right)
- Harry Wilson: 6 corners (1 left, 5 right)
- Sean Longstaff: 6 corners (6 left, 0 right)
- Daniel James: 1 corners (1 left, 0 right, 1 short)
