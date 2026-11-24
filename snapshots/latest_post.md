# POST snapshot — GW11 (generated 2026-11-24T16:59:05Z, live)

## ⛔ GATE: HOLD — 5 item(s)

| # | Param | Status | What is needed |
|---|---|---|---|
| 1 | C2 | PARTIAL | SofaScore minutes are browser-only |
| 2 | C11 | PARTIAL | three models; FotMob and SofaScore share the Opta feed — count them as ONE provider |
| 3 | C13 | PARTIAL | free key in secret PITCHAPI_KEY; zone-14 and deep completions not provided; NULL = MISSING: xAG / xG chain / xG build-up empty for 6/10 matches (AVL v SUN, COV v CRY, HUL v BHA, CHE v LEE, TOT v IPS, BOU v NFO) — re-pulled automatically by later runs (late-field refresh); PL id resolved from /v1/leagues: l_4WFCIZ |
| 4 | C13b | MISSING | confirm |
| 5 | C15 | PARTIAL | confirm |

### Expected — accepted states, no decision needed (never ask about these)

| Param | Tag | Runner sees | Why it is expected |
|---|---|---|---|
| C5 | EXPECTED — FEEDER | PARTIAL | starter baseline (last-3 ×3, older ×1, injured excluded, contested slots) is computed by gen.py from SofaScore lineups; not a runner item |
| C16 | EXPECTED — FEEDER | MISSING | per-match heat maps for every player come from the SofaScore feeder (Block B-ext); the runner cannot reach SofaScore |
| C19 | EXPECTED — FEEDER | PARTIAL | through balls, progressive carries, offsides per player come from the SofaScore feeder ext stats; the runner's FotMob part is the cross-check |

Sources: Understat clubs 0/20, FotMob matches 10/10.

## PitchAPI (C13) — creation and progression, last GW

