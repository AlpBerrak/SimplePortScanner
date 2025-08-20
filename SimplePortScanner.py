import socket
from datetime import datetime
import threading
from queue import Queue

# Queue to hold ports to scan

portQueue = Queue()
openPorts = []
lock = threading.Lock()

def scanPort(targetIP):
  while not portQueue.empty():
    port = portQueue.get()
    try:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.settimeout(0.5)
      result = sock.connect_ex((targetIP, port))
      if result == 0:
        with lock:
          print(f"Port {port} is OPEN")
          openPorts.append(port)
        sock.close()
    except Exception as e:
      pass
    portQueue.task_done()

def scanner():
  # Get target host from user
  target = input("Enter target IP or hostname: ")

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
  
  for port in range(1,1025):
    portQueue.put(port)
    
  # Start threads
  threadCount = 50
  threads = []
  for i in range(threadCount):
    t = threading.Thread(target=scanPort, args=(targetIP,))
    t.start()
    threads.append(t)
  portQueue.join() # after all ports are scanned
  
  print(f"\nScanning finished at: {datetime.now()}")
  print(f"Open ports: {sorted(openPorts)}")
 
if __name__  == "__main__":
  scanner()