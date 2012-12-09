from server import Server
from client import Client
import thread

class Master():
  def __init__(self):
    self.client = None
    self.server = None

  def call(self, host, port):
    if self.client==None:
      self.client = Client(self)
      self.client.call(host, port)
  
  def callOn(self, addr):
    if self.client == None:
      self.client = Client(self)
      thread.start_new_thread(
        self.client.call, addr)

  def serve(self):
    if self.server==None:
      self.server = Server(self)
      self.server.listen()

  def serveOn(self, socket):
    if self.server==None:
      self.server = Server(self)
      thread.start_new_thread(
          self.server.listenTo, (socket,))
