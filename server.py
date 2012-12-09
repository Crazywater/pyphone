#!/usr/bin/python
from config import Config
from nettoaudio import NetToAudio
from audiotonet import AudioToNet
from speaker import Speaker
from microphone import Microphone
from trafficprinter import TrafficPrinter
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
    print "Listening on port {0}".format(Config.port)
    while True:
      chunk = self.readChunk(socket)
      audio = self.netToAudio.convert(chunk)
      self.speaker.play(audio)

  def readChunk(self, socket):
    data, addr = socket.recvfrom(Config.net_chunksize)
    self.master.notifyCall(addr)
    return data

class Client():
  def __init__(self, master):
    self.microphone = Microphone()
    self.audioToNet = AudioToNet()
    self.trafficPrinter = TrafficPrinter()
    self.server = master

  def call(self, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.microphone.init()
    self.sendTo(s, host, port)
    self.microphone.destroy()
    self.master.notifyServeOn(s)

  def sendTo(self, socket, host, port):
    print "Sending to {0}, port {1}".format(host, port)
    while True:
      audio = self.microphone.nextAudioChunk()
      chunk = self.audioToNet.convert(audio)
      self.sendChunk(chunk, socket, host, port)
  
  def sendChunk(self, chunk, socket, host, port):
    socket.sendto(chunk, (host, port))
    self.trafficPrinter.addTraffic(len(chunk))
