"""
    Basics of web frameworks
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home() :
    return "Hello HBNB!" 

if __name__ == "__main__":

    app.run(port="5000", host="0.0.0.0", strict_slashes=False)