# emotiv-matlab
**Acquiring raw EEG signals from Emotiv EPOC+ in MATLAB**

The python script routes the raw EEG signals of all channels acquired from Emotiv EPOC+ headset to MATLAB using a TCP/IP connection.

The script is based on [Emokit](https://github.com/openyou/emokit) by The OpenYou Organization.

## Installation
Add **matlab** folder to your path in MATLAB in order to use its functions.

## Usage
A pre-compiled binary can be used in windows to start up quickly.

Double click **Emotiv.exe** in *bin/Windows/* and then Open MATLAB.

Use the following functions to establish a TCP/IP connection and read the raw signals:

```matlab
emotiv_connect
emotiv_read
```

When done using the headset, close the connection to python using:

```matlab
emotiv_disconnect
```

Raw data should be around 4k and contact quality above above 1k for getting good readings
