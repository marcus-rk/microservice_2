from flask import Flask, jsonify, request, make_response
import requests
from db.db import init_db, read
import os

PRODUCT_SERVICE_URL = os.getenv('PRODUCT_SERVICE_URL')

app = Flask(__name__)

inventory_db = []
data = requests.get('https://dummyjson.com/products')

products = data.json().get('products')

for product in products:
    product_inventory = {
        'product_id': product.get('id'),
        'stock': product.get('stock')
    }

    inventory_db.append(product_inventory)

@app.route('/stock/<int:product_id>', methods=['GET'])
def find_stock_by_id(product_id):
    product = read(product_id)

    print("PRODUCT SERVICE URL:", f'{PRODUCT_SERVICE_URL}/products/{product_id}')
    print("REQUEST:", requests.get(f'{PRODUCT_SERVICE_URL}/products/{product_id}'))

    # Fetch product details from the product_service
    product_service = requests.get(f'{PRODUCT_SERVICE_URL}/products/{product_id}')

    response = {
        "product_detail" : product_service.json(),
        "stock" : product[1]
    }

    return jsonify(response), 200
        
@app.route('/change/<int:product_id>/<int:new_value>', methods=['POST'])
def change_product_stock(product_id, new_value):
    for product in products:
        if product['product_id']==product_id:
            product['stock']=new_value
            return jsonify({'message': 'product has been updated'})
        

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001)