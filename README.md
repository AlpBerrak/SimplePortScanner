# SimplePortScanner
## About:
A Python script to quickly scan TCP ports on a target host and identify open ports along with their common service names. This tool is useful for network diagnostics, security testing, and understanding which services are running on a system.

## Features:
- Scans a range of TCP ports (default: 1–1024)
- Detects open ports and prints them in real-time
- Identifies common service names for open ports using the system’s port database
- Multithreaded scanning for faster results (50 threads by default)
- Thread-safe output to avoid print conflicts
- Displays a final sorted list of all open ports with their service names

## Installation:
1. Clone the repo
```git clone https://github.com/AlpBerrak/SimplePortScanner.git```
2. Naviagate to the folder
```cd SimplePortScanner``` 
3. Run the script
```python SimplePortScanner.py```

## Usage:
Upon execution, the script prompts you to enter a target IP address or hostname. It then scans ports 1 through 1024 (modifiable in the script) and displays any open ports along with their corresponding service names.

### Example Output:
```
Enter target IP or hostname: 127.0.0.1
Scanning Target: 127.0.0.1
Scanning started at: 2025-08-20 11:32:22.214505
Port 135 is OPEN (epmap)
Port 445 is OPEN (microsoft-ds)
Port 902 is OPEN (Unknown)
Port 912 is OPEN (Unknown)

Scanning finished at: 2025-08-20 11:32:33.009913
Open ports and services:
Port 135: epmap
Port 445: microsoft-ds
Port 902: Unknown
Port 912: Unknown
```

## Customization: 
- Port Range: Modify the for port in range(1,1025): line to change the range of ports scanned.
- Thread Count: Adjust the threadCount = 50 line to increase or decrease the number of concurrent threads.
- Timeout Duration: Change the sock.settimeout(0.5) line to set a different timeout duration for socket connections.