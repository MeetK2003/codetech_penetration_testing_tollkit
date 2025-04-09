from port_scanner.port_scanner import scan_ports
from brute_forcer.brute_forcer import brute_force

print("Welcome to the Penetration Testing Toolkit!")

# Run port scanner
ip_to_scan = input("Enter an IP to scan (e.g., 127.0.0.1): ")
scan_ports(ip_to_scan)

# Run brute-forcer
passwords = ["1234", "admin", "password", "letmein"]
target = input("Enter a password to test brute force: ")
brute_force(passwords, target)
