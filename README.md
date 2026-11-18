# E-Commerce Shopping Cart REST API

## Project Description
A Python Flask-based REST API for managing an e-commerce shopping cart. It supports product listing, adding products to the cart, cart management, stock validation, and checkout with discount and GST calculations.

## Technologies Used
- Python
- Flask
- REST API
- Postman
- Git
- GitHub

## Features
- View all available products.
- Add products to the shopping cart.
- View shopping cart details.
- Validate product IDs.
- Validate positive quantities.
- Check product stock availability.
- Prevent checkout with an empty cart.
- Apply a 10% discount on orders above ₹1000.
- Calculate 5% GST.
- Generate the final checkout bill.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/products` | View all products |
| POST | `/cart/add` | Add product to cart |
| GET | `/cart` | View shopping cart |
| POST | `/checkout` | Checkout and generate bill |

## Installation

1. Clone the repository:

```bash
git clone https://github.com/rahulx27/-Ecommerce_API_Testing.git
```

2. Navigate to the project folder:

```bash
cd -Ecommerce_API_Testing
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
python app.py
```

7. Open the API:

`http://127.0.0.1:5000/`

## Postman API Testing

The project includes a Postman collection containing 9 API requests.

Collection location:

`postman/My Collection.postman_collection.json`

### How to Import
1. Open Postman.
2. Click Import.
3. Select the JSON collection from the postman folder.
4. Import the collection.
5. Run the collection using Collection Runner.

## API Testing Results

All API requests were tested successfully using Postman.

| Test Result | Count |
|---|---:|
| Total Tests | 29 |
| Passed | 29 |
| Failed | 0 |
| Errors | 0 |

**Overall Result: 100% Tests Passed**

## Developed By

Rahul Yadav

## Repository

GitHub: https://github.com/rahulx27/-Ecommerce_API_Testing