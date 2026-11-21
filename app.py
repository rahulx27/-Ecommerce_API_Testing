
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# --------------------------------
# PRODUCT DATABASE
# --------------------------------

products = {
    1: {"name": "Laptop", "price": 50000, "stock": 10},
    2: {"name": "Mouse", "price": 500, "stock": 20},
    3: {"name": "Keyboard", "price": 1000, "stock": 15},
    4: {"name": "Headphones", "price": 2000, "stock": 10}
}

cart = []


# --------------------------------
# CART SUMMARY
# --------------------------------

def get_cart_summary():

    subtotal = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    total_items = sum(
        item["quantity"] for item in cart
    )

    cart_details = []

    for item in cart:
        cart_details.append({
            **item,
            "total": item["price"] * item["quantity"]
        })

    return {
        "cart": cart_details,
        "total_items": total_items,
        "subtotal": subtotal
    }


# --------------------------------
# HOME PAGE
# --------------------------------

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "E-Commerce Shopping Cart API is Running!",
        "demo": "/demo",
        "products": "/products"
    })


# --------------------------------
# FRONTEND
# --------------------------------

@app.route("/demo", methods=["GET"])
def demo():

    return render_template("index.html")


# --------------------------------
# GET ALL PRODUCTS
# --------------------------------

@app.route("/products", methods=["GET"])
def get_products():

    return jsonify(products)


# --------------------------------
# ADD PRODUCT TO CART
# --------------------------------

@app.route("/cart/add", methods=["POST"])
def add_to_cart():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON input"}), 400

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if type(product_id) != int or product_id not in products:
        return jsonify({"error": "Invalid product ID"}), 400

    if type(quantity) != int or quantity <= 0:
        return jsonify({
            "error": "Quantity must be a positive integer"
        }), 400

    product = products[product_id]

    existing_item = next(
        (item for item in cart
         if item["product_id"] == product_id),
        None
    )

    current_quantity = (
        existing_item["quantity"] if existing_item else 0
    )

    if current_quantity + quantity > product["stock"]:
        return jsonify({"error": "Insufficient stock"}), 400

    if existing_item:
        existing_item["quantity"] += quantity

    else:
        cart.append({
            "product_id": product_id,
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })

    return jsonify({
        "message": "Product added successfully",
        **get_cart_summary()
    }), 201


# --------------------------------
# VIEW SHOPPING CART
# --------------------------------

@app.route("/cart", methods=["GET"])
def view_cart():

    return jsonify(get_cart_summary())


# --------------------------------
# UPDATE CART QUANTITY
# --------------------------------

@app.route("/cart/update", methods=["PUT"])
def update_cart():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON input"}), 400

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if type(product_id) != int or product_id not in products:
        return jsonify({"error": "Invalid product ID"}), 400

    if type(quantity) != int or quantity <= 0:
        return jsonify({
            "error": "Quantity must be a positive integer"
        }), 400

    item = next(
        (item for item in cart
         if item["product_id"] == product_id),
        None
    )

    if not item:
        return jsonify({"error": "Product not found in cart"}), 404

    if quantity > products[product_id]["stock"]:
        return jsonify({"error": "Insufficient stock"}), 400

    item["quantity"] = quantity

    return jsonify({
        "message": "Cart quantity updated successfully",
        **get_cart_summary()
    })


# --------------------------------
# REMOVE INDIVIDUAL PRODUCT
# --------------------------------

@app.route("/cart/remove", methods=["DELETE"])
def remove_from_cart():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON input"}), 400

    product_id = data.get("product_id")

    if type(product_id) != int or product_id not in products:
        return jsonify({"error": "Invalid product ID"}), 400

    item = next(
        (item for item in cart
         if item["product_id"] == product_id),
        None
    )

    if not item:
        return jsonify({"error": "Product not found in cart"}), 404

    cart.remove(item)

    return jsonify({
        "message": "Product removed successfully",
        **get_cart_summary()
    })


# --------------------------------
# CLEAR ENTIRE CART
# --------------------------------

@app.route("/cart/clear", methods=["DELETE"])
def clear_cart():

    cart.clear()

    return jsonify({
        "message": "Shopping cart cleared successfully",
        **get_cart_summary()
    })


# --------------------------------
# CHECKOUT AND GENERATE BILL
# --------------------------------

@app.route("/checkout", methods=["POST"])
def checkout():

    if not cart:
        return jsonify({"error": "Cart is empty"}), 400

    # Validate stock before checkout
    for item in cart:

        product = products[item["product_id"]]

        if item["quantity"] > product["stock"]:
            return jsonify({
                "error": f"Insufficient stock for {item['name']}"
            }), 400

    subtotal = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    # 10% discount for orders of Rs. 1000 or more
    discount = subtotal * 0.10 if subtotal >= 1000 else 0

    taxable_amount = subtotal - discount

    # 5% GST
    gst = taxable_amount * 0.05

    final_amount = taxable_amount + gst

    # Update product stock
    for item in cart:
        products[item["product_id"]]["stock"] -= item["quantity"]

    bill = {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "gst": round(gst, 2),
        "final_amount": round(final_amount, 2)
    }

    cart.clear()

    return jsonify({
        "message": "Order placed successfully",
        "bill": bill
    })


# --------------------------------
# RUN APPLICATION
# --------------------------------

if __name__ == "__main__":
    app.run(debug=True)
