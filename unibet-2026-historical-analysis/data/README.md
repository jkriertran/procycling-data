# Unibet historical blog analysis dataset package

This folder contains the source tables and joined exports used to build the Unibet 2026 historical blog analysis.

## What is included

| File | Purpose |
|---|---|
| `unibet_blog_analysis_dataset.xlsx` | Main workbook with raw and joined sheets for the article |
| `benchmark_panel.csv` | Same-date early-April benchmark panel used for the historical comparison section |
| `peer_team_summary.csv` | Current peer-team comparison table for Cofidis, Q36.5, Tudor, and Unibet |
| `rider_team_joined.csv` | Rider-level table joined to team context for the peer set |
| `role_counts_joined.csv` | Current peer-team operational role counts joined to team context |
| `historical_role_benchmark.csv` | Historical role-share benchmark by rank bucket |
| `raw_source_tables/` | Exact raw CSV inputs copied from the analysis folder |

## Notes

The data pull used in the article reflects the 07 April 2026 snapshot for Unibet and matched early-April checkpoints for the historical comparison seasons.

The workbook includes a `source_index` sheet that maps each joined sheet to the part of the article or chart pack where it was used.
