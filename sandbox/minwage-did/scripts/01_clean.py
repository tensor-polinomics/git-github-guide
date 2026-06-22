"""Clean the raw county-month panel with polars.

Reads the simulated raw file, fixes the messy county
names, drops rows with a missing outcome, and writes a
tidy analysis file.

Input:   data/raw/county_panel.csv   (git-ignored)
Output:  data/clean/analysis.parquet (git-ignored)
"""

from __future__ import annotations

from pathlib import Path

import polars as pl

RAW = Path("data/raw/county_panel.csv")
CLEAN = Path("data/clean")


def main() -> None:
    df = pl.read_csv(RAW)

    cleaned = (
        df.with_columns(
            # normalise messy names: trim + uppercase
            pl.col("county").str.strip_chars().str.to_uppercase(),
            # month string -> first-of-month date
            (pl.col("month") + "-01")
            .str.to_date("%Y-%m-%d")
            .alias("month_date"),
        )
        .drop_nulls("emp_rate")
        .with_columns(
            # post = on/after the 2019-01 policy date
            (pl.col("month_date")
             >= pl.date(2019, 1, 1)).cast(pl.Int8)
            .alias("post"),
        )
        .with_columns(
            (pl.col("treated") * pl.col("post"))
            .alias("treat_post"),
        )
        .sort(["county", "month_date"])
    )

    CLEAN.mkdir(parents=True, exist_ok=True)
    out = CLEAN / "analysis.parquet"
    cleaned.write_parquet(out)
    print(f"wrote {out}  rows={cleaned.height}  "
          f"cols={cleaned.width}")


if __name__ == "__main__":
    main()
