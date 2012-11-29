#!/usr/bin/python
from config import Config
from microphone import Microphone
from audiotonet import AudioToNet
import socket

class Client():
  def __init__(self):
    self.microphone = Microphone()
    self.audioToNet = AudioToNet()
    
  def call(self, host):
    s = socket.socket()
    print "Connecting to {0}, port {1}".format(host, Config.port)
    s.connect((host, Config.port))
    print "Connected."
    
  def sendTo(self, socket):
    while True:
      audio = self.microphone.nextAudioChunk()
      chunk = self.audioToNet.process(audio)
      self.sendChunk(chunk, socket)
  
  def sendChunk(self, chunk, socket):
    socket.send(chunk)
