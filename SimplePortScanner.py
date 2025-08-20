import socket
from datetime import datetime

def scanner()
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
  
  
