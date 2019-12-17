' A simple fast application '

from flask import Flask

# application
app = Flask(__name__) 

# root
@app.route("/")

# function
def hello():
    return " Hello world"

if __name__== "__main__":
    app.run()