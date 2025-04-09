import socket

def scan_ports(ip):
    print(f"Scanning ports on {ip}...")
    for port in range(1, 100):  # check ports 1 to 99
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN 🔓")
        sock.close()
