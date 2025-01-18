from flask import render_template, request, redirect, url_for
from sellmanager import app, db
from sellmanager.models import Category, Sells

#app route
@app.route('/')
def home():
    sells = list(Sells.query.order_by(Sells.sold_id).all())
    return render_template('sells.html', sells=sells)


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



@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    edit_category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        edit_category.category_name = request.form.get('category_name')
        db.session.commit()
        return redirect(url_for('sells_category'))
    return render_template('edit_category.html', edit_category=edit_category)



@app.route("/delete_sells/<int:category_id>", methods=["GET", "POST"])
def delete_sells(category_id):
    delete_sells = Category.query.get_or_404(category_id)
    db.session.delete(delete_sells)
    db.session.commit()
    return redirect(url_for('sells_category'))


@app.route("/new_sells", methods=["GET", "POST"])
def new_sells():
    new_sells = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        sell = Sells(
            sold_name=request.form.get("sold_name"),
            sold_total=request.form.get("sold_total"),
            sold_to=request.form.get("sold_to"),
            sold_date=request.form.get("sold_date"),
            sold_id=request.form.get("sold_id") 
        )
        db.session.add(sell)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_sells.html', new_sells=new_sells)



@app.route('/edit_sells/<int:sells_id>', methods=["GET", "POST"])
def edit_sells(sells_id):
    edit_sells = Sells.query.get_or_404(sells_id)
    new_sells = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        edit_sells.sold_name = request.form.get("sold_name")
        edit_sells.sold_total = request.form.get("sold_total")
        edit_sells.sold_to = request.form.get("sold_to")
        edit_sells.sold_date = request.form.get("sold_date")
        edit_sells.sold_id = request.form.get("sold_id")
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_sells.html', edit_sells=edit_sells, new_sells=new_sells)



@app.route("/delete_sold/<int:sells_id>", methods=["GET", "POST"])
def delete_sold(sells_id):
    delete_sold = Category.query.get_or_404(sells_id)
    db.session.delete(delete_sold)
    db.session.commit()
    return redirect(url_for('home'))
