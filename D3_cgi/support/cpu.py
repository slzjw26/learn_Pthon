#!/usr/bin/python
# -*- coding:utf-8 -*- 
# 显示本机的CPU 使用状况

from __future__ import print_function, unicode_literals

import subprocess as sub

p = sub.Popen(['uptime'], stdout=sub.PIPE)
stdout, stderr = p.communicate()
min1, min5, min15 = stdout.replace(',', '').split()[-3:]
print('Content-Type: text/plain\n\n', end='')
print('%10s%10s%10s' % ('1min', '5min', '10min'))
print('%10s%10s%10s' % (min1, min5, min15))
