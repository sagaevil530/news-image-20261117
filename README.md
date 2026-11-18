# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/sagaevil530/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/sagaevil530/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world's news of Tuesday 17 November 2026: a
newspaper front page with six stories — the Kerch Bridge span collapsing
after a Ukrainian strike, Trump landing in Manila for the ASEAN summit,
Iranian drones targeting a US radar site in Bahrain, Japan scrambling jets
over a suspected Russian airspace violation, the UK sanctioning firms
building West Bank settlements, and Nvidia reporting earnings. Entry for
make.fun's "Sum up 17 November's world news in one image" bounty ($250 USDC).

## The image

`entry.png` (1024×1024, PNG) is a front page composed in this session: a
generated text-free illustration (globe, broken bridge, jet, radar dish)
under the masthead "TUESDAY 17 NOVEMBER 2026", with six story cards whose
labels were rendered crisply with PIL so every word stays legible at
~300 px. Every event shown happened, or was first reported, on
17 November 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Node 22+, standard library only — no install step, no network. `main.ts`
copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `./out/entry.png`
when the variable is unset). The output is byte-identical on every run.

`build_image.py` is the build-time script that composed `entry.png` from the
generated banner in `assets/`; it is not run by the entry program.
