import threading
import time

def working(name, n, lock):
    with lock:
        print('Thread %s start to work' % name)
        for i in range(n):
            print('%s: #%s' % (name, i))
        print('Thread %s stop working' % name)

if __name__ == '__main__':
    threads = []
    lock = threading.Lock()
    for i in range(2):
        t = threading.Thread(target=working, args=(i, 7, lock))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    time.sleep(10)