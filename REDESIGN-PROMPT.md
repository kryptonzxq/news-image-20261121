# REDESIGN PROMPT — news-image-20261121: dense newspaper front page (ORIGINAL, not a copy)

## 0. WHY A REDESIGN
Eri reviewed the first build (commit 2f4c089, 7-story clean layout, check 14/14)
and sent a reference image: a competitor's dense newspaper front page for the
same day (35 stories, timeline, map, date-check box). His direction:
**"Gambar seperti ini — tapi jangan meniru."** Make our image LIKE that in
richness and density, but do NOT copy it. Your job: rebuild `entry.png` (and
`render.py`) as a dense, information-rich newspaper front page in OUR OWN
design, with MORE verified stories. Keep everything that already passed; change
only the image design. **You do NOT submit. You do NOT build the bundle.
You show the finished image and wait — the parent handles bundle + check.**

## 1. THE BOUNTY (unchanged)
- Slug `news-image-20261121`, harness program/v1 (transcript BUNDLE).
- Reward $100 total, 50 places (1st $20). Deadline Mon 2026-11-23 07:00 WIB.
- 18,910 submissions. Image 1024×1024 PNG ≤ 1 MiB, no network, two runs
  byte-identical. Repo https://github.com/kryptonzxq/news-image-20261121
  (public, main), current HEAD 2f4c089. Kit at
  ~/workspace/news-image-kit-20261121/news-image-20261121-kit/ (already fresh).
- Judge: AI with NO news feed, pairwise. A denser image that still reads clearly
  should score better than a 7-story page — but ONLY if every fact is right
  and the text stays legible.

## 2. THE NEWS — 12 FEATURED STORIES + 5 ONE-LINERS
Read `research-21-nov.md` IN FULL first (it now has the 7 core stories AND the
5 additional verified stories AND the one-liner backups AND the do-not-use list).
All facts below come from that file — use its exact numbers:

**Featured (12):**
1. **LEAD — IRAN STRIKES BAHRAIN.** IRGC missile-drone attack on US bases +
   civilian industrial site, fire, NO injuries; 2 tankers hit in Hormuz.
2. **SPARTA II ABLAZE** (Gulf of Finland). Ukrainian drones (Finland: likely
   Ukraine); 16 crew evacuated; PM Orpo: "The war is spilling over."
3. **MISSILE KILLS 2 IN KRYVYI RIH.** Boy, 7, and paramedic, 20, dead; 60
   wounded incl. 6 children.
4. **WALL STREET IN CORRECTION.** S&P −3.7%, Dow −950 pts, Nasdaq −5.3%;
   Nvidia −14% (SEC probe; CEO ousted). Label "Friday's Rout" (Friday's close,
   reported Saturday).
5. **EL CHAPO ISIDRO CAUGHT** (Sinaloa). FBI 10-most-wanted; 11 killed.
6. **UK–EU RESET DEAL SEALED.** Food, carbon, youth mobility.
7. **COP31 DEADLOCKED IN OVERTIME.** Antalya, 2nd day of overtime; fossil-fuel
   language dropped.
8. **PERU QUAKE 6.7** (Junín). Friday 19:09 local = Sat 00:09 GMT; felt in
   Lima; **1 dead, 16 injured** (updated toll — early reports said none).
   Label the Friday-night/Saturday-GMT honesty note.
9. **INDONESIA–EU SIGN TRADE PACT** (Brussels). CEPA + Investment Protection
   Agreement signed Sat 21 Nov (the 18 Nov event was only the authorisation —
   see research file correction). 90.4% of Indonesian tariff lines duty-free
   from day one; in force 2027.
10. **BASRA POWER-STATION FIRE.** Hartha plant; **4 killed, 30 injured**
    (some reports 35 — do not claim more than "30 injured" or say "dozens").
11. **TAIWAN BANS SHORT-SELLING.** TAIEX −17.5% in a week (worst since 1990);
    FSC bans shorting below previous close from Mon 23 Nov; margin 130%→150%.
12. **ENGLAND 37–12 ALL BLACKS.** Record margin (25 pts); five tries;
    first back-to-back wins over NZ since 2003.

**"MORE FROM SATURDAY" one-liners (5, small type):** Bolsonaro in intensive
care (bowel obstruction); Gen Z walkouts in 25 European countries; Denmark
backs US–Greenland security deal 109–0; IAEA: North Korea expanding uranium
enrichment at Yongbyon; Saudi defences down 3 Houthi missiles over Riyadh.

