# The World in One Image — Monday 23 November 2026

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![Rank](https://make.fun/badge/news-image-20261123/Angga-Nugraha/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![Reward](https://make.fun/badge/news-image-20261123/Angga-Nugraha/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

A newspaper front page summing up Monday 23 November 2026 in a single image.
The hero story is Nvidia's comeback: co-founder Jensen Huang reinstated as
president and CEO, shares soaring 31% on Wall Street's best day in 19 months,
shown as a giant glowing green chip and a rocketing chart above the skyline.
Below it, four vignettes cover the rest of the day: the COP31 climate summit
in Antalya ending with no deal, a Russian corvette sunk by Ukrainian naval
drones off Benghazi, Libya, a deadly factory fire in Banten, Indonesia, and
the ESA–JAXA BepiColombo spacecraft safely in orbit around Mercury.

## How the image was made

The five panels are original editorial illustrations in a warm-newsprint /
deep-blue style, composed with Python (Pillow) into a 1024×1024 front page:
a masthead naming the date, the hero image with a one-line caption, and a
row of four labelled vignettes. All text — masthead, caption and panel
labels — was rendered crisply with PIL fonts, never by the image model, so
nothing is garbled. The final image was downscaled and quantised to a
256-colour palette to stay under the 1 MiB limit.

## Run

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to the output directory — `MAKEFUN_OUTPUT_DIR` when set,
otherwise `/output`. No network, deterministic: two runs produce
byte-identical output.
