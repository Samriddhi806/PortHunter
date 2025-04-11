import sys
import socket 
import threading 

usage = "python 3 port_scanner.py TARGET START_PORT END_PORT"

print("-"*70)
print("Python Simple Port Scanner")
print("-"*70)

if(len(sys.argv)!=4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

    