from pymongo import MongoClient

client = MongoClient("mongodb://localhost/animalshelter")
db = client["animalshelter"]
products_collection = db["products"]