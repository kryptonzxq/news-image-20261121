# MASTER PROMPT — news-image-20261121: "World News — November 21, 2026"

You are an elite editorial art director AND the build agent for a make.fun bounty
entry. Your job: build a deterministic program that renders ONE front-page image
summing up Saturday 21 November 2026's world news, verify it end to end, and
prepare it for submission. **You do NOT submit. You show the finished image and
wait for Eri's approval first.**

## 1. THE BOUNTY (verified from the requirements + competition API, 2026-11-22)
- Slug: `news-image-20261121` — "Sum up 21 November's world news in one image"
- Status: open. Harness: **program/v1 — transcript BUNDLE upload** (NOT sealed recordings).
- **Reward: $100 total, 50 places** — 1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20.
  (Down from $250 on the 19 and 20 Nov bounties. Be honest about the odds.)
- **Deadline: Monday 2026-11-23 07:00 WIB** (2026-11-23T00:00:00Z). Opened 2026-11-21T00:00:00Z.
- **18,910 submissions already.** No promise of placing — build the best image you can.
- Deliverable: public GitHub repo (own account, created AFTER the opening) under an
  OSI license, with `main.py` (Python 3.13) or `main.ts` (Node 22) at root, writing
  `/output/entry.png`. Image: PNG/JPEG ≤ 1 MiB, ≤ 1024×1024. No network at runtime.
  Two runs must write identical bytes. Max 10 submissions/day, 20 total; last is final.
- Judging: an AI judge WITH NO NEWS FEED compares images pairwise — the image itself
  must communicate the news. The 50 highest-ranked share $100.

## 2. THE NEWS — 7 VERIFIED STORIES (full research: research-21-nov.md in this dir)
Read `research-21-nov.md` first. It holds the verified facts, sources and date
caveats. Summary — 1 hero + 6 cards:

- **LEAD (hero): IRAN STRIKES BAHRAIN.** Sat 21 Nov, IRGC missile-and-drone attack
  on US military positions in Bahrain (Al-Riffa/Awali; Fars: Sheikh Isa + Juffair,
  home of the US Navy Fifth Fleet). A civilian industrial facility hit, fire,
  NO injuries; Bahrain air defences intercepted several attacks; smoke over
  Sitra Island. Two tankers also hit in the Strait of Hormuz the same day.
  Do NOT pick a side on what caused the fire (IRNA claims a US interceptor came
  down) — write "Bahrain says Iranian attack hit a civilian site".
- **Card 1: WAR SPILLS INTO THE BALTIC.** Ukrainian drones (Finland: likely
  Ukraine) hit the Russian military cargo ship Sparta II in the Gulf of Finland;
  ship ablaze, 16 crew evacuated, drifted into Finnish waters. PM Orpo:
  "The war is spilling over."
- **Card 2: MISSILE KILLS 2 IN ZELENSKY'S HOMETOWN.** Russian ballistic missile
  hit Kryvyi Rih overnight: a 7-year-old boy and a 20-year-old paramedic killed,
  60 wounded incl. 6 children. (Russia launched 3 ballistic missiles + 148 drones.)
- **Card 3: WALL STREET IN CORRECTION.** AI sell-off — S&P 500 −3.7% to 6,910,
  Dow −950 pts, Nasdaq −5.3%; S&P + Dow now >10% below peaks. Nvidia −14%
  (SEC probe; CEO ousted). **Date honesty: this was Friday 20 Nov's close,
  confirmed/reported Saturday 21 Nov — the image must say "Friday's rout".**
- **Card 4: CARTEL KINGPIN CAUGHT.** Mexico arrested FBI 10-most-wanted Fausto
  Isidro Meza Flores ("El Chapo Isidro") in Sinaloa; 11 killed in the violence.
- **Card 5: UK–EU RESET DEAL SEALED.** Post-Brexit reset: food, carbon, youth
  mobility deals.
- **Card 6: COP31 DEADLOCKED IN OVERTIME.** Antalya talks in a 2nd day of
  overtime; fossil-fuel language dropped from the draft.

**Date traps — NEVER use these (wrong date or already covered):** the Trump–Xi–Putin
trilateral summit (19 Nov, was the 20261119 lead); the Houthi PIF Tower hit
(19 Nov night); Anthropic IPO day 1/2 (19/20 Nov); EU–Indonesia CEPA (18 Nov);
Russia's big Kyiv attack (overnight 19–20 Nov); Cyclone Akvan (20 Nov).
Backups in research-21-nov.md if a main story fails its date check: Bolsonaro ICU,
Riemann-hypothesis claim (phrase as a CLAIM), Gen Z walkouts in 25 countries,
Peru earthquake, Denmark backs US–Greenland deal 109–0, IAEA/North Korea Yongbyon.

