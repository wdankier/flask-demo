from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", user="Niet ingelogd")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        return redirect(url_for("user", usr=name))
    else:
        return render_template("login.html")


@app.route("/user/<usr>")
def user(usr):
    return render_template("index.html", user=usr)
    # return f"<h1>Welkom {usr}!</h1><a href='/'>Back</a>"


if __name__ == "__main__":
    app.run(debug=True)
