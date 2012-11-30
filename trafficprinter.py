#!/usr/bin/python
import time

class TrafficPrinter():
  def __init__(self):
    self.traffic = 0
    self.lastTime = 0
    
  def addTraffic(self, bytes):
    self.traffic += bytes
    now = time.time()
    if now - self.lastTime > 1:
      perSecond = float(self.traffic)
      print "{0} KiB/s\r".format(perSecond/1024)
      self.lastTime = now
      self.traffic = 0