| Player | Min | SCA | GCA | xAG | xT off | xG chain / build-up | Prog passes | Into box | Prog carries | Carries into box | Take-ons |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Verbruggen (BHA) | 95 | 0 | 0 | None | 0.0221 | None / None | 0 | 0 | 0 | 0 | 0/0 |
| De Cuyper (BHA) | 95 | 6 | 0 | None | 0.5352 | None / None | 7 | 4 | 0 | 1 | 0/2 |
| Calafiori (ARS) | 99 | 4 | 0 | 0.0315 | 0.0107 | 1.3683 / 1.3683 | 4 | 1 | 0 | 0 | 0/0 |
| Konsa (ARS) | 99 | 1 | 0 | 0.0696 | 0.0386 | 1.162 / 1.162 | 0 | 0 | 0 | 0 | 0/0 |
| Van Hecke (TOT) | 96 | 2 | 0 | None | -0.0382 | None / None | 2 | 0 | 0 | 0 | 0/0 |
| Groß (BHA) | 95 | 3 | 0 | None | 0.2842 | None / None | 7 | 3 | 3 | 1 | 1/3 |
| Manzambi (AVL) | 59 | 0 | 0 | None | -0.2118 | None / None | 1 | 1 | 1 | 1 | 0/0 |
| Rudoni (COV) | 94 | 5 | 3 | None | 0.3258 | None / None | 3 | 2 | 6 | 1 | 2/3 |
| Haaland (MCI) | 93 | 3 | 0 | 0.1111 | -0.7336 | 1.5621 / 0.8251 | 1 | 1 | 1 | 0 | 0/0 |
| Barry (EVE) | 68 | 0 | 0 | 0 | -0.0139 | 0.1348 / 0.0197 | 0 | 0 | 0 | 0 | 0/1 |
| Isak (LIV) | 84 | 4 | 1 | 0 | -1.224 | 2.1306 / 1.1459 | 1 | 0 | 3 | 2 | 1/4 |
| Rushworth (COV) | 94 | 0 | 0 | None | 0.0495 | None / None | 0 | 0 | 0 | 0 | 0/0 |
| Tavernier (BOU) | 94 | 9 | 1 | None | 1.0013 | None / None | 6 | 2 | 4 | 2 | 4/6 |
| Rogers (CHE) | 96 | 4 | 2 | None | 0.0408 | None / None | 1 | 0 | 3 | 1 | 3/7 |
| Bogle (LEE) | 85 | 4 | 1 | None | 0.1052 | None / None | 5 | 3 | 1 | 2 | 3/6 |
| Raya (ARS) | 69 | 2 | 0 | 0 | 0.0518 | 1.0358 / 1.0358 | 0 | 0 | 0 | 0 | 0/0 |
| Ødegaard (ARS) | 93 | 2 | 1 | 0.1907 | 0.338 | 0.7573 / 0.7573 | 3 | 3 | 2 | 1 | 0/0 |
| Hill (BOU) | 94 | 3 | 1 | None | 0.2358 | None / None | 3 | 2 | 0 | 0 | 0/0 |
| Evanilson (BOU) | 94 | 5 | 1 | None | 0.517 | None / None | 4 | 0 | 0 | 0 | 0/2 |
| Kelleher (BRE) | 94 | 0 | 0 | 0 | 0.013 | 0.5681 / 0.5681 | 0 | 0 | 0 | 0 | 0/0 |
| Palmer (CHE) | 96 | 3 | 0 | None | 0.0947 | None / None | 3 | 2 | 6 | 2 | 1/2 |
| N.Jackson (AVL) | 72 | 4 | 0 | None | 0.121 | None / None | 0 | 0 | 2 | 1 | 0/1 |
| Okafor (LEE) | 72 | 6 | 1 | None | 1.9061 | None / None | 1 | 1 | 1 | 0 | 1/3 |
| Calvert-Lewin (LEE) | 96 | 6 | 2 | None | -0.1946 | None / None | 1 | 1 | 1 | 0 | 0/1 |
| Wirtz (LIV) | 92 | 13 | 1 | 1.9783 | 1.5199 | 2.7823 / 0.8928 | 10 | 7 | 1 | 0 | 1/2 |
| Szoboszlai (LIV) | 92 | 8 | 0 | 0.0878 | 0.7277 | 2.4773 / 1.9219 | 4 | 4 | 2 | 0 | 1/2 |
| Trafford (LEE) | 96 | 0 | 0 | None | 0.0274 | None / None | 1 | 0 | 0 | 0 | 0/0 |
| Cherki (MCI) | 24 | 0 | 0 | 0 | 0.0198 | 0.0568 / 0.0568 | 0 | 0 | 1 | 0 | 1/4 |
| Wissa (NEW) | 17 | 0 | 0 | 0 | -0.0046 | 0 / 0 | 0 | 0 | 0 | 0 | 0/0 |
| E.Le Fée (SUN) | 93 | 3 | 0 | None | 0.0642 | None / None | 2 | 2 | 1 | 0 | 1/3 |
| Tzolakis (HUL) | 95 | 1 | 0 | None | 0.0344 | None / None | 0 | 0 | 0 | 0 | 0/0 |

Team (PitchAPI): MCI PPDA 10.03, field tilt 66.9, box entries 18, direct speed 1.92; BOU PPDA 12.81, field tilt 45.5, box entries 12, direct speed 2.97; AVL PPDA 6.71, field tilt 76.6, box entries 21, direct speed 1.62; SUN PPDA 16.82, field tilt 23.4, box entries 7, direct speed 3.29; CHE PPDA 16.5, field tilt 49.1, box entries 8, direct speed 1.87; LEE PPDA 11.18, field tilt 50.9, box entries 14, direct speed 2.32; COV PPDA 10.17, field tilt 49.6, box entries 9, direct speed 2.95; TOT PPDA 7.43, field tilt 59.3, box entries 18, direct speed 2.19; NEW PPDA 11.56, field tilt 33.2, box entries 8, direct speed 3.14; ARS PPDA 9.57, field tilt 66.8, box entries 9, direct speed 2.3; HUL PPDA 17.58, field tilt 28.5, box entries 9, direct speed 4.45; BHA PPDA 4.92, field tilt 71.5, box entries 18, direct speed 2.25; LIV PPDA 6.95, field tilt 85, box entries 36, direct speed 2.13; BRE PPDA 10.62, field tilt 86.3, box entries 28, direct speed 1.57; EVE PPDA 28.16, field tilt 13.7, box entries 1, direct speed 2.93; FUL PPDA 12.16, field tilt 33.1, box entries 5, direct speed 1.96; CRY PPDA 7.5, field tilt 50.4, box entries 13, direct speed 1.92; NFO PPDA 7.35, field tilt 54.5, box entries 10, direct speed 2.72; IPS PPDA 13.65, field tilt 40.7, box entries 10, direct speed 2.62; MUN PPDA 16.7, field tilt 15, box entries 5, direct speed 2.86

