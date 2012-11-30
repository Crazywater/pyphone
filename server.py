#!/usr/bin/python
from config import Config
from nettoaudio import NetToAudio
from speaker import Speaker
import socket

class Server():
  chunksize = 1024
  
  def __init__(self):
    self.netToAudio = NetToAudio()
    self.speaker = Speaker()
    self.connected = False
    
  def listen(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = "0.0.0.0"
    s.bind((host, Config.port))
    self.speaker.init()
    self.recvFrom(s)
    self.speaker.destroy()
  
  def recvFrom(self, socket):
    print "Listening on port {0}".format(Config.port)

    while True:
      chunk = self.readChunk(socket)
      audio = self.netToAudio.convert(chunk)
      self.speaker.play(audio)

  def readChunk(self, socket):
    data, addr = socket.recvfrom(Config.net_chunksize)
    return data
