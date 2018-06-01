#!/urs/bin/env python
# -*- coding:utf-8 -*-

import sys

class Argument(Exception):
    pass


def try_argv(argv):
    if len(argv) == 3:
        argv1, argv2 = argv[1:3]
        if not argv1.isdigit():
            raise Argument('Argv1 must be an integer!')
        if not argv2.isdigit():
            raise Argument('Argv2 must be an integer!') 
        return int(argv1), int(argv2)
    else:
        raise Argument('Require two argument!')


def add(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    try:
        argv1, argv2 = try_argv(sys.argv)
    except Argument as e:
        print(e)
        exit(1)

    num = add(argv1, argv2)
    print(num)
