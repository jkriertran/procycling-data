# ProCycling Data

A collection of procycling datasets for analysis, scraped from ProCyclingStats.com. This repository serves as a centralized hub for various datasets and analyses related to professional cycling.

## Contents

- `unibet-2026-historical-analysis/`: Data and assets related to the "Unibet 2026 Season Performance vs. Historical ProTeam Benchmarks" analysis.
- `procycling_data/`: A Python package providing raw Markdown files containing team rosters, season results, and points per rider data for various pro cycling teams across different seasons.

## Python Package

The `procycling_data` package allows for easy access to the raw data files.

### Installation

```bash
pip install procycling_data
```

### Usage

```python
import pkg_resources

def get_data_path(filename):
    return pkg_resources.resource_filename(
        'procycling_data',
        f'data/raw/procycling_proteam_analysis/{filename}'
    )

# Example: Get path to a roster file
roster_file = get_data_path('wt_rosters_md/ag2r-citroen-team-2022.md')
print(f"Path to roster file: {roster_file}")

# You can then read and parse this Markdown file as needed.
```

## Unibet 2026 Historical Analysis

This directory contains the specific data and assets for the Unibet 2026 season performance analysis.

- `docs/`: Blog post content, charts, and other supporting documentation.
- `data/`: Raw and processed data files, including Excel workbooks and CSVs.
- `README.md`: A detailed explanation of the dataset, methodology, and contents specific to that analysis.

## License

MIT License
