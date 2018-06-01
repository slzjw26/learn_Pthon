import time
import socket
from datetime import datetime

def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    while True:
        msg = datetime.now().strftime('%F %T')
        sock.send(msg.encode())
        echoed = sock.recv(2048)
        print(echoed.decode(), flush=True)
        time.sleep(1)


addr = ('127.0.0.1', 3001)


if __name__ == '__main__':
    run()