## Tracked players — per-match facts (owned first, then pool)

| Player | Opp | Min FPL/US/FM | Pts | G/A | xG FPL / US / Opta | xA US / Opta | Shots (SoT) | KP | DefCon (CBI+R+T) | BPS/Bonus | Sub | Ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Cuyper (BHA) | @ HUL | 90/—/90 | 1 | 0/0 | 0.00 / — / None | — / 0.45 | None (None) | 3 | 3 (2+7+1) | 10/0 | 90 | Peter Bankes |
| Calafiori (ARS) | @ NEW | 90/—/90 | 1 | 0/0 | 0.04 / — / 0.04 | — / 0.03 | 1 (0) | 1 | 4 (4+3+0) | 4/0 | 90 | Chris Kavanagh |
| Konsa (ARS) | @ NEW | 90/—/90 | 1 | 0/0 | 0.00 / — / None | — / 0.01 | None (None) | 1 | 7 (6+1+1) | 15/0 | 90 | Chris Kavanagh |
| Van Hecke (TOT) | v IPS | 90/—/90 | 6 | 0/0 | 0.07 / — / 0.07 | — / 0.05 | 1 (0) | 1 | 3 (3+2+0) | 24/0 | 90 | Robert Jones |
| Bogle (LEE) | @ CHE | 85/—/86 | 4 | 0/1 | 0.06 / — / 0.06 | — / 0.17 | 3 (0) | 1 | 3 (0+7+3) | 18/0 | 85' | Michael Oliver |
| Haaland (MCI) | v FUL | 90/—/90 | 2 | 0/0 | 1.03 / — / 1.03 | — / 0.05 | 4 (1) | 1 | 0 (0+0+0) | 5/0 | 90 | Thomas Bramall |
| Barry (EVE) | @ BRE | 68/—/69 | 2 | 0/0 | 0.12 / — / 0.12 | — / None | 1 (1) | 0 | 5 (4+0+1) | 3/0 | 68' | Craig Pawson |
| Isak (LIV) | v MUN | 84/—/85 | 5 | 0/1 | 1.32 / — / 1.32 | — / 0.04 | 6 (3) | 0 | 7 (0+6+1) | 18/0 | 84' | Samuel Barrott |
| Verbruggen (BHA) | @ HUL | 90/—/90 | 2 | 0/0 | 0.00 / — / None | — / None | None (None) | None | 0 (1+14+0) | 15/0 | 90 | Peter Bankes |
| Rushworth (COV) | v CRY | 90/—/90 | 2 | 0/0 | 0.00 / — / None | — / None | None (None) | None | 0 (0+11+0) | 14/0 | 90 | Darren England |
| Groß (BHA) | @ HUL | 90/—/90 | 4 | 0/0 | 0.04 / — / 0.04 | — / 0.4 | 1 (1) | 2 | 12 (4+7+1) | 24/0 | 90 | Peter Bankes |
| Manzambi (AVL) | v SUN | 59/—/60 | 1 | 0/0 | 0.14 / — / 0.14 | — / 0.03 | 2 (1) | 0 | 5 (1+1+3) | 13/0 | 59' | Andy Madley |
| Rudoni (COV) | v CRY | 90/—/90 | 10 | 0/2 | 0.05 / — / 0.05 | — / 0.36 | 1 (1) | 3 | 4 (0+4+0) | 41/2 | 90 | Darren England |
| Tavernier (BOU) | v NFO | 90/—/90 | 8 | 0/1 | 0.06 / — / 0.06 | — / 0.91 | 2 (1) | 5 | 7 (1+6+0) | 39/2 | 90 | Adam Herczeg |
| Rogers (CHE) | v LEE | 90/—/90 | 5 | 0/1 | 0.21 / — / 0.21 | — / 0.03 | 5 (1) | 1 | 6 (1+2+3) | 14/0 | 90 | Michael Oliver |
| Hill (BOU) [pool] | v NFO | 90/—/90 | 14 | 0/1 | 0.00 / — / None | — / 0.05 | None (None) | 1 | 14 (12+3+2) | 40/3 | 90 | Adam Herczeg |
| Evanilson (BOU) [pool] | v NFO | 90/—/90 | 6 | 1/0 | 1.12 / — / 1.12 | — / 0.02 | 5 (2) | 2 | 2 (1+0+1) | 32/0 | 90 | Adam Herczeg |
| N.Jackson (AVL) [pool] | v SUN | 72/—/73 | 2 | 0/0 | 0.10 / — / 0.1 | — / 0.23 | 1 (0) | 3 | 0 (0+0+0) | 8/0 | 72' | Andy Madley |
| Calvert-Lewin (LEE) [pool] | @ CHE | 90/—/90 | 9 | 1/1 | 1.40 / — / 1.4 | — / 0.03 | 6 (3) | 3 | 5 (0+5+0) | 25/0 | 90 | Michael Oliver |
| Wissa (NEW) [pool] | v ARS | 7/—/7 | 1 | 0/0 | 0.00 / — / None | — / None | None (None) | 0 | 0 (0+0+0) | 2/0 | 7' | Chris Kavanagh |
| Raya (ARS) [pool] | @ NEW | 69/—/70 | 1 | 0/0 | 0.00 / — / None | — / None | None (None) | None | 0 (1+6+0) | 5/0 | 69' | Chris Kavanagh |
| Kelleher (BRE) [pool] | v EVE | 90/—/90 | 6 | 0/0 | 0.00 / — / None | — / None | None (None) | None | 0 (0+9+0) | 29/0 | 90 | Craig Pawson |
| Trafford (LEE) [pool] | @ CHE | 90/—/90 | 2 | 0/0 | 0.00 / — / None | — / None | None (None) | None | 0 (2+6+0) | 9/0 | 90 | Michael Oliver |
| Tzolakis (HUL) [pool] | v BHA | 90/—/90 | 10 | 0/0 | 0.00 / — / None | — / None | None (None) | None | 0 (0+9+0) | 44/2 | 90 | Peter Bankes |
| Ødegaard (ARS) [pool] | @ NEW | 90/—/89 | 5 | 0/1 | 0.00 / — / None | — / 0.43 | None (None) | 2 | 4 (1+2+1) | 24/0 | 90 | Chris Kavanagh |
| Palmer (CHE) [pool] | v LEE | 90/—/90 | 2 | 0/0 | 0.03 / — / 0.03 | — / 0.07 | 1 (0) | 1 | 4 (0+3+1) | 18/0 | 90 | Michael Oliver |
| Okafor (LEE) [pool] | @ CHE | 72/—/73 | 15 | 2/0 | 0.27 / — / 0.27 | — / 0.06 | 3 (2) | 3 | 3 (1+2+0) | 52/3 | 72' | Michael Oliver |
| Wirtz (LIV) [pool] | v MUN | 90/—/90 | 14 | 1/1 | 0.36 / — / 0.36 | — / 1.08 | 2 (1) | 10 | 8 (1+7+0) | 69/3 | 90 | Samuel Barrott |
| Szoboszlai (LIV) [pool] | v MUN | 90/—/90 | 9 | 1/0 | 0.34 / — / 0.34 | — / 0.15 | 7 (3) | 3 | 10 (2+8+0) | 43/1 | 90 | Samuel Barrott |
| Cherki (MCI) [pool] | v FUL | 20/—/20 | 1 | 0/0 | 0.05 / — / 0.05 | — / 0.01 | 1 (0) | 0 | 6 (1+4+1) | 8/0 | 20' | Thomas Bramall |
| E.Le Fée (SUN) [pool] | @ AVL | 90/—/90 | 3 | 0/0 | 0.09 / — / 0.09 | — / 0.08 | 2 (1) | 1 | 9 (0+6+3) | 21/0 | 90 | Andy Madley |

