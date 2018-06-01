import socket


def sent():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    while True:
        line = input('>>> ')
        if not line:
            break
        sock.send(line.encode() + b'\n')


addr = ('127.0.0.1', 3001)


if __name__ == '__main__':
    sent()