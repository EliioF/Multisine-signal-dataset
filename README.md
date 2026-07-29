# Multisine SWIPT RSSI/Power Dataset

This repository contains the FAIR²/Clara submission package for the dataset associated with:

**Multisine Signal Tone and Power Harvesting Measurements across Gain and Distance Settings**

The dataset contains receiver-side RSSI/power readouts in milliwatts (mW) collected from a software-defined-radio-based simultaneous wireless information and power transfer (SWIPT) testbed. Multisine waveforms with different tone counts are transmitted using an NI USRP 2920, and the receiver-side readout is obtained from a Powercast-based RF energy harvesting receiver chain.

## Main data file

```text
data/multisine_signals_v1.0.0.csv
```

The main CSV contains 750 rows and 14 columns: one sample identifier, 12 RSSI/power measurement columns, and one target label column.

## Expected columns

```text
ID,
Gain100_Distance10,
Gain100_Distance15,
Gain100_Distance20,
Gain75_Distance10,
Gain75_Distance15,
Gain75_Distance20,
Gain90_Distance25,
Gain90_Distance30,
Gain90_Distance35,
Gain65_Distance25,
Gain65_Distance30,
Gain65_Distance35,
Indicator
```

## Dataset groups

Dataset A is used for model development: training, validation, and internal testing.

Dataset B is reserved for external testing and generalization assessment.

The partitioning is condition-based, using transmitter gain and transmitter-receiver distance.

## Repository structure

```text
data/       Main dataset CSV and data notes
docs/       Human-readable documentation
metadata/   Machine-readable metadata tables
schema/     JSON schema
src/        Reproducibility and integrity-check scripts
figures/    Workflow diagram TikZ source
results/    Validation outputs generated from the submitted CSV
```

## License

The dataset is released under the Open Data Commons Attribution License (ODC-By v1.0). Reuse requires appropriate attribution.

## Citation

See `CITATION.cff`.
