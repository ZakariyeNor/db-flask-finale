from sellmanager import db

#create sells category
class Category(db.Model):
    #sells modal
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String, unique=True, nullable=False)
    sells = db.relationship('Sells', backref='category', cascade='all, delete', lazy=True)


    #Represent function
    def __repr__(self):
        return self.category_name


class Sells(db.Model):
    #sells 
    id = db.Column(db.Integer, primary_key=True)
    sold_name = db.Column(db.String, unique=True, nullable=False)
    sold_total = db.Column(db.Integer,nullable=False)
    sold_to = db.Column(db.String, nullable=False)
    sold_date = db.Column(db.Date, nullable=False)
    sold_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        # __repr__ to represent it self in the form of a string
        return "#{0} - Sells: {1} | Sold_date {2}".format(
            self.id, self.sold_name, self.sold_date
        )