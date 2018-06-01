#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while 1:
    s = input('Please input a string:\n')
    if s == '':
        print("you don't input!Please try again.")
    else:
    	break
if s[0] in 'AEIOUaeiou':
    print(s+'ay')
else:
    print(s[1:]+s[0]+'ay')