import pyaudio
import wave
from config import Config

class Wavelog():
  def __init__(self, logfile):
    self.logfile = logfile
    self.pyaudio = pyaudio.PyAudio()
  
  def init(self):
    self.wf = wave.open(self.logfile, 'wb')
    self.wf.setnchannels(Config.mic_channels)
    self.wf.setsampwidth(self.pyaudio.get_sample_size(Config.mic_format))
    self.wf.setframerate(Config.mic_rate)
  
  def destroy(self):
    self.wf.close()
  
  def log(self, chunk):
    self.wf.writeframes(chunk)
