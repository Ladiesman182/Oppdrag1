from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profil" methods=["GET", "POST"])
def profil():
    if request.method == "POST":
        brukernavn = request.form["brukernavn"]

        passord = request.form["passord"]

        return render_template("profil.html",
                               brukernavn=brukernavn,
                               passord=passord,)
    return render_template("registrering.html")

@app.route("/registrering")
def registrering():
    return render_template("registrering.html")

if __name__ == "__main__":
    app.run(debug=True)