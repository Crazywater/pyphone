#!/usr/bin/python
from config import Config
from microphone import Microphone
from audiotonet import AudioToNet
import socket
import time

class Client():
  def __init__(self):
    self.microphone = Microphone()
    self.audioToNet = AudioToNet()
    self.traffic = 0
    self.lastTime = 0
    
  def call(self, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.microphone.init()
    self.sendTo(s, host)
    self.microphone.destroy()
    
  def sendTo(self, socket, host):
    print "Sending to {0}, port {1}".format(host, Config.port)
    while True:
      audio = self.microphone.nextAudioChunk()
      chunk = self.audioToNet.convert(audio)
      self.sendChunk(chunk, socket, host)
  
  def sendChunk(self, chunk, socket, host):
    socket.sendto(chunk, (host, Config.port))
    self.addTraffic(len(chunk))
  
  def addTraffic(self, bytes):
    self.traffic += bytes
    now = time.time()
    if now - self.lastTime > 1:
      perSecond = float(self.traffic)
      print "{0} KiB/s\r".format(perSecond/1024)
      self.lastTime = now
      self.traffic = 0