## Consistency flags

- Minutes disagree: [('Manzambi', {'fpl': 59, 'understat': None, 'fotmob': 60}), ('Barry', {'fpl': 68, 'understat': None, 'fotmob': 69}), ('Isak', {'fpl': 84, 'understat': None, 'fotmob': 85}), ('Bogle', {'fpl': 85, 'understat': None, 'fotmob': 86}), ('Raya', {'fpl': 69, 'understat': None, 'fotmob': 70}), ('Ødegaard', {'fpl': 90, 'understat': None, 'fotmob': 89}), ('N.Jackson', {'fpl': 72, 'understat': None, 'fotmob': 73}), ('Okafor', {'fpl': 72, 'understat': None, 'fotmob': 73})]
- xG models differ by >0.25: none
- FPL points vs FotMob fantasy points: all equal

## Team level

- MCI: Understat xG None goals None (A v None); FotMob ref Thomas Bramall; Expected goals (xG) ['1.87', '0.74']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.87', '0.74']; xG open play ['1.40', '0.58']
- BOU: Understat xG None goals None (A v None); FotMob ref Adam Herczeg; Expected goals (xG) ['2.89', '1.99']; Expected goals (xG) [None, None]; Expected goals (xG) ['2.89', '1.99']; xG open play ['2.62', '0.80']
- AVL: Understat xG None goals None (A v None); FotMob ref Andy Madley; Expected goals (xG) ['1.03', '0.25']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.03', '0.25']; xG open play ['0.67', '0.13']
- SUN: Understat xG None goals None (A v None); FotMob ref Andy Madley; Expected goals (xG) ['1.03', '0.25']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.03', '0.25']; xG open play ['0.67', '0.13']
- CHE: Understat xG None goals None (A v None); FotMob ref Michael Oliver; Expected goals (xG) ['0.64', '2.77']; Expected goals (xG) [None, None]; Expected goals (xG) ['0.64', '2.77']; xG open play ['0.30', '0.89']
- LEE: Understat xG None goals None (A v None); FotMob ref Michael Oliver; Expected goals (xG) ['0.64', '2.77']; Expected goals (xG) [None, None]; Expected goals (xG) ['0.64', '2.77']; xG open play ['0.30', '0.89']
- COV: Understat xG None goals None (A v None); FotMob ref Darren England; Expected goals (xG) ['2.06', '1.73']; Expected goals (xG) [None, None]; Expected goals (xG) ['2.06', '1.73']; xG open play ['1.34', '1.26']
- TOT: Understat xG None goals None (A v None); FotMob ref Robert Jones; Expected goals (xG) ['2.65', '0.47']; Expected goals (xG) [None, None]; Expected goals (xG) ['2.65', '0.47']; xG open play ['2.13', '0.38']
- NEW: Understat xG None goals None (A v None); FotMob ref Chris Kavanagh; Expected goals (xG) ['1.71', '1.49']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.71', '1.49']; xG open play ['0.67', '1.43']
- ARS: Understat xG None goals None (A v None); FotMob ref Chris Kavanagh; Expected goals (xG) ['1.71', '1.49']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.71', '1.49']; xG open play ['0.67', '1.43']
- HUL: Understat xG None goals None (A v None); FotMob ref Peter Bankes; Expected goals (xG) ['1.83', '2.23']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.83', '2.23']; xG open play ['1.74', '2.19']
- BHA: Understat xG None goals None (A v None); FotMob ref Peter Bankes; Expected goals (xG) ['1.83', '2.23']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.83', '2.23']; xG open play ['1.74', '2.19']
- LIV: Understat xG None goals None (A v None); FotMob ref Samuel Barrott; Expected goals (xG) ['4.35', '0.65']; Expected goals (xG) [None, None]; Expected goals (xG) ['4.35', '0.65']; xG open play ['3.94', '0.55']
- BRE: Understat xG None goals None (A v None); FotMob ref Craig Pawson; Expected goals (xG) ['2.57', '0.23']; Expected goals (xG) [None, None]; Expected goals (xG) ['2.57', '0.23']; xG open play ['1.41', '0.20']
- EVE: Understat xG None goals None (A v None); FotMob ref Craig Pawson; Expected goals (xG) ['2.57', '0.23']; Expected goals (xG) [None, None]; Expected goals (xG) ['2.57', '0.23']; xG open play ['1.41', '0.20']
- FUL: Understat xG None goals None (A v None); FotMob ref None; 
- CRY: Understat xG None goals None (A v None); FotMob ref None; 
- NFO: Understat xG None goals None (A v None); FotMob ref None; 
- IPS: Understat xG None goals None (A v None); FotMob ref None; 
- MUN: Understat xG None goals None (A v None); FotMob ref None; 

