from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.args.get("name")
    dorm = request.args.get("dorm")

    if not name or not dorm:
        return "failure"
    render_template("success.html")
