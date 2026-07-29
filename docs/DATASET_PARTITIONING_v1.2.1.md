# Dataset Partitioning v1.2.1

This file defines the condition-based partitioning of the dataset.

The partitioning is based on transmitter gain and transmitter-receiver distance. It is not a purely random split.

## Target variable

`Indicator` is the class label and must not be used as an input feature.

| Indicator | Class name | Number of tones |
|---:|---|---:|
| 0 | N2 | 2 |
| 1 | N4 | 4 |
| 2 | N8 | 8 |
| 3 | N16 | 16 |
| 4 | N32 | 32 |

## Dataset A: model-development group

Dataset A is used for training, validation, and internal testing.

| variable_name | tx_gain_percent | tx_gain_db | distance_cm | unit |
|---|---:|---:|---:|---|
| `Gain100_Distance10` | 100 | 31 | 10 | mW |
| `Gain100_Distance15` | 100 | 31 | 15 | mW |
| `Gain100_Distance20` | 100 | 31 | 20 | mW |
| `Gain75_Distance10` | 75 | 23.25 | 10 | mW |
| `Gain75_Distance15` | 75 | 23.25 | 15 | mW |
| `Gain75_Distance20` | 75 | 23.25 | 20 | mW |

## Dataset B: external-test group

Dataset B is reserved for external testing and generalization assessment. It should not be used for training, scaler fitting, hyperparameter tuning, cross-validation, or model selection.

| variable_name | tx_gain_percent | tx_gain_db | distance_cm | unit |
|---|---:|---:|---:|---|
| `Gain90_Distance25` | 90 | 27.9 | 25 | mW |
| `Gain90_Distance30` | 90 | 27.9 | 30 | mW |
| `Gain90_Distance35` | 90 | 27.9 | 35 | mW |
| `Gain65_Distance25` | 65 | 20.15 | 25 | mW |
| `Gain65_Distance30` | 65 | 20.15 | 30 | mW |
| `Gain65_Distance35` | 65 | 20.15 | 35 | mW |

## Recommended Python feature groups

```python
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
```
