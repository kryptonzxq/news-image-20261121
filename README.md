# World News — November 21, 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/kryptonzxq/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/kryptonzxq/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

An editorial front-page illustration summing up the world news of Saturday,
November 21, 2026, built for the
[make.fun bounty "Sum up 21 November's world news in one image"](https://make.fun/bounty/news-image-20261121).

## The image

The entry is a 1024 × 1024 PNG front page: a midnight-blue masthead, the
Apollo 17 Blue Marble Earth (NASA, public domain), and seven verified stories
from November 21, 2026. The entrypoint `main.py` (Python 3.13, standard
library only) copies the bundled `entry.png` to the output directory — the
grader's image has no third-party packages, so the program renders nothing
at runtime. The image is rendered locally by `render.py` (Pillow) and
committed as `entry.png`; re-running the renderer and re-copying the output
reproduces the same bytes:

- **Lead** — Iran strikes Bahrain in a Gulf escalation (missiles and drones
  hit US bases and a civilian site; fire, no injuries; two tankers also hit
  in the Strait of Hormuz).
- Russian ship Sparta II ablaze after a drone strike in the Gulf of Finland;
  16 crew evacuated.
- Russian missile kills 2 in Zelensky's hometown Kryvyi Rih; 60 wounded.
- Wall Street in correction as the AI sell-off deepens (Friday's rout:
  S&P −3.7%, Dow −950 pts, Nasdaq −5.3%; Nvidia −14%, CEO ousted).
- FBI most-wanted cartel boss "El Chapo Isidro" caught in Sinaloa; 11 killed.
- UK–EU seal a post-Brexit reset deal.
- COP31 deadlocked as climate talks run into overtime in Antalya.

Sources: AFP, Reuters, AP, CNN, ISW. The program runs twice and writes
identical bytes (SHA-256 verified), uses no network, and bundles its fonts
(DejaVu, free) and the Earth photo in `assets/`.

## Run it

```sh
python3 main.py        # copies entry.png to /output/entry.png (or ./output/entry.png)
python3 test_entry.py  # checks size, dimensions and determinism (stdlib only)
python3 render.py      # re-render entry.png locally with Pillow, then copy it to the repo root
```

## License

MIT, see LICENSE. The Earth photo is NASA public domain; fonts are DejaVu
(free license).
