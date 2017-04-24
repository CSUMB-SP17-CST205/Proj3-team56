import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def login():
	return render_template('index.html')
	
@app.route('/doubledouble')
def doubledouble():
	return render_template('doubledouble.html')
	
@app.route('/inofries')
def INOFries():
	return render_template('INOFries.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port = int(os.getenv('PORT', 8080)),
        host = os.getenv('IP', '0.0.0.0')
    )	