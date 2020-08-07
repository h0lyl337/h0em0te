#!/usr/bin/env python
from flask import request, render_template
from flask import Flask , request, redirect, render_template , sessions, session
import flask
import webbrowser
import jinja2.ext


app = Flask(__name__, static_folder='./static')

users = ['killerrob']
webbrowser.open('192.168.2.76:5000')


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=False, host='192.168.2.76')
