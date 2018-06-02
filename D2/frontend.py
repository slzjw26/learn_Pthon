import socket


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    while True:
        msg = input('>>> ')
        if not msg:
            break
        sock.send(msg.encode()+b'\n')


addr = ('127.0.0.1', 3001)


if __name__ == '__main__':
    run()