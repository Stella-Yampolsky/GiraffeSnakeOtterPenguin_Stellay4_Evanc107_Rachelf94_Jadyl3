from flask import Flask, render_template, request, redirect, flash, url_for, session
import sqlite3

from sitedb import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def landing():
    if 'username' in session:
        return redirect(url_for('home'))
    else: return redirect(url_for('login'))

@app.route('/home')
def home():
    if "username" not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session["username"])

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

@app.route("/login", methods=["GET", "POST"])# will code registering and logging forms later
def login():
    if 'username' in session:
        return redirect("/home")

    if request.method =="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:# checks if both form entries were filled out
            flash("Missing username/password", "error")
            return redirect("/login")

        if checkPassword(username, password):# if password is correct, given user exists
            session["username"] = username# adds user to session
            return redirect("/home")

        else:# if password isnt correct
            flash("Invalid username/password", "error")
            return redirect("/login")

    return render_template("login.html")# if GET request, just renders login page

@app.route('/profile/<int:user_id>')
def search():
    return render_template('profile.html') #change later

@app.route('/profile')
def self():
    return redirect('/profile/1')#change later

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method =="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("register.html", warning = "empty field(s)")

        #check if user has special chars
        #check for existing username
        message = addUser(username, password)
        if message:
            return render_template("register.html", warning = message)
        else:
            return redirect("/login")

    return render_template("register.html")

@app.route('/logout', methods = ['GET','POST'])
def logout():
    if 'username' in session:
        user = session.pop('username')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
