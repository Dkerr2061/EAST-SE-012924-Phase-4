#!/usr/bin/env python3
import ipdb

from flask import Flask, make_response

# New imports start here
from flask_migrate import Migrate

from models import db, Hotel
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

@app.route('/hotels')
def all_hotels():
    hotels = Hotel.query.all()
    hotel_list_with_dictionaries = [hotel.to_dict() for hotel in hotels]
    return make_response(hotel_list_with_dictionaries)

if __name__ == "__main__":
    app.run(port=7777, debug=True)