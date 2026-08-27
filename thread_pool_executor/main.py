# Thread Pooling
# This program demonstrates the usage of thread pooling through ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor
from time import sleep

def scan_port(port):
    sleep(0.5) # Simulating a preset socket timeout
    return f"Port {port} scanned..."

ports = range(1, 65536)

with ThreadPoolExecutor(max_workers=100) as executor:
    print("Scanning in progress...\n")
    print("Estimated time to completion: 5-6 minutes.")
    results = executor.map(scan_port, ports)

for result in results:
    print(result)