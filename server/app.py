#!/usr/bin/env python3
#1.creating an instance
from flask import Flask

app = Flask(__name__)

#routing views
'''@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'
app.run()
'''

@app.route('/<username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'
app.run()

'''@app.route('/<string:username>')
def user(username):
    return '<h1>profile for {username}</h1>'
'''
