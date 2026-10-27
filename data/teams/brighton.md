# Brighton & Hove Albion — data doc
*Feeder-written (2026-10-27 07:42 UTC); do not edit. Narrative: `profiles/teams/brighton.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-10-27 07:42 UTC)
**Manager:** Fabian Hurzeler · **Venue:** American Express Stadium · **SofaScore:** https://www.sofascore.com/football/team/brighton-and-hove-albion/30 · **FPL code:** BHA
**Table:** 3rd, 16 pts (5W 1D 2L, GF 23 GA 7) · Home 3rd (3-1-0, 13:1) · Away 5th (2-0-2, 10:6)
**Standing context (F15):** 30 league games left · points v 4th +1, v 5th +3, v 17th (last safe) +9, v 18th +10 · goal difference +16
**Suspension watch (D7, all players of the club):** Boscagli — 🟨 2 from a ban (3/5); Groß — 🟨 2 from a ban (3/5) [FPL]
**Goal timing & game state (F17, 8 league matches):** goals after 75′ — for 5/23 (22%), against 0/7 (0%) · scored first 5, conceded first 3 (38% of matches), goalless 0 · points from losing positions 1 of 9 (3 matches behind at some point) · points from winning positions 15 of 15 (5 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Vuskovic (DEF) 9.7/90, hit 4/8; Gomez (MID) 9.1/90, hit 2/8; Dunk (DEF) 7.0/90, hit 1/7; F.Kadıoğlu (DEF) 4.9/90, hit 1/7
**Manager tenure (F13, SofaScore):** Fabian Hurzeler since 01 Jul 2024 · 101 matches in charge, all competitions (46W 27D 28L) · 8 league matches this season · contract to 30 Jun 2029 · previous club FC St. Pauli · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Crystal Palace — last 4: Oct 2026 Premier League Brighton & Hove Albion 5–0 Crystal Palace (yellows 2–1, xG 2.00–0.77); Feb 2026 Premier League Brighton & Hove Albion 0–1 Crystal Palace (yellows 1–3, xG 0.74–1.16); Nov 2025 Premier League Crystal Palace 0–0 Brighton & Hove Albion (yellows 1–4, xG 0.75–0.38); Apr 2025 Premier League Crystal Palace 2–1 Brighton & Hove Albion (yellows 4–3, reds 2–1, xG 0.60–1.00) · 19 yellows in 4 | v Bournemouth — last 4: Jan 2026 Premier League Brighton & Hove Albion 1–1 Bournemouth (yellows 2–3, xG 1.02–1.29); Sep 2025 Premier League Bournemouth 2–1 Brighton & Hove Albion (yellows 4–4, xG 1.45–0.62); Feb 2025 Premier League Brighton & Hove Albion 2–1 Bournemouth (yellows 2–1, xG 2.42–1.46); Nov 2024 Premier League Bournemouth 1–2 Brighton & Hove Albion (yellows 2–4, reds 0–1, xG 1.63–0.94) · 22 yellows in 4
**Archetype (F5):** used **HP** — derived HP [DERIVED] · signals, last 6 league matches: possession 55.8%, PPDA 7.5 (Understat, 6 matches; lower = harder press), opponent offsides forced 2.7/match (line height), fast breaks 1.9/match (season), both sides' xG 3.20/match (openness). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap).
**Squad changes (F20, since 01 Jun 2026):** in 17 (permanent 11, loan 1, free 0, loan returns 5) · out 19 · flags: Diego Coppola: FPL still lists him at BHA (status a) — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 8 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 16.22 | 2 | Big chances against | 17 | 7 |
| xGOT | 17.07 | 2 | Box shots against | 67 | 8 |
| xA | 7.99 | 8 | Corners against | 39 | 13 |
| Shots | 142 | 2 | Crosses faced | 98 | 1 |
| SoT | 43 | 2 | Dribbled past | 54 | 6 |
| Big chances | 31 | 1 | Errors→shot | 8 | 16 |
| Shots in box | 87 | 2 | GK goals prevented | 2.32 | 1 |
| Corners | 42 | 7 | Clearances | 208 | 12 |
| Crosses | 178 | 1 | Tackles | 113 | 16 |
| Fast breaks | 15 | 3 | Interceptions | 63 | 12 |
| FK shots | 2 | 11 | Def. contributions | 411 | 16 |
| Possession % | 60.25 | 4 | Aerial % | 48.38 | 14 |
| Pass % | 84.96 | 6 | Duel % | 47.81 | 17 |
| Long balls | 295 | 5 | Fouls | 99 | 14 |
| Dribbles | 47 | 16 | Yellows | 17 | 13 |
| Shots against | 88 | 5 | Km covered | 920 | 8 |
| SoT against | 27 | 4 | Sprints | 827 | 14 |
Per match: xG 2.03 · xGOT 2.13 · shots 17.8 · shots against 11.0 · big chances 3.9 for / 2.1 against · corners 5.2 / 4.9 · crosses 22.2 / 12.2 · possession 60.25%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Leeds United | 1–1 | 2.19/2.27 | 2.49/3.04 | 67 | 20/10 | 5/5 | 11/10 | 7/1 | 4/5 | 7/6 | 35/6 v 13/1 | 2/4 |
| 4 | A | Coventry City | 5–0 | 2.81/2.81 | 1.33/1.07 | 69 | 22/14 | 7/6 | 14/12 | 5/2 | 4/1 | 3/5 | 17/3 v 12/5 | 2/2 |
| 5 | H | Arsenal | 3–0 | 1.31/2.25 | 1.63/1.29 | 40 | 17/11 | 5/2 | 10/10 | 3/5 | 3/2 | 5/6 | 15/6 v 16/6 | 2/0 |
| 6 | A | Sunderland | 2–0 | 1.41/1.64 | 0.72/0.87 | 38 | 13/12 | 4/3 | 6/4 | 2/7 | 5/1 | 5/7 | 13/3 v 27/5 | 5/0 |
| 7 | H | Crystal Palace | 5–0 | 2/2.59 | 0.77/0.63 | 57 | 17/5 | 9/1 | 8/4 | 4/1 | 3/1 | 8/5 | 21/5 v 12/1 | 2/2 |
| 8 | A | Liverpool FC | 0–2 | 1.32/1.31 | 1.20/1.28 | 64 | 17/13 | 1/4 | 10/10 | 7/3 | 1/1 | 2/4 | 23/5 v 5/2 | 3/3 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | H | Leeds United | 1–1 | 4-2-3-1 | 13/16 | 3/3 | 0/0 | 522/252 | 55/38 | Ferguson (Ankle Injury), Azeez (Muscle Injury), Hinshelwood (Knock Injury), Mitoma (Hamstring Injury), Wieffer (Knee Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Rutter (Physical Discomfort; doubtful) | Gruev (Meniscus Injury), Rodon (Hamstring Injury), Joseph (Knee Injury) | Stuart Attwell |
| 4 | A | Coventry City | 5–0 | 4-2-3-1 | 15/9 | 0/0 | 0/1 | 584/249 | 46/34 | Ferguson (Ankle Injury), Hinshelwood (Knock Injury), Mitoma (Hamstring Injury), Wieffer (Knee Injury), Svoboda (Knock Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Yohanna (Knock Injury) | Wright (Muscle Injury), Eccles (Knock Injury), Kesler-Hayden (Hamstring Injury), Woolfenden (Knee Injury) | Tony Harrington |
| 5 | H | Arsenal | 3–0 | 4-2-3-1 | 13/11 | 4/1 | 0/0 | 343/511 | 62/51 | Ferguson (Ankle Injury), Azeez (Muscle Injury), Hinshelwood (Knock Injury), Mitoma (Hamstring Injury), Wieffer (Knee Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Yohanna (Knock Injury) | Saliba (Back Injury), White (Groin Injury; doubtful) | Darren England |
| 6 | A | Sunderland | 2–0 | 4-2-3-1 | 12/8 | 1/0 | 1/0 | 309/501 | 56/70 | Ferguson (Ankle Injury), Azeez (Muscle Injury), Wieffer (Knee Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Yohanna (Knock Injury) | Brobbey (Hamstring Injury), Ballard (Hamstring Injury), Diarra (Hamstring Injury), Mundle (Knee Injury) | Thomas Bramall |
| 7 | H | Crystal Palace | 5–0 | 4-2-3-1 | 13/11 | 2/1 | 0/0 | 517/384 | 60/29 | Struijk (ban (red)), Ferguson (Ankle Injury), Azeez (Muscle Injury), Mitoma (Hamstring Injury), Wieffer (Knee Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Yohanna (Knock Injury) | Disasi (ban (red)), Riad (Knee Injury), Chilwell (Physical Discomfort; doubtful) | Robert Jones |
| 8 | A | Liverpool FC | 0–2 | 4-2-3-1 | 9/13 | 2/0 | 0/0 | 579/326 | 77/57 | Ferguson (Ankle Injury), Azeez (Muscle Injury), Mitoma (Hamstring Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Yohanna (Knock Injury), Struijk (Lack of Fitness; doubtful) | Bradley (Knee Injury), Szoboszlai (Hamstring Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Frimpong (Hamstring Injury), Muñoz (injury; doubtful) | Samuel Barrott |
Per match: fouls 12.4 / 10.6 · yellows 2.12 / 1.12 · reds 1 / 2 (season) · offsides forced 2.2, committed 2.1 · crosses attempted 22.2 / faced 12.2. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (4): xG 2.32 for / 1.29 against per match · Away (4): xG 1.74 / 1.54. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW8 A v Liverpool FC 0–2 (Sun 25 Oct 14:00 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Bart Verbruggen | G | 90 | 6.9 | 0.00 | 0.00 | 0 | 0 | 2 | 0 | 54 |
| Ferdi Kadıoğlu | D | 6 | — | 0.00 | 0.00 | 0 | 0 | 0 | 0 | 4 |
| Luka Vušković | D | 90 | 6.3 | 0.14 | 0.01 | 0 | 2 | 6 | 1 | 83 |
| Lewis Dunk | D | 90 | 7.1 | 0.00 | 0.01 | 0 | 0 | 7 | 0 | 84 |
| Olivier Boscagli | D | 45 | 5.7 | 0.07 | 0.04 | 0 | 1 | 4 | 3 | 36 |
| Pascal Groß | M | 90 | 5.9 | 0.00 | 0.35 | 4 | 0 | 1 | 5 | 104 |
| Chema Andrés | M | 54 | 6.8 | 0.02 | 0.01 | 0 | 1 | 6 | 0 | 53 |
| Diego Gómez | M | 90 | 6.7 | 0.13 | 0.22 | 3 | 2 | 3 | 3 | 70 |
| Yasin Ayari | M | 75 | 6.6 | 0.32 | 0.03 | 0 | 3 | 2 | 1 | 47 |
| Maxim De Cuyper | M | 90 | 6.6 | 0.05 | 0.28 | 3 | 2 | 5 | 5 | 67 |
| Charalampos Kostoulas | F | 90 | 6.7 | 0.52 | 0.03 | 1 | 4 | 2 | 0 | 53 |
Subs used: Costinha (84'), Jack Hinshelwood (45'), Malick Yalcouyé (36'), Georginio Rutter (15')
Goals: 17' Pascal Groß [opp, ownGoal]; 21' Alexander Isak (assist Bradley Barcola) [opp]
Substitutions (own): 6' Costinha for Ferdi Kadıoğlu [injury]; 46' Jack Hinshelwood for Olivier Boscagli; 54' Malick Yalcouyé for Chema Andrés [injury]; 75' Georginio Rutter for Yasin Ayari
Cards: 45' Olivier Boscagli (yellow, own); 73' Costinha (yellow, own)
**Baseline XI change vs GW7 (4-2-3-1 → 4-2-3-1):** in — none; out — none.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 3 | H Leeds United | 15' | AGAINST | Jayden Bogle | Ao Tanaka | corner | 0.97 |
| 3 | H Leeds United | 71' | FOR | Luka Vušković | Maxim De Cuyper | corner | 0.37 |
| 4 | A Coventry City | 35' | FOR | Charalampos Kostoulas | Pascal Groß | open play | 0.35 |
| 4 | A Coventry City | 51' | FOR | Malick Yalcouyé | Maxim De Cuyper | open play | 0.27 |
| 4 | A Coventry City | 70' | FOR | Pascal Groß | — | penalty | 0.76 |
| 4 | A Coventry City | 83' | FOR | Lewis Dunk | Chema Andrés | open play | 0.02 |
| 4 | A Coventry City | 90' | FOR | Yasin Ayari | Pascal Groß | open play | 0.07 |
| 5 | H Arsenal | 31' | FOR | Pascal Groß | Charalampos Kostoulas | open play | 0.03 |
| 5 | H Arsenal | 45' | FOR | Charalampos Kostoulas | Diego Gómez | open play | 0.05 |
| 5 | H Arsenal | 57' | FOR | Chema Andrés | Pascal Groß | corner | 0.53 |
| 6 | A Sunderland | 53' | FOR | Maxim De Cuyper | Pascal Groß | open play | 0.28 |
| 6 | A Sunderland | 90' | FOR | Jaouen Hadjam | Georginio Rutter | open play | 0.35 |
| 7 | H Crystal Palace | 4' | FOR | Jaydee Canvot | — | own goal | — |
| 7 | H Crystal Palace | 7' | FOR | Diego Gómez | Olivier Boscagli | open play | 0.02 |
| 7 | H Crystal Palace | 10' | FOR | Yasin Ayari | Charalampos Kostoulas | open play | 0.12 |
| 7 | H Crystal Palace | 49' | FOR | Charalampos Kostoulas | — | open play | 0.62 |
| 7 | H Crystal Palace | 84' | FOR | Jack Hinshelwood | — | corner | 0.78 |
| 8 | A Liverpool FC | 17' | AGAINST | Pascal Groß | — | own goal | — |
| 8 | A Liverpool FC | 21' | AGAINST | Alexander Isak | Bradley Barcola | open play | 0.60 |
Scored 23: open play 16, own goal 3, corner 3, penalty 1 · Conceded 7: open play 4, corner 2, own goal 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW6 FOR v Sunderland 53' Maxime De Cuyper (assist Pascal Gross, key pass Diego Gomez): G O O O A A A L - Maxim De Cuyper scores with the left foot! · before: 53' Pascal Gross creates a scoring opportunity for his teammate ‹ 52' Diego Gomez relieves the pressure with a clearance ‹ 52' Pascal Struijk from Brighton goes a bit too far there as he pulls down Wilson Isidor
- GW6 FOR v Sunderland 90+3' Jaouen Hadjam (assist Georginio Rutter): G O O O A A A L - Jaouen Hadjam scores with the left foot! · before: 90+3' Georginio Rutter creates a scoring opportunity for his teammate ‹ 90+3' Chema Andres relieves the pressure with a clearance ‹ 90+3' Luka Vuskovic from Brighton intercepts a cross aimed towards the box.
- GW7 AG v Crystal Palace 4' Jaydee Canvot [OG]: OWN GOAL - Jaydee Canvot sends the ball into his own net! · before: 3' The referee signals a free kick as Anan Khalaili from Crystal Palace trips Lewis Dunk ‹ 3' Daichi Kamada relieves the pressure with a clearance ‹ 1' The pitch is wet and slippery and it is not helping the players.
- GW7 FOR v Crystal Palace 7' Diego Gomez (assist Olivier Boscagli): G O O O A A A L - An excellent lob by Diego Gomez from Brighton with the right foot. · before: 7' Chema Andres makes the tackle and wins possession for his team ‹ 7' Luka Vuskovic from Brighton goes a bit too far there as he pulls down Quinten Timber ‹ 6' The referee signals a free kick as Maxim De Cuyper from Brighton trips Daichi Kamada
- GW7 FOR v Crystal Palace 10' Yasin Ayari (assist Charalampos Kostoulas, key pass Diego Gomez): GOAL! - Yasin Ayari score from a shot with the right foot, that takes a deflection. · before: 9' Tyrick Mitchell makes the tackle and wins possession for his team ‹ 7' Olivier Boscagli provided the assist for the goal. ‹ 7' G O O O A A A L - An excellent lob by Diego Gomez from Brighton with the right foot.
- GW7 FOR v Crystal Palace 49' Charalampos Kostoulas: G O O O A A A L - Charalampos Kostoulas reacts first on the loose ball and puts it away with the left! · before: 49' Honest Ahanor successfully blocks the shot ‹ 49' A shot by Yasin Ayari is blocked. ‹ 49' Chris Richards could cost his team a goal after a defensive blunder.
- GW7 FOR v Crystal Palace 84' Jack Hinshelwood: GOAL! It's an easy finish as Jack Hinshelwood from Brighton taps the ball into an open goal with the right foot! · before: 84' Luka Vuskovic sends a header towards goal, but Walter Benitez is there to comfortably save  ‹ 84' Maxim De Cuyper from Brighton swings in the corner from the right. ‹ 83' Jaydee Canvot relieves the pressure with a clearance
- GW8 FOR v Liverpool FC 17' Pascal Groß [OG]: OWN GOAL - Pascal Gross sends the ball into his own net! · before: 17' Florian Wirtz from Liverpool sends an effort wide of target ‹ 17' Pascal Gross from Brighton intercepts a cross aimed towards the box. ‹ 17' Ronald Araujo makes the tackle and wins possession for his team
- GW8 AG v Liverpool FC 21' Alexander Isak (assist Bradley Barcola): G O O O A A A L - Alexander Isak scores with the left foot! · before: 21' Bradley Barcola creates a scoring opportunity for his teammate ‹ 21' Liverpool with a potentially dangerous attack. ‹ 21' Bradley Barcola makes the tackle and wins possession for his team

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW3 H v Leeds United 15' Jayden Bogle: no structured culprit — reports only
  · GW3 other flags: Lewis Dunk clearanceOffLine 1; Charalampos Kostoulas errorLeadToAShot 1
- GW8 A v Liverpool FC 17' Pascal Groß [OG]: Pascal Groß own goal [CONFIRMED — SofaScore]
- GW8 A v Liverpool FC 21' Alexander Isak: no structured culprit — reports only
  · GW8 error leading to a goal (SofaScore, match level — 2 conceded, the goal is not identified): Olivier Boscagli, Pascal Groß [CONFIRMED — SofaScore error flag]
  · GW8 other flags: Olivier Boscagli errorLeadToAShot 1; Costinha errorLeadToAShot 1; Maxim De Cuyper errorLeadToAShot 1

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 109 | 13.36 | 16 | 65 | 8.78 | 4 |
| corner | 17 | 3.36 | 3 | 19 | 3.37 | 2 |
| set piece | 14 | 1.17 | 0 | 5 | 0.12 | 0 |
| direct FK | 2 | 0.11 | 0 | 2 | 0.10 | 0 |
| penalty | 1 | 0.76 | 1 | 0 | 0.00 | 0 |
Totals per match: xG 2.34 (npxG 2.25) for, xGA 1.55 (np 1.55) against · dead-ball share of xG 29% for, 29% against · penalties won 1, conceded 0 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 17 shots, xG 3.36, 3 goals, headed 6: 6-yard box, central 7 shots, xG 2.84, 3 goals; penalty area, central 4 shots, xG 0.30, 0 goals; penalty area, right 3 shots, xG 0.16, 0 goals · against — 19 shots conceded, xG 3.37, 2 goals, headed 13: 6-yard box, central 10 shots, xG 2.88, 2 goals; penalty area, central 4 shots, xG 0.35, 0 goals; penalty area, right 2 shots, xG 0.08, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 39 · corner shots conceded 19 (headed 13), xG 3.37, goals 2 · xG per corner faced 0.086 (rank 1 of 20, 1 = weakest) · weak zone: six-yard box (2.94 xG, 87% of theirs v 65% league) · signal: **WEAK — positive pairing for opposing aerial targets** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–8 [CONFIRMED — LiveScore Block L, 42 corners; side L/R as LiveScore records it; foot from SofaScore]: Pascal Gross 24 (12L/12R, 1 short, right foot); Maxim De Cuyper 16 (0L/16R, 1 short, left foot); Malick Junior Yalcouye 2 (0L/2R, 2 short, right foot). First contact on corners that ended in a shot (Understat) — for: Luka Vuskovic 6 (4 headed) — 1 goal, Yasin Ayari 2, Georginio Rutter 2, Chema Andres 1 (1 headed) — 1 goal, Pascal Struijk 1 (1 headed) · against (who beat them): João Pedro 2 (1 headed), Ao Tanaka 2, Ross Barkley 1 (1 headed), Dominic Calvert-Lewin 1 (1 headed), James Justin 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 46.7 (rank 1 of 20, 1 = highest line) · block length 17.1 (rank 1, 1 = most compact) · width 60.8. Per match: GW3 H v Leeds United 4-2-3-1: back line 47, front 62, length 16, width 65 (67% poss); GW4 A v Coventry City 4-2-3-1: back line 48, front 62, length 15, width 61 (69% poss); GW5 H v Arsenal 4-2-3-1: back line 44, front 74, length 29, width 64 (40% poss); GW6 A v Sunderland 4-2-3-1: back line 40, front 55, length 15, width 61 (38% poss); GW7 H v Crystal Palace 4-2-3-1: back line 47, front 66, length 19, width 54 (57% poss); GW8 A v Liverpool FC 4-2-3-1: back line 46, front 60, length 14, width 65 (64% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 2 league match(es) v LB-coded sides — xG 2.41/match and 3.0 pts/match v 1.90 and 1.7 against the rest → **works — chance creation holds up** (threshold: xG v LB at least 90% of the rest). GW4 A v Coventry City 5–0, xG 2.81, box shots 14, poss 69%; GW7 H v Crystal Palace 5–0, xG 2, box shots 8, poss 57%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Cuyper 6, Groß 2, Wieffer 1** · FPL editorial order: Groß #1, De Cuyper #2, F.Kadıoğlu #3
- Direct free-kick shooters: **Vuskovic 1, Cuyper 1** · FPL order: Groß #1, Ayari #2, Dunk #3
- Penalties taken: **Groß 1** · FPL order: Groß #1, David #2, O'Riley #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Boscagli 5, Groß 3, Cuyper 1**
- Corner targets (headed shots from corners): **Vuskovic 4, Andres 1, Struijk 1** · corner shots 17
- **DISAGREEMENT:** observed corner taker Maxim De Cuyper (6) v FPL #1 Groß — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Charalampos Kostoulas 2 (0.31/90, percentile 79, 577 min); Malick Yalcouyé 1 (0.30/90, percentile 77, 305 min); Olivier Boscagli 2 (0.29/90, percentile 75, 631 min) · club total 14 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 289 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 3.87, field tilt 77, possession 71.7%, box entries 15, direct speed 1.45, SCA 37; GW2: PPDA 5.92, field tilt 69.4, possession 74.1%, box entries 15, direct speed 2.15, SCA 29; GW3: PPDA 5.53, field tilt 66.1, possession 66.3%, box entries 11, direct speed 2.01, SCA 40; GW4: PPDA 7, field tilt 66.8, possession 69%, box entries 10, direct speed 1.92, SCA 38; GW5: PPDA 9.73, field tilt 45.1, possession 40%, box entries 9, direct speed 3.15, SCA 34; GW6: PPDA 10.05, field tilt 29.3, possession 37.7%, box entries 8, direct speed 3.74, SCA 21; GW7: PPDA 8.47, field tilt 76, possession 56.6%, box entries 9, direct speed 2.03, SCA 32; GW8: PPDA 7, field tilt 60.5, possession 63.5%, box entries 15, direct speed 2.36, SCA 33

**Zone 14 (C13, SofaScore heat-map points, 8 league matches):** for 36.0/match (rank 4 of 20) · conceded 19.2/match (rank 20 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 7.1/match · allowed 7.0/match · PPDA 6.7. Per match for/allowed: GW3 6/8; GW4 2/8; GW5 6/10; GW6 2/4; GW7 7/4; GW8 16/9 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 8 league matches, weights last-3 ×3 / older ×1
- GK: Bart Verbruggen (14, 3/3)
- DEF: Luka Vušković (14, 3/3), Olivier Boscagli (14, 3/3), Lewis Dunk (10, 2/3)
- MID: Pascal Groß (14, 3/3), Diego Gómez (14, 3/3), Maxim De Cuyper (14, 3/3), Yasin Ayari (13, 3/3), Malick Yalcouyé (3, 0/3)
- FWD: Charalampos Kostoulas (13, 3/3)
- Contested slots: none · Excluded (FPL flag): Ferdi Kadıoğlu — Hip injury - 75% chance of playing; Pascal Struijk — Hamstring injury - 75% chance of playing; Mats Wieffer — Knee injury - 25% chance of playing; Chema Andrés — Thigh injury - 75% chance of playing
- Absent last match (E12, SofaScore list): Ferguson (Ankle Injury), Azeez (Muscle Injury), Mitoma (Hamstring Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Yohanna (Knock Injury), Struijk (Lack of Fitness; doubtful)
- Substitutions this season (C3): GW6 68' Maxim De Cuyper→Malick Yalcouyé TACTICAL; GW6 68' Olivier Boscagli→Costinha CARD-RISK; GW6 60' Charalampos Kostoulas→Lewis Dunk TACTICAL; GW7 90' Lewis Dunk→Michael Svoboda LATE; GW7 81' Yasin Ayari→Malick Yalcouyé GAME-STATE; GW7 81' Olivier Boscagli→Jaouen Hadjam GAME-STATE; GW7 71' Charalampos Kostoulas→Georginio Rutter GAME-STATE; GW7 71' Pascal Groß→Jack Hinshelwood CARD-RISK; GW8 75' Yasin Ayari→Georginio Rutter CHASING; GW8 54' Chema Andrés→Malick Yalcouyé INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']; GW8 46' Olivier Boscagli→Jack Hinshelwood HALF-TIME; GW8 6' Ferdi Kadıoğlu→Costinha INJURY [CONFIRMED: SofaScore flag + LiveScore 'injury']

### First-choice players and absences (F14) — generated 2026-10-27 07:42 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Bart Verbruggen | start weight 14 | OK | a | — | — |
| CB | Luka Vušković | start weight 14 | OK | a | Pascal Struijk | — |
| CB | Lewis Dunk | start weight 10 | OK | a 100% | Pascal Struijk | — |
| xGI #1 | Pascal Groß | xGI 3.67 | OK | a | Charalampos Kostoulas | — |
| xGI #2 | Maxim De Cuyper | xGI 2.93 | OK | a | Charalampos Kostoulas | — |
| Penalties #1 (FPL) | Groß | FPL order | OK | a | David | — |
| Direct FK #1 (FPL) | Groß | FPL order | OK | a | Ayari | — |
| Corners (observed) | Pascal Gross | 24 corners taken | OK | a | Maxim De Cuyper | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 H Aston Villa: all started · GW2 A Chelsea: all started · GW3 H Leeds United: all started · GW4 A Coventry City: all started · GW5 H Arsenal: Lewis Dunk (did not start) · GW6 A Sunderland: Lewis Dunk (did not start) · GW7 H Crystal Palace: all started · GW8 A Liverpool FC: all started

### Next fixtures (all competitions)
- Wed 28 Oct 19:30 UTC · EFL Cup R4 · A v Manchester City
- Sat 31 Oct 15:00 UTC · Premier League R9 · A v Manchester City
- Thu 05 Nov 20:00 UTC · UEFA Conference League R3 · A v Getafe
- Sun 08 Nov 14:00 UTC · Premier League R10 · H v Brentford
- Sun 22 Nov 14:00 UTC · Premier League R11 · A v Hull City
- Thu 26 Nov 17:45 UTC · UEFA Conference League R4 · H v Universitatea Craiova

### FPL availability flags (players with league minutes this season)
F.Kadıoğlu — Hip injury - 75% chance of playing (75%); Wieffer — Knee injury - 25% chance of playing (25%); Yohanna — Unspecified injury - Expected back 31 Oct (0%); Struijk — Hamstring injury - 75% chance of playing (75%); Andrés — Thigh injury - 75% chance of playing (75%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 H Aston Villa 4–0 · xG 3.77–0.29 · poss 73% · 4-2-3-1 · scorers: Victor Lindelöf 8', Maxim De Cuyper 18', Jack Hinshelwood 30', Jack Hinshelwood 31'
- GW2 A Chelsea 3–4 · xG 1.41–2.93 · poss 74% · 4-2-3-1 · scorers: Malick Yalcouyé 35', João Pedro 63', Pascal Groß 90'
- GW3 H Leeds United 1–1 · xG 2.19–2.49 · poss 67% · 4-2-3-1 · scorers: Luka Vušković 71'
- GW4 A Coventry City 5–0 · xG 2.81–1.33 · poss 69% · 4-2-3-1 · scorers: Charalampos Kostoulas 35', Malick Yalcouyé 51', Pascal Groß 70', Lewis Dunk 83', Yasin Ayari 90'
- GW5 H Arsenal 3–0 · xG 1.31–1.63 · poss 40% · 4-2-3-1 · scorers: Pascal Groß 31', Charalampos Kostoulas 45', Chema Andrés 57'
- GW6 A Sunderland 2–0 · xG 1.41–0.72 · poss 38% · 4-2-3-1 · scorers: Maxim De Cuyper 53', Jaouen Hadjam 90'
- GW7 H Crystal Palace 5–0 · xG 2–0.77 · poss 57% · 4-2-3-1 · scorers: Jaydee Canvot 4', Diego Gómez 7', Yasin Ayari 10', Charalampos Kostoulas 49', Jack Hinshelwood 84'
- GW8 A Liverpool FC 0–2 · xG 1.32–1.20 · poss 64% · 4-2-3-1 · scorers: none
### Corner takers observed (LiveScore Block L)
- Pascal Gross: 24 corners (12 left, 12 right, 1 short)
- Maxim De Cuyper: 16 corners (0 left, 16 right, 1 short)
- Malick Junior Yalcouye: 2 corners (0 left, 2 right, 2 short)
