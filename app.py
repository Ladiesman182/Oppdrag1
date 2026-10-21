from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registrering")
def registrering():
    return render_template("registrering.html")

@app.route("/bestilling")
def bestilling():
    return render_template("bestilling.html")

@app.route("/resultat")
def resultat():
    return render_template("resultat.html")

if __name__ == "__main__":
    app.run(debug=True)