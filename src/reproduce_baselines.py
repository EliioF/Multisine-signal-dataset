from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

DATA_PATH = Path("data/multisine_signals_v1.0.0.csv")
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

dataset_A_columns = [
    "Gain100_Distance10",
    "Gain100_Distance15",
    "Gain100_Distance20",
    "Gain75_Distance10",
    "Gain75_Distance15",
    "Gain75_Distance20",
]

dataset_B_columns = [
    "Gain90_Distance25",
    "Gain90_Distance30",
    "Gain90_Distance35",
    "Gain65_Distance25",
    "Gain65_Distance30",
    "Gain65_Distance35",
]

target_column = "Indicator"
RANDOM_STATE = 1

df = pd.read_csv(DATA_PATH)

X_A = df[dataset_A_columns]
X_B = df[dataset_B_columns]
y = df[target_column].astype(int)

X_train, X_val, y_train, y_val = train_test_split(
    X_A, y, test_size=0.30, random_state=RANDOM_STATE, stratify=y
)

models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=RANDOM_STATE),
    "svm_linear": SVC(kernel="linear", C=1, random_state=RANDOM_STATE),
    "svm_rbf": SVC(kernel="rbf", C=25, gamma=0.2, random_state=RANDOM_STATE),
}

rows = []

for model_name, model in models.items():
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", model),
    ])
    pipe.fit(X_train, y_train)

    for split_name, X_eval, y_eval in [
        ("dataset_A_validation", X_val, y_val),
        ("dataset_B_external", X_B, y),
    ]:
        pred = pipe.predict(X_eval)
        rows.append({
            "model": model_name,
            "split": split_name,
            "accuracy": accuracy_score(y_eval, pred),
            "weighted_precision": precision_score(y_eval, pred, average="weighted", zero_division=0),
            "weighted_recall": recall_score(y_eval, pred, average="weighted", zero_division=0),
            "weighted_f1": f1_score(y_eval, pred, average="weighted", zero_division=0),
        })

metrics = pd.DataFrame(rows)
metrics.to_csv(RESULTS_DIR / "baseline_metrics.csv", index=False)
print(metrics)
