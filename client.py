#!/usr/bin/python
from config import Config
from microphone import Microphone
from audiotonet import AudioToNet
from trafficprinter import TrafficPrinter
import socket

class Client():
  def __init__(self):
    self.microphone = Microphone()
    self.audioToNet = AudioToNet()
    self.trafficPrinter = TrafficPrinter()
    
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
    self.trafficPrinter.addTraffic(len(chunk))
  

