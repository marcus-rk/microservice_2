from flask import Flask, jsonify, request, make_response
import requests
from service.products import fetch_products

app = Flask(__name__)

product_db = []
data = requests.get('https://dummyjson.com/products')
product_db = data.json()['products'] 

#find alle products
@app.route('/products', methods=['GET'])
def get_all_products():
    products = fetch_products()
    return jsonify(products), 200

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    products = fetch_products()
    return jsonify([product for product in products if product['id'] == id]), 200

@app.route('/product/search/<string:title>', methods=['GET'])
def get_product_by_title(title):
    products = fetch_products()
    for product in products:
        if product['title'].lower() == title.lower():
            return jsonify(product), 200

if __name__ == '__main__':
    #init_db()
    app.run(host='0.0.0.0', port=5002)