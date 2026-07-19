import socket
def scan_port(ip, port):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.settimeout(1)
    try:
        tcp_socket.connect((ip, port))
        return True
    except OSError:
        return False
    finally:
        tcp_socket.close()