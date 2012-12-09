#!/usr/bin/python
from config import Config
from nettoaudio import NetToAudio
from speaker import Speaker
import socket

class Server():
  def __init__(self, master):
    self.netToAudio = NetToAudio()
    self.speaker = Speaker()
    self.master = master

  def listenTo(self, theSocket):
    self.speaker.init()
    self.recvFrom(theSocket)
    self.speaker.destroy()

  def listen(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = "0.0.0.0"
    s.bind((host, Config.port))
    self.listenTo(s)

  def recvFrom(self, socket):
    print "Listening on ".format(socket.getsockname())
    while True:
      chunk = self.readChunk(socket)
      audio = self.netToAudio.convert(chunk)
      self.speaker.play(audio)

  def readChunk(self, socket):
    data, addr = socket.recvfrom(Config.net_chunksize)
    self.master.callOn(addr)
    return data