from flask import Flask, jsonify
app = Flask(__name__)
from alerter import views

from flask.ext.pymongo import PyMongo

mongo = PyMongo(app)
app.config.from_pyfile('alerter.cfg')

if __name__ == '__main__':
    app.run(debug=True)
