#!/usr/bin/python
import pyaudio

class Config:
  port = 25526
  mic_rate = 44100
  mic_channels = 1
  mic_format = pyaudio.paInt16
  mic_chunksize = 1024
  net_chunksize = 2048
  
