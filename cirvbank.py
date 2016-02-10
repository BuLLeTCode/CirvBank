from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

c = MongoClient()

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
