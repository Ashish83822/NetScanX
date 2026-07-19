import ipaddress
from scanner import scan_port
target_ip=input("Enter the target IP address:")
print("Target IP address is:", target_ip)
try:
    ipaddress.ip_address(target_ip)
    print("Valid IP address")
    while True:
        target_port=int(input("Enter the target port number:"))
        print("The target port number is:", target_port)
        is_open=scan_port(target_ip,target_port)
        if is_open:
            print("Port",target_port,"is open on",target_ip)
        else:
            print("Port",target_port,"is closed on",target_ip)
        scan_again=input("Do you want to scan another port? (y/n):")
        if scan_again.lower() == 'n':
            break
except ValueError:
    print("Invalid IP address")