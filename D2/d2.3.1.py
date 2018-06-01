import socket


def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(addr)
    while True:
        date, caddr = sock.recvfrom(2048)
        l = len(date)
        print('Receive %s bytes from %s:%s' %((l,) + caddr))



addr = ('127.0.0.1', 8312)


if __name__ == '__main__':
    run_server()