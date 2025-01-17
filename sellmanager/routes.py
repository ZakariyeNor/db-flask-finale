from flask import render_template
from sellmanager import app, db

#app route
@app.route('/')
def home():
    return render_template('base.html')