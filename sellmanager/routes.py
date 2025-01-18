from flask import render_template, request, redirect, url_for
from sellmanager import app, db
from sellmanager.models import Category, Sells

#app route
@app.route('/')
def home():
    return render_template('base.html')


@app.route('/sells_category')
def sells_category():
    sells_category = list(Category.query.order_by(Category.category_name).all())
    return render_template('sells_category.html', sells_category=sells_category)



@app.route("/new_category", methods=["GET", "POST"])
def new_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('sells_category'))
    return render_template('new_category.html')



@app.route("/edit_sells/<int:category_id>", methods=["GET", "POST"])
def edit_sells(category_id):
    edit_sells = Category.query.get_or_404(category_id)
    if request.method == "POST":
        edit_sells.category_name = request.form.get('category_name')
        db.session.commit()
        return redirect(url_for('sells_category'))
    return render_template('edit_sells.html', edit_sells=edit_sells)



@app.route("/delete_sells/<int:category_id>", methods=["GET", "POST"])
def delete_sells(category_id):
    delete_sells = Category.query.get_or_404(category_id)
    db.session.delete(delete_sells)
    db.session.commit()
    return redirect(url_for('sells_category'))