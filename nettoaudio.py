#!/usr/bin/python 
import speex
import array
import struct
from config import Config

class NetToAudio():
  def __init__(self):
    self.speex = speex.new(Config.speex_quality)
  
  def convert(self, netinput):
    counter, payload = struct.unpack("!Ls", netinput)
    print "Received packet {0}".format(counter)
    ints = self.speex.decode(payload)
    return struct.pack(len(ints)*Config.speex_fmt, *ints)
