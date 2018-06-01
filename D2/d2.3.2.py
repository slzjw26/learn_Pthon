import socket
import random

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'01234567890123456789'
    while True:
        l = random.randint(5, 20)
        sock.sendto(data[:l], addr)
        print('Sent %s bytes to %s:%s' %((l,) + addr))



addr = ('127.0.0.1', 8312)


if __name__ == '__main__':
    run_client()