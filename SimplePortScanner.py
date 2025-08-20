import socket
from datetime import datetime

def scanner():
  # Get target host from user
  target = input("Enter target IP or hostname")

  # Resolve hostname to IP if needed

  try: 
    targetIP = socket.gethostbyname(target)
  except socket.gaierror:
    print("Hostname could not be resolved")
    exit()
    
  print(f"Scanning Targer: {targetIP}")
  print(f"Scanning started at: {datetime.now()}")
  
  # Scan a range of ports
  # For now ports 1 - 1024
  openPorts = []
  
  for port in range(1,1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = sock.connect_ex((targetIP, port))
    if result == 0:
      print(f"Port {port} is OPEN")
      openPorts.append(port)
    sock.close()
  print(f"\nScanning finished at: {datetime.now()}")  
  print(f"Open ports: {openPorts}")
