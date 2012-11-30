#!/usr/bin/python 
import speex
import array
import struct
from config import Config

class NetToAudio():
  def __init__(self):
    self.speex = speex.new(Config.speex_quality)
  
  def convert(self, netinput):
    #return netinput
    ints = netinput
    ints = self.speex.decode(netinput)
    return struct.pack(len(ints)*Config.speex_fmt, *ints)
