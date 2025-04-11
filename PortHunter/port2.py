import socket
from datetime import datetime
import threading

open_ports = []
closed_ports = []
filtered_ports = []
total_ports_scanned = 0
lock = threading.Lock()

def scan_port(target, port):
    global total_ports_scanned

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        
        with lock:
            total_ports_scanned += 1

            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open.")
                # Banner grabbing
                try:
                    sock.settimeout(1)  # Short timeout for banner grabbing
                    banner = sock.recv(1024).decode().strip()
                    print(f"Banner for port {port}: {banner}")
                except :
                    pass
            else:
                closed_ports.append(port)
                
        sock.close()

    except socket.timeout:
        with lock:
            filtered_ports.append(port)
    except socket.error:
        pass

def port_hunter(target, start_port, end_port):
    print(f"Starting Port Hunter scan on {target} at {datetime.now()}...\n")

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

        if len(threads) >= 100:  # Limit concurrency to 100 threads
            for t in threads:
                t.join()
            threads = []

    # Wait for all remaining threads to finish
    for t in threads:
        t.join()

    # Log results to a file
    with open("port_scan_log.txt", "a") as log_file:
        log_file.write(f"Scan on {target} at {datetime.now()}\n")
        log_file.write(f"Total ports scanned: {total_ports_scanned}\n")
        log_file.write(f"Open ports: {open_ports}\n")
        log_file.write(f"Closed ports: {closed_ports}\n")
        log_file.write(f"Filtered ports: {filtered_ports}\n\n")

    print("\nScan completed!")
    print(f"Total ports scanned: {total_ports_scanned}")
    print(f"Open ports: {open_ports}")
    print(f"Closed ports: {closed_ports}")
    print(f"Filtered ports: {filtered_ports}")
    print("Results logged to port_scan_log.txt.")

if __name__ == "__main__":
    target = input("Enter the target IP or domain: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    port_hunter(target, start_port, end_port)
