# Nottingham Forest — data doc
*Feeder-written (2026-11-03 07:42 UTC); do not edit. Narrative: `profiles/teams/nottm-forest.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-03 07:42 UTC)
**Manager:** Oliver Glasner · **Venue:** City Ground · **SofaScore:** https://www.sofascore.com/football/team/nottingham-forest/14 · **FPL code:** NFO
**Table:** 19th, 6 pts (1W 3D 5L, GF 6 GA 12) · Home 20th (0-1-3, 0:3) · Away 12th (1-2-2, 6:9)
**Standing context (F15):** 29 league games left · points v 4th -10, v 5th -9, v 17th (last safe) -1, v 18th -1 · goal difference -6
**Suspension watch (D7, all players of the club):** Murillo — 🟨 2 from a ban (3/5); Aina — 🟨 2 from a ban (3/5); McAtee — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 9 league matches):** goals after 75′ — for 1/6 (17%), against 4/12 (33%) · scored first 4, conceded first 4 (44% of matches), goalless 1 · points from losing positions 0 of 15 (5 matches behind at some point) · points from winning positions 5 of 12 (4 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Murillo (DEF) 10.1/90, hit 6/9; Schlager (MID) 12.2/90, hit 4/9; McAtee (MID) 11.3/90, hit 4/9; Milenković (DEF) 9.2/90, hit 2/5; N.Williams (DEF) 5.4/90, hit 2/9; Diomande (DEF) 8.7/90, hit 1/5
**Manager tenure (F13, SofaScore):** Oliver Glasner since 06 Jul 2026 · 9 matches in charge, all competitions (1W 3D 5L) · 9 league matches this season · contract to 30 Jun 2029 · previous club Crystal Palace · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Leeds United — last 4: Aug 2026 EFL Cup Nottingham Forest 0–2 Leeds United (yellows 4–3, xG 1.21–2.58); Aug 2026 Premier League Nottingham Forest 0–1 Leeds United (yellows 2–1, xG 0.66–0.47); Feb 2026 Premier League Leeds United 3–1 Nottingham Forest (yellows 1–1, xG 2.50–1.33); Nov 2025 Premier League Nottingham Forest 3–1 Leeds United (yellows 2–1, xG 2.55–0.74) · 15 yellows in 4
**Archetype (F5):** used **TR** — derived TR [DERIVED] — **narrative LB v data TR** — data TR used; review the narrative line · signals, last 6 league matches: possession 50.0%, PPDA 13.6 (Understat, 5 matches; lower = harder press), opponent offsides forced 1.3/match (line height), fast breaks 1.6/match (season), both sides' xG 2.79/match (openness) · note: computed from 5 of 6 GWs (no PPDA/possession for GW9). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 11 (permanent 6, loan 0, free 0, loan returns 5) · out 17 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 9 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 14.64 | 5 | Big chances against | 14 | 2 |
| xGOT | 7.38 | 20 | Box shots against | 57 | 2 |
| xA | 9.82 | 4 | Corners against | 37 | 4 |
| Shots | 152 | 2 | Crosses faced | 149 | 7 |
| SoT | 31 | 15 | Dribbled past | 71 | 15 |
| Big chances | 26 | 5 | Errors→shot | 1 | 1 |
| Shots in box | 96 | 3 | GK goals prevented | -2.72 | 16 |
| Corners | 42 | 10 | Clearances | 233 | 12 |
| Crosses | 174 | 4 | Tackles | 166 | 3 |
| Fast breaks | 14 | 4 | Interceptions | 65 | 17 |
| FK shots | 5 | 5 | Def. contributions | 485 | 15 |
| Possession % | 47.56 | 13 | Aerial % | 51.35 | 7 |
| Pass % | 78.82 | 14 | Duel % | 49.32 | 12 |
| Long balls | 363 | 2 | Fouls | 127 | 19 |
| Dribbles | 64 | 12 | Yellows | 20 | 13 |
| Shots against | 88 | 1 | Km covered | 1024 | 11 |
| SoT against | 27 | 2 | Sprints | 945 | 15 |
Per match: xG 1.63 · xGOT 0.82 · shots 16.9 · shots against 9.8 · big chances 2.9 for / 1.6 against · corners 4.7 / 4.1 · crosses 19.3 / 16.6 · possession 47.555555555556%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | A | Aston Villa | 2–1 | 2.28/2.80 | 0.82/1.09 | 46 | 22/7 | 7/5 | 14/6 | 3/1 | 6/2 | 1/6 | 14/9 v 15/3 | 0/4 |
| 5 | H | Coventry City | 0–1 | 1.10/1.33 | 0.67/0.69 | 62 | 24/10 | 3/3 | 12/5 | 12/1 | 1/1 | 6/2 | 32/10 v 14/5 | 2/2 |
| 6 | A | Crystal Palace | 1–3 | 3.34/3.80 | 2.41/2.43 | 57 | 24/13 | 6/7 | 16/11 | 8/2 | 8/5 | 8/5 | 29/10 v 15/6 | 2/1 |
| 7 | H | Arsenal | 0–1 | 0.90/0.75 | 1.14/0.92 | 26 | 14/9 | 2/1 | 8/7 | 6/3 | 0/1 | 8/6 | 14/1 v 27/7 | 1/2 |
| 8 | A | Ipswich Town | 1–1 | 2.29/2.76 | 0.46/0.86 | 51 | 17/7 | 5/3 | 15/3 | 1/0 | 4/1 | 5/0 | 22/5 v 6/1 | 2/1 |
| 9 | A | Brentford | 0–2 | 0.86/— | 0.46/— | 58 | 15/7 | 1/1 | 9/3 | 6/1 | 1/1 | 4/3 | 18/4 v 10/2 | 1/1 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | A | Aston Villa | 2–1 | 3-4-2-1 | 16/11 | 5/2 | 0/0 | 360/421 | 46/62 | Savona (Knee Injury) | Gomes (ban (red)), Onana (Cruciate Ligament Injury), Madjo (Knock Injury), Goretzka (Knee Injury), Cash (Physical Discomfort; doubtful) | Andy Madley |
| 5 | H | Coventry City | 0–1 | 3-4-2-1 | 12/10 | 2/0 | 0/0 | 508/311 | 61/56 | Savona (Knee Injury), Milenković (Hamstring Injury) | Awoniyi (ban (red)), Amenda (Calf Injury), Wright (Muscle Injury), Eccles (Knock Injury), Kesler-Hayden (Hamstring Injury), Woolfenden (Knee Injury) | Jarred Gillett |
| 6 | A | Crystal Palace | 1–3 | 3-4-2-1 | 10/11 | 2/2 | 0/0 | 498/386 | 50/47 | Jesus (Calf Injury), Savona (Knee Injury) | Disasi (ban (red)), Riad (Knee Injury), Henderson (Foot Injury), Mateta (Hamstring Injury) | Peter Bankes |
| 7 | H | Arsenal | 0–1 | 3-4-2-1 | 14/8 | 1/1 | 0/0 | 224/634 | 33/76 | Jesus (Calf Injury), Savona (Knee Injury), Gibbs-White (Knock Injury; doubtful) | Tzolis (Hamstring Injury), Hincapié (Ankle Injury) | Michael Oliver |
| 8 | A | Ipswich Town | 1–1 | 3-4-2-1 | 11/9 | 1/1 | 0/0 | 480/486 | 60/58 | Jesus (Calf Injury), Savona (Knee Injury) | Lukić (Groin Injury) | Thomas Bramall |
| 9 | A | Brentford | 0–2 | 3-4-2-1 | 17/6 | 3/1 | 0/0 | 489/346 | 69/47 | Jesus (Calf Injury), Domínguez (Knock Injury), Savona (Knee Injury) | Yarmoliuk (ban (red)), Carvalho (Knock Injury), Furo (Knee Surgery), Henry (Muscle Injury) | Darren England |
Per match: fouls 14.1 / 10.7 · yellows 2.22 / 1.56 · reds 0 / 0 (season) · offsides forced 1.7, committed 1.8 · crosses attempted 19.3 / faced 16.6. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 0.90 for / 0.83 against per match · Away (5): xG 2.21 / 1.18. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW9 A v Brentford 0–2 (Sat 31 Oct 15:00 UTC) — formation 3-4-2-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Matz Sels | G | 90 | 6 | 0.00 | 0.00 | 0 | 0 | 0 | 0 | 32 |
| Jair | D | 90 | 6.7 | 0.00 | 0.05 | 3 | 0 | 6 | 1 | 67 |
| Nikola Milenković | D | 90 | 5.6 | 0.00 | 0.00 | 0 | 0 | 9 | 0 | 56 |
| Murillo | D | 90 | 7 | 0.04 | 0.01 | 0 | 1 | 15 | 0 | 90 |
| Ola Aina | M | 45 | 6.6 | 0.00 | 0.00 | 1 | 0 | 2 | 2 | 34 |
| James McAtee | M | 90 | 7.3 | 0.15 | 0.40 | 2 | 3 | 5 | 2 | 96 |
| Xaver Schlager | M | 45 | 5.9 | 0.02 | 0.01 | 0 | 1 | 0 | 0 | 37 |
| Neco Williams | M | 90 | 6.6 | 0.00 | 0.05 | 0 | 0 | 5 | 8 | 75 |
| Dan Ndoye | F | 65 | 6.5 | 0.01 | 0.03 | 1 | 1 | 0 | 0 | 21 |
| Morgan Gibbs-White | F | 90 | 6.5 | 0.13 | 0.24 | 1 | 3 | 0 | 3 | 46 |
| Liam Delap | F | 65 | 5.9 | 0.18 | 0.01 | 0 | 3 | 0 | 0 | 17 |
Subs used: Daniel Muñoz (45'), Ryan Yates (45'), Chris Wood (25'), Arnaud Kalimuendo (25')
Goals: 30' Nikola Milenković [opp, ownGoal]; 76' Igor Thiago (assist Jaidon Anthony) [opp]
Substitutions (own): 46' Ryan Yates for Xaver Schlager; 46' Daniel Muñoz for Ola Aina; 65' Arnaud Kalimuendo for Dan Ndoye; 65' Chris Wood for Liam Delap
Cards: 36' Nikola Milenković (yellow, own); 64' Daniel Muñoz (yellow, own); 68' Michael Kayode (yellow, opp); 83' James McAtee (yellow, own)
**Baseline XI change vs GW8 (3-4-2-1 → 3-4-2-1):** in — Ola Aina; out — Daniel Muñoz.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 4 | A Aston Villa | 46' | FOR | Liam Delap | Murillo | open play | 0.01 |
| 4 | A Aston Villa | 74' | AGAINST | Alysson | John McGinn | [unmatched] | — |
| 4 | A Aston Villa | 88' | FOR | Igor Jesus | Morgan Gibbs-White | open play | 0.53 |
| 5 | H Coventry City | 55' | AGAINST | Jay DaSilva | Carl Rushworth | open play | 0.28 |
| 6 | A Crystal Palace | 3' | FOR | Dan Ndoye | — | open play | 0.28 |
| 6 | A Crystal Palace | 41' | AGAINST | Daichi Kamada | Quinten Timber | open play | 0.54 |
| 6 | A Crystal Palace | 45' | AGAINST | Jefferson Lerma | Adam Wharton | corner | 0.48 |
| 6 | A Crystal Palace | 59' | AGAINST | Yéremy Pino | — | open play | 0.40 |
| 7 | H Arsenal | 80' | AGAINST | Noni Madueke | Declan Rice | open play | 0.04 |
| 8 | A Ipswich Town | 13' | FOR | Neco Williams | Daniel Muñoz | open play | 0.44 |
| 8 | A Ipswich Town | 41' | AGAINST | Julio Enciso | — | open play | 0.27 |
| 9 | A Brentford | 30' | AGAINST | Nikola Milenković | — | own goal | — |
| 9 | A Brentford | 76' | AGAINST | Igor Thiago | Jaidon Anthony | [no Understat] | — |
Scored 6: open play 5, penalty 1 · Conceded 12: open play 7, direct FK 1, [unmatched] 1, corner 1, own goal 1, [no Understat] 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW7 AG v Arsenal 80' Noni Madueke (assist Declan Rice): GOAL! - Noni Madueke score from a shot with the right foot, that takes a deflection. · before: 80' Jair Cunha from Nottingham Forest intercepts a cross aimed towards the box. ‹ 79' Daniel Munoz from Nottingham Forest intercepts a cross aimed towards the box. ‹ 79' Jair Cunha successfully blocks the shot
- GW8 FOR v Ipswich Town 13' Neco Williams (assist Daniel Munoz, key pass Morgan Gibbs-White): G O O O A A A L - Neco Williams volleys the ball into the back of the net with the right. A great finish! · before: 13' The cross by Daniel Munoz from Nottingham Forest successfully finds a teammate in the box. ‹ 12' Jair Cunha relieves the pressure with a clearance ‹ 11' James McAtee relieves the pressure with a clearance
- GW8 AG v Ipswich Town 41' Julio Enciso: G O O O A A A L - Julio Enciso from Ipswich scores from outside the box with the left foot! · before: 41' Ipswich start a counter attack. ‹ 41' Nikola Milenkovic could cost his team a goal after a defensive blunder. ‹ 41' Dara O'Shea makes the tackle and wins possession for his team
- GW9 FOR v Brentford 30' Nikola Milenković [OG]: OWN GOAL - Nikola Milenkovic sends the ball into his own net! · before: 30' Nikola Milenkovic from Nottingham Forest intercepts a cross aimed towards the box. ‹ 29' Kevin Schade makes the tackle and wins possession for his team ‹ 28' Neco Williams makes the tackle and wins possession for his team
- GW9 AG v Brentford 76' Igor Thiago (assist Jaidon Anthony, key pass Aaron Hickey): GOAL! - Igor Thiago score from a shot with the right foot, that takes a deflection. · before: 76' Jaidon Anthony creates a scoring opportunity for his teammate ‹ 75' Keane Lewis-Potter is penalised for pushing Arnaud Kalimuendo-Muinga. ‹ 75' Neco Williams relieves the pressure with a clearance

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW4 A v Aston Villa 74' Alysson: no structured culprit — reports only
- GW5 H v Coventry City 55' Jay DaSilva: no structured culprit — reports only
- GW6 A v Crystal Palace 41' Daichi Kamada: no structured culprit — reports only
- GW6 A v Crystal Palace 45' Jefferson Lerma: no structured culprit — reports only
- GW6 A v Crystal Palace 59' Yéremy Pino: no structured culprit — reports only
- GW7 H v Arsenal 80' Noni Madueke: no structured culprit — reports only
  · GW7 other flags: Ousmane Diomande lastManTackle 1
- GW8 A v Ipswich Town 41' Julio Enciso: Nikola Milenković error leading to the goal [CONFIRMED — SofaScore error flag]
- GW9 A v Brentford 30' Nikola Milenković [OG]: Nikola Milenković own goal [CONFIRMED — SofaScore]
- GW9 A v Brentford 76' Igor Thiago: no structured culprit — reports only

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

**Corners (E10 data layer):** observed takers GW1–9 [CONFIRMED — LiveScore Block L, 42 corners; side L/R as LiveScore records it; foot from SofaScore]: James McAtee 19 (0L/19R, 1 short, left foot); Neco Williams 19 (19L/0R, right foot); Xaver Schlager 2 (0L/2R, left foot); Luca Netz 1 (0L/1R, left foot). First contact on corners that ended in a shot (Understat) — for: Murillo 8 (4 headed), Xaver Schlager 4, Ousmane Diomande 2 (1 headed), Nikola Milenkovic 1 (1 headed), Igor Jesus 1 (1 headed) · against (who beat them): Jefferson Lerma 2 (2 headed) — 1 goal, Jan Paul van Hecke 2 (1 headed), Gabriel 2 (1 headed), Alexander Isak 1 (1 headed), Micky van de Ven 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 39.5 (rank 14 of 20, 1 = highest line) · block length 23.0 (rank 18, 1 = most compact) · width 63.1. Per match: GW4 A v Aston Villa 3-4-2-1: back line 39, front 63, length 24, width 72 (46% poss); GW5 H v Coventry City 3-4-2-1: back line 42, front 67, length 25, width 57 (62% poss); GW6 A v Crystal Palace 3-4-2-1: back line 43, front 68, length 26, width 66 (57% poss); GW7 H v Arsenal 3-4-2-1: back line 35, front 66, length 30, width 64 (26% poss); GW8 A v Ipswich Town 3-4-2-1: back line 41, front 64, length 23, width 70 (51% poss); GW9 A v Brentford 3-4-2-1: back line 43, front 68, length 24, width 60 (58% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 3 league match(es) v LB-coded sides — xG 2.24/match and 0.3 pts/match v 1.32 and 0.8 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW5 H v Coventry City 0–1, xG 1.10, box shots 12, poss 62%; GW6 A v Crystal Palace 1–3, xG 3.34, box shots 16, poss 57%; GW8 A v Ipswich Town 1–1, xG 2.29, box shots 15, poss 51%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Williams 6, McAtee 5, Delap 1** · FPL editorial order: McAtee #1, N.Williams #2, Schlager #3
- Direct free-kick shooters: **Gibbs-White 2, McAtee 2, Williams 1** · FPL order: Gibbs-White #1, Murillo #2, N.Williams #3
- Penalties taken: **Gibbs-White 1** · FPL order: Gibbs-White #1, Wood #2, Delap #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Gibbs-White 6, Aina 1, Murillo 1**
- Corner targets (headed shots from corners): **Murillo 4, Milenkovic 1, Jesus 1, Diomande 1** · corner shots 19
- **DISAGREEMENT:** observed corner taker Neco Williams (6) v FPL #1 McAtee — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Morgan Gibbs-White 5 (0.62/90, percentile 93, 720 min); James McAtee 5 (0.58/90, percentile 92, 773 min); Igor Jesus 1 (0.35/90, percentile 83, 256 min); Liam Delap 2 (0.30/90, percentile 80, 593 min); Xaver Schlager 2 (0.27/90, percentile 75, 667 min) · club total 19 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 306 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 10.19, field tilt 56.4, possession 55.8%, box entries 12, direct speed 3.11, SCA 23; GW2: PPDA 20.04, field tilt 27.2, possession 31.7%, box entries 10, direct speed 4.01, SCA 24; GW3: PPDA 7.26, field tilt 41.6, possession 41.5%, box entries 6, direct speed 3.26, SCA 24; GW4: PPDA 8.85, field tilt 49.4, possession 46.6%, box entries 14, direct speed 2.86, SCA 44; GW5: PPDA 9.38, field tilt 73.6, possession 62.6%, box entries 17, direct speed 2.14, SCA 47; GW6: PPDA 9.47, field tilt 62.1, possession 56.5%, box entries 21, direct speed 2.37, SCA 42; GW7: PPDA 18.4, field tilt 23.7, possession 26.7%, box entries 6, direct speed 2.61, SCA 28; GW8: PPDA 12.16, field tilt 53.5, possession 50.6%, box entries 8, direct speed 2.67, SCA 33

**Zone 14 (C13, SofaScore heat-map points, 9 league matches):** for 33.8/match (rank 6 of 20) · conceded 26.4/match (rank 14 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 7.1/match · allowed 4.9/match · PPDA 13.2. Per match for/allowed: GW3 6/3; GW4 9/8; GW5 9/2; GW6 9/6; GW7 6/10; GW8 6/4 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 3-4-2-1, 9 league matches, weights last-3 ×3 / older ×1
- GK: Matz Sels (15, 3/3)
- DEF: Murillo (15, 3/3), Jair (13, 3/3), Nikola Milenković (9, 2/3)
- MID: James McAtee (15, 3/3), Neco Williams (15, 3/3), Xaver Schlager (14, 3/3), Ola Aina (8, 1/3), Ibrahim Sangaré (1, 0/3)
- FWD: Dan Ndoye (15, 3/3)
- Contested slots: D Nikola Milenković 9 v Daniel Muñoz 9 · Excluded (FPL flag): Nicolás Domínguez — Muscular injury - 75% chance of playing
- Absent last match (E12, SofaScore list): Jesus (Calf Injury), Domínguez (Knock Injury), Savona (Knee Injury)
- Substitutions this season (C3): GW6 66' Xaver Schlager→Ibrahim Sangaré CHASING; GW7 85' James McAtee→Callum Hudson Odoi LATE; GW7 85' Jair→Chris Wood INJURY [ONE SOURCE: SofaScore flag; LiveScore called it tactical; FPL shows him available]; GW7 74' Nicolás Domínguez→Ibrahim Sangaré TACTICAL; GW7 73' Dan Ndoye→Arnaud Kalimuendo TACTICAL; GW8 90' Liam Delap→Chris Wood LATE; GW8 84' Neco Williams→Luca Netz INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW8 69' Dan Ndoye→Callum Hudson Odoi TACTICAL; GW9 65' Dan Ndoye→Arnaud Kalimuendo CHASING; GW9 65' Liam Delap→Chris Wood CHASING; GW9 46' Xaver Schlager→Ryan Yates HALF-TIME; GW9 46' Ola Aina→Daniel Muñoz HALF-TIME

### First-choice players and absences (F14) — generated 2026-11-03 07:42 UTC
First choice = starter baseline (GK, 3 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Matz Sels | start weight 15 | OK | a | — | — |
| CB | Murillo | start weight 15 | OK | a 100% | Ousmane Diomande | — |
| CB | Jair | start weight 13 | OK | a 100% | Ousmane Diomande | — |
| CB | Nikola Milenković | start weight 9 | OK | a 100% | Ousmane Diomande | — |
| xGI #1 | Morgan Gibbs-White | xGI 4.80 | OK | a 100% | Liam Delap | — |
| xGI #2 | Dan Ndoye | xGI 3.67 | OK | a 100% | Liam Delap | — |
| Penalties #1 (FPL) | Gibbs-White | FPL order | OK | a 100% | Wood | — |
| Direct FK #1 (FPL) | Gibbs-White | FPL order | OK | a 100% | Murillo | — |
| Corners (observed) | James McAtee | 19 corners taken | OK | a | Neco Williams | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Leeds United: all started · GW2 A Liverpool FC: all started · GW3 H Tottenham Hotspur: all started · GW4 A Aston Villa: Jair (did not start), Nikola Milenković (did not start) · GW5 H Coventry City: Nikola Milenković (Hamstring Injury) · GW6 A Crystal Palace: Jair (did not start), Nikola Milenković (did not start) · GW7 H Arsenal: Nikola Milenković (did not start), Morgan Gibbs-White (Knock Injury) · GW8 A Ipswich Town: all started · GW9 A Brentford: all started

### Next fixtures (all competitions)
- Sat 07 Nov 17:30 UTC · Premier League R10 · H v Manchester City
- Sat 21 Nov 15:00 UTC · Premier League R11 · A v Bournemouth
- Fri 27 Nov 20:00 UTC · Premier League R12 · H v Chelsea
- Wed 02 Dec 19:30 UTC · Premier League R13 · A v Hull City
- Sat 05 Dec 17:30 UTC · Premier League R14 · H v Brighton & Hove Albion
- Sun 13 Dec 14:00 UTC · Premier League R15 · A v Sunderland

### FPL availability flags (players with league minutes this season)
Dominguez — Muscular injury - 75% chance of playing (75%); Igor Jesus — Calf injury - Unknown return date (0%)
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
### Corner takers observed (LiveScore Block L)
- James McAtee: 19 corners (0 left, 19 right, 1 short)
- Neco Williams: 19 corners (19 left, 0 right)
- Xaver Schlager: 2 corners (0 left, 2 right)
- Luca Netz: 1 corners (0 left, 1 right)
- Nicolas Dominguez: 1 corners (1 left, 0 right)
