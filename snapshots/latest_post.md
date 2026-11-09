# POST snapshot — GW10 (generated 2026-11-09T15:13:28Z, live)

## ⛔ GATE: HOLD — 5 item(s)

| # | Param | Status | What is needed |
|---|---|---|---|
| 1 | C2 | PARTIAL | SofaScore minutes are browser-only |
| 2 | C11 | PARTIAL | three models; FotMob and SofaScore share the Opta feed — count them as ONE provider |
| 3 | C13 | PARTIAL | free key in secret PITCHAPI_KEY; zone-14 and deep completions not provided; NULL = MISSING: xAG / xG chain / xG build-up empty for 8/10 matches (BHA v BRE, ARS v HUL, EVE v COV, IPS v BOU, FUL v NEW, NFO v MCI, CRY v LIV, LEE v TOT) — re-pulled automatically by later runs (late-field refresh); PL id resolved from /v1/leagues: l_4WFCIZ |
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
| Verbruggen (BHA) | 95 | 0 | 0 | None | 0.0349 | None / None | 1 | 0 | 0 | 0 | 0/0 |
| De Cuyper (BHA) | 81 | 4 | 1 | None | -0.2333 | None / None | 5 | 5 | 1 | 0 | 1/3 |
| Calafiori (ARS) | 68 | 1 | 0 | None | 0.0399 | None / None | 1 | 0 | 3 | 0 | 0/0 |
| Konsa (ARS) | 94 | 0 | 0 | None | -0.078 | None / None | 0 | 0 | 0 | 0 | 0/0 |
| Rogers (CHE) | 96 | 1 | 0 | 0 | 0.1637 | 0.3799 / 0.3799 | 5 | 1 | 3 | 0 | 1/6 |
| Groß (BHA) | 95 | 11 | 1 | None | 0.7069 | None / None | 8 | 7 | 2 | 0 | 0/0 |
| Manzambi (AVL) | 77 | 2 | 0 | 0.0427 | 0.1326 | 0.9573 / 0.9573 | 5 | 1 | 4 | 0 | 3/6 |
| Tavernier (BOU) | 99 | 7 | 0 | None | -0.553 | None / None | 4 | 4 | 3 | 0 | 1/4 |
| Haaland (MCI) | 95 | 1 | 0 | None | -0.2814 | None / None | 1 | 0 | 0 | 0 | 1/1 |
| Barry (EVE) | 96 | 2 | 2 | None | 1.2156 | None / None | 1 | 1 | 1 | 0 | 2/3 |
| Isak (LIV) | 90 | 3 | 1 | None | 0.7271 | None / None | 2 | 1 | 0 | 0 | 2/2 |
| Rushworth (COV) | 96 | 1 | 0 | None | 0.0448 | None / None | 0 | 0 | 0 | 0 | 0/0 |
| Rudoni (COV) | 85 | 5 | 0 | None | 0.1555 | None / None | 3 | 2 | 5 | 0 | 2/6 |
| Davis (IPS) | 99 | 1 | 0 | None | 0.1058 | None / None | 2 | 1 | 0 | 0 | 0/0 |
| Bogle (LEE) | 92 | 7 | 0 | None | 0.3058 | None / None | 3 | 3 | 1 | 0 | 0/0 |
| Raya (ARS) | 94 | 0 | 0 | None | 0.0328 | None / None | 0 | 0 | 0 | 0 | 0/0 |
| Gabriel (ARS) | 94 | 1 | 0 | None | 0.0609 | None / None | 1 | 0 | 0 | 0 | 0/0 |
| Rice (ARS) | 62 | 2 | 0 | None | -0.0595 | None / None | 2 | 0 | 0 | 0 | 2/3 |
| Evanilson (BOU) | 84 | 5 | 1 | None | 0.7786 | None / None | 0 | 1 | 1 | 1 | 1/1 |
| Van Hecke (TOT) | 94 | 1 | 0 | None | 0.0816 | None / None | 4 | 1 | 0 | 0 | 0/0 |
| Palmer (CHE) | 96 | 3 | 0 | 0.1295 | 0.1329 | 0.3161 / 0.3161 | 6 | 1 | 2 | 0 | 0/1 |
| N.Jackson (AVL) | 85 | 4 | 2 | 0.3777 | 0.8866 | 1.9555 / 1.0268 | 1 | 0 | 1 | 0 | 0/3 |
| Dewsbury-Hall (EVE) | 96 | 4 | 0 | None | 0.9607 | None / None | 1 | 1 | 4 | 2 | 1/3 |
| Szoboszlai (LIV) | 68 | 7 | 1 | None | 0.2835 | None / None | 4 | 7 | 0 | 0 | 1/1 |
| Trafford (LEE) | 94 | 0 | 0 | None | 0.0332 | None / None | 0 | 0 | 0 | 0 | 0/0 |
| Cherki (MCI) | 95 | 3 | 1 | None | 0.9835 | None / None | 5 | 0 | 1 | 0 | 0/0 |
| Wissa (NEW) | 60 | 1 | 0 | None | -0.1059 | None / None | 1 | 0 | 2 | 1 | 1/2 |
| Vuskovic (BHA) | 95 | 0 | 0 | None | 0.1042 | None / None | 4 | 0 | 1 | 0 | 0/0 |

