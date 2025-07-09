# Multisine-signal-dataset
This repository contains the dataset for implementing simultaneous wireless information and power transfer (SWIPT) using multisine signals.

The data were obtained as follows:

A National Instruments Universal Software Radio Peripheral (NI USRP) 2920 device is used as a signal generator, and the Powercast P21XXCSR module is used as the energy harvester.

The proposed SWIPT design considers that the information is encoded by varying the number of tones in the multisine signals, while having the receiver simultaneously harvest energy. More specifically, for each multisine signal, several samples of the harvested power are collected across a set of distances and transmit power levels to expand and diversify the dataset. Each configuration contributes to the formation of features that are subsequently used to train the machine learning model on the generated data.

For the experimental measurements, we consider multisine signals with a number of tones $N \in \left\lbrace 2,4,8,16,32 \right\rbrace$. The USRP gain setting is $G \in \left\lbrace 31,27.9,23.25,20.15 \right\rbrace$ dB, and the transmitter-receiver distance is $d \in \left\lbrace 10,15,20,25,30,35 \right\rbrace$ cm. A fixed operating frequency of 915 MHz is considered.

For more details, please refer to the research paper available at: https://ieeexplore.ieee.org/document/11062143.
