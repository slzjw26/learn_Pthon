import socket
import threading


def echoed(csock, caddr):
    while True:
        data = csock.recv(4096)
        if not data:
            break
        data = b'received: ' + data
    csock.send(data)


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(addr)
    sock.listen(barklog)
    while True:
        csock, caddr = sock.accept()
        t = threading.Thread(target=echoed, args=(csock, caddr))
        t.start()


barklog = 5
addr = ('127.0.0.1', 3001)


if __name__ == '__main__':
    run()