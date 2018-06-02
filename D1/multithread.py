import threading


def working(name, n):
    print('threading %s start to work' % name)
    for i in range(n):
        print('%s: #%s' % (name, i))
    print('threading %s stop working' % name)


if __name__ == '__main__':
    threads = []
    for i in range(2):
        t = threading.Thread(target=working, args=(i, 7))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
