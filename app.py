from flask import Flask
from flask import render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "sjkdfbhasjk"

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
