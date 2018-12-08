from flask import Flask
from flask import render_template

app = Flask(__name__)

API_KEY = '61465cb89fcacaf8f3988c1b4296fe2b'

@app.route('/')
def hello_world(name=None):
    return render_template('layout.html', name=name)
