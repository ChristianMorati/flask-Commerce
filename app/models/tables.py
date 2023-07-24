from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


    def __repr__(self):
        return "<User %>" % self.username


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    url = db.Column(db.Text)
    price = db.Column(db.Float)


    def __init__(self, description, url, price):
        self.description = description
        self.url = url
        self.price = price


    def __repr__(self):
        return "<Product %>" % self.id


class LikedItem(db.Model):
    __tablename__ = "likeditems"

    likeditem_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    product = db.relationship('Product', foreign_keys=product_id)
    user = db.relationship('User', foreign_keys=user_id)


    def __init__(self, product_id, user_id):
        self.product_id = product_id
        self.user_id = user_id


    def __repr__(self):
        return "<LikedItem %>" % self.product_id, self.user_id

