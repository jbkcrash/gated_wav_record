# gated_wav_record
Gated Wav Record Module for GNU Radio.

Used to record audio into a .wav file, creating a new file for every squelch break.

## Install

These instructions assume you are using Ubuntu 18.04 with the packaged version of GNU Radio 3.7+

In the project's directory do the following.
```
mkdir build
cd build
cmake ../
make
sudo make install
cp ../gate_wav_record_f.xml /usr/share/gnuradio/grc/blocks/
```

Restart GNU Radio Companion and you should have an "audio" block called Gated Wav Record.

## Use

### Parameters

- Base File Name -
Fill out the Base File Name with the directory and prefix that is used in front of all the files generated by this block. This could be some identifier that will identify the source of the audio, like a call sign or frequency label. The block will add a hypehn between Base File Name and datetime stamp. It will also add .wav to the end automatically, just put the prefix you want in here.
- Number Channels -
For now this should be left at 1, we only support one channel to record on currently.
- Sampling Rate -
This can usually be left to default variable, otherwise set this to a variable that contains your sampling rate or set it manually.
- Bytes per Channel -
This must be set to 2 for now. Based on the math used to create the wav stream we are locked to 16bit wave files for now.

### Connection
To use the block to record an audio stream through a "Power Squelch" gate for one example. When using Power Squelch do not set the "gate" flag to yes. This will prevent our module from generating a new file name between breaks in squelch as it prevents the module from ever seeing a zero based stream it uses to detect silence.
