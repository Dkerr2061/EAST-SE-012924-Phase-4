#!/usr/bin/env python3

from app import app
from models import db, Hotel, Customer, Review

with app.app_context():
    Hotel.query.delete()
    Customer.query.delete()
    Review.query.delete()

    hotel1 = Hotel(name="Marriott")
    hotel2 = Hotel(name="Hampton Inn")
    hotel3 = Hotel(name="The Chanler at Cliff Walk")

    customer1 = Customer(first_name="Alice", last_name="Baker")
    customer2 = Customer(first_name="Bob", last_name="Willis")
    customer3 = Customer(first_name="Cindy", last_name="Davidson")

    review1 = Review(rating=5, text="Best hotel ever!", hotel_id=1, customer_id=1)
    review2 = Review(rating=4, text="Good, but not the best.", hotel_id=1, customer_id=2)
    review3 = Review(rating=2, text="Worst place ever!", hotel_id=2, customer_id=3)
    review4 = Review(rating=2, text="Not as good as I remembered", hotel_id=1, customer_id=1)
    
    db.session.add_all([hotel1, hotel2, hotel3])
    db.session.add_all([customer1, customer2, customer3])
    db.session.add_all([review1, review2, review3, review4])

    db.session.commit()
    print("🌱 Hotels, Reviews, and Customers successfully seeded! 🌱")