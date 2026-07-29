# Metadata and Provenance v1.2.1

## Dataset summary

This dataset contains receiver-side RSSI/power readouts in mW collected from a point-to-point SWIPT experiment using multisine RF waveforms. Information is encoded in the number of tones in the multisine waveform.

## Hardware

| Component | Model / description |
|---|---|
| Transmitter | National Instruments USRP 2920 |
| Transmit antenna | DA-915-01 dipole antenna |
| Receiver / RF energy harvester | Powercast P21XXCSR |
| Wireless sensor board | Powercast WSN-EVAL-01 |
| Access point / interface | Microchip XLP PIC24F |
| Signal-generation software | NI LabVIEW |
| Measurement readout | HyperTerminal |

## Software and operating environment

| Component | Version / status |
|---|---|
| Operating system | Windows 11 |
| Signal generation | NI LabVIEW 19 |
| NI-USRP driver | Version not recorded |
| Analysis language | Python 3.12 |
| Terminal/readout software | HyperTerminal |

## RF and waveform parameters

| Parameter | Value |
|---|---|
| Operating frequency | 915 MHz |
| Bandwidth | 200 kHz |
| Number of tones | 2, 4, 8, 16, 32 |
| Transmit-gain settings | 100%, 90%, 75%, 65% |
| Nominal gain values | 31 dB, 27.9 dB, 23.25 dB, 20.15 dB |
| Distances | 10 cm, 15 cm, 20 cm, 25 cm, 30 cm, 35 cm |

## Acquisition session

The measurements were collected during a single experimental session/campaign. The full acquisition process required time to complete because all tone-count, gain, and distance conditions were measured systematically. The dataset does not include timestamps or session identifiers, so within-session temporal effects cannot be analyzed from the released CSV.

## Environmental monitoring

Temperature, humidity, and RF interference were not continuously monitored or logged during data collection. The measurements were collected in a controlled laboratory setting, but the dataset does not include environmental sensor metadata or ambient RF spectrum measurements.

## Receiver-chain interpretation

The reported values are receiver-side RSSI/power readouts from the complete implemented receiver chain. They should not be interpreted as independently calibrated incident RF power at the antenna input. The diode-based rectenna and readout chain may introduce nonlinear behavior, especially at low received-power levels.

## Raw SDR/IQ data

Raw SDR/IQ recordings were not acquired during the measurement campaign and are not included in this release. The dataset focuses on the receiver-side RSSI/power response of the implemented energy-harvesting receiver chain.

## Provenance chain

```text
Multisine parameter selection
    -> LabVIEW waveform generation
    -> USRP 2920 RF transmission at 915 MHz
    -> DA-915-01 dipole antenna radiation
    -> Powercast P21XXCSR RF harvesting receiver
    -> WSN-EVAL-01 / Microchip XLP PIC24F readout chain
    -> HyperTerminal RSSI/power readout in mW
    -> CSV logging
    -> annotation by gain, distance, and tone class
    -> Dataset A/B partitioning
    -> quality checks
    -> final FAIR² data package
```
