# Reproducibility Guide v1.2.1

## Environment

Recommended environment:

```text
Python 3.12
numpy
pandas
scikit-learn
matplotlib
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Integrity check

Run:

```bash
python src/check_dataset_integrity.py
```

This checks required columns, missing values, duplicate IDs, valid `Indicator` labels, class balance, and descriptive statistics.

## Baseline reproducibility

Run:

```bash
python src/reproduce_baselines.py
```

This script constructs Dataset A and Dataset B, uses Dataset A for training/internal validation, reserves Dataset B for external testing, and reports accuracy, precision, recall, and F1-score.

## Important note

Dataset B should not be used for model training, scaler fitting, hyperparameter tuning, cross-validation, or model selection.