## Coverage C1–C19

| # | Status | Source | Note |
|---|---|---|---|
| C1 | OK | event/N/live minutes | official FPL minutes |
| C2 | PARTIAL | Understat (0/31) + FotMob/Opta (31/31) | SofaScore minutes are browser-only |
| C3 | OK | FotMob events (sub minute, injuredPlayerOut flag) | the REASON (tactical/game state) is a MID-cadence report item |
| C4 | OK | live minutes/starts + bootstrap status/news | why-absent text = FPL news; empty news → check reports |
| C5 | PARTIAL | derived across GWs | needs a per-club regular-starter baseline — not yet computed |
| C6 | OK | event/N/live total_points |  |
| C7 | OK | event/N/live |  |
| C8 | OK | event/N/live bonus + bps | final after data_checked |
| C9 | OK | event/N/live defensive_contribution, CBI, recoveries, tackles |  |
| C10 | OK | FPL saves; goals prevented needs xGOT faced (FotMob/SofaScore GK stats) | GK-only |
| C11 | PARTIAL | FPL own xG/xA/xGI + Understat + FotMob(Opta) | three models; FotMob and SofaScore share the Opta feed — count them as ONE provider |
| C12 | OK | FotMob total/on-target shots, big chances; Understat shots |  |
| C13 | PARTIAL | PitchAPI advanced/players (31/31 matched, 10/10 matches) — SCA, GCA, xT (possession value), progressive passes/carries, carries into box, take-ons, xG chain/build-up, xAG; team PPDA/field tilt | free key in secret PITCHAPI_KEY; zone-14 and deep completions not provided; NULL = MISSING: xAG / xG chain / xG build-up empty for 6/10 matches (AVL v SUN, COV v CRY, HUL v BHA, CHE v LEE, TOT v IPS, BOU v NFO) — re-pulled automatically by later runs (late-field refresh); PL id resolved from /v1/leagues: l_4WFCIZ |
| C14 | OK | event/N/live cards |  |
| C15 | PARTIAL | Understat shot list (X, Y, xG, result, situation, body, last action) + FotMob shotmap (xGOT) |  |
| C16 | MISSING | SofaScore /event/{id}/player/{pid}/heatmap — browser only | not scriptable; attended POST step or device-bound task |
| C17 | OK | fixtures/?event=N (opponent, venue) | archetype comes from the team profile (F5) |
| C18 | OK | FotMob tackles/interceptions/clearances/blocks/aerials/recoveries |  |
| C19 | PARTIAL | FotMob accurate crosses, dribbles, passes into final third | through balls, progressive carries, offsides per player: SofaScore (browser) or FBref (blocked) |
