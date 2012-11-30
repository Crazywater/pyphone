#!/usr/bin/python
from config import Config
from wavelog import Wavelog
import pyaudio
import wave

class Microphone():
  def __init__(self):
    self.log = Wavelog(Config.mic_log)

  def init(self):
    self.pyaudio = pyaudio.PyAudio()
    self.stream = self.pyaudio.open(format = Config.mic_format,
                      channels = Config.mic_channels,
                      rate = Config.mic_rate,
                      input = True,
                      frames_per_buffer = Config.mic_chunksize,
                      input_device_index = Config.mic_device_index)
    self.log.init()
    
  def destroy(self):
    self.stream.stop_stream()
    self.stream.close()
    self.pyaudio.terminate()
    self.log.destroy()
    
  def nextAudioChunk(self):
    chunk = self.stream.read(Config.mic_chunksize)
    self.log.log(chunk)
    return chunk
