import socket


def receive_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(addr)
    sock.listen(backlog)
    data, saddr = sock.accept()
    f = open('message', 'wb')
    while True:
        line = data.recv(2048)
        if not line:
            break
        f.write(line)
        f.flush()
        

backlog = 5
addr = ('127.0.0.1', 3001)


if __name__ == '__main__':
    receive_server()