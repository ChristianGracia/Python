from flask import Flask, render_template, request

# needed to init flask app
app = Flask(__name__)


@app.route("/")
def index():
    # second param in request is default value if name is not entered
    name = request.args.get("name", "lil_cuffy")
    return render_template("index.html", name=name)

# set name value in request
# ex 127.0.0.1:5000/?name=christian
