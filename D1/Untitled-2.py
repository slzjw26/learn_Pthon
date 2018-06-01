#!/urn/bin/env python
# -*- coding:utf-8 -*-

import sys


class ArgumentError(Exception):
    ...


def parse_argv(argv):
    if len(argv) == 3:
        argv1, argv2 = argv[1: 3]
        if not argv1.isdigit():
            raise ArgumentError('argv1 must be integer')
        if not argv2.isdigit():
            raise ArgumentError('argv2 must be integer')
    else:
        raise ArgumentError('require two argument')
    return int(argv1), int(argv2)

def add(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    try:
        argv1, argv2 = parse_argv(sys.argv)
    except ArgumentError as e:
        print(e)
        exit(1)

    result = add(argv1, argv2)
    print(result)