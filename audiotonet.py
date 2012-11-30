#!/usr/bin/python
import speex
import struct
from config import Config

class AudioToNet():
  def __init__(self):
    self.speex = speex.new(Config.speex_quality)
   
  def convert(self, audioChunk):
    fmt = len(audioChunk) / Config.mic_format_size * Config.speex_fmt
    ints = struct.unpack(fmt, audioChunk)
    return self.speex.encode(ints)
    #return audioChunk
