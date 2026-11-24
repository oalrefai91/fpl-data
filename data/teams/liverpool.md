# Liverpool FC — data doc
*Feeder-written (2026-11-24 07:45 UTC); do not edit. Narrative: `profiles/teams/liverpool.md`. Detailed rows keep the last 6 matches (FX-17).*

<!-- AUTO:START — machine-written from SofaScore + FPL; do not edit inside the markers -->
## Data block (SofaScore, fetched 2026-11-24 07:45 UTC)
**Manager:** Andoni Iraola · **Venue:** Anfield · **SofaScore:** https://www.sofascore.com/football/team/liverpool/44 · **FPL code:** LIV
**Table:** 4th, 21 pts (6W 3D 2L, GF 18 GA 10) · Home 12th (2-2-2, 8:6) · Away 1st (4-1-0, 10:4)
**Standing context (F15):** 27 league games left · points v 4th +0, v 5th +3, v 17th (last safe) +12, v 18th +12 · goal difference +8
**Suspension watch (D7, all players of the club):** Virgil — 🟨 2 from a ban (3/5); Kerkez — 🟨 2 from a ban (3/5); Mac Allister — 🟨 **ONE FROM A BAN** (4/5 before GW19); Araujo — 🟨 2 from a ban (3/5); Barcola — 🟨 **ONE FROM A BAN** (4/5 before GW19) [FPL]
**Goal timing & game state (F17, 11 league matches):** goals after 75′ — for 4/18 (22%), against 2/10 (20%) · scored first 5, conceded first 5 (45% of matches), goalless 1 · points from losing positions 5 of 15 (5 matches behind at some point) · points from winning positions 18 of 18 (6 matches ahead)
**DefCon candidates (F11, FPL defensive_contribution; hit = DEF ≥10, MID/FWD ≥12 in a GW):** Virgil (DEF) 9.4/90, hit 6/11; Jacquet (DEF) 9.2/90, hit 5/11; Araujo (DEF) 8.7/90, hit 4/11; Mac Allister (MID) 11.2/90, hit 2/11; Szoboszlai (MID) 9.7/90, hit 1/9; Gakpo (MID) 7.0/90, hit 1/8
**Manager tenure (F13, SofaScore):** Andoni Iraola since 01 Jul 2026 · 15 matches in charge, all competitions (9W 3D 3L) · 11 league matches this season · contract to 30 Jun 2028 · previous club Bournemouth · interim flag not published by SofaScore
**Rivalry record (F18, SofaScore h2h, competitive meetings):** v Everton — last 4: Apr 2026 Premier League Everton 1–2 Liverpool FC (yellows 2–0, xG 1.00–1.45); Sep 2025 Premier League Liverpool FC 2–1 Everton (yellows 2–3, xG 0.90–0.70); Apr 2025 Premier League Liverpool FC 1–0 Everton (yellows 2–2, xG 1.47–0.67); Feb 2025 Premier League Everton 2–2 Liverpool FC (yellows 4–4, reds 1–1, xG 0.95–0.62) · 19 yellows in 4 | v Manchester United — last 4: Nov 2026 Premier League Liverpool FC 4–0 Manchester United (yellows 1–0, reds 0–1, xG 4.35–0.65); May 2026 Premier League Manchester United 3–2 Liverpool FC (yellows 2–2, xG 2.34–0.88); Oct 2025 Premier League Liverpool FC 1–2 Manchester United (yellows 0–2, xG 2.74–1.34); Jan 2025 Premier League Liverpool FC 2–2 Manchester United (yellows 2–4, xG 2.82–1.05) · 13 yellows in 4
**Archetype (F5):** used **TR** — derived TR [DERIVED] · signals, last 6 league matches: possession 49.3%, PPDA 11.2 (Understat, 3 matches; lower = harder press), opponent offsides forced 2.3/match (line height), fast breaks 2.1/match (season), both sides' xG 3.26/match (openness) · note: computed from 3 of 6 GWs (no PPDA/possession for GW9, GW10, GW11). Rule: HP = PPDA among the 5 lowest in the league · PM = possession ≥ 52% · LB = possession ≤ 47.5% and PPDA ≥ league median · TR = the rest (last 6 league matches; checked in that order; needs ≥ 3 GWs with both PPDA and possession, else the hand-set code fills the gap; margin rule Q-86: a code moves from last week's only when every cut is cleared by 0.6 PPDA / 1.5 possession points, otherwise last week's code is held).
**Squad changes (F20, since 01 Jun 2026):** in 13 (permanent 9, loan 1, free 0, loan returns 3) · out 12 — full list in `claude/squad-changes.md`.