Team (PitchAPI): EVE PPDA 11.17, field tilt 48.6, box entries 12, direct speed 2.26; COV PPDA 8.81, field tilt 51.4, box entries 10, direct speed 2.57; LEE PPDA 9.55, field tilt 40, box entries 10, direct speed 3.05; TOT PPDA 8.12, field tilt 60, box entries 9, direct speed 2.46; ARS PPDA 13.18, field tilt 76.2, box entries 30, direct speed 2.58; NEW PPDA 11.53, field tilt 34.5, box entries 12, direct speed 2.04; MCI PPDA 9.88, field tilt 74.4, box entries 16, direct speed 1.53; BHA PPDA 6.17, field tilt 90.1, box entries 19, direct speed 1.61; LIV PPDA 10.93, field tilt 46.6, box entries 14, direct speed 3.07; IPS PPDA 9.3, field tilt 51.1, box entries 8, direct speed 1.99; BOU PPDA 10.59, field tilt 48.9, box entries 7, direct speed 2.46; CHE PPDA 9.15, field tilt 71.8, box entries 11, direct speed 1.67; AVL PPDA 21.93, field tilt 27.7, box entries 6, direct speed 2.12; HUL PPDA 12.34, field tilt 23.8, box entries 7, direct speed 2.89; FUL PPDA 9.45, field tilt 65.5, box entries 16, direct speed 2.3; NFO PPDA 14.3, field tilt 25.6, box entries 9, direct speed 4.65; BRE PPDA 21.68, field tilt 9.9, box entries 4, direct speed 2.33; CRY PPDA 12.22, field tilt 53.4, box entries 13, direct speed 3.05; SUN PPDA 14.74, field tilt 28.2, box entries 4, direct speed 3.12; MUN PPDA 7.09, field tilt 72.3, box entries 22, direct speed 2.82

## Tracked players — per-match facts (owned first, then pool)

