#!/usr/bin/python
import speex
import struct
from config import Config

class AudioToNet():
  def __init__(self):
    self.speex = speex.new(Config.speex_quality)
    self.counter = 0
   
  def convert(self, audioChunk):
    self.counter += 1
    fmt = len(audioChunk) / Config.mic_format_size * Config.speex_fmt
    ints = struct.unpack(fmt, audioChunk)
    payload = self.speex.encode(ints)
    print "Sending packet {0} payloadsize {1}".format(self.counter, len(payload))
    return struct.pack("!L", self.counter) + payload
    #return audioChunk
