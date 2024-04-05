#!/usr/bin/env python3
import ipdb

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Hotel, Customer, Review

app = Flask(__name__)

# configure a database connection to the local file examples.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'

# disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

@app.route('/hotels')
def all_hotels():
    hotels = Hotel.query.all(only=('id', 'name'))
    hotel_list_with_dictionaries = [hotel.to_dict() for hotel in hotels]
    return make_response(hotel_list_with_dictionaries, 200)

@app.route('/hotels/<int:id>')
def hotel_by_id(id):
    hotel = db.session.get(Hotel, id)
    if hotel:
        body = hotel.to_dict(rules=('-reviews.hotel', '-reviews.customer.reviews'))
        status = 200
    else:
        body = {"message": f"Hotel {id} is not found."}
        status = 404
    return make_response(body, status)

@app.route('/customers')
def all_customers():
    customers = Customer.query.all()
    customer_list_with_dict = [customer.to_dict(only=('id', 'first_name', 'last_name')) for customer in customers]
    return make_response(customer_list_with_dict, 200)

@app.route('/reviews')
def all_reviews():
    reviews = Review.query.all()
    review_list_with_dict = [review.to_dict(rules=('-hotel.reviews', '-customer.reviews')) for review in reviews]
    return make_response(review_list_with_dict, 200)

if __name__ == "__main__":
    app.run(port=7777, debug=True)