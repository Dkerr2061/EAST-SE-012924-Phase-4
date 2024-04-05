# Lecture # 5 - REST APIs with Flask

## Lecture Topics

- Building REST APIs with `flask-restful`
- Retrieve with `flask-restful` (handling `GET` requests)
- Create with `flask-restful` (handling `POST` requests)
- Update with `flask-restful` (handling `PATCH` requests)
- Delete with `flask-restful` (handling `DELETE` requests)

## Setup

1. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then enter the command `pipenv install` in your terminal to install the required packages.

2. Now that your `pipenv` virtual environment is ready to use, enter the command `pipenv shell` in your terminal to enter the virtual environment.

3. Enter the command `cd server` in your terminal to move into the server directory.

4. Run these two terminal commands while in the `server` directory:

```
export FLASK_APP=app.py

export FLASK_RUN_PORT=7777
```

## Deliverables

1. Refactor your code for the `/hotels` route's `all_hotels()` view, instead using `flask_restful` to create an `AllHotels` Resource that contains a `get()` method and a `post()` method. The `get()` method should be able to retrieve all hotels and return the appropriate response and status code, same as before. The `post()` method should be able to add a new hotel to the database and return the appropriate response and status code, same as before.

2. Refactor your code for the `/hotels/<int:id>` route's `hotel_by_id()` view, instead using `flask_restful` to create a `HotelByID` Resource that contains a `get()` method, a `patch()` method, and a `delete()` method. The `get()` method should be able to find a hotel by its `id` and return the appropriate response and status code, same as before. The `patch()` method should be able to find a hotel by its `id`, update it, and return the appropriate response and status code, same as before. The `delete()` method, should be able to find a hotel by its `id`, delete it, and return the appropriate response and status code, same as before. For the `get()`, `patch()`, and `delete()` methods, if the hotel is not found, return the appropriate response and status code, same as before.

3. Refactor your code for the `/customers` route's `all_customers()` view, instead using `flask_restful` to create an `AllCustomers` Resource that contains a `get()` method and a `post()` method. The `get()` method should be able to retrieve all customers and return the appropriate response and status code, same as before. The `post()` method should be able to add a new customer to the database and return the appropriate response and status code, same as before.

4. Refactor your code for the `/customers/<int:id>` route's `customer_by_id()` view, instead using `flask_restful` to create a `CustomerByID` Resource that contains a `get()` method, a `patch()` method, and a `delete()` method. The `get()` method should be able to find a customer by its `id` and return the appropriate response and status code, same as before. The `patch()` method should be able to find a customer by its `id`, update it, and return the appropriate response and status code, same as before. The `delete()` method, should be able to find a customer by its `id`, delete it, and return the appropriate response and status code, same as before. For the `get()`, `patch()`, and `delete()` methods, if the customer is not found, return the appropriate response and status code, same as before.

5. Refactor your code for the `/reviews` route's `all_reviews()` view, instead using `flask_restful` to create an `AllReviews` Resource that contains a `get()` method and a `post()` method. The `get()` method should be able to retrieve all reviews and return the appropriate response and status code, same as before. The `post()` method should be able to add a new review to the database and return the appropriate response and status code, same as before.

6. Refactor your code for the `/reviews/<int:id>` route's `review_by_id()` view, instead using `flask_restful` to create a `ReviewByID` Resource that contains a `get()` method, a `patch()` method, and a `delete()` method. The `get()` method should be able to find a review by its `id` and return the appropriate response and status code, same as before. The `patch()` method should be able to find a review by its `id`, update it, and return the appropriate response and status code, same as before. The `delete()` method, should be able to find a review by its `id`, delete it, and return the appropriate response and status code, same as before. For the `get()`, `patch()`, and `delete()` methods, if the review is not found, return the appropriate response and status code, same as before.