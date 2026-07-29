from pathlib import Path
import pandas as pd
import numpy as np

DATA_PATH = Path("data/multisine_signals_v1.0.0.csv")
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

EXPECTED_COLUMNS = [
    "ID",
    "Gain100_Distance10",
    "Gain100_Distance15",
    "Gain100_Distance20",
    "Gain75_Distance10",
    "Gain75_Distance15",
    "Gain75_Distance20",
    "Gain90_Distance25",
    "Gain90_Distance30",
    "Gain90_Distance35",
    "Gain65_Distance25",
    "Gain65_Distance30",
    "Gain65_Distance35",
    "Indicator",
]

df = pd.read_csv(DATA_PATH)

missing_columns = [c for c in EXPECTED_COLUMNS if c not in df.columns]
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

if df["ID"].duplicated().any():
    raise ValueError("Duplicate IDs found.")

allowed_labels = {0, 1, 2, 3, 4}
labels = set(df["Indicator"].dropna().astype(int).unique())
if not labels.issubset(allowed_labels):
    raise ValueError(f"Unexpected Indicator labels: {labels - allowed_labels}")

df[EXPECTED_COLUMNS].isna().sum().rename("missing_values").to_csv(RESULTS_DIR / "missing_values_summary.csv")
df["Indicator"].value_counts().sort_index().rename("count").to_csv(RESULTS_DIR / "class_balance.csv")

measurement_columns = [c for c in EXPECTED_COLUMNS if c.startswith("Gain")]
summary = df[measurement_columns].describe().T
summary["se"] = summary["std"] / np.sqrt(summary["count"])
summary["ci95_half_width"] = 1.96 * summary["se"]
summary["cv"] = summary["std"] / summary["mean"]
summary.to_csv(RESULTS_DIR / "measurement_summary_statistics.csv")

print("Dataset integrity checks complete.")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("Class balance:")
print(df["Indicator"].value_counts().sort_index())
