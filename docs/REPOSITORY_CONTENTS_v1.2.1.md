# Repository Contents v1.2.1

| Path | Category | Format | Purpose |
|---|---|---|---|
| `data/multisine_signals_v1.0.0.csv` | main data | CSV | Authoritative wide-format RSSI/power measurements and class labels. |
| `data/README_DATA.md` | documentation | Markdown | Explains the data directory and main dataset file. |
| `metadata/DATA_DICTIONARY_v1.2.1.csv` | metadata | CSV | Machine-readable variable definitions. |
| `docs/DATA_DICTIONARY_v1.2.1.md` | documentation | Markdown | Human-readable variable definitions. |
| `metadata/DATASET_PARTITIONING_v1.2.1.csv` | metadata | CSV | Machine-readable Dataset A/B partitioning. |
| `docs/DATASET_PARTITIONING_v1.2.1.md` | documentation | Markdown | Human-readable Dataset A/B partitioning. |
| `docs/METADATA_AND_PROVENANCE_v1.2.1.md` | documentation | Markdown | Hardware setup, software, session information, environment monitoring, provenance, and limitations. |
| `docs/REPRODUCIBILITY_GUIDE_v1.2.1.md` | documentation | Markdown | How to validate the dataset and reproduce baseline ML workflows. |
| `docs/REPOSITORY_CONTENTS_v1.2.1.md` | documentation | Markdown | Repository file list with purpose and format. |
| `docs/LIMITATIONS_AND_REUSE_NOTES_v1.2.1.md` | documentation | Markdown | Known limitations and recommended reuse context. |
| `schema/JSON_Schema.json` | schema | JSON | Expected column names, data types, and valid labels. |
| `src/check_dataset_integrity.py` | code | Python | Checks expected columns, labels, missingness, duplicate IDs, class balance, and summary statistics. |
| `src/reproduce_baselines.py` | code | Python | Baseline ML workflow with Dataset A/B partitioning. |
| `figures/workflow_diagram_tikz.tex` | figure source | LaTeX/TikZ | Workflow diagram source. |
| `results/dataset_validation_summary.json` | validation output | JSON | Validation summary generated from the submitted CSV. |
| `results/class_balance.csv` | validation output | CSV | Class counts for Indicator values. |
| `results/missing_values_summary.csv` | validation output | CSV | Missing-value counts per expected column. |
| `results/measurement_summary_statistics.csv` | validation output | CSV | Descriptive statistics, standard error, CI half-width, and coefficient of variation for measurement columns. |
| `requirements.txt` | software | Text | Python package requirements. |
| `LICENSE` | license | Text | Open data license notice. |
| `CITATION.cff` | citation | CFF | Citation metadata. |
| `README.md` | documentation | Markdown | Repository overview. |
| `CHANGELOG.md` | documentation | Markdown | Version history. |
