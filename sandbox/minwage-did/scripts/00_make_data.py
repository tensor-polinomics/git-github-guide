"""Generate a synthetic county-month panel for the
minimum-wage difference-in-differences example.

All data in this project are SIMULATED. Nothing here is
real CRSP, Compustat, or survey microdata. The point of
generating data from a seeded script is that the raw data
never needs to live in Git: anyone can rebuild it from
this file. See Chapters 6 and 8.

Output:
  data/raw/county_panel.csv  (git-ignored)
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20260621
RAW = Path("data/raw")


def main() -> None:
    rng = np.random.default_rng(SEED)

    n_counties = 40
    months = pd.period_range("2018-01", "2019-12", freq="M")
    treated_ids = set(range(0, n_counties, 2))  # even = treated
    policy_month = pd.Period("2019-01", freq="M")
    true_effect = -0.018  # 1.8% drop in teen employment

    rows = []
    for cid in range(n_counties):
        county_fe = rng.normal(0, 0.05)
        treated = cid in treated_ids
        # messy on purpose: vary the name casing + spacing
        name = f"County_{cid:02d}"
        if cid % 3 == 0:
            name = name.upper()
        if cid % 5 == 0:
            name = "  " + name + " "
        for m in months:
            month_fe = rng.normal(0, 0.02)
            post = m >= policy_month
            effect = true_effect if (treated and post) else 0.0
            noise = rng.normal(0, 0.03)
            emp = 0.45 + county_fe + month_fe + effect + noise
            rows.append(
                {
                    "county": name,
                    "month": str(m),
                    "treated": int(treated),
                    "emp_rate": round(emp, 4),
                }
            )

    df = pd.DataFrame(rows)

    # inject realistic messiness: a few missing outcomes
    miss = rng.choice(len(df), size=12, replace=False)
    df.loc[miss, "emp_rate"] = np.nan

    RAW.mkdir(parents=True, exist_ok=True)
    out = RAW / "county_panel.csv"
    df.to_csv(out, index=False)
    print(f"wrote {out}  rows={len(df)}  "
          f"counties={n_counties}  months={len(months)}")


if __name__ == "__main__":
    main()
