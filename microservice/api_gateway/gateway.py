from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Routes for Currency Service
@app.route('/currency/<currency>/<price>', methods=['GET'])
def currency_service(currency, price):
    currency_url = f"http://currency_service:5003/currency/{currency}/{price}"
    response = requests.get(currency_url)
    return jsonify(response.json())

# Routes for Product Service
@app.route('/product/<int:id>', methods=['GET'])
def product_service(id):
    product_url = f"http://product_service:5002/product/{id}"
    response = requests.get(product_url)
    return jsonify(response.json())

# Routes for Inventory Service
@app.route('/inventory/<int:product_id>', methods=['GET'])
def inventory_service(product_id):
    inventory_url = f"http://inventory_service:5001/inventory/{product_id}"
    response = requests.get(inventory_url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
