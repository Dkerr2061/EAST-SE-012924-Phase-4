#!/usr/bin/env python3

from app import app
from models import db, Example, Hotel, Customer

with app.app_context():
    # Write code to seed hotels into the hotels table in the database
    Example.query.delete()
    Hotel.query.delete()
    Customer.query.delete()


    example1 = Example(columnname="Hello World", price= 5.99)
    example2 = Example(columnname="Good night", price= 12)
    example3 = Example(columnname="Pizza", price= 159.65)

    hotel1 = Hotel(name='Marriott')
    hotel2 = Hotel(name='Caribe Hilton')
    hotel3 = Hotel(name='Melia')

    customer1 = Customer(first_name='David', last_name='Giannoni')
    customer2 = Customer(first_name='Natalia', last_name='Giannoni')
    customer3 = Customer(first_name='Emilio', last_name='Kerr')

    db.session.add_all([customer1, customer2, customer3])
    db.session.add_all([example1, example2, example3])
    db.session.add_all([hotel1, hotel2, hotel3])
    
    db.session.commit()
    
    print("🌱 Hotels successfully seeded! 🌱")