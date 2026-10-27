# Ipswich Town — data doc
*Feeder-written (2026-10-27 07:42 UTC); do not edit. Narrative: `profiles/teams/ipswich.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-10-27 07:42 UTC)
**Manager:** Gary O'Neil · **Venue:** Portman Road Stadium · **SofaScore:** https://www.sofascore.com/football/team/ipswich-town/32 · **FPL code:** IPS
**Table:** 12th, 10 pts (3W 1D 4L, GF 12 GA 16) · Home 7th (2-1-1, 5:5) · Away 18th (1-0-3, 7:11)
**Standing context (F15):** 30 league games left · points v 4th -5, v 5th -3, v 17th (last safe) +3, v 18th +4 · goal difference -4
**Suspension watch (D7, all players of the club):** nobody within 2 yellows of a ban, nobody suspended [FPL]
**Goal timing & game state (F17, 8 league matches):** goals after 75′ — for 6/12 (50%), against 1/16 (6%) · scored first 2, conceded first 6 (75% of matches), goalless 0 · points from losing positions 7 of 21 (7 matches behind at some point) · points from winning positions 9 of 12 (4 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Palacios (MID) 16.2/90, hit 4/7; Diop (DEF) 8.6/90, hit 4/8; O'Shea (DEF) 9.8/90, hit 3/8; Florentino (MID) 11.7/90, hit 1/5; Lukić (MID) 9.2/90, hit 1/6; Greaves (DEF) 7.4/90, hit 1/5
**Manager tenure (F13, SofaScore):** Gary O'Neil since 01 Jul 2026 · 10 matches in charge, all competitions (4W 1D 5L) · 8 league matches this season · contract to 30 Jun 2029 · previous club RC Strasbourg · interim flag not published by SofaScore
**Archetype (F5):** used **LB** — derived LB [DERIVED] (hand-set code agrees) · signals, last 6 league matches: possession 45.7%, PPDA 12.4 (Understat, 6 matches; lower = harder press), opponent offsides forced 1.5/match (line height), fast breaks 1.2/match (season), both sides' xG 3.06/match (openness). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap).
**Squad changes (F20, since 01 Jun 2026):** in 17 (permanent 14, loan 0, free 0, loan returns 3) · out 20 · flags: Zian Flemming arrived 01 Sep, 0 league starts since — role security low (FPL-owned ≥ 1% or tracked) — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 8 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 11.19 | 11 | Big chances against | 30 | 20 |
| xGOT | 13.86 | 4 | Box shots against | 90 | 19 |
| xA | 5.80 | 15 | Corners against | 38 | 12 |
| Shots | 84 | 20 | Crosses faced | 150 | 14 |
| SoT | 34 | 11 | Dribbled past | 60 | 12 |
| Big chances | 16 | 13 | Errors→shot | 5 | 6 |
| Shots in box | 52 | 19 | GK goals prevented | -2.92 | 18 |
| Corners | 23 | 20 | Clearances | 204 | 15 |
| Crosses | 113 | 19 | Tackles | 131 | 9 |
| Fast breaks | 10 | 10 | Interceptions | 79 | 6 |
| FK shots | 2 | 11 | Def. contributions | 454 | 7 |
| Possession % | 44 | 18 | Aerial % | 47.32 | 16 |
| Pass % | 81.86 | 12 | Duel % | 47.75 | 18 |
| Long balls | 206 | 18 | Fouls | 91 | 10 |
| Dribbles | 57 | 12 | Yellows | 15 | 7 |
| Shots against | 135 | 18 | Km covered | 940 | 4 |
| SoT against | 44 | 18 | Sprints | 955 | 4 |
Per match: xG 1.40 · xGOT 1.73 · shots 10.5 · shots against 16.9 · big chances 2.0 for / 3.8 against · corners 2.9 / 4.8 · crosses 14.1 / 18.8 · possession 44%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Liverpool FC | 0–2 | 0.75/0.60 | 0.69/0.74 | 45 | 14/10 | 5/7 | 4/5 | 4/2 | —/— | 4/3 | 15/4 v 11/3 | 4/5 |
| 4 | A | Crystal Palace | 3–2 | 1.68/2.10 | 0.62/0.94 | 54 | 12/11 | 6/4 | 8/9 | 1/1 | 3/1 | 3/6 | 21/5 v 20/2 | 0/1 |
| 5 | A | Everton | 0–1 | 1.44/1.10 | 2.24/2.59 | 48 | 13/21 | 4/2 | 9/13 | 4/8 | 1/5 | 4/4 | 13/3 v 16/4 | 1/0 |
| 6 | H | Fulham | 2–1 | 1.15/1.26 | 1.81/1.78 | 48 | 11/13 | 5/5 | 7/9 | 1/2 | 2/3 | 2/5 | 19/4 v 14/5 | 1/0 |
| 7 | A | Manchester City | 2–3 | 1.86/1.37 | 3.35/4.01 | 30 | 8/19 | 3/6 | 7/15 | 1/6 | 3/6 | 3/2 | 15/5 v 20/8 | 2/5 |
| 8 | H | Nottingham Forest | 1–1 | 0.46/0.86 | 2.29/2.76 | 49 | 7/17 | 3/5 | 3/15 | 0/1 | 1/4 | 0/5 | 6/1 v 22/5 | 1/2 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Liverpool FC | 0–2 | 4-2-3-1 | 6/13 | 1/3 | 0/0 | 428/531 | 46/67 | Matusiwa (Muscle Injury), Taylor (Knee Injury), Philogene-Bidace (Ankle Injury) | Bradley (Knee Injury), Chiesa (Back Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Gomez (Strain Injury) | Darren England |
| 4 | A | Crystal Palace | 3–2 | 4-2-3-1 | 16/6 | 3/1 | 0/1 | 452/389 | 65/45 | Taylor (Knee Injury) | Riad (Knee Injury), Sarr (Groin Injury), Mateta (Hamstring Injury), Nketiah (Physical Discomfort; doubtful) | Chris Kavanagh |
| 5 | A | Everton | 0–1 | 4-2-3-1 | 12/6 | 3/2 | 1/0 | 472/513 | 53/63 | Taylor (Knee Injury) | Nørgaard (Muscle Injury), Röhl (Knock Injury; doubtful) | Stuart Attwell |
| 6 | H | Fulham | 2–1 | 4-2-3-1 | 8/10 | 2/4 | 0/0 | 454/505 | 66/57 | Issahaku (ban (cards)) | Robinson (Ankle Injury; doubtful) | Lewis Smith |
| 7 | A | Manchester City | 2–3 | 3-4-2-1 | 16/8 | 2/1 | 0/0 | 319/753 | 39/85 | — | — | Farai Hallam |
| 8 | H | Nottingham Forest | 1–1 | 4-2-3-1 | 9/11 | 1/1 | 0/0 | 486/480 | 58/60 | Lukić (Groin Injury) | Jesus (Calf Injury), Savona (Knee Injury) | Thomas Bramall |
Per match: fouls 11.4 / 9.4 · yellows 1.88 / 2.00 · reds 1 / 1 (season) · offsides forced 1.6, committed 1.9 · crosses attempted 14.1 / faced 18.8. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 1.04 for / 1.36 against per match · Away (4): xG 1.76 / 2.75. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW8 H v Nottingham Forest 1–1 (Fri 23 Oct 19:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Christian Walton | G | 90 | 6.3 | 0.00 | 0.00 | 0 | 0 | 1 | 0 | 49 |
| Abdoul Ouattara | D | 90 | 6.8 | 0.00 | 0.02 | 0 | 0 | 7 | 0 | 56 |
| Issa Diop | D | 90 | 6.4 | 0.00 | 0.00 | 0 | 0 | 6 | 0 | 65 |
| Dara O'Shea | D | 90 | 6.4 | 0.00 | 0.01 | 0 | 0 | 8 | 0 | 66 |
| Leif Davis | D | 90 | 8.1 | 0.00 | 0.06 | 0 | 0 | 6 | 2 | 64 |
| Exequiel Palacios | M | 90 | 7 | 0.00 | 0.08 | 2 | 0 | 3 | 1 | 103 |
| Florentino Luís | M | 85 | 6.7 | 0.00 | 0.02 | 0 | 0 | 7 | 0 | 74 |
| Abdul Fatawu Issahaku | M | 73 | 6 | 0.03 | 0.00 | 0 | 1 | 1 | 1 | 29 |
| Julio Enciso | M | 86 | 8.3 | 0.31 | 0.04 | 0 | 4 | 1 | 2 | 53 |
| Jaden Philogene-Bidace | M | 61 | 6.5 | 0.07 | 0.01 | 0 | 1 | 2 | 0 | 41 |
| Emersonn | F | 60 | 6.5 | 0.00 | 0.05 | 1 | 0 | 1 | 0 | 17 |
Subs used: Zian Flemming (30'), Jack Clarke (29'), Daizen Maeda (17'), Azor Matusiwa (14'), Chuba Akpom (13')
Goals: 13' Neco Williams (assist Daniel Muñoz) [opp]; 41' Julio Enciso [own]
Substitutions (own): 60' Zian Flemming for Emersonn; 61' Jack Clarke for Jaden Philogene-Bidace; 73' Daizen Maeda for Abdul Fatawu Issahaku; 85' Azor Matusiwa for Florentino Luís; 86' Chuba Akpom for Julio Enciso
Cards: 51' Issa Diop (yellow, own); 54' Murillo (yellow, opp)
**Baseline XI change vs GW7 (3-4-2-1 → 4-2-3-1):** in — Abdul Fatawu Issahaku, Jaden Philogene-Bidace; out — Daizen Maeda, Jacob Greaves.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 3 | H Liverpool FC | 6' | AGAINST | Alexander Isak | Cody Gakpo | open play | 0.12 |
| 3 | H Liverpool FC | 9' | AGAINST | Alexander Isak | Cody Gakpo | open play | 0.13 |
| 4 | A Crystal Palace | 14' | AGAINST | Anan Khalaili | Daichi Kamada | open play | 0.04 |
| 4 | A Crystal Palace | 23' | FOR | Emersonn | Leif Davis | open play | 0.39 |
| 4 | A Crystal Palace | 45' | FOR | Leif Davis | Emersonn | open play | 0.47 |
| 4 | A Crystal Palace | 75' | AGAINST | Jørgen Strand Larsen | Daichi Kamada | open play | 0.07 |
| 4 | A Crystal Palace | 90' | FOR | Zian Flemming | — | open play | 0.64 |
| 5 | A Everton | 11' | AGAINST | Thierno Barry | James Tarkowski | open play | 0.35 |
| 6 | H Fulham | 55' | AGAINST | Ryan Sessegnon | — | corner | 0.02 |
| 6 | H Fulham | 88' | FOR | Abdoul Ouattara | — | open play | 0.01 |
| 6 | H Fulham | 90' | FOR | Dara O'Shea | Jack Clarke | set piece | 0.55 |
| 7 | A Manchester City | 19' | AGAINST | Phil Foden | Jérémy Doku | open play | 0.64 |
| 7 | A Manchester City | 21' | FOR | Daizen Maeda | Abdoul Ouattara | open play | 0.17 |
| 7 | A Manchester City | 34' | AGAINST | Erling Haaland | Mateo Kovačić | open play | 0.34 |
| 7 | A Manchester City | 69' | AGAINST | Erling Haaland | Iliman Ndiaye | open play | 0.65 |
| 7 | A Manchester City | 90' | FOR | Zian Flemming | — | penalty | 0.76 |
| 8 | H Nottingham Forest | 13' | AGAINST | Neco Williams | Daniel Muñoz | open play | 0.44 |
| 8 | H Nottingham Forest | 41' | FOR | Julio Enciso | — | open play | 0.27 |
Scored 12: open play 10, set piece 1, penalty 1 · Conceded 16: open play 12, direct FK 1, own goal 1, penalty 1, corner 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW6 AG v Fulham 55' Ryan Sessegnon: G O O O A A A L - Ryan Sessegnon from Fulham scores from outside the box with the right foot! · before: 55' Issa Diop from Ipswich intercepts a cross aimed towards the box. ‹ 55' Alex Iwobi swings in the ball from a corner on the left, but it is nowhere near a teammate. ‹ 55' Dara O'Shea from Ipswich intercepts a cross aimed towards the box.
- GW6 FOR v Fulham 88' Abdoul Ouattara: G O O O A A A L - Abdoul Ouattara from Ipswich scores from outside the box with the right foot! · before: 88' Calvin Bassey from Fulham intercepts a cross aimed towards the box. ‹ 87' Alex Iwobi is leaving the field to be replaced by Emile Smith Rowe in a tactical substituti ‹ 87' Gonzalo Garcia is leaving the field to be replaced by Hugo Larsson in a tactical substituti
- GW6 FOR v Fulham 90+2' Dara O'Shea (assist Jack Clarke): G O O O A A A L - Dara O'Shea from Ipswich heads the ball home! · before: 90+2' The cross by Jack Clarke from Ipswich successfully finds a teammate in the box. ‹ 90+1' The referee signals a free kick as David Affengruber from Fulham trips Chuba Akpom ‹ 90' The fourth official shows there are 5 minute(s) of time to be added.
- GW7 AG v Manchester City 19' Phil Foden (assist Jeremy Doku, key pass Mateo Kovacic): G O O O A A A L - Phil Foden scores with the left foot! · before: 19' Jeremy Doku creates a scoring opportunity for his teammate ‹ 18' Leif Davis from Ipswich intercepts a cross aimed towards the box. ‹ 18' Christian Walton makes a crucial save!
- GW7 FOR v Manchester City 21' Daizen Maeda (assist Abdoul Ouattara): G O O O A A A L - Daizen Maeda scores with the left foot! · before: 21' Marc Guehi could cost his team a goal after a defensive blunder. ‹ 21' Abdoul Ouattara creates a scoring opportunity for his teammate ‹ 21' Ayyoub Bouaddi relieves the pressure with a clearance
- GW7 AG v Manchester City 34' Erling Haaland (assist Mateo Kovacic): G O O O A A A L - Erling Haaland from Manchester City heads the ball home! · before: 34' Mateo Kovacic creates a scoring opportunity for his teammate ‹ 34' Mateo Kovacic creates a scoring opportunity for his teammate ‹ 34' Jacob Greaves successfully blocks the shot
- GW7 AG v Manchester City 69' Erling Haaland (assist Iliman Ndiaye): G O O O A A A L - Erling Haaland scores with the left foot! · before: 69' Iliman Ndiaye creates a scoring opportunity for his teammate ‹ 69' Florentino makes the tackle and wins possession for his team ‹ 68' Gianluigi Donnarumma from Manchester City intercepts a cross aimed towards the box.
- GW7 FOR v Manchester City 90' Zian Flemming [pen]: G O O O A A A L - Zian Flemming from Ipswich puts it away from the penalty spot in the middle with the right foot. Gianluigi Donnarumma jumped on the  · before: 90' After VAR check, the referee changed the call and decided to award a penalty for Ipswich! ‹ 89' VAR - PENALTY! - The referee has stopped the play. VAR check in progress, a potential penal ‹ 88' PENALTY - Marc Guehi from Manchester City concedes a penalty for tripping Abdul Fatawu.
- GW8 AG v Nottingham Forest 13' Neco Williams (assist Daniel Munoz, key pass Morgan Gibbs-White): G O O O A A A L - Neco Williams volleys the ball into the back of the net with the right. A great finish! · before: 13' The cross by Daniel Munoz from Nottingham Forest successfully finds a teammate in the box. ‹ 12' Jair Cunha relieves the pressure with a clearance ‹ 11' James McAtee relieves the pressure with a clearance
- GW8 FOR v Nottingham Forest 41' Julio Enciso: G O O O A A A L - Julio Enciso from Ipswich scores from outside the box with the left foot! · before: 41' Ipswich start a counter attack. ‹ 41' Nikola Milenkovic could cost his team a goal after a defensive blunder. ‹ 41' Dara O'Shea makes the tackle and wins possession for his team

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW3 H v Liverpool FC 6' Alexander Isak: no structured culprit — reports only
- GW3 H v Liverpool FC 9' Alexander Isak: no structured culprit — reports only
- GW4 A v Crystal Palace 14' Anan Khalaili: no structured culprit — reports only
- GW4 A v Crystal Palace 75' Jørgen Strand Larsen: no structured culprit — reports only
  · GW4 other flags: Kjell Scherpen errorLeadToAShot 1
- GW5 A v Everton 11' Thierno Barry: no structured culprit — reports only
  · GW5 other flags: Florentino Luís errorLeadToAShot 1
- GW6 H v Fulham 55' Ryan Sessegnon: no structured culprit — reports only
  · GW6 other flags: Issa Diop clearanceOffLine 1
- GW7 A v Manchester City 19' Phil Foden: no structured culprit — reports only
- GW7 A v Manchester City 34' Erling Haaland: no structured culprit — reports only
- GW7 A v Manchester City 69' Erling Haaland: no structured culprit — reports only
  · GW7 error leading to a goal (SofaScore, match level — 3 conceded, the goal is not identified): Abdoul Ouattara [CONFIRMED — SofaScore error flag]
- GW8 H v Nottingham Forest 13' Neco Williams: Dara O'Shea error leading to the goal [CONFIRMED — SofaScore error flag]
  · GW8 other flags: Issa Diop errorLeadToAShot 1; Florentino Luís errorLeadToAShot 2; Leif Davis clearanceOffLine 1

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 71 | 8.58 | 10 | 107 | 16.56 | 12 |
| corner | 7 | 0.49 | 0 | 17 | 1.21 | 1 |
| set piece | 4 | 0.73 | 1 | 5 | 0.29 | 0 |
| direct FK | 2 | 0.11 | 0 | 5 | 0.26 | 1 |
| penalty | 1 | 0.76 | 1 | 1 | 0.76 | 1 |
Totals per match: xG 1.33 (npxG 1.24) for, xGA 2.39 (np 2.29) against · dead-ball share of xG 20% for, 13% against · penalties won 1, conceded 1 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 7 shots, xG 0.49, 0 goals, headed 3: 6-yard box, central 1 shots, xG 0.24, 0 goals; penalty area, central 2 shots, xG 0.12, 0 goals; penalty area, right 1 shots, xG 0.06, 0 goals · against — 17 shots conceded, xG 1.21, 1 goals, headed 7: 6-yard box, central 3 shots, xG 0.51, 0 goals; penalty area, central 7 shots, xG 0.49, 0 goals; outside box, central 4 shots, xG 0.09, 1 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 38 · corner shots conceded 17 (headed 7), xG 1.21, goals 1 · xG per corner faced 0.032 (rank 16 of 20, 1 = weakest) · weak zone: penalty-spot band (0.49 xG, 40% of theirs v 26% league) · signal: **STRONG — no corner pairing against them** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–8 [CONFIRMED — LiveScore Block L, 23 corners; side L/R as LiveScore records it; foot from SofaScore]: Abdul Fatawu 8 (0L/8R, left foot); Sasa Lukic 8 (8L/0R, right foot); Jaden Philogene-Bidace 3 (2L/1R, 2 short, right foot); Leif Davis 2 (0L/2R, left foot). First contact on corners that ended in a shot (Understat) — for: Dara O&#039;Shea 1 (1 headed), Jacob Greaves 1 (1 headed), Emersonn 1 (1 headed), Marcelino Núñez 1, Sasa Lukic 1 · against (who beat them): Diogo Dalot 2 (1 headed), Murillo 2 (1 headed), Kobbie Mainoo 2, Nilson Angulo 1 (1 headed), Alexis Mac Allister 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 39.1 (rank 14 of 20, 1 = highest line) · block length 20.1 (rank 8, 1 = most compact) · width 65.8. Per match: GW3 H v Liverpool FC 4-2-3-1: back line 40, front 51, length 11, width 68 (45% poss); GW4 A v Crystal Palace 4-2-3-1: back line 45, front 69, length 24, width 70 (54% poss); GW5 A v Everton 4-2-3-1: back line 36, front 63, length 26, width 67 (48% poss); GW6 H v Fulham 4-2-3-1: back line 45, front 62, length 17, width 64 (48% poss); GW7 A v Manchester City 3-4-2-1: back line 36, front 57, length 21, width 58 (30% poss); GW8 H v Nottingham Forest 4-2-3-1: back line 36, front 59, length 23, width 66 (49% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 2 league match(es) v LB-coded sides — xG 1.07/match and 2.0 pts/match v 1.51 and 1.0 against the rest → **struggles — chance creation drops** (threshold: xG v LB at least 90% of the rest). GW4 A v Crystal Palace 3–2, xG 1.68, box shots 8, poss 54%; GW8 H v Nottingham Forest 1–1, xG 0.46, box shots 3, poss 49%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Davis 2, Fatawu 1, Núñez 1** · FPL editorial order: Lukić #1, Fatawu #2, Philogene #3
- Direct free-kick shooters: **Davis 1, Enciso 1** · FPL order: Enciso #1, Davis #2, Clarke #3
- Penalties taken: **Flemming 1** · FPL order: Clarke #1, Flemming #2, Philogene #3
- Set-piece deliverers (assisted 'SetPiece' shots): **O&#039;Shea 2, Clarke 1**
- Corner targets (headed shots from corners): **O&#039;Shea 1, Greaves 1, Emersonn 1** · corner shots 7
- **DISAGREEMENT:** observed corner taker Leif Davis (2) v FPL #1 Lukić — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Abdul Fatawu 2 (0.40/90, percentile 85, 449 min); Jack Clarke 1 (0.39/90, percentile 84, 229 min); Julio Enciso 2 (0.28/90, percentile 75, 650 min) · club total 9 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 289 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 11.49, field tilt 41, possession 37.4%, box entries 7, direct speed 2.51, SCA 20; GW2: PPDA 13.43, field tilt 33.7, possession 40.4%, box entries 8, direct speed 2.43, SCA 16; GW3: PPDA 14.64, field tilt 42, possession 45.9%, box entries 10, direct speed 3.01, SCA 27; GW4: PPDA 8.37, field tilt 57, possession 53.3%, box entries 12, direct speed 2.8, SCA 20; GW5: PPDA 15.52, field tilt 40.1, possession 48.2%, box entries 7, direct speed 2, SCA 23; GW6: PPDA 12.06, field tilt 60.1, possession 47.6%, box entries 15, direct speed 2.08, SCA 22; GW7: PPDA 13.2, field tilt 23.2, possession 30.5%, box entries 8, direct speed 2.84, SCA 16; GW8: PPDA 13.54, field tilt 46.5, possession 49.4%, box entries 6, direct speed 2.43, SCA 12

**Zone 14 (C13, SofaScore heat-map points, 8 league matches):** for 26.2/match (rank 13 of 20) · conceded 34.5/match (rank 5 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 4.9/match · allowed 7.8/match · PPDA 12.6. Per match for/allowed: GW3 5/6; GW4 11/9; GW5 5/7; GW6 5/5; GW7 2/12; GW8 4/6 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 8 league matches, weights last-3 ×3 / older ×1
- GK: Christian Walton (10, 3/3)
- DEF: Issa Diop (14, 3/3), Dara O'Shea (14, 3/3), Leif Davis (14, 3/3), Abdoul Ouattara (10, 3/3)
- MID: Julio Enciso (14, 3/3), Florentino Luís (9, 3/3), Exequiel Palacios (9, 2/3), Daizen Maeda (9, 2/3), Abdul Fatawu Issahaku (8, 1/3)
- FWD: Emersonn (14, 3/3)
- Contested slots: M Abdul Fatawu Issahaku 8 v Saša Lukić 8 · Excluded (FPL flag): none
- Absent last match (E12, SofaScore list): Lukić (Groin Injury)
- Substitutions this season (C3): GW6 63' Jaden Philogene-Bidace→Jack Clarke CHASING; GW6 63' Florentino Luís→Exequiel Palacios CHASING; GW7 90' Jacob Greaves→Jack Clarke LATE; GW7 78' Julio Enciso→Chuba Akpom CHASING; GW7 78' Emersonn→Zian Flemming CHASING; GW7 71' Daizen Maeda→Abdul Fatawu Issahaku CHASING; GW7 71' Florentino Luís→Azor Matusiwa CHASING; GW8 86' Julio Enciso→Chuba Akpom LATE; GW8 85' Florentino Luís→Azor Matusiwa LATE; GW8 73' Abdul Fatawu Issahaku→Daizen Maeda TACTICAL; GW8 61' Jaden Philogene-Bidace→Jack Clarke TACTICAL; GW8 60' Emersonn→Zian Flemming TACTICAL

### First-choice players and absences (F14) — generated 2026-10-27 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Christian Walton | start weight 10 | OK | a | Kjell Scherpen | — |
| CB | Issa Diop | start weight 14 | OK | a | Jacob Greaves | — |
| CB | Dara O'Shea | start weight 14 | OK | a | Jacob Greaves | — |
| xGI #1 | Julio Enciso | xGI 3.31 | OK | a 100% | Leif Davis | — |
| xGI #2 | Emersonn | xGI 2.66 | OK | a 100% | Leif Davis | — |
| Penalties #1 (FPL) | Clarke | FPL order | OK | a | Flemming | — |
| Direct FK #1 (FPL) | Enciso | FPL order | OK | a 100% | Davis | — |
| Corners (observed) | Abdul Fatawu | 8 corners taken | OK | a 100% | Sasa Lukic | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Sunderland: Christian Walton (did not start) · GW2 A Manchester United: Christian Walton (did not start) · GW3 H Liverpool FC: Christian Walton (did not start) · GW4 A Crystal Palace: Christian Walton (did not start) · GW5 A Everton: all started · GW6 H Fulham: all started · GW7 A Manchester City: all started · GW8 H Nottingham Forest: all started

### Next fixtures (all competitions)
- Sat 31 Oct 15:00 UTC · Premier League R9 · A v Hull City
- Sun 08 Nov 14:00 UTC · Premier League R10 · H v Bournemouth
- Sat 21 Nov 15:00 UTC · Premier League R11 · A v Tottenham Hotspur
- Sat 28 Nov 17:30 UTC · Premier League R12 · H v Aston Villa
- Tue 01 Dec 20:00 UTC · Premier League R13 · A v Coventry City
- Sat 05 Dec 15:00 UTC · Premier League R14 · A v Leeds United

### FPL availability flags (players with league minutes this season)
Lukić — Groin injury - Unknown return date (0%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 H Sunderland 2–1 · xG 1.80–0.66 · poss 38% · 4-2-3-1 · scorers: Emersonn 24', Jack Clarke 90'
- GW2 A Manchester United 2–5 · xG 2.06–4.77 · poss 40% · 4-2-3-1 · scorers: Leif Davis 29', Chuba Akpom 90'
- GW3 H Liverpool FC 0–2 · xG 0.75–0.69 · poss 45% · 4-2-3-1 · scorers: none
- GW4 A Crystal Palace 3–2 · xG 1.68–0.62 · poss 54% · 4-2-3-1 · scorers: Emersonn 23', Leif Davis 45', Zian Flemming 90'
- GW5 A Everton 0–1 · xG 1.44–2.24 · poss 48% · 4-2-3-1 · scorers: none
- GW6 H Fulham 2–1 · xG 1.15–1.81 · poss 48% · 4-2-3-1 · scorers: Abdoul Ouattara 88', Dara O'Shea 90'
- GW7 A Manchester City 2–3 · xG 1.86–3.35 · poss 30% · 3-4-2-1 · scorers: Daizen Maeda 21', Zian Flemming 90'
- GW8 H Nottingham Forest 1–1 · xG 0.46–2.29 · poss 49% · 4-2-3-1 · scorers: Julio Enciso 41'
### Corner takers observed (LiveScore Block L)
- Abdul Fatawu: 8 corners (0 left, 8 right)
- Sasa Lukic: 8 corners (8 left, 0 right)
- Jaden Philogene-Bidace: 3 corners (2 left, 1 right, 2 short)
- Leif Davis: 2 corners (0 left, 2 right)
- Marcelino Nunez: 1 corners (1 left, 0 right)
- Exequiel Palacios: 1 corners (1 left, 0 right, 1 short)
