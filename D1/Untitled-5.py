import multiprocessing as mul
from datetime import datetime
import time

def work(n):
    now = datetime.now()
    for i in range(10):
        print('Process %d, %s' %(i, now))


if __name__ == '__main__':
    procs = []
    for n in range(2):
        p = mul.Process(target=work, args=(n, ))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()

time.sleep(10)
