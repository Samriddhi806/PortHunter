import sys
import socket 
import time

usage = "python3 port_scan.py TARGET START_PORT END_PORT"

print("-"*70)
print("Python Simple Port Scanner")
print("-"*70)


if(len(sys.argv) !=4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()
    
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target",target)

for port in range(start_port, end_port+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    try:
        s.connect((target,port))
        print(f"Port {port} is OPEN")
    except (socket.timeout, socket.error):
        pass
    finally:
        s.close()

