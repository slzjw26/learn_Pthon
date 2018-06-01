#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = ['as','asd','asd']
n=0
with open('C:/users/administrator/files/1.txt','w') as f:
	for i in s:
		if n == 2:
			f.write(i+'\n')
			break
		f.write(i+' ')
		n += 1



