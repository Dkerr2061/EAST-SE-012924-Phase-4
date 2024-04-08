#!/usr/bin/env python3
import ipdb

from flask import Flask, make_response, request
from flask_migrate import Migrate

### new imports start here ###
from flask_restful import Api, Resource
### new imports end here ###

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

### new code begins here ###
api = Api(app)
### new code ends here ###

class AllHotels(Resource):
    def get(self):
        hotels = Hotel.query.all()
        hotel_dict_list = [hotel.to_dict(only=('id', 'name')) for hotel in hotels]
        return make_response(hotel_dict_list, 200)
    
    def post(self):
        new_hotels = Hotel(name=request.json.get('name'))
        db.session.add(new_hotels)
        db.session.commit()
        hotel_dict = new_hotels.to_dict(only=('id', 'name'))
        return make_response(hotel_dict, 201)

api.add_resource(AllHotels, '/hotels')

class HotelByID(Resource):
    def get(self, id):
        hotel = db.session.get(Hotel, id)
        if hotel:
                response_body = hotel.to_dict(rules=('-reviews.hotel', '-reviews.customer'))
                # Add in the association proxy data (The hotel's customers)
                response_body['customers'] = [customer.to_dict(only=('id', 'first_name', 'last_name')) for customer in hotel.customers]
                return make_response(response_body, 200)
        else:
            response_body = {
            "error": "Hotel Not Found"
             }
            return make_response(response_body, 404)
        
    def patch(self, id):
        hotel = db.session.get(Hotel, id)
        if hotel:
            for attr in request.json:
                setattr(hotel, attr, request.json[attr])
            db.session.commit()

            response_body = hotel.to_dict(only=('id', 'name'))
            return make_response(response_body, 201)
        else:
            response_body = {
            "error": "Hotel Not Found"
            }
            return make_response(response_body, 404)
        
    def delete(self, id):
        hotel = db.session.get(Hotel, id)
        if hotel:
            db.session.delete(hotel)
            db.session.commit()
            return make_response({}, 204)
        else:
            response_body = {
            "error": "Hotel Not Found"
            }
            return make_response(response_body, 404)

api.add_resource(HotelByID, '/hotels/<int:id>')

class AllCustomers(Resource):
    def get(self):
        customers = Customer.query.all()
        customer_list_dict = [customer.to_dict(only=('id', 'first_name', 'last_name')) for customer in customers]
        return make_response(customer_list_dict, 200)
    
    def post(self):
        new_customer = Customer(first_name=request.json.get('first_name'), last_name=request.json.get('last_name'))
        db.session.add(new_customer)
        db.session.commit()
        response_body = new_customer.to_dict(only=('id', 'first_name', 'last_name'))
        return make_response(response_body, 201)

api.add_resource(AllCustomers, '/customers')

class CustomersByID(Resource):

    def get(self, id):
        customer = db.session.get(Customer, id)
        if customer:
            body = customer.to_dict(only=('id', 'first_name', 'last_name'))
            return make_response(body, 200)
        else:
            body = { "message": f"Customer {id} was not found."}
            return make_response(body, 404)
        
    def patch(self, id):
        customer = db.session.get(Customer, id)
        if customer:
            for attr in request.json:
                setattr(customer, attr, request.json[attr])
            db.session.commit()
            body = customer.to_dict(only=('id', 'first_name', 'last_name'))
            return make_response(body, 200)
        else: 
            body = { "message": f"Customer {id} was not found."}
            return make_response(body, 404)
        
    def delete(self, id):
        customer = db.session.get(Customer, id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
            body = {}
            return make_response(body, 204)
        else:
            body = { "message": f"Customer {id} was not found."}
            return make_response(body, 404)

api.add_resource(CustomersByID, '/customers/<int:id>')

class AllReviews(Resource):

    def get(self):
        reviews = Review.query.all()
        review_dict_list = [review.to_dict(rules=('-customer.reviews', '-hotel.reviews')) for review in reviews]
        return make_response(review_dict_list, 200)
    
    def post(self):
        new_review = Review(rating=request.json.get('rating'), text=request.json.get('text'), hotel_id=request.json.get('hotel_id'), customer_id=request.json.get('customer_id'))
        db.session.add(new_review)
        db.session.commit()
        body = new_review.to_dict(rules=('-customer.reviews', '-hotel.reviews'))
        return make_response(body, 201)

api.add_resource(AllReviews, '/reviews')

# GET review by id with /reviews/<int:id>
class ReviewByID(Resource):

    def get(self, id):
        reviews = db.session.get(Review, id)
        if reviews:
            body = reviews.to_dict(rules=('-hotel.reviews', '-customer.reviews'))
            return make_response(body, 200)
        else:
            body = {"error": f"Review {id} not found"}
            return make_response(body, 404)
    
    def patch(self, id):
        review = db.session.get(Review, id)
        if review:
            for attr in request.json:
                setattr(review, attr, request.json[attr])
            db.session.commit()
            body = review.to_dict(rules=('-hotel.reviews', '-customer.reviews'))
            return make_response(body, 200)
        else:
            body = {"error": f"Review {id} not found."}

    def delete(self, id):
        review = db.session.get(Review, id)
        if review:
            db.session.delete(review)
            db.session.commit()
            body = {}
            return make_response(body, 204)
        else:
            body = {"error": f"Review {id} not found."}
            return make_response(body, 404)

api.add_resource(ReviewByID, '/reviews/<int:id>')

if __name__ == "__main__":
    app.run(port=7777, debug=True)