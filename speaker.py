#!/usr/bin/python 
from config import Config
import pyaudio

class Speaker():
  def __init__(self):
    pass
  
  def init(self):
    self.pyaudio = pyaudio.PyAudio()
    self.stream = self.pyaudio.open(format=Config.mic_format,
                      channels=Config.mic_channels,
                      rate=Config.mic_rate,
                      output=True)
    
  def destroy(self):
    self.stream.stop_stream()
    self.stream.close()
    self.pyaudio.terminate()
  
  def play(self, audio):
   self.stream.write(audio)
