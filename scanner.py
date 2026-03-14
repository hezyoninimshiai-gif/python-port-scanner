import socket

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()


def main():
    target = input("Enter target IP or domain: ")

    print(f"\nScanning target: {target}")
    print("Scanning ports 1–1024...\n")

    for port in range(1, 1025):
        scan_port(target, port)


if __name__ == "__main__":
    main()