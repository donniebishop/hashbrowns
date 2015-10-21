#!usr/bin/env python

from www import app
from flask import render_template, request
from functions import hash_maker

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/hello/<name>')
def hello(name=None):
	name = str(name).capitalize()
	return render_template('hello.html', name=name)

@app.route('/hashbrowns', methods=['POST', 'GET'])
def hashbrowns():
	if request.method == 'POST' and request.form['potato']:
		original = str(request.form['potato'])
		h_dict = hash_maker(original)

		return render_template('hashbrowns.html',
				original=h_dict['original'],
				md5=h_dict['md5'],
				sha1=h_dict['sha1'],
				sha224=h_dict['sha224'],
				sha256=h_dict['sha256'])
	else:
		return render_template('hashbrowns.html')
