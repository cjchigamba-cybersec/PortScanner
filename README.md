Port Scanner
-A multithreaded Python port scanner with banner grabbing and JSON export. Scans any target host across a custom port range and saves results for later analysis.

Features
-Concurrent scanning via ThreadPoolExecutor (100 workers)
-Banner grabbing on open HTTP ports
-Structured JSON output
-No external dependencies

Prerequisites
-Python 3.x — standard library only.

Usage
-bashpython3 scanner.py
-Enter target host and port range when prompted.

Example Output
-Enter target: 192.168.1.1
-Enter first port: 1
-Enter the last port to be scanned: 1000
Port 22 is open
Port 80 is open
Banner: HTTP/1.1 200 OK Server: Apache...
Port 443 is closed
Results saved to scan_results.json
json[
  { "port": 22,  "status": "open",   "banner": null },
  { "port": 80,  "status": "open",   "banner": "HTTP/1.1 200 OK..." },
  { "port": 443, "status": "closed", "banner": null }
