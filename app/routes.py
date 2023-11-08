from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/info')
def about():
    return render_template('about.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact')


