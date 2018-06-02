import socket
import threading


def add(csock, caddr):
    while True:
        msg = csock.recv(4096)
        if not msg:
            break
        csock.send(b'Receive: '+ msg)


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(addr)
    sock.listen(backlog)
    while True:
        csock, caddr = sock.accept()
        t = threading.Thread(target=add, args=(csock, caddr))
        t.start()


backlog = 5
addr = ('127.0.0.1', 8001)


if __name__ == '__main__':
    run()