**DO NOT USE:** Verstappen Las Vegas pole, "128 nations robot-arms talks",
Pakistan "15 militants killed", or ANY other claim from the reference image —
all unverified by us. The reference is a competitor's entry, NOT a source.

## 3. THE NEW DESIGN — DENSE NEWSPAPER FRONT PAGE, OUR OWN LOOK
Keep our identity (deep midnight blue, gold accents, DejaVu Serif/Sans).
**Do NOT copy the reference:** no light-paper background, no red banner
headlines, no "35 STORIES · 9 REGIONS" header, no serif masthead that mimics
it, no identical timeline/map/date-check blocks. Build a DIFFERENT layout
that is dense in its own way:

- **Masthead (top):** "WORLD NEWS" large + "SATURDAY, NOVEMBER 21, 2026" +
  a one-line day summary: "Iran hits Bahrain bases · Quake shakes Peru ·
  Wall Street in correction". Keep the gold rule under it.
- **Timeline strip ("THE DAY IN UTC"):** 6 timed events, honest times only:
  00:09 Peru quake (Sat 00:09 GMT; Fri night Lima) · 03:00 Basra fire ·
  ≈07:00 Sparta II struck (shortly before 09:00 local) · 14:10 England
  kick-off (GMT) · afternoon CEPA signing, Brussels · 21:00 Fri Wall St close
  (UTC). Mark Friday events as Friday. Use "≈" where the time is approximate.
- **Hero (Bahrain):** large, spans the width under the timeline, with a
  compact 2-line caption. Keep the Apollo 17 Earth as a SMALL circular visual
  beside the hero headline (not the giant centrepiece of v1 — the page is
  denser now; the Earth must not eat the space the stories need).
- **Story grid (12 cards):** region labels + headline + 1–2 line caption each.
  Hero is story 1; the other 11 in a 3-column grid. Headlines short enough to
  fit; captions ≤ 2 lines. Minimum caption size that stays legible at full
  size — if a caption does not fit, shorten the WORDS, never shrink the font
  below legibility.
- **Map band ("WHERE IT HAPPENED"):** a slim horizontal stylised world map
  (procedural Pillow drawing on the dark background: faint continent shapes
  or a dotted-grid world, gold numbered dots 1–12 at the approximate city
  locations, tiny labels for the numbered dots). Approximate positions are
  fine — it is a locator, not a survey map. If the map looks wrong or cluttered,
  drop it and use the space for the story grid instead; say so in your report.
- **"MORE FROM SATURDAY" ticker:** the 5 one-liners in small type, separated
  by gold dots.
- **Footer — "DATE CHECK" box + sources:** state plainly what was Friday vs
  Saturday (Peru quake: Friday night local, Saturday 00:09 GMT; Wall Street:
  Friday's close; CEPA: authorised Wed 18 Nov, SIGNED Sat 21 Nov) + "Sources:
  AFP · Reuters · AP · CNN · ISW · Focus Taiwan — Editorial illustration,
  November 21, 2026".

## 4. HARD RULES (unchanged — violating any of these kills the entry)
- `main.py` stays the stdlib-only copier (os + shutil). Do NOT touch its
  logic except if the redesign needs a path change — and if you touch it, keep
  it stdlib-only and re-verify determinism. The grader has NO Pillow.
- `render.py` is the Pillow renderer (local use only). `entry.png` committed
  at the repo root. Output 1024×1024 PNG ≤ 1 MiB.
- Determinism: `python3 -P -s main.py` twice → exit 0, byte-identical; plus a
  read-only repo simulation. `test_entry.py` must pass.
- **Visually inspect the render yourself and fix overlaps.** A dense page is
  where overlaps happen: check EVERY card, the timeline, the map labels and
  the footer at full size. No cut-off text anywhere. If 12 stories + extras
  cannot fit legibly at 1024×1024, cut the map band first, then shorten
  captions — never shrink type below legibility and never let text overlap.
- Keep the repo's other files (README badges with the REAL repo name, LICENSE
  with SPDX first line, About/topics) as they are. New commit on main, push it.
- You MAY run a preliminary `makefun check` WITHOUT a bundle to catch repo
  issues early.

## 5. STOP POINT — DO NOT DO THESE (the parent does them after your report)
- Do NOT build the transcript bundle. Do NOT run the final check with a
  bundle. Do NOT submit.
- REPORT BACK with: new commit SHA, rendered image path, verification results
  (render size, determinism hashes, read-only simulation, visual-inspection
  notes), and any deviation (stories dropped, map band dropped, captions
  shortened) with the reason. Never invent a number.