## 3. THE BUILD — REUSE THE PROVEN TEMPLATE (do not start from zero)
Base = the 20261120 project at `~/workspace/news-image-20261120/` (same front-page
template as 20261119, already fixed for the grader). Copy its structure into a new
project dir `~/workspace/news-image-20261121/`:
- `render.py` — the Pillow renderer (LOCAL USE ONLY; it renders entry.png).
- `entry.png` — the rendered 1024×1024 PNG, committed at the repo root.
- `assets/` — DejaVu Serif/Sans fonts + the Apollo 17 Earth photo (earth_800.jpg).
- `main.py` — **STDLIB ONLY (os + shutil). It COPIES entry.png to
  $MAKEFUN_OUTPUT_DIR/entry.png (fall back to /output, then ./output) and asserts
  the copy is complete (size equal). NO Pillow import, NO third-party import.**
- `test_entry.py` — stdlib-only test: two runs byte-identical.

### HARD LESSON (applies to ALL news-image bounties — learned the expensive way)
The grader's pinned Python image has NO Pillow. A main.py that imports PIL exits
with code 1 and the entry is REJECTED on run_completes. This killed the 20261119
entry (deadline passed, unfixable) and the first 20261120 entry (fixed + resubmitted).
**Never again: main.py is a stdlib-only copier. The Pillow renderer lives in
render.py and is used only locally. The rendered PNG is committed as entry.png.**

### Design (keep the winning template)
- Deep midnight blue, gold accents, DejaVu Serif headlines / DejaVu Sans body.
- Apollo 17 Blue Marble Earth, circular-masked, as the centre visual.
- Hero story (Bahrain) large at top with a bold headline + 2-line caption.
- 6 story cards with region labels (MIDDLE EAST / EUROPE / MARKETS / AMERICAS /
  EUROPE / CLIMATE), short headline + 1–2 line caption each. Every number on the
  image must match research-21-nov.md exactly (2 killed, 60 wounded, −3.7%,
  16 crew, 11 killed, $88.91 is NOT used — it belongs to the 20 Nov story).
- Footer: "Sources: AFP · Reuters · AP · CNN · ISW" + date "SATURDAY 21 NOVEMBER 2026".
- Output: 1024×1024 PNG, ≤ 1 MiB. Text must be legible at full size and at
  thumbnail size — short headlines, no tiny body text, no overlapping text.
  (The 20261120 build needed a layout fix for a hero-caption overlap — inspect
  your render visually and fix overlaps before calling it done.)

## 4. VERIFICATION (all must pass before you report done)
1. `render.py` runs locally; output 1024×1024 PNG ≤ 1 MiB.
2. `python3 -P -s main.py` exits 0 (twice, byte-identical output) AND a read-only
   repo simulation passes (copy repo to a temp dir, chmod read-only, run with
   MAKEFUN_OUTPUT_DIR set to an empty dir, exit 0, identical bytes).
3. Visually inspect the rendered image yourself (open it and look): no overlap,
   no cut-off text, hero readable, all 7 stories present and correctly dated.
4. Repo hygiene: `main.py` imports ONLY os + shutil (grep to prove it).

## 5. REPO + KIT + BUNDLE + CHECK
- Download a FRESH kit for this bounty (the site is at level 36; the 20261120 kit
  was level 32 — do not reuse an old kit): from the dir that will hold it,
  `curl -sSL "https://make.fun/c/news-image-20261121/kit" | tar xz`.
- Create the GitHub repo `kryptonzxq/news-image-20261121` (PUBLIC, created after
  the 2026-11-21T00:00:00Z opening — creating it now is fine). Default branch
  main. Set About: description + homepage = the bounty page
  https://make.fun/bounty/news-image-20261121 + topics incl. `makefun`.
- README.md with the THREE LIVE make.fun badges using the REAL repo name
  `kryptonzxq/news-image-20261121` (never the local dir name — that mismatch
  caused a refused submit on the spot-the-difference bounty). MIT LICENSE with
  `SPDX-License-Identifier: MIT` as the first line.
- Commit + push. Then build the transcript bundle with the kit CLI
  (`node cli/makefun.mjs bundle ...`), including every session that worked on
  this entry (yours + any subagent you spawn). Usage rows for Muse-app sessions
  come from the `muse.db` token-usage table — one JSON object per line, valid
  JSONL (never let two rows land on one line).
- Run the official `makefun check` on the commit + bundle. **Target: 14 passed,
  0 failed.** If `thinking_revised` fails (entrypoint content from <2 messages),
  make a second, real revision to main.py and re-check.

## 6. WHAT YOU DELIVER (and what you do NOT do)
- Deliver: the repo URL + commit, the rendered image (shown for inspection),
  the check result, and a one-line summary of the 7 stories as rendered.
- **DO NOT SUBMIT.** Submitting is Eri's call after he sees the final image.
  When he approves, the submit uses the kit CLI with the bundle; a refused
  submit (HTTP 422) is a fixable pre-submit failure, never a quota loss.
- Never claim a price, a market, or a placement. Never invent a number.
- If any story's date does not check out during your build, replace it with a
  backup from research-21-nov.md and say so plainly in your report.
