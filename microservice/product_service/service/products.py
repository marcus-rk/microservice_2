import requests, os

PRODUCTS_API_URL = 'https://dummyjson.com/products/category/smartphones'
CURRENCY_SERVICE_URL = os.getenv('CURRENCY_SERVICE_URL')

def _convert_currency(currency, price):
    response = requests.get(f'{CURRENCY_SERVICE_URL}/currency/{currency}/{price}')
    data = response.json()
    return data["currency"]

def fetch_products():
    response = requests.get(PRODUCTS_API_URL)
    
    if response.status_code == 200:
        full_data = response.json()
        
        products = full_data if isinstance(full_data, list) else full_data.get('products', [])
        
        filtered_products = []
        for product in products:
            product_price = product["price"]
            
            filtered_products.append({
                "brand": product["brand"],
                "category": product["category"],
                "description": product["description"],
                "dimensions": product["dimensions"],
                "id": product["id"],
                "images": product["images"],
                "org_price": product["price"],
                "ddk_price": _convert_currency('dkk', int(product_price)),
                "tags": product["tags"],
                "thumbnail": product["thumbnail"],
                "title": product["title"],
                "weight": product["weight"]
            })
        return filtered_products
    return []