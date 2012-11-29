#!/usr/bin/python
from config import Config
import pyaudio
import wave

class Microphone():
  def __init__(self):
    pass

  def init(self):
    self.pyaudio = pyaudio.PyAudio()
    self.stream = self.pyaudio.open(format = Config.mic_format,
                      channels = Config.mic_channels,
                      rate = Config.mic_rate,
                      input = True,
                      frames_per_buffer = Config.mic_chunksize)

  def destroy(self):
    self.stream.stop_stream()
    self.stream.close()
    self.pyaudio.terminate()
    
  def nextAudioChunk(self):
    return self.stream.read(Config.mic_chunksize)
