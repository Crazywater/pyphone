from microphone import Microphone
from trafficprinter import TrafficPrinter
from audiotonet import AudioToNet
import socket

class Client():
  def __init__(self, master):
    self.microphone = Microphone()
    self.audioToNet = AudioToNet()
    self.trafficPrinter = TrafficPrinter()
    self.master = master

  def call(self, host, port):
    self.microphone.init()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.master.notifyServeOn(s)
    self.sendTo(s, host, port)
    self.microphone.destroy()

  def sendTo(self, socket, host, port):
    print "Sending to {0}, port {1}".format(host, port)
    while True:
      audio = self.microphone.nextAudioChunk()
      chunk = self.audioToNet.convert(audio)
      self.sendChunk(chunk, socket, host, port)
  
  def sendChunk(self, chunk, socket, host, port):
    socket.sendto(chunk, (host, port))
    self.trafficPrinter.addTraffic(len(chunk))
