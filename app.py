from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bestilling")
def registrering():
    return render_template("registrering.html")

@app.route("/bestilling")
def registrering():
    return render_template("registrering.html")

@app.route("/resultat")
def registrering():
    return render_template("registrering.html")

if __name__ == "__main__":
    app.run(debug=True)