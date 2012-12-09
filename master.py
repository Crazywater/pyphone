from server import Server
from server import Client
import thread

class Master():
  def __init__(self):
    self.client = None
    self.server = None

  def notifyCall(self, addr):
    if self.client==None:
      self.client = Client(self)
      thread.start_new_thread(
        self.client.call, addr)
    
  def notifyServeOn(self, socket):
    if self.server==None:
      self.server = Server(self)
      thread.start_new_thread(
          self.server.listenTo, socket)

  def notifyServe(self):
    if self.server==None:
      self.server = Server(self)
      self.server.listen()