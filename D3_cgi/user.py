#!/usr/bin/python3

import os
import subprocess as sub


def query():
    text = sub.getoutput('grep ^ /etc/passwd')
    print(text)

def add():
    pass


def update():
    pass


def delete():
    pass


if __name__ == '__main__':
    method = os.getenv('REQUEST_METHOD', '')
    active = os.getenv('QUERY_STRING', '')
    if 'get' in method and 'query' in active:
        query()
    elif 'post' in method and ('add' in active or 'update' in active or 'delete' in active):
        if 'add' in active:
            add()
        elif 'update' in active:
            update()
        elif 'delete' in active:
            delete()
        
    
