from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def landing():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
