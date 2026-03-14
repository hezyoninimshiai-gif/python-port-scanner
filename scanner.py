import socket
import time
from concurrent.futures import ThreadPoolExecutor

# store scan results
results = []

# common ports and services
common_services = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    179: "BGP",
    443: "HTTPS",
    465: "SMTPS",
    500: "ISAKMP",
    587: "SMTP",
    993: "IMAPS",
    995: "POP3S"
}


def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            service = common_services.get(port, "Unknown Service")

            try:
                s.send(b"Hello\r\n")
                banner = s.recv(1024).decode(errors="ignore").split("\n")[0].strip()    
            except:
                banner = "No banner"

            output = f"Port {port} OPEN ({service}) | Banner: {banner}"
            print(output)

            results.append(output)

        s.close()

    except:
        pass


def main():
    target = input("Enter target IP or domain: ")

    try:
        target_ip = socket.gethostbyname(target)
    except:
        print("Invalid target")
        return

    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    print(f"\nScanning target: {target_ip}")
    print(f"Scanning ports {start_port}–{end_port}...\n")

    start_time = time.time()

    checked_ports = 0

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target_ip, port)

            checked_ports += 1
            if checked_ports % 100 == 0:
                print(f"Checked {checked_ports} ports...")

    end_time = time.time()

    # save results to file
    with open("scan_results.txt", "w") as f:
        for line in results:
            f.write(line + "\n")

    print("\nScan completed.")
    print(f"Scan completed in {end_time - start_time:.2f} seconds")
    print("Results saved to scan_results.txt")


if __name__ == "__main__":
    main()