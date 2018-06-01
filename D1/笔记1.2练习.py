#!/urs/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing as mul
from datetime import datetime
import time

def worker(n):
    now = datetime.now()
    for i in range(10):
        print('process#%d, %s' % (n, now))

if __name__ == '__main__':
    proc = []
    for i in range(2):
        p = mul.Process(target=worker, args=(i,))
        p.start()
        proc.append(p)
    for p in proc:
        p.join()

    time.sleep(10)