from flask import Flask, jsonify
app = Flask(__name__)
from alerter import views

if __name__ == '__main__':
    app.run(debug=True)
