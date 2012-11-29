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
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, Config.port))
    while True:
      print "Listening on host {0}, port {1}".format(host, Config.port)
      s.listen(0)
      (clientsocket, address) = s.accept()
      print "Incoming call from {0}".format(address)
      self.connected = True
      self.recvFrom(clientsocket)
      print "Call over."
  
  def recvFrom(self, clientsocket):
    while self.connected:
      chunk = self.readChunk(clientsocket)
      audio = self.netToAudio.convert(chunk)
      self.speaker.play(audio)
  
  def readChunk(self, clientsocket):
    msg = ''
    chunksize = Config.net_chunksize
    while len(msg) < chunksize:
      chunk = clientsocket.recv(chunksize-len(msg))
      if not chunk:
        print "Socket disconnected."
        self.connected = False
        break
      else:     
        msg = msg + chunk
    return msg

