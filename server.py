import socket

MAX_SIZE_BYTES = 65535

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = '127.0.0.1'
s.bind((hostname, port))
print('Listening at {}'.format(s.getsockname()))

while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    upperCaseMessage = message.upper()
    print(f'The client at {clientAddress} says {message!r}')
    data = upperCaseMessage.encode('ascii')
    s.sendto(data, clientAddress)


