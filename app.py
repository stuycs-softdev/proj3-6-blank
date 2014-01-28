from flask import Flask
from flask import render_template, redirect, url_for, session, request
import utils
app = Flask(__name__)
app.secret_key = "sjkdfbhasjk"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
	if request.method=="POST":
		movieQuery = request.form['movie']
	

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("index.html")
    if request.form.get("password_register","")==request.form.get("confirm_password",""):
            #createUser will return a number depending on what the error was
        result=utils.createUser(request.form.get("username_register","").lower(),request.form.get("password_register",""))
            #success. Login page will have confirmation message
        if result==0:
            return render_template("index.html",type_register=0)
            #username is already taken
        elif result==1:
            return render_template("index.html",type_register=1)
            #username or pw is invalid
        else: 
            return render_template("index.html",type_register=2)
        #pw mismatch
    else:
        return render_template("index.html",type_register=3)
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="POST":
        result = utils.authorize(str(request.form.get("username_login","")).lower(), str(request.form.get("password_login","")))
        #successful login
        if result == 0:  
            session["username"] = request.form.get("username_login","")
            return redirect("/")
        #failed attempt!
        else:
            return render_template("index.html",type_login=1)
    else:
        return render_template("index.html")
@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)
