from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

    
if __name__ == '__main__':
    app.run(
        debug=True,
        port = int(os.getenv('PORT', 8080)),
        host = os.getenv('IP', '0.0.0.0')
    )    