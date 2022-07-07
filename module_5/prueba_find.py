import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.cptgd.mongodb.net/")
mydb = myclient["pytech"]
mycol = mydb["students"]


# Print Students documents
#
docs = mycol.find({})
for doc in docs:
    print(doc)
