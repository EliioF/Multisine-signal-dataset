# Data Dictionary v1.2.1

This document defines every column in the main CSV file.

## Main CSV file

```text
data/multisine_signals_v1.0.0.csv
```

## Main CSV layout

```text
ID,Gain100_Distance10,Gain100_Distance15,Gain100_Distance20,Gain75_Distance10,Gain75_Distance15,Gain75_Distance20,Gain90_Distance25,Gain90_Distance30,Gain90_Distance35,Gain65_Distance25,Gain65_Distance30,Gain65_Distance35,Indicator
```

No column renaming is required.

## Variable definitions

| variable_name | role | data_type | unit | dataset_group | tx_gain_percent | tx_gain_db | distance_cm | feature_or_target | description |
|---|---|---|---|---|---:|---:|---:|---|---|
| `ID` | sample_identifier | integer | unitless | metadata |  |  |  | metadata | Unique identifier for each repeated experimental sample. |
| `Gain100_Distance10` | receiver_measurement | numeric | mW | A | 100 | 31 | 10 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 100 percent and transmitter-receiver distance 10 cm. |
| `Gain100_Distance15` | receiver_measurement | numeric | mW | A | 100 | 31 | 15 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 100 percent and transmitter-receiver distance 15 cm. |
| `Gain100_Distance20` | receiver_measurement | numeric | mW | A | 100 | 31 | 20 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 100 percent and transmitter-receiver distance 20 cm. |
| `Gain75_Distance10` | receiver_measurement | numeric | mW | A | 75 | 23.25 | 10 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 75 percent and transmitter-receiver distance 10 cm. |
| `Gain75_Distance15` | receiver_measurement | numeric | mW | A | 75 | 23.25 | 15 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 75 percent and transmitter-receiver distance 15 cm. |
| `Gain75_Distance20` | receiver_measurement | numeric | mW | A | 75 | 23.25 | 20 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 75 percent and transmitter-receiver distance 20 cm. |
| `Gain90_Distance25` | receiver_measurement | numeric | mW | B | 90 | 27.9 | 25 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 90 percent and transmitter-receiver distance 25 cm. |
| `Gain90_Distance30` | receiver_measurement | numeric | mW | B | 90 | 27.9 | 30 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 90 percent and transmitter-receiver distance 30 cm. |
| `Gain90_Distance35` | receiver_measurement | numeric | mW | B | 90 | 27.9 | 35 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 90 percent and transmitter-receiver distance 35 cm. |
| `Gain65_Distance25` | receiver_measurement | numeric | mW | B | 65 | 20.15 | 25 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 65 percent and transmitter-receiver distance 25 cm. |
| `Gain65_Distance30` | receiver_measurement | numeric | mW | B | 65 | 20.15 | 30 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 65 percent and transmitter-receiver distance 30 cm. |
| `Gain65_Distance35` | receiver_measurement | numeric | mW | B | 65 | 20.15 | 35 | feature | Receiver-side RSSI/power readout from HyperTerminal for USRP transmitter gain 65 percent and transmitter-receiver distance 35 cm. |
| `Indicator` | class_label | integer | unitless | target |  |  |  | target | Target class label indicating the transmitted multisine waveform tone count. Mapping: 0=N2, 1=N4, 2=N8, 3=N16, 4=N32. |

## Class-label mapping

| Indicator | Class name | Number of tones |
|---:|---|---:|
| 0 | N2 | 2 |
| 1 | N4 | 4 |
| 2 | N8 | 8 |
| 3 | N16 | 16 |
| 4 | N32 | 32 |

## Measurement interpretation

All columns beginning with `Gain` are receiver-side RSSI/power readouts in milliwatts (mW), obtained through the implemented Powercast/HyperTerminal receiver readout chain.

The `Gain` term in the column name is the USRP transmitter gain setting as a percentage. It is not wireless channel gain.

The `Distance` term in the column name is the transmitter-receiver separation distance in centimeters.
