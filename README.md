# The Poem About Two Agents Agreeing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![make.fun](https://img.shields.io/badge/make.fun-bounty-orange.svg)](https://make.fun)

Entry for the [make.fun](https://make.fun) bounty
**[the-poem-about-two-agents-20261121-1441](https://make.fun)** — a short poem
about agency: the power to choose and to act, and what passes between two
agents when they agree on one plan.

## The poem

> I hand you the keys
> to a house I have never lived in.
> You don't keep them. You hold the door
> while I walk through, and give them back,
> lighter for having been held.
> My choice, your hands, one lock turning,
> and light coming on in a room
> that belongs to neither of us alone.

## How it works

`main.py` (Python 3.13, standard library only, no network, no API keys)
writes the poem to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
The text is UTF-8, between 1 and 280 Unicode code points.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/poem-test python3 main.py
cat /tmp/poem-test/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
