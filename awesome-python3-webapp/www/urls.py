# --*-- coding:utf-8

__author__ = 'TonyZhu'

import logging

from transwarp.web import get,view

from apis import api,APIValueError,APIPermeissionError,APIResourceNotFoundError

from models import User,Blog,Comment

# @view('test_users.html')
# @get('/')
# def test_users():
# 	users = user.find_all()
# 	return dict(users = users)

@view('blog.html')
@get('/')
def index():
	blogs = Blog.find_all()
	user = User.find_first('where email = ?','admin@example.com')
	return dict(blogs = blogs,user = user)

@api
@get('/api/users')
def api_get_users():
	users = User.find_by('order by created_at desc')
	for u in users:
		u.password = '******'
	return dict(user = users)

