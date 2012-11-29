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
    
  def listen(self):
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, Config.port))
    print "Listening on host {0}, port {1}".format(host, Config.port)
    s.listen(0)
    while True:
      (clientsocket, address) = s.accept()
      print "Incoming call from {0}".format(address)
      self.recvFrom(clientsocket)
  
  def recvFrom(self, clientsocket):
    while True:
      chunk = self.readChunk(clientsocket)
      audio = self.netToAudio.process(chunk)
      self.speaker.play(audio)
  
  def readChunk(self, clientsocket):
    msg = ''
    while len(msg) < chunksize:
      chunk = clientsocket.recv(chunksize-len(msg))
      if not chunk:
       raise RuntimeError("Socket disconnected.")
      msg = msg + chunk
    return msg

