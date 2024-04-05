from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.
class Hotel(db.Model, SerializerMixin):
    __tablename__ = 'hotels'

    # serialize_rules = ('-reviews.hotel', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    reviews = db.relationship('Review', back_populates='hotel', cascade='all')

    customers = association_proxy('reviews', 'customer', creator = lambda c: Review(customer = c))

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    # serialize_rules = ('-reviews.customer', )

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    reviews = db.relationship('Review', back_populates='customer', cascade='all')

    hotels = association_proxy('reviews', 'hotel', creator = lambda h: Review(hotel = h))

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    # serialize_rules = ('-hotel.reviews', '-customer.reviews')

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    text = db.Column(db.String)
    
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotels.id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))

    hotel = db.relationship('Hotel', back_populates='reviews')
    customer = db.relationship('Customer', back_populates='reviews')



