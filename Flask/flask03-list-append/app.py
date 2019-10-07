from flask import Flask, render_template, request


# list init
students = []

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return "failure"
    students.append(f"{name} from {dorm}")
    for x in students:
        print(x)
    return render_template("success.html")