### Season statistics — value and league rank of 20 (after 11 matches)
| Metric | Value | Rank | Metric | Value | Rank |
|---|---|---|---|---|---|
| xG | 20.16 | 4 | Big chances against | 23 | 7 |
| xGOT | 17.85 | 4 | Box shots against | 84 | 6 |
| xA | 12.84 | 3 | Corners against | 46 | 4 |
| Shots | 188 | 2 | Crosses faced | 169 | 5 |
| SoT | 58 | 3 | Dribbled past | 62 | 2 |
| Big chances | 26 | 12 | Errors→shot | 7 | 7 |
| Shots in box | 122 | 2 | GK goals prevented | 2.10 | 4 |
| Corners | 67 | 4 | Clearances | 281 | 12 |
| Crosses | 216 | 5 | Tackles | 168 | 14 |
| Fast breaks | 23 | 1 | Interceptions | 110 | 4 |
| FK shots | 10 | 1 | Def. contributions | 601 | 11 |
| Possession % | 53.73 | 6 | Aerial % | 57.88 | 1 |
| Pass % | 83.34 | 9 | Duel % | 50.70 | 8 |
| Long balls | 424 | 5 | Fouls | 161 | 20 |
| Dribbles | 95 | 3 | Yellows | 27 | 15 |
| Shots against | 139 | 7 | Km covered | 1222 | 20 |
| SoT against | 38 | 3 | Sprints | 1441 | 1 |
Per match: xG 1.83 · xGOT 1.62 · shots 17.1 · shots against 12.6 · big chances 2.4 for / 2.1 against · corners 6.1 / 4.2 · crosses 19.6 / 15.4 · possession 53.7%. Note: SofaScore does not publish team xGA; use the opponents' xG in the match table below.

### Matches this season (league) — attack and defence, for/against
| GW | H/A | Opponent | Score | xG for (Opta/Understat) | xG ag (Opta/Understat) | Poss % | Shots | SoT | In box | Blocked | Big ch. | Corners | Crosses (att/comp) | Offsides forced/committed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | H | Manchester City | 0–3 | 0.94/0.76 | 1.28/1.59 | 35 | 13/15 | 6/4 | 6/8 | 4/4 | 0/3 | 5/6 | 13/2 v 12/2 | 2/2 |
| 7 | A | Brentford | 2–1 | 1.64/1.55 | 0.88/0.86 | 60 | 21/10 | 5/2 | 10/10 | 4/4 | 1/2 | 9/3 | 15/2 v 16/2 | 1/2 |
| 8 | H | Brighton & Hove Albion | 2–0 | 1.20/1.28 | 1.32/1.31 | 36 | 13/17 | 4/1 | 10/10 | 3/7 | 1/1 | 4/2 | 5/2 v 23/5 | 3/3 |
| 9 | H | Arsenal | 0–1 | 1.05/— | 0.98/— | 56 | 17/10 | 0/3 | 14/6 | 9/3 | 1/2 | 7/4 | 33/5 v 10/4 | 3/2 |
| 10 | A | Crystal Palace | 3–1 | 2.65/— | 2.60/— | 46 | 20/19 | 8/7 | 18/12 | 4/5 | 5/5 | 7/4 | 21/8 v 22/6 | 3/0 |
| 11 | H | Manchester United | 4–0 | 4.35/— | 0.65/— | 63 | 28/10 | 11/3 | 19/4 | 10/2 | 9/0 | 15/5 | 23/3 v 12/3 | 2/2 |
Crosses = sum of every player's attempted/completed crosses in the match (SofaScore per-player stats); offsides forced = the opponent's offsides. Two xG providers: Opta (SofaScore/FPL) and Understat — different models, both kept.

