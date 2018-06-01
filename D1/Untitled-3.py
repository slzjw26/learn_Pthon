# -*-coding:utf-8 -*-

import os

with open('notes.txt', 'w') as f:
    for i in range(10):
        f.write('Python is good, #%d\n' % i)

os.system('notepad notes.txt')
