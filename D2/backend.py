import socket


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    csock, caddr = sock.accept()
    while True:
        msg = csock.recv(2048)
        if not msg:
            break
        with open('message', 'a') as f:
            f.write(msg.decode())


addr = ('127.0.0.1', 3001)


if __name__ == '__main__':
    run()