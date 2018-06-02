import socket


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(addr)
    while True:
        csock, caddr = sock.recvfrom(4096)
        l = len(csock)
        print('Received %s bytes from %s:%s' % ((l,) + caddr))


addr = ('127.0.0.1', 8001)


if __name__ == '__main__':
    run()