#!/usr/bin/python
import argparse
from server import Server
from client import Client

def main():
  parser = argparse.ArgumentParser(description="Python Phone")
  parser.add_argument("--srv", dest="srv", action="store_true",
      help="Start the server")
  parser.add_argument("--call", dest="call",
      help="Call a hostname")
  args = parser.parse_args()

  if args.srv:
    server = Server()
    server.listen()
  elif args.call:
    client = Client()
    client.call(args.call)
  else:
    print "Please specify either --srv or --call."
    
if __name__ == "__main__":
  main()