| Player | Opp | Min FPL/US/FM | Pts | G/A | xG FPL / US / Opta | xA US / Opta | Shots (SoT) | KP | DefCon (CBI+R+T) | BPS/Bonus | Sub | Ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| De Cuyper (BHA) | v BRE | 81/—/82 | 6 | 0/0 | 0.35 / — / 0.35 | — / 0.38 | 3 (0) | 2 | 2 (1+3+1) | 27/0 | 81' | Michael Oliver |
| Calafiori (ARS) | v HUL | 68/—/69 | 6 | 0/0 | 0.00 / — / None | — / 0.01 | None (None) | 1 | 6 (6+4+0) | 26/0 | 68' | Farai Hallam |
| Konsa (ARS) | v HUL | 90/—/90 | 8 | 0/0 | 0.03 / — / 0.03 | — / 0.01 | 1 (0) | 0 | 11 (10+6+1) | 29/0 | 90 | Farai Hallam |
| Davis (IPS) | v BOU | 90/—/90 | -1 | 0/0 | 0.00 / — / None | — / 0.03 | None (None) | 1 | 9 (5+3+4) | 5/0 | 90 | Simon Hooper |
| Bogle (LEE) | v TOT | 90/—/89 | 7 | 0/0 | 0.11 / — / 0.11 | — / 0.21 | 3 (0) | 3 | 1 (0+3+1) | 27/1 | 90 | John Brooks |
| Haaland (MCI) | @ NFO | 90/—/90 | 2 | 0/0 | 0.50 / — / 0.5 | — / 0.02 | 4 (2) | 0 | 0 (0+0+0) | 6/0 | 90 | Samuel Barrott |
| Barry (EVE) | v COV | 90/—/90 | 16 | 2/1 | 0.92 / — / 0.92 | — / 0.1 | 6 (2) | 1 | 4 (2+2+0) | 59/3 | 90 | Stuart Attwell |
| Isak (LIV) | @ CRY | 90/—/89 | 8 | 1/0 | 0.53 / — / 0.53 | — / 0.02 | 3 (2) | 0 | 3 (2+1+0) | 34/2 | 90 | Tony Harrington |
| Verbruggen (BHA) | v BRE | 90/—/90 | 6 | 0/0 | 0.00 / — / None | — / None | None (None) | None | 0 (1+10+0) | 27/0 | 90 | Michael Oliver |
| Rushworth (COV) | @ EVE | 90/—/90 | 2 | 0/0 | 0.00 / — / None | — / None | None (None) | None | 0 (1+5+0) | 7/0 | 90 | Stuart Attwell |
| Rogers (CHE) | @ SUN | 90/—/90 | 2 | 0/0 | 0.26 / — / 0.26 | — / 0.07 | 2 (1) | 0 | 8 (0+7+1) | 15/0 | 90 | Jarred Gillett |
| Groß (BHA) | v BRE | 90/—/90 | 10 | 1/0 | 0.87 / — / 0.87 | — / 0.65 | 2 (1) | 5 | 3 (0+2+1) | 34/2 | 90 | Michael Oliver |
| Manzambi (AVL) | @ MUN | 77/—/78 | 2 | 0/0 | 0.07 / — / 0.07 | — / 0.29 | 1 (0) | 1 | 9 (2+5+2) | 19/0 | 77' | Chris Kavanagh |
| Tavernier (BOU) | @ IPS | 90/—/90 | 3 | 0/0 | 0.50 / — / 0.5 | — / 0.09 | 1 (1) | 2 | 12 (2+9+1) | 12/0 | 90 | Simon Hooper |
| Rudoni (COV) | @ EVE | 85/—/86 | 2 | 0/0 | 0.12 / — / 0.12 | — / 0.26 | 3 (0) | 3 | 8 (3+4+1) | 19/0 | 85' | Stuart Attwell |
| Gabriel (ARS) [pool] | v HUL | 90/—/90 | 8 | 0/0 | 0.00 / — / None | — / None | None (None) | 0 | 10 (9+5+1) | 29/0 | 90 | Farai Hallam |
| Van Hecke (TOT) [pool] | @ LEE | 90/—/90 | 4 | 0/0 | 0.07 / — / 0.07 | — / 0.03 | 1 (1) | 0 | 10 (10+2+0) | 11/0 | 90 | John Brooks |
| Vuskovic (BHA) [pool] | v BRE | 90/—/90 | 12 | 0/1 | 0.01 / — / 0.01 | — / 0.04 | 1 (0) | 0 | 6 (5+5+1) | 37/3 | 90 | Michael Oliver |
| Evanilson (BOU) [pool] | @ IPS | 84/—/85 | 9 | 1/0 | 0.85 / — / 0.85 | — / 0.04 | 4 (1) | 1 | 9 (5+3+1) | 39/3 | 84' | Simon Hooper |
| N.Jackson (AVL) [pool] | @ MUN | 85/—/86 | 11 | 1/1 | 1.30 / — / 1.3 | — / 0.02 | 2 (1) | 2 | 2 (0+1+1) | 44/2 | 85' | Chris Kavanagh |
| Wissa (NEW) [pool] | @ FUL | 60/—/61 | 2 | 0/0 | 0.04 / — / 0.04 | — / 0.05 | 1 (0) | 1 | 3 (0+2+1) | 7/0 | 60' | Robert Jones |
| Raya (ARS) [pool] | v HUL | 90/—/90 | 6 | 0/0 | 0.00 / — / None | — / None | None (None) | None | 0 (2+7+0) | 31/0 | 90 | Farai Hallam |
| Trafford (LEE) [pool] | v TOT | 90/—/90 | 10 | 0/0 | 0.00 / — / None | — / None | None (None) | None | 0 (5+9+0) | 34/3 | 90 | John Brooks |
| Rice (ARS) [pool] | v HUL | 62/—/63 | 3 | 0/0 | 0.13 / — / 0.13 | — / 0.03 | 3 (2) | 0 | 5 (0+5+0) | 14/0 | 62' | Farai Hallam |
| Palmer (CHE) [pool] | @ SUN | 90/—/90 | 2 | 0/0 | 0.04 / — / 0.04 | — / 0.07 | 1 (1) | 2 | 3 (0+2+1) | 18/0 | 90 | Jarred Gillett |
| Dewsbury-Hall (EVE) [pool] | v COV | 90/—/90 | 9 | 1/0 | 0.18 / — / 0.18 | — / 0.11 | 2 (1) | 1 | 9 (2+3+4) | 41/2 | 90 | Stuart Attwell |
| Szoboszlai (LIV) [pool] | @ CRY | 68/—/69 | 7 | 0/1 | 0.02 / — / 0.02 | — / 0.49 | 1 (0) | 6 | 7 (1+6+0) | 31/1 | 68' | Tony Harrington |
| Cherki (MCI) [pool] | @ NFO | 90/—/90 | 9 | 1/0 | 0.16 / — / 0.16 | — / 0.05 | 1 (1) | 2 | 5 (1+3+1) | 36/2 | 90 | Samuel Barrott |

