from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

# Настройка подключения к MongoDB
client = MongoClient('mongodb://localhost/animalshelter')
db = client.animalshelter
products_collection = db.products

# Маршрут для получения списка продуктов
@app.route('/api/products', methods=['GET'])
def get_products():
    products = list(products_collection.find())
    for product in products:
        product['_id'] = str(product['_id'])
    return jsonify(products)

# Маршрут для добавления нового продукта
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    product = {
        "name": data.get('name'),
        "price": data.get('price'),
        "image": data.get('image')
    }
    result = products_collection.insert_one(product)
    product['_id'] = str(result.inserted_id)
    return jsonify(product), 201

if __name__ == '__main__':
    app.run(debug=True)
