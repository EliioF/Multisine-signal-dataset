# Limitations and Reuse Notes v1.2.1

## Receiver nonlinearities

The Powercast rectenna uses diode-based RF-to-DC conversion. Therefore, the relation between incident RF power and the recorded receiver-side RSSI/power value may be nonlinear. This nonlinear response is part of the implemented SWIPT receiver chain and is captured by the dataset.

## Lowest-gain readout resolution

At the lowest recorded gain setting, 65% USRP gain corresponding to 20.15 dB, the received power values are closer to the lower part of the receiver dynamic range. In this regime, finite readout resolution, receiver sensitivity limits, and possible floor effects may have a larger relative influence on the recorded values.

A separate quantitative analysis of quantization resolution was not performed because raw ADC outputs, digitizer-level logs, and independent readout-resolution metadata were not stored during the original measurement campaign.

## Environmental variables

Temperature, humidity, and RF interference were not monitored or logged.

## Acquisition session

Measurements were collected during a single experimental session/campaign, but timestamps were not recorded in the released CSV.

## Raw SDR/IQ recordings

Raw SDR/IQ samples were not recorded and are not included.

## Scope of reuse

The dataset is suitable for benchmarking RSSI/power-domain waveform classification and SWIPT receiver response analysis under the reported hardware conditions. It is not intended for studies requiring raw baseband reconstruction, channel estimation from IQ samples, or antenna-independent energy-harvesting efficiency measurements.
