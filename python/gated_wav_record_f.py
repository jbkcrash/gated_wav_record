#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
import wave
import datetime
import struct

from gnuradio import gr

class gated_wav_record_f(gr.sync_block):
    """
    docstring for block gated_wav_record_f
    """
    def __init__(self, base_filename, n_channels, sample_rate, bytes_per_sample):
        self.bRecordToggle = False # We start not recording
        self.base_filename = base_filename # This string is used with date_time to generate filename.
        self.n_channels = n_channels = 1 # TODO; fix, only one channel for now.
        self.sample_rate = sample_rate # Sample rate for recording.
        self.bytes_per_sample = bytes_per_sample # Sample size.
        gr.sync_block.__init__(self,
            name="gated_wav_record_f",
            in_sig=[numpy.float32],
            out_sig=None)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        # Recording Gate State Machine
        if any(in0) and not self.bRecordToggle: # We need to open file and start recording
            print "Opening File\r\n"
            filename = self.base_filename + "-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".wav"
            self.waveFile = wave.open(filename, "wb")
            self.waveFile.setnchannels(self.n_channels)
            self.waveFile.setframerate(self.sample_rate)
            self.waveFile.setsampwidth(self.bytes_per_sample) # Based on how I am generating audio this is 2 for now
            audio_frames = numpy.int16(in0/numpy.max(numpy.abs(in0)) * self.sample_rate)
            self.waveFile.writeframes(audio_frames)
            self.bRecordToggle = True # We are now recording
        elif not any(in0) and self.bRecordToggle: # We detect an idle state and need to stop recording
            print "Closing File\r\n"
            self.waveFile.close();
            self.bRecordToggle = False # We are not recording
        elif any(in0) and self.bRecordToggle: # We need to just record these frames, file should be open
            audio_frames = numpy.int16(in0/numpy.max(numpy.abs(in0)) * self.sample_rate)
            self.waveFile.writeframes(audio_frames)            
        return len(input_items[0])

