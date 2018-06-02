import socket
import random

def run():
    msg = b'abcdefghijklmnopqrstuvwxyz'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        i = random.randint(0, 26)
        sock.sendto(msg[:i], addr)


addr = ('127.0.0.1', 8001)


if __name__ == '__main__':
    run()