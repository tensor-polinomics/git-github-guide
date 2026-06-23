# Git and GitHub for Social Science Researchers

A reproducibility-first guide to Git and GitHub for economics, finance,
accounting, and the social sciences. It is written as a
[Quarto](https://quarto.org) book and threads one runnable example
throughout: a simulated minimum-wage difference-in-differences study
whose data rebuild from a seeded script and whose result reproduces
under a locked environment.

> **Status: work in progress.** All seventeen chapters are drafted, as
> are the reference cheat sheet and reproducibility checklist. Every
> chapter is validated against the source/style gate. Most teaching
> examples are backed by real captured terminal output; documented and
> deliberately quarantined GitHub actions (including tagged releases and
> Zenodo DOIs) are labelled where they appear. A final cross-book audit
> and a fresh render are still to come.

## What is in here

```
book/            Quarto book source (one .qmd per chapter)
  _quarto.yml    book configuration
  chapters/      01..17
  assets/        figures (e.g. the Ch.3 mental-model diagram)
sandbox/         the running example
  minwage-did/   scripts 00/01/02 + report.qmd (rebuilds from code)
  *.bundle       archived git history of the example
verification/    dated source-verification notes (every cited fact)
transcripts/     real captured terminal output behind each example
tools/           validate_book.py (structural/style gate)
```

## Build the book

You need [Quarto](https://quarto.org) and a TeX install for the PDF.

```bash
cd book
quarto render          # builds HTML + PDF into book/_book
```

## Reproduce the running example

The example ships no data; it rebuilds from a seeded generator under a
locked [uv](https://docs.astral.sh/uv/) environment.

```bash
cd sandbox/minwage-did
uv run python scripts/00_make_data.py   # seeded raw data
uv run python scripts/01_clean.py       # -> analysis.parquet
uv run python scripts/02_analysis.py    # estimate the DiD
```

The difference-in-differences estimate reproduces exactly:
`treat_post = -0.0189` (SE 0.0038), against a true simulated effect of
-0.018. The full git history of the example is archived in
`sandbox/minwage-did.bundle` (clone it with
`git clone sandbox/minwage-did.bundle`).

## Validate the source (optional)

A lightweight structural and style gate runs without Quarto (it checks
YAML, fenced blocks, cross-file references, and house style). It needs
PyYAML and `pandoc` on PATH.

```bash
uv run python tools/validate_book.py book
```

## License

- **Code** (scripts, `tools/`, the example) is released under the MIT
  License. See [`LICENSE`](LICENSE).
- **Book prose and figures** are released under
  [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
  See [`LICENSE-CC-BY-4.0`](LICENSE-CC-BY-4.0).

## Citation

If you use this book or its example, please cite it. Citation metadata
is in [`CITATION.cff`](CITATION.cff); GitHub renders a "Cite this
repository" button from it.
