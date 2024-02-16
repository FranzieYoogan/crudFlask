

from flask import Flask, render_template
from dbConnection import *

app = Flask(__name__)  # Setup the flask app by creating an instance of Flask


    


@app.route("/")
def index():
    return render_template('index.htm',rows = rows);


