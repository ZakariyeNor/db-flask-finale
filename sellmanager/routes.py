from flask import render_template, request, redirect, url_for
from sellmanager import app, db
from sellmanager.models import Category, Sells

#app route
@app.route('/')
def home():
    return render_template('base.html')


@app.route('/sells_category')
def sells_category():
    return render_template('sells_category.html')



@app.route('/new_sells', methods=["GET", "POST"])
def new_sells():
    if request.method == "POST":
        category = Category(category_name=request.form.get('category_name'))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('sells_category'))
    return render_template('new_sells.html')