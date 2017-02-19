# blog.py - controller

# imports
from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3

# configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'b"\xc9\xcfIk\xc8\x8b\r\xff)\xab\xd7\xc7#\x17\xcfV\xae\x92\x81\x1b\xb1N\x01"'

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function to connect to the db
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def login():
	error = none
	status_code = 200
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid credentials. Please try again.'
			status_code= 401
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error=error), status_code

@app.route('/main')
def main():
	return render_template('main.html')

if __name__ =='__main__':
    app.run(debug=True)

