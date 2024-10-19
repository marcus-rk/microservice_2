from flask import Flask, jsonify, request
import requests, os

CURRENCY_SERVICE_URL = os.getenv('CURRENCY_SERVICE_URL')
PRODUCT_SERVICE_URL = os.getenv('PRODUCT_SERVICE_URL')
INVENTORY_SERVICE_URL = os.getenv('INVENTORY_SERVICE_URL')

app = Flask(__name__)

# Routes for Currency Service
@app.route('/currency/<string:currency>/<int:price>', methods=['GET'])
def currency_service(currency, price):
    currency_url = f'{CURRENCY_SERVICE_URL}/currency/{currency}/{price}'
    response = requests.get(currency_url)
    return jsonify(response.json())

# Routes for Product Service
@app.route('/products/<int:id>', methods=['GET'])
def product_service(id):
    product_url = f'{PRODUCT_SERVICE_URL}/products/{id}'
    response = requests.get(product_url)
    return jsonify(response.json())

# Routes for Inventory Service
@app.route('/inventory/<int:product_id>', methods=['GET'])
def inventory_service(product_id):
    inventory_url = f'{INVENTORY_SERVICE_URL}/stock/{product_id}'
    response = requests.get(inventory_url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
