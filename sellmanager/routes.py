from flask import render_template
from sellmanager import app, db

#app route
@app.route('/')
def home():
    return render_template('base.html')


@app.route('/sells_category')
def sells_category():
    return render_template('sells_category.html')



@app.route('/new_sells')
def new_sells():
    return render_template('new_sells.html')