#!/usr/bin/env python3

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Welcome to my website!</h1>'

@app.route('/another_page')
def different_page():
  return '<h1>This is a different page.</h1>'

@app.route('/intro/<string:name>')
def intro(name):
  return f'<h1>Hi! My name is {name}!</h1>', 200

@app.route('/intro/<string:name>/<int:age>')
def hello(name, age):
  return f'<h1>Hi! My name is {name} and my age is {age}</h1>', 200

@app.route('/greeting/<string:first_name>/<string:last_name>')
def greeting(first_name, last_name):
  return f"Greetings, {first_name} {last_name}!"

@app.route('/count_and_square/<int:number>')
def count_and_square(number):
  numbers = '\n'.join(str(num * num) for num in range(1, number + 1))
  return numbers

if __name__ == "__main__":
  app.run(port=7777, debug=True)
