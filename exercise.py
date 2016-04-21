#! /usr/bin/python3
# -*- coding:utf-8 -*-
def gen():
	while True:
		print('Before...')
		s = yield
		print(s)
		print('After...')

s = gen()

next(s)

s.send('Kiss')