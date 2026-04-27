import socket
import json 
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target:")
begin_ports = int(input("Enter first port :"))
final_port = int(input("Enter the last port to be scanned :"))
results = []

def scanaport(port):
    sock = socket.socket()
    sock.settimeout(10)
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open ✅")
        banner = None

        try:
           if port == 80 or port == 220:
                sock.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode())
                banner = sock.recv(4096).decode(errors="ignore").strip()[:100]
                print(f"Banner :{banner}")
        except Exception as e:
                print(f"Banner grab failed :{e}")

        results.append({"port": port, "status": "open", "banner": banner})

    else:
        print(f"Port {port} is closed ❌")
        results.append({"port": port, "status": "closed", "banner": None})

    sock.close()

ports = range(begin_ports,final_port+1)

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scanaport, ports)

with open(r"C:\Users\CJ\Desktop\scan_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Results saved to scan_results.json ✅")