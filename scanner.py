import socket
from concurrent.futures import ThreadPoolExecutor

# Common ports and services
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
            print(f"Port {port} OPEN ({service})")

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

    print(f"\nScanning target: {target_ip}")
    print("Scanning ports 1–1024...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1, 1025):
            executor.submit(scan_port, target_ip, port)


if __name__ == "__main__":
    main()