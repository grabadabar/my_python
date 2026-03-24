#!/usr/bin/env python3

import argparse
from os import system as s


parser = argparse.ArgumentParser() 

# Add arguments 
parser.add_argument("-s","--start",action='store_true') 
parser.add_argument("-n","--next",action='store_true')
parser.add_argument("-p","--prev",action='store_true')
parser.add_argument("-st","--stop",action='store_true')

# Parse the arguments 
args = parser.parse_args() 

if args.start:
   s("mpv --loop-playlist=inf --input-ipc-server=/tmp/mpvsocket /home/georgi.i.dimitrov/Videos/first.mp4 /home/georgi.i.dimitrov/Videos/second.mp4 /home/georgi.i.dimitrov/Videos/third.mp4  > /dev/null 2>&1")
elif args.next:
   s("echo '{ \"command\": [\"playlist-next\"] }' |  socat - /tmp/mpvsocket")
elif args.prev:   
   s("echo '{ \"command\": [\"playlist-prev\"] }' |  socat - /tmp/mpvsocket")
elif args.stop:
   s("pkill mpv")
else:
   print("provide correct option")
   exit()  
