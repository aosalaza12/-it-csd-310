import  pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.cptgd.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
print("Collection:", " ", db.list_collection_names())
