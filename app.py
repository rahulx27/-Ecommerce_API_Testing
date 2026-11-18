from flask import Flask, request, jsonify

app = Flask(__name__)

# Product database
products = {
    1: {"name": "Laptop", "price": 50000, "stock": 10},
    2: {"name": "Mouse", "price": 500, "stock": 20},
    3: {"name": "Keyboard", "price": 1000, "stock": 15},
    4: {"name": "Headphones", "price": 2000, "stock": 10}
}

cart = []


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "E-Commerce Shopping Cart API is Running!"
    })


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


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
        return jsonify({"error": "Quantity must be a positive integer"}), 400

    product = products[product_id]

    if quantity > product["stock"]:
        return jsonify({"error": "Insufficient stock"}), 400

    for item in cart:
        if item["product_id"] == product_id:
            if item["quantity"] + quantity > product["stock"]:
                return jsonify({"error": "Insufficient stock"}), 400

            item["quantity"] += quantity
            break
    else:
        cart.append({
            "product_id": product_id,
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })

    return jsonify({"message": "Product added successfully", "cart": cart}), 201


@app.route("/cart", methods=["GET"])
def view_cart():
    subtotal = sum(item["price"] * item["quantity"] for item in cart)

    return jsonify({
        "cart": cart,
        "subtotal": subtotal
    })


@app.route("/checkout", methods=["POST"])
def checkout():
    if not cart:
        return jsonify({"error": "Cart is empty"}), 400

    subtotal = sum(item["price"] * item["quantity"] for item in cart)

    discount = subtotal * 0.10 if subtotal >= 1000 else 0

    taxable_amount = subtotal - discount
    gst = taxable_amount * 0.05
    total = taxable_amount + gst

    bill = {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "gst": round(gst, 2),
        "final_amount": round(total, 2)
    }

    cart.clear()

    return jsonify({
        "message": "Order placed successfully",
        "bill": bill
    })


if __name__ == "__main__":
    app.run(debug=True)