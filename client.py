import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f'The OS assigned the address {s.getsockname()} to me')
