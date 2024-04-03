#!/usr/bin/env python3
import ipdb

from flask import Flask, make_response

# New imports start here
from flask_migrate import Migrate

from models import db, Hotel, Customer
# New imports end here

app = Flask(__name__)

# New code starts here

# configure a database connection to the local file examples.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///examples.db'

# disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

# New code ends here
@app.route('/')
def index():
    hotel = Hotel.query.all()
    return f'<h1>Welcome! We have these {len(hotel)} avalilable.</h1>'

@app.route('/hotels')
def all_hotels():
    hotels = Hotel.query.all()
    hotels_list = [hotel.to_dict() for hotel in hotels]
    return make_response(hotels_list, 200)

@app.route('/customers')
def all_customers():
    customers = Customer.query.all()
    customers_list = [customer.to_dict() for customer in customers]
    return make_response(customers_list, 200)



if __name__ == "__main__":
    app.run(port=7777, debug=True)