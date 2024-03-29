#!/usr/bin/python
from master import Master
from config import Config
import pyaudio
import argparse

def main():
  parser = argparse.ArgumentParser(description="Python Phone")
  parser.add_argument("--srv", dest="srv", action="store_true",
      help="Start the server")
  parser.add_argument("--call", dest="hostname",
      help="Call a hostname")
  parser.add_argument("--dev", dest="devices", action="store_true",
    help="List devices")

  args = parser.parse_args()
  master = Master()

  if args.devices:
    p = pyaudio.PyAudio()
    i = 0
    while True:
      try:
        print "{0}: {1}".format(i, p.get_device_info_by_index(i)['name'])
        i += 1
      except:
        break
  if args.srv:
    master.serve()
  elif args.hostname:
    master.call(args.hostname, Config.port)
  else:
    print "Please specify either --srv or --call."
    
if __name__ == "__main__":
  main()
