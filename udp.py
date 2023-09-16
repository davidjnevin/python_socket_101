import argparse, socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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

def client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hosts = []
    while True:
        host = input('Input the host IP address: ')
        if host == '':
            break
        hosts.append((host, port))
        message = input('Input lowercase sentence:' )
        data = message.encode('ascii')
        s.sendto(data, (host, port))
        print(f'The OS assigned the address {s.getsockname()} to me')
        data, address = s.recvfrom(MAX_SIZE_BYTES)
        text = data.decode('ascii')
        if (address in hosts):
            print(f'The server {address} replied with {text!r}')
            hosts.remove(address)
        else:
            print(f'{message!r} from unexpected host {address}')


if __name__ == '__main__':
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000,
                        help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    function(args.p)
