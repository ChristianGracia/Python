from flask import Flask, render_template, request

# needed to init flask app
app = Flask(__name__)


@app.route("/")
def index():
    return "lil_cuffy"