### Matches this season (league) — discipline, shape and absences
| GW | H/A | Opponent | Score | Formation | Fouls for/ag | Yellows for/ag | Reds for/ag | Passes for/ag | Final-third entries for/ag | Absent (own) | Absent (opponent) | Referee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | H | Manchester City | 0–3 | 4-2-3-1 | 19/14 | 4/2 | 1/0 | 301/562 | 41/48 | Isak (Thigh Injury), Gakpo (Ankle Injury), Bradley (Knee Injury), Szoboszlai (Hamstring Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury) | Foden (ban (red)) | Chris Kavanagh |
| 7 | A | Brentford | 2–1 | 4-2-3-1 | 13/7 | 3/4 | 0/2 | 503/330 | 61/50 | Gravenberch (ban (cards)), Bradley (Knee Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury) | Milambo (Cruciate Ligament Injury), Dasilva (Hamstring Injury), Furo (Knee Surgery) | John Brooks |
| 8 | H | Brighton & Hove Albion | 2–0 | 4-2-3-1 | 13/9 | 0/2 | 0/0 | 326/579 | 57/77 | Bradley (Knee Injury), Szoboszlai (Hamstring Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Frimpong (Hamstring Injury), Muñoz (injury; doubtful) | Ferguson (Ankle Injury), Azeez (Muscle Injury), Mitoma (Hamstring Injury), Tzimas (Cruciate Ligament Injury), Minteh (Leg Injury), Yohanna (Knock Injury), Struijk (Lack of Fitness; doubtful) | Samuel Barrott |
| 9 | H | Arsenal | 0–1 | 4-2-3-1 | 18/10 | 4/4 | 0/0 | 464/372 | 72/45 | Bradley (Knee Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Frimpong (Hamstring Injury) | Dowman (ban (red)), Saka (Muscle Injury), Saliba (Back Injury) | Andy Madley |
| 10 | A | Crystal Palace | 3–1 | 4-2-3-1 | 18/10 | 4/2 | 0/0 | 358/420 | 60/60 | Bradley (Knee Injury), Leoni (Cruciate Ligament Injury), Ekitiké (Achilles Tendon Injury), Frimpong (Hamstring Injury), Gravenberch (Heel Injury; doubtful) | Mateta (ban (red)), Riad (Knee Injury), Sarr (Groin Injury), Tomiyasu (Calf Injury) | Tony Harrington |
| 11 | H | Manchester United | 4–0 | 4-2-3-1 | 15/7 | 1/0 | 0/1 | 581/341 | 70/31 | Gakpo (injury), Ekitiké (Achilles Tendon Injury), Gravenberch (Heel Injury; doubtful) | Šeško (Leg Injury), Baleba (Hamstring Injury), Ugarte (Cruciate Ligament Injury) | Samuel Barrott |
Per match: fouls 14.6 / 9.8 · yellows 2.55 / 2.18 · reds 1 / 3 (season) · offsides forced 2.4, committed 2.0 · crosses attempted 19.6 / faced 15.4. Absent = SofaScore missing-players list at kick-off (E12; '—' = none listed or not captured for that match).
Home (6): xG 1.76 for / 1.20 against per match · Away (5): xG 1.92 / 1.32. [INSUFFICIENT SAMPLE until 4 home + 4 away — flat ±0.5 venue term applies in the model]

### Last league match — GW11 H v Manchester United 4–0 (Sun 22 Nov 16:30 UTC) — formation 4-2-3-1
| Player | Pos | Min | Rating | xG | xA | KP | Shots | CBIT | Crosses | Touches |
|---|---|---|---|---|---|---|---|---|---|---|
| Alisson | G | 90 | 7.3 | 0.00 | 0.00 | 0 | 0 | 1 | 0 | 22 |
| Ronald Araújo | D | 85 | 7.2 | 0.00 | 0.20 | 0 | 0 | 6 | 2 | 61 |
| Jérémy Jacquet | D | 90 | 7.4 | 0.00 | 0.05 | 0 | 0 | 5 | 0 | 76 |
| Virgil van Dijk | D | 90 | 7.5 | 0.22 | 0.02 | 0 | 2 | 7 | 0 | 69 |
| Miloš Kerkez | D | 90 | 7.3 | 0.00 | 0.06 | 0 | 0 | 4 | 2 | 84 |
| Dominik Szoboszlai | M | 90 | 8.6 | 0.34 | 0.15 | 3 | 7 | 2 | 11 | 109 |
| Alexis Mac Allister | M | 72 | 7.2 | 0.12 | 0.06 | 2 | 2 | 4 | 0 | 69 |
| Bradley Barcola | M | 72 | 7.5 | 0.70 | 0.60 | 2 | 3 | 3 | 1 | 37 |
| Florian Wirtz | M | 90 | 10 | 0.36 | 1.08 | 10 | 2 | 1 | 2 | 76 |
| Rio Ngumoha | M | 78 | 10 | 0.71 | 1.05 | 4 | 4 | 3 | 3 | 80 |
| Alexander Isak | F | 85 | 7.1 | 1.32 | 0.04 | 0 | 6 | 1 | 0 | 39 |
Subs used: Víctor Muñoz (18'), Trey Nyoni (18'), Jeremie Frimpong (12'), Joe Gomez (8'), Lewis Koumas (8')
Goals: 10' Dominik Szoboszlai [own]; 13' Florian Wirtz (assist Rio Ngumoha) [own]; 66' Rio Ngumoha (assist Bradley Barcola) [own]; 82' Víctor Muñoz (assist Florian Wirtz) [own]
Substitutions (own): 72' Víctor Muñoz for Bradley Barcola; 72' Trey Nyoni for Alexis Mac Allister; 78' Jeremie Frimpong for Rio Ngumoha; 85' Lewis Koumas for Alexander Isak; 85' Joe Gomez for Ronald Araújo
Cards: 8' Leny Yoro (red, opp); 62' Bradley Barcola (yellow, own)
**Baseline XI change vs GW10 (4-2-3-1 → 4-2-3-1):** in — Rio Ngumoha; out — Cody Gakpo.

### Goals for and against (E1 — SofaScore incidents; type = Understat situation)
| GW | Opp | Min | For/Ag | Scorer | Assist | Type | xG of shot |
|---|---|---|---|---|---|---|---|
| 6 | H Manchester City | 65' | AGAINST | Erling Haaland | — | open play | 0.09 |
| 6 | H Manchester City | 68' | AGAINST | Jérémy Doku | Elliot Anderson | open play | 0.06 |
| 6 | H Manchester City | 78' | AGAINST | Rayan Cherki | Joško Gvardiol | open play | 0.75 |
| 7 | A Brentford | 44' | AGAINST | Keane Lewis-Potter | Igor Thiago | open play | 0.26 |
| 7 | A Brentford | 62' | FOR | Víctor Muñoz | Florian Wirtz | open play | 0.18 |
| 7 | A Brentford | 70' | FOR | Alexander Isak | Bradley Barcola | open play | 0.13 |
| 8 | H Brighton & Hove Albion | 17' | FOR | Pascal Groß | — | own goal | — |
| 8 | H Brighton & Hove Albion | 21' | FOR | Alexander Isak | Bradley Barcola | open play | 0.60 |
| 9 | H Arsenal | 16' | AGAINST | Kai Havertz | Declan Rice | [no Understat] | — |
| 10 | A Crystal Palace | 40' | FOR | Alexis Mac Allister | Dominik Szoboszlai | [no Understat] | — |
| 10 | A Crystal Palace | 54' | FOR | Florian Wirtz | Bradley Barcola | [no Understat] | — |
| 10 | A Crystal Palace | 89' | FOR | Alexander Isak | Florian Wirtz | [no Understat] | — |
| 10 | A Crystal Palace | 90' | AGAINST | Eddie Nketiah | — | penalty | — |
| 11 | H Manchester United | 10' | FOR | Dominik Szoboszlai | — | [no Understat] | — |
| 11 | H Manchester United | 13' | FOR | Florian Wirtz | Rio Ngumoha | [no Understat] | — |
| 11 | H Manchester United | 66' | FOR | Rio Ngumoha | Bradley Barcola | [no Understat] | — |
| 11 | H Manchester United | 82' | FOR | Víctor Muñoz | Florian Wirtz | [no Understat] | — |
Scored 18: open play 9, [no Understat] 7, penalty 1, own goal 1 · Conceded 10: open play 7, penalty 2, [no Understat] 1. Counter-attack goals are not tagged by any provider — narrative only.

### Goal build-up (LiveScore Block L, last 3 league matches; key pass = the pass before the assist)
- GW9 AG v Arsenal 16' Kai Havertz (assist Declan Rice, key pass Noni Madueke): G O O O A A A L - Kai Havertz scores with the left foot! · before: 16' The cross by Declan Rice from Arsenal successfully finds a teammate in the box. ‹ 16' Goal kick for Liverpool. ‹ 16' Declan Rice from Arsenal tries to score from outside the penalty box, but the shot is nowhe
- GW10 FOR v Crystal Palace 40' Alexis Mac Allister (assist Dominik Szoboszlai): G O O O A A A L - Alexis Mac Allister from Liverpool heads the ball home! · before: 40' The cross by Dominik Szoboszlai from Liverpool successfully finds a teammate in the box. ‹ 39' Obstruction as Jefferson Lerma cuts off the run of Cody Gakpo. A free-kick is awarded. ‹ 39' Alisson Becker makes a crucial save!
- GW10 FOR v Crystal Palace 54' Florian Wirtz (assist Bradley Barcola, key pass Ronald Araujo): G O O O A A A L - Florian Wirtz scores with the right foot! · before: 54' The cross by Bradley Barcola from Liverpool successfully finds a teammate in the box. ‹ 53' Jeremy Jacquet is penalised for pushing Axel Disasi. ‹ 52' The referee signals a free kick as Oscar Mingueza from Crystal Palace trips Alexis Mac Alli
- GW10 FOR v Crystal Palace 89' Alexander Isak (assist Florian Wirtz, key pass Victor Munoz): G O O O A A A L - Alexander Isak scores with the right foot! · before: 89' Florian Wirtz creates a scoring opportunity for his teammate ‹ 89' The cross by Victor Munoz from Liverpool successfully finds a teammate in the box. ‹ 89' Liverpool start a counter attack.
- GW10 AG v Crystal Palace 90+5' Eddie Nketiah [pen]: G O O O A A A L - Edward Nketiah from Crystal Palace puts it away from the penalty spot with the right foot! Alisson Becker was close to denying the o · before: 90+5' The game is restarted. ‹ 90+5' After VAR check, the referee decided to stay with the initial call - penalty for Crystal  ‹ 90+3' VAR - PENALTY! - The referee has stopped the play. VAR check in progress, a potential pen
- GW11 FOR v Manchester United 10' Dominik Szoboszlai: — no commentary line — · before: 8' Alexander Isak (Liverpool) wins a free kick in the attacking half. ‹ 8' Foul by Leny Yoro (Manchester United). ‹ 8' Leny Yoro (Manchester United) is shown the red card.
- GW11 FOR v Manchester United 13' Florian Wirtz (assist Rio Ngumoha): — no commentary line — · before: 12' Attempt missed. Kobbie Mainoo (Manchester United) right footed shot from outside the box mi ‹ 10' Goal! Liverpool 1, Manchester United 0. Dominik Szoboszlai (Liverpool) from a free kick wit ‹ 8' Alexander Isak (Liverpool) wins a free kick in the attacking half.
- GW11 FOR v Manchester United 66' Rio Ngumoha (assist Bradley Barcola): — no commentary line — · before: 65' Substitution, Manchester United. Mason Mount replaces Youri Tielemans. ‹ 65' Substitution, Manchester United. Noussair Mazraoui replaces Patrick Dorgu. ‹ 64' Attempt blocked. Rio Ngumoha (Liverpool) right footed shot from the left side of the box is
- GW11 FOR v Manchester United 82' Victor Munoz (assist Florian Wirtz): — no commentary line — · before: 81' Corner, Liverpool. Conceded by Diogo Dalot. ‹ 79' Attempt missed. Joshua Zirkzee (Manchester United) header from the centre of the box misses ‹ 79' Attempt saved. Bruno Fernandes (Manchester United) right footed shot from outside the box i

### Goals conceded — culpability (FX-59: SofaScore error flags [CONFIRMED] + LiveScore phrases [DERIVED]; reports remain the third source; last 6 league matches)
- GW6 H v Manchester City 65' Erling Haaland: no structured culprit — reports only
- GW6 H v Manchester City 68' Jérémy Doku: no structured culprit — reports only
- GW6 H v Manchester City 78' Rayan Cherki: no structured culprit — reports only
- GW7 A v Brentford 44' Keane Lewis-Potter: no structured culprit — reports only
  · GW7 other flags: Jérémy Jacquet lastManTackle 1
- GW9 H v Arsenal 16' Kai Havertz: Alisson error leading to the goal [CONFIRMED — SofaScore error flag]; Jérémy Jacquet error leading to the goal [CONFIRMED — SofaScore error flag]
  · GW9 other flags: Bradley Barcola errorLeadToAShot 1
- GW10 A v Crystal Palace 90' Eddie Nketiah [pen]: Miloš Kerkez conceded the penalty [CONFIRMED — SofaScore]
  · GW10 other flags: Virgil van Dijk lastManTackle 1; Jérémy Jacquet errorLeadToAShot 1

### xG by situation (E5, Understat, 8 matches: GW1, 2, 3, 4, 5, 6, 7, 8)
| Situation | Shots for | xG for | Goals for | Shots against | xG against | Goals against |
|---|---|---|---|---|---|---|
| open play | 88 | 7.74 | 9 | 84 | 9.24 | 7 |
| corner | 21 | 2.72 | 0 | 9 | 0.42 | 0 |
| set piece | 5 | 0.27 | 0 | 3 | 0.14 | 0 |
| direct FK | 8 | 0.42 | 0 | 4 | 0.20 | 0 |
| penalty | 1 | 0.76 | 1 | 1 | 0.76 | 1 |
Totals per match: xG 1.49 (npxG 1.39) for, xGA 1.34 (np 1.25) against · dead-ball share of xG 35% for, 14% against · penalties won 1, conceded 1 (E9; includes missed).

**Corner shot zones (E6, Understat; lane from the attacking team's view, side of delivery not published):** for — 21 shots, xG 2.72, 0 goals, headed 9: 6-yard box, central 4 shots, xG 1.89, 0 goals; penalty area, central 4 shots, xG 0.26, 0 goals; 6-yard box, right 3 shots, xG 0.24, 0 goals · against — 9 shots conceded, xG 0.42, 0 goals, headed 4: penalty area, central 2 shots, xG 0.17, 0 goals; penalty area, right 2 shots, xG 0.09, 0 goals; 6-yard box, central 1 shots, xG 0.08, 0 goals. Delivery type (in/out-swinging) and first-contact winner are video items — see the narrative Set pieces block.

**Set-piece defending (F10, 8 league matches):** corners faced 33 · corner shots conceded 9 (headed 4), xG 0.42, goals 0 · xG per corner faced 0.013 (rank 20 of 20, 1 = weakest) · weak zone: none stands out · signal: **STRONG — no corner pairing against them** [DERIVED] · scheme: not recorded  (claude/set-piece-takers.md)

**Corners (E10 data layer):** observed takers GW1–11 [CONFIRMED — LiveScore Block L, 90 corners; side L/R as LiveScore records it; foot from SofaScore]: Dominik Szoboszlai 39 (19L/20R, 3 short, right foot); Konstantinos Tsimikas 20 (7L/13R, 3 short, left foot); Alexis Mac Allister 12 (5L/7R, 5 short, right foot); Florian Wirtz 10 (7L/3R, 2 short, right foot). First contact on corners that ended in a shot (Understat) — for: Alexander Isak 4 (4 headed), Alexis Mac Allister 4 (3 headed), Cody Gakpo 2 (1 headed), Víctor Muñoz 2 (1 headed), Florian Wirtz 2 · against (who beat them): Joshua King 2, Elliot Anderson 2, Murillo 1 (1 headed), Calvin Bassey 1 (1 headed), Ryan Christie 1 (1 headed). Swing (in/out) is not derivable from foot and side (test failed 3 Oct) — report/video item.

**Shape from average positions (E10 data layer, SofaScore, starters; in and out of possession mixed — x 0 = own goal line, 100 = opponent's) [DERIVED]:** back line 43.6 (rank 5 of 20, 1 = highest line) · block length 23.6 (rank 19, 1 = most compact) · width 68.0. Per match: GW6 H v Manchester City 4-2-3-1: back line 38, front 58, length 20, width 70 (35% poss); GW7 A v Brentford 4-2-3-1: back line 43, front 70, length 27, width 71 (60% poss); GW8 H v Brighton & Hove Albion 4-2-3-1: back line 37, front 56, length 19, width 67 (36% poss); GW9 H v Arsenal 4-2-3-1: back line 46, front 68, length 23, width 62 (56% poss); GW10 A v Crystal Palace 4-2-3-1: back line 42, front 63, length 21, width 65 (46% poss); GW11 H v Manchester United 4-2-3-1: back line 50, front 72, length 23, width 69 (63% poss). A back line that drops 8+ below the club's average marks a deep block that day; formation = SofaScore line-up.

**Plan B v a low block (E10 data layer) [DERIVED]:** 3 league match(es) v LB-coded sides — xG 1.70/match and 2.3 pts/match v 1.89 and 1.8 against the rest → **struggles — chance creation drops** (threshold: xG v LB at least 90% of the rest). GW2 H v Nottingham Forest 2–2, xG 1.75, box shots 8, poss 69%; GW3 A v Ipswich Town 2–0, xG 0.69, box shots 5, poss 55%; GW10 A v Crystal Palace 3–1, xG 2.65, box shots 18, poss 46%. Opponent codes are this week's Used codes, not the code at the time.

### Set pieces observed (D5, Understat shots, GWs 1, 2, 3, 4, 5, 6, 7, 8; counts = shots created, ≥2 is the signal, 1 can be a flick-on)
- Corner takers (assisted corner shots): **Wirtz 6, Szoboszlai 5, Ngumoha 1** · FPL editorial order: Szoboszlai #1, Mac Allister #2, Wirtz #3
- Direct free-kick shooters: **Szoboszlai 6, Allister 2** · FPL order: Szoboszlai #1, Wirtz #2, Mac Allister #3
- Penalties taken: **Szoboszlai 1** · FPL order: Szoboszlai #1, Isak #2, Gakpo #3
- Set-piece deliverers (assisted 'SetPiece' shots): **Szoboszlai 2, Jacquet 1, Wirtz 1**
- Corner targets (headed shots from corners): **Isak 4, Allister 3, Muñoz 1, Gakpo 1** · corner shots 21
- **DISAGREEMENT:** observed corner taker Florian Wirtz (6) v FPL #1 Szoboszlai — verify before crediting set-piece pairings

**Through-ball suppliers (Block P, PL/Opta, season):** Florian Wirtz 7 (0.71/90, percentile 96, 885 min); Cody Gakpo 4 (0.60/90, percentile 95, 604 min); Alexis Mac Allister 5 (0.54/90, percentile 93, 830 min); Trey Nyoni 1 (0.37/90, percentile 84, 242 min); Bradley Barcola 2 (0.27/90, percentile 77, 656 min) · club total 23 attempted. Top quartile = percentile 75+ of through balls attempted per 90 among 334 players with 180+ min — the supply half of the offside-trap pairing (`context-factors.md`).

**Pressing & territory (C13, PitchAPI):** GW1: PPDA 7, field tilt 70.5, possession 60%, box entries 9, direct speed 2.2, SCA 50; GW2: PPDA 4.89, field tilt 72.8, possession 68.3%, box entries 12, direct speed 1.97, SCA 26; GW3: PPDA 10.88, field tilt 58, possession 54.1%, box entries 8, direct speed 1.83, SCA 19; GW4: PPDA 9.48, field tilt 63.3, possession 55.5%, box entries 9, direct speed 2.72, SCA 26; GW5: PPDA 9.83, field tilt 44.8, possession 53.4%, box entries 10, direct speed 2.71, SCA 24; GW6: PPDA 9.5, field tilt 35.3, possession 35.4%, box entries 6, direct speed 3.1, SCA 21; GW7: PPDA 7.29, field tilt 68.8, possession 60.1%, box entries 21, direct speed 2.3, SCA 41; GW8: PPDA 16.41, field tilt 39.5, possession 36.5%, box entries 11, direct speed 3.59, SCA 19; GW9: PPDA 6.35, field tilt 61.1, possession 56.4%, box entries 29, direct speed 2.57, SCA 34; GW10: PPDA 10.93, field tilt 46.6, possession 46.4%, box entries 14, direct speed 3.07, SCA 36

**Zone 14 (C13, SofaScore heat-map points, 11 league matches):** for 42.3/match (rank 2 of 20) · conceded 22.2/match (rank 18 — 1 = concedes the most, a vulnerability for opposing creators) [heat-map points, not Opta touches]
**Deep completions (Understat, team, 8 matches):** for 6.6/match · allowed 8.4/match · PPDA 9.2. Per match for/allowed: GW3 6/5; GW4 5/9; GW5 8/8; GW6 3/11; GW7 14/9; GW8 9/16 [Understat model; per-player deep completions have no free source]

### Starter baseline (C5) — 4-2-3-1, 10 league matches, weights last-3 ×3 / older ×1
- GK: Alisson (16, 3/3)
- DEF: Jérémy Jacquet (16, 3/3), Virgil van Dijk (16, 3/3), Ronald Araújo (15, 3/3), Miloš Kerkez (15, 3/3)
- MID: Florian Wirtz (16, 3/3), Alexis Mac Allister (15, 3/3), Dominik Szoboszlai (11, 2/3), Víctor Muñoz (5, 0/3), Trey Nyoni (3, 1/3)
- FWD: Alexander Isak (15, 3/3)
- Contested slots: M Trey Nyoni 3 v Ryan Gravenberch 3; F Alexander Isak 15 v Bradley Barcola 14 · Excluded (FPL flag): Cody Gakpo — Calf injury - 75% chance of playing
- Absent last match (E12, SofaScore list): Gakpo (injury), Ekitiké (Achilles Tendon Injury), Gravenberch (Heel Injury; doubtful)
- Substitutions this season (C3): GW9 67' Cody Gakpo→Rio Ngumoha CHASING; GW9 58' Trey Nyoni→Dominik Szoboszlai CHASING; GW10 90' Ronald Araújo→Joe Gomez CARD-RISK; GW10 90' Alexander Isak→Lewis Koumas LATE; GW10 76' Cody Gakpo→Rio Ngumoha GAME-STATE; GW10 69' Dominik Szoboszlai→Trey Nyoni GAME-STATE; GW10 69' Bradley Barcola→Víctor Muñoz CARD-RISK; GW11 85' Alexander Isak→Lewis Koumas LATE; GW11 85' Ronald Araújo→Joe Gomez LATE; GW11 78' Rio Ngumoha→Jeremie Frimpong GAME-STATE; GW11 72' Bradley Barcola→Víctor Muñoz CARD-RISK; GW11 72' Alexis Mac Allister→Trey Nyoni GAME-STATE

### First-choice players and absences (F14) — generated 2026-11-24 07:45 UTC
First choice = starter baseline (GK, 2 centre-backs — defenders whose median heat-map y sits in 25–75), the top 2 by league xGI, and the primary takers. Absent = FPL status i/s/u/n or chance ≤ 25%. COVER = next available in the same role. The effect column is the I-adj the PRE run applies to **this club's opponents** (`selection-model.md`).
| Role | Player | Evidence | Availability | FPL status / news | COVER | I-adj when absent |
|---|---|---|---|---|---|---|
| GK | Alisson | start weight 16 | OK | a | — | — |
| CB | Jérémy Jacquet | start weight 16 | OK | a 100% | Ronald Araújo (DEF, not a CB by heat map) | — |
| CB | Virgil van Dijk | start weight 16 | OK | a 100% | Ronald Araújo (DEF, not a CB by heat map) | — |
| xGI #1 | Alexander Isak | xGI 6.50 | OK | a 100% | Bradley Barcola | — |
| xGI #2 | Florian Wirtz | xGI 4.53 | OK | a 100% | Bradley Barcola | — |
| Penalties #1 (FPL) | Szoboszlai | FPL order | OK | a 100% | Isak | — |
| Direct FK #1 (FPL) | Szoboszlai | FPL order | OK | a 100% | Wirtz | — |
| Corners (observed) | Dominik Szoboszlai | 39 corners taken | OK | a 100% | Konstantinos Tsimikas | — |
**Back-fill — first-choice players who did not start (current first-choice set; reason from the SofaScore missing list):** GW1 A Newcastle United: all started · GW2 H Nottingham Forest: all started · GW3 A Ipswich Town: all started · GW4 H Fulham: all started · GW5 A Bournemouth: all started · GW6 H Manchester City: Alexander Isak (Thigh Injury) · GW7 A Brentford: all started · GW8 H Brighton & Hove Albion: all started · GW9 H Arsenal: all started · GW10 A Crystal Palace: all started · GW11 H Manchester United: all started

### Next fixtures (all competitions)
- Wed 25 Nov 20:00 UTC · UEFA Champions League R5 · A v Club Brugge KV
- Sun 29 Nov 12:00 UTC · Premier League R12 · A v Everton
- Wed 02 Dec 19:30 UTC · Premier League R13 · H v Sunderland
- Sat 05 Dec 12:30 UTC · Premier League R14 · A v Chelsea
- Wed 09 Dec 20:00 UTC · UEFA Champions League R6 · H v FC Porto
- Sat 12 Dec 15:00 UTC · Premier League R15 · H v Leeds United

### FPL availability flags (players with league minutes this season)
Gakpo — Calf injury - 75% chance of playing (75%); Gravenberch — Foot injury - 75% chance of playing (75%)
<!-- AUTO:END -->
### Match-log facts (FX-09, one line per league match)
- GW1 A Newcastle United 2–2 · xG 2.98–1.58 · poss 61% · 4-2-3-1 · scorers: Cody Gakpo 55', Dominik Szoboszlai 90'
- GW2 H Nottingham Forest 2–2 · xG 1.75–2.30 · poss 69% · 4-2-3-1 · scorers: Alexander Isak 60', Víctor Muñoz 82'
- GW3 A Ipswich Town 2–0 · xG 0.69–0.75 · poss 55% · 4-2-3-1 · scorers: Alexander Isak 6', Alexander Isak 9'
- GW4 H Fulham 0–0 · xG 1.28–0.70 · poss 56% · 4-2-3-1 · scorers: none
- GW5 A Bournemouth 1–0 · xG 1.65–0.79 · poss 54% · 4-2-3-1 · scorers: Alexander Isak 57'
- GW6 H Manchester City 0–3 · xG 0.94–1.28 · poss 35% · 4-2-3-1 · scorers: none
- GW7 A Brentford 2–1 · xG 1.64–0.88 · poss 60% · 4-2-3-1 · scorers: Víctor Muñoz 62', Alexander Isak 70'
- GW8 H Brighton & Hove Albion 2–0 · xG 1.20–1.32 · poss 36% · 4-2-3-1 · scorers: Pascal Groß 17', Alexander Isak 21'
- GW9 H Arsenal 0–1 · xG 1.05–0.98 · poss 56% · 4-2-3-1 · scorers: none
- GW10 A Crystal Palace 3–1 · xG 2.65–2.60 · poss 46% · 4-2-3-1 · scorers: Alexis Mac Allister 40', Florian Wirtz 54', Alexander Isak 89'
- GW11 H Manchester United 4–0 · xG 4.35–0.65 · poss 63% · 4-2-3-1 · scorers: Dominik Szoboszlai 10', Florian Wirtz 13', Rio Ngumoha 66', Víctor Muñoz 82'
### Corner takers observed (LiveScore Block L)
- Dominik Szoboszlai: 39 corners (19 left, 20 right, 3 short)
- Konstantinos Tsimikas: 20 corners (7 left, 13 right, 3 short)
- Alexis Mac Allister: 12 corners (5 left, 7 right, 5 short)
- Florian Wirtz: 10 corners (7 left, 3 right, 2 short)
- Cody Gakpo: 6 corners (4 left, 2 right, 1 short)
- Milos Kerkez: 2 corners (0 left, 2 right)
- Luke Chambers: 1 corners (0 left, 1 right)
