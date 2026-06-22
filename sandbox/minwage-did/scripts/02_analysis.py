"""Two-way fixed-effects difference-in-differences.

Estimates the effect of the minimum-wage increase on the
teen employment rate, with county and month fixed effects
and standard errors clustered by county.

  emp_rate = b * treat_post + a_county + g_month + e

Input:   data/clean/analysis.parquet (git-ignored)
Outputs: output/tables/did_main.txt
         output/figures/event_means.png
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pyfixest as pf
import polars as pl

CLEAN = Path("data/clean/analysis.parquet")
TAB = Path("output/tables")
FIG = Path("output/figures")


def main() -> None:
    df = pl.read_parquet(CLEAN).to_pandas()

    fit = pf.feols(
        "emp_rate ~ treat_post | county + month",
        data=df,
        vcov={"CRV1": "county"},
    )

    TAB.mkdir(parents=True, exist_ok=True)
    summary = fit.tidy().round(4).to_string()
    (TAB / "did_main.txt").write_text(summary + "\n")
    print(summary)

    # group means by treatment status over time
    g = (
        pl.read_parquet(CLEAN)
        .group_by(["month_date", "treated"])
        .agg(pl.col("emp_rate").mean())
        .sort("month_date")
    )
    FIG.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 4))
    for t, label in [(1, "Treated"), (0, "Control")]:
        sub = g.filter(pl.col("treated") == t)
        ax.plot(sub["month_date"], sub["emp_rate"],
                marker="o", ms=3, label=label)
    ax.axvline(x=__import__("datetime").date(2019, 1, 1),
               color="grey", ls="--", lw=1)
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean teen employment rate")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG / "event_means.png", dpi=120)
    print(f"\nwrote {TAB/'did_main.txt'} and "
          f"{FIG/'event_means.png'}")


if __name__ == "__main__":
    main()
