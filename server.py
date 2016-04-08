#! /usr/bin/python3
#  -*- coding:utf-8 -*-

#server.py
#import from wsgiref module

from wsgiref.simple_server import make_server
from exercise import application

httpd = make_server('',8000,application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()