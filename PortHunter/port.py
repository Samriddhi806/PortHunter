import socket
from datetime import datetime

def port_hunter(target, start_port, end_port):
    open_ports = []
    closed_ports = []
    total_ports_scanned = 0

    print(f"Starting Port Hunter scan on {target} at {datetime.now()}...\n")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Set timeout to avoid hanging
            result = sock.connect_ex((target, port))
            total_ports_scanned += 1

            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open.")
            else:
                closed_ports.append(port)

            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except socket.gaierror:
            print("Hostname could not be resolved.")
            break
        except socket.error:
            print("Could not connect to server.")
            break

    # Log results to a file
    with open("port_scan_log.txt", "a") as log_file:
        log_file.write(f"Scan on {target} at {datetime.now()}\n")
        log_file.write(f"Total ports scanned: {total_ports_scanned}\n")
        log_file.write(f"Open ports: {open_ports}\n")
        log_file.write(f"Closed ports: {closed_ports}\n\n")

    print("\nScan completed!")
    print(f"Total ports scanned: {total_ports_scanned}")
    print(f"Open ports: {open_ports}")
    print(f"Closed ports: {closed_ports}")
    print("Results logged to port_scan_log.txt.")

if __name__ == "__main__":
    target = input("Enter the target IP or domain: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    port_hunter(target, start_port, end_port)
