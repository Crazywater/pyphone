#!/usr/bin/python
import pyaudio

class Config:
  mic_device_index = 7 # use --dev to find out your device index
  speaker_device_index = 7
  port = 25527
  mic_rate = 44100
  mic_channels = 1
  mic_format = pyaudio.paInt16
  mic_format_size = 2 # bytes, needs to match mic_format
  speex_fmt = 'h' # needs to match mic_format (int16, see python module struct)
  mic_chunksize = 1024
  net_chunksize = 2048
  speex_quality = 10
  speaker_log = "speaker.wav"
  mic_log = "mic.wav"

