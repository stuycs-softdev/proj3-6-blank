from flask import Flask
from flask import render_template, redirect, url_for, session, request
import utils
import movie_info
import getData
import oauthgoogle
import json
import urllib,urllib2

app = Flask(__name__)
app.secret_key = "sjkdfbhasjk"

oauthurl = "https://..."

url="https://accounts.google.com/o/oauth2/auth"

values = {'response_type':'code',
          'client_id':'1079207299172-mip8h70opk227f35q8uj3k8md80pjt3f.apps.googleusercontent.com',
          'scope':'profile email',
          'static':'somethingstatic',
          'redirect_uri': oauthurl
          }



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method=="POST":
		movieQuery = request.form['movie']
		stats = movie_info.findMovieLinks(movieQuery, 10)
                session['stats'] = stats
                return redirect("/results")

@app.route("/results")
def results():
    choice = request.args.get("choice")
    if choice != None:
        x = session['stats'][int(choice)]
        ans = []
        ans.append(movie_info.findActorLinks(x['link'],20))
        ans.append(movie_info.getResults(ans[0]))
        return render_template("res.html", results=[x], data = ans);
    else: 
        return render_template("res.html",results=session["stats"])

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

@app.route("/glogin")
def glogin():
    data = urllib.urlencode(values)
    req = urllib2.Request(url+"?"+data)
    response = urllib2.urlopen(req)
    return response.read()

    

@app.route("/oauth2callback")
def back():
    if request.args.has_key('error'):
        return "ERROR"
    code = request.args.get('code')

    values={'code':code,
            'client_id':'1079207299172-mip8h70opk227f35q8uj3k8md80pjt3f.apps.googleusercontent.com',
            'client_secret':'7-LAQae58JlhOc2JE4jtG65P',
            'grant_type':'authorization_code',
            'redirect_uri': oauthurl
            }
    
    data=urllib.urlencode(values)
    url="https://accounts.google.com/o/oauth2/token"
    req = urllib2.Request(url,data)
    response = urllib2.urlopen(req)
    rawresult = response.read()
    result=json.loads(rawresult)
    url="https://www.googleapis.com/plus/v1/people/me"
    data=urllib.urlencode({'access_token':result['access_token'],
                           })
    req = urllib2.Request(url+"?"+data)
    response = urllib2.urlopen(req)
    result = response.read()
    print result
    return "BACK"+result

if __name__ == "__main__":
    app.run(debug = True)
