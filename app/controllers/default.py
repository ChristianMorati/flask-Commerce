from app import app, db
from app.models import tables
from flask import Flask, render_template, request, redirect, url_for


def hankingProduts():
    first_most_famous = tables.Product.query.filter_by(id=12).first()
    second_most_famous = tables.Product.query.filter_by(id=14).first()
    return (first_most_famous, second_most_famous)


@app.route('/')
def index():
    most_famous = hankingProduts()
    products = tables.Product.query.all()
    
    return render_template(
        'index.html',
        products=products, first_most_famous=most_famous[0],
        second_most_famous=most_famous[1]
    )


# crud actions
@app.route('/register')
def Register():
    return render_template('product_register.html')


@app.route('/delete/<int:product_id>')
def delete(product_id):
    product = tables.Product.query.filter_by(id=product_id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/add', methods=['POST'])
def productRegister():
    if request.method == "POST":
        description = request.form["description"]
        url = request.form["url"]
        price = request.form["product_value"]
        new_product = tables.Product(description, url, price)

        db.session.add(new_product)
        db.session.commit()
    return redirect(url_for('index'))


@app.route("/update/<int:product_id>")
def update(product_id):
    product = tables.Product.query.filter_by(id=product_id).first()
    return render_template('product_register_update.html', product=product)


@app.route("/commitChanges/<int:product_id>", methods=['POST'])
def commitChanges(product_id):
    if request.method == "POST":
        produto = tables.Product.query.filter_by(id=product_id).first()
        produto.description = request.form["description"]
        produto.url = request.form["url"]
        produto.price = request.form["product_value"]
        db.session.commit()

    return redirect(url_for("index"))

