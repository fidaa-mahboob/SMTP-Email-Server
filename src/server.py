import config
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hi_world():
    return "<p>Hi, World!</p>"