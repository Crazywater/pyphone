#!/usr/bin/python 
from config import Config
from wavelog import Wavelog
import pyaudio
import wave

class Speaker():
  def __init__(self):
    self.log = Wavelog(Config.speaker_log)
  
  def init(self):
    self.pyaudio = pyaudio.PyAudio()
    self.stream = self.pyaudio.open(format=Config.mic_format,
                      channels=Config.mic_channels,
                      rate=Config.mic_rate,
                      output=True)
    self.log.init()
    
  def destroy(self):
    self.stream.stop_stream()
    self.stream.close()
    self.pyaudio.terminate()
    self.log.destroy()
  
  def play(self, audio):
   self.stream.write(audio)
   self.log.log(audio)

