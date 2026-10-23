from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/om")
def om():
    return render_template("om.html")

@app.route("/bestilling", methods=["GET", "POST"])
def bestilling():
    if request.method == "POST":
        navn = request.form["navn"]
        klasse = request.form["Klasse"]
        epost = request.form["epost"]
        produkter = request.form["produkter"]

        return render_template(
            "resultat.html",
            navn=navn,
            epost=epost,
            klasse=klasse,
            produkter=produkter
        )     

    return render_template("bestilling.html")



if __name__ == "__main__":
    app.run(debug=True)
