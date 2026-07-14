import ipaddress
target_ip=input("Enter the target IP address:")
print("Target IP address is:", target_ip)
try:
    ipaddress.ip_address(target_ip)
    print("Valid IP address")
except ValueError:
    print("Invalid IP address")