## Consistency flags

- Minutes disagree: [('De Cuyper', {'fpl': 81, 'understat': None, 'fotmob': 82}), ('Calafiori', {'fpl': 68, 'understat': None, 'fotmob': 69}), ('Manzambi', {'fpl': 77, 'understat': None, 'fotmob': 78}), ('Isak', {'fpl': 90, 'understat': None, 'fotmob': 89}), ('Rudoni', {'fpl': 85, 'understat': None, 'fotmob': 86}), ('Bogle', {'fpl': 90, 'understat': None, 'fotmob': 89}), ('Rice', {'fpl': 62, 'understat': None, 'fotmob': 63}), ('Evanilson', {'fpl': 84, 'understat': None, 'fotmob': 85}), ('N.Jackson', {'fpl': 85, 'understat': None, 'fotmob': 86}), ('Szoboszlai', {'fpl': 68, 'understat': None, 'fotmob': 69}), ('Wissa', {'fpl': 60, 'understat': None, 'fotmob': 61})]
- xG models differ by >0.25: none
- FPL points vs FotMob fantasy points: all equal

## Team level

- EVE: Understat xG None goals None (A v None); FotMob ref Stuart Attwell; Expected goals (xG) ['1.43', '1.21']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.43', '1.21']; xG open play ['1.38', '1.00']
- COV: Understat xG None goals None (A v None); FotMob ref Stuart Attwell; Expected goals (xG) ['1.43', '1.21']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.43', '1.21']; xG open play ['1.38', '1.00']
- LEE: Understat xG None goals None (A v None); FotMob ref John Brooks; Expected goals (xG) ['1.96', '0.72']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.96', '0.72']; xG open play ['0.69', '0.63']
- TOT: Understat xG None goals None (A v None); FotMob ref John Brooks; Expected goals (xG) ['1.96', '0.72']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.96', '0.72']; xG open play ['0.69', '0.63']
- ARS: Understat xG None goals None (A v None); FotMob ref Farai Hallam; Expected goals (xG) ['1.26', '0.36']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.26', '0.36']; xG open play ['1.04', '0.16']
- NEW: Understat xG None goals None (A v None); FotMob ref Robert Jones; Expected goals (xG) ['0.70', '1.14']; Expected goals (xG) [None, None]; Expected goals (xG) ['0.70', '1.14']; xG open play ['0.44', '1.14']
- MCI: Understat xG None goals None (A v None); FotMob ref Samuel Barrott; Expected goals (xG) ['1.06', '1.76']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.06', '1.76']; xG open play ['0.86', '1.64']
- BHA: Understat xG None goals None (A v None); FotMob ref Michael Oliver; Expected goals (xG) ['2.11', '0.59']; Expected goals (xG) [None, None]; Expected goals (xG) ['2.11', '0.59']; xG open play ['1.20', '0.39']
- LIV: Understat xG None goals None (A v None); FotMob ref Tony Harrington; Expected goals (xG) ['2.60', '2.65']; Expected goals (xG) [None, None]; Expected goals (xG) ['2.60', '2.65']; xG open play ['1.44', '1.05']
- IPS: Understat xG None goals None (A v None); FotMob ref Simon Hooper; Expected goals (xG) ['1.26', '2.23']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.26', '2.23']; xG open play ['0.32', '1.69']
- BOU: Understat xG None goals None (A v None); FotMob ref Simon Hooper; Expected goals (xG) ['1.26', '2.23']; Expected goals (xG) [None, None]; Expected goals (xG) ['1.26', '2.23']; xG open play ['0.32', '1.69']
- CHE: Understat xG None goals None (A v None); FotMob ref Jarred Gillett; Expected goals (xG) ['2.38', '0.66']; Expected goals (xG) [None, None]; Expected goals (xG) ['2.38', '0.66']; xG open play ['1.31', '0.42']
- AVL: Understat xG None goals None (A v None); FotMob ref Chris Kavanagh; Expected goals (xG) ['3.55', '2.88']; Expected goals (xG) [None, None]; Expected goals (xG) ['3.55', '2.88']; xG open play ['2.36', '0.38']
- HUL: Understat xG None goals None (A v None); FotMob ref None; 
- FUL: Understat xG None goals None (A v None); FotMob ref None; 
- NFO: Understat xG None goals None (A v None); FotMob ref None; 
- BRE: Understat xG None goals None (A v None); FotMob ref None; 
- CRY: Understat xG None goals None (A v None); FotMob ref None; 
- SUN: Understat xG None goals None (A v None); FotMob ref None; 
- MUN: Understat xG None goals None (A v None); FotMob ref None; 

## Coverage C1–C19

| # | Status | Source | Note |
|---|---|---|---|
| C1 | OK | event/N/live minutes | official FPL minutes |
| C2 | PARTIAL | Understat (0/28) + FotMob/Opta (28/28) | SofaScore minutes are browser-only |
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
| C13 | PARTIAL | PitchAPI advanced/players (28/28 matched, 10/10 matches) — SCA, GCA, xT (possession value), progressive passes/carries, carries into box, take-ons, xG chain/build-up, xAG; team PPDA/field tilt | free key in secret PITCHAPI_KEY; zone-14 and deep completions not provided; NULL = MISSING: xAG / xG chain / xG build-up empty for 8/10 matches (BHA v BRE, ARS v HUL, EVE v COV, IPS v BOU, FUL v NEW, NFO v MCI, CRY v LIV, LEE v TOT) — re-pulled automatically by later runs (late-field refresh); PL id resolved from /v1/leagues: l_4WFCIZ |
| C14 | OK | event/N/live cards |  |
| C15 | PARTIAL | Understat shot list (X, Y, xG, result, situation, body, last action) + FotMob shotmap (xGOT) |  |
| C16 | MISSING | SofaScore /event/{id}/player/{pid}/heatmap — browser only | not scriptable; attended POST step or device-bound task |
| C17 | OK | fixtures/?event=N (opponent, venue) | archetype comes from the team profile (F5) |
| C18 | OK | FotMob tackles/interceptions/clearances/blocks/aerials/recoveries |  |
| C19 | PARTIAL | FotMob accurate crosses, dribbles, passes into final third | through balls, progressive carries, offsides per player: SofaScore (browser) or FBref (blocked) |
