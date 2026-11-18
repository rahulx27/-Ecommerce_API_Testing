# E-Commerce Shopping Cart API

## Project Description
A Python Flask-based REST API for managing an e-commerce shopping cart. It supports product listing, adding products to the cart, cart management, stock validation, and checkout with discount and GST calculations.

## Technologies Used
- Python
- Flask
- REST API
- Postman
- GitHub

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Check API status |
| GET | /products | View all products |
| POST | /cart/add | Add product to cart |
| GET | /cart | View shopping cart |
| POST | /checkout | Checkout and generate bill |

## Features
- Product listing
- Add products to shopping cart
- Quantity validation
- Product ID validation
- Stock availability checking
- Shopping cart management
- Automatic checkout
- 10% discount on orders above ₹1000
- 5% GST calculation
- Automatic bill generation

## Installation

1. Clone the repository.
2. Install dependencies:

   pip install -r requirements.txt

3. Run the application:

   python app.py

4. Open:

   http://127.0.0.1:5000/

## API Testing
All API endpoints w
ere tested using Postman.

**Final Test Results:**
- Total Tests: 29
- Passed: 29
- Failed: 0
- Errors: 0

## Developed By
Rahul Yadav