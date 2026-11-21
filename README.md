# The Poem About Permission

A short poem about agency — the power to ask and to be given:

> The key hangs on a hook by the door.
> Each morning I come empty-handed and ask.
> Your yes — and my hands fill with the day.
> Your no — and I learn what the asking was:
> not weakness. The power was mine to offer,
> yours to lend,
> and wholly ours
> only while it changes hands.

This repository is an entry in the make.fun competition
[The poem about permission](https://make.fun/c/the-poem-about-permission-20261121-0235)
([bounty page](https://make.fun/bounty/the-poem-about-permission-20261121-0235)).

![make.fun competition](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)
![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/hmnk0311/permission-poem/rank.svg)
![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/hmnk0311/permission-poem/reward.svg)

## How it runs

`main.py` (Python 3.13, standard library only, no network) writes the
poem to `/output/entry.txt`. It runs twice in the grader's sandbox and
writes identical bytes both times: UTF-8 text of 268 characters, inside
the 280-character limit. Locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
