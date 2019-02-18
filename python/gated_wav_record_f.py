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

from gnuradio import gr

class gated_wav_record_f(gr.sync_block):
    """
    docstring for block gated_wav_record_f
    """
    def __init__(self, base_filename, n_channels, sample_rate, bits_per_sample):
        self.bRecordToggle = False # We start not recording
        self.base_filename = base_filename # This string is used with date_time to generate filename.
        self.n_channels = n_channels = 1 # TODO; fix, only one channel for now.
        self.sample_rate = sample_rate # Sample rate for recording.
        self.bits_per_sample = bits_per_sample # Sample size.
        gr.sync_block.__init__(self,
            name="gated_wav_record_f",
            in_sig=[numpy.float32],
            out_sig=None)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        # Recording Gate State Machine
        if any(in0) and not self.bRecordToggle: # We need to open file and start recording
            filename = self.base_filename + "-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".wav"
            self.waveFile = wave.open(filename, "wb")
            self.waveFile.setnchannels(self.n_channels)
            self.waveFile.setframerate(self.sample_rate)
            self.waveFile.setsampwidth(self.bits_per_sample)
            #waveFile.writeframes(b''.join(in0)) # File is open, now write these frames
            self.waveFile.writeframes(in0)
            self.bRecordToggle = True # We are now recording
        elif not any(in0) and self.bRecordToggle: # We detect an idle state and need to stop recording
            waveFile.close();
            self.bRecordToggle = False # We are not recording
        elif any(in0) and self.bRecordToggle: # We need to just record these frames, file should be open
            #waveFile.writeframes(b''.join(in0))
            self.waveFile.writeframes(in0)
        return len(input_items[0])

