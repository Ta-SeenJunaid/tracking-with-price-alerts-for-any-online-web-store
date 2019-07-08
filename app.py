from flask import Flask

__author__ = 'Junaid'

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def hello_world():
    return "Hello, world!"




