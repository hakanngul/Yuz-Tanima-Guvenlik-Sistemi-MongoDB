import pymongo

from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId


def CreateConnection():
    db = MongoClient(
        "mongodb+srv://hakangul:J0tdnWc4dqpMni11@cluster0.wvlyd.mongodb.net/node-app?retryWrites=true&w=majority")
    myDb = db["python-project"]
    return myDb


# myDb = CreateConnection()
# myCollection = myDb["products"]
# result = myCollection.find()
from uuid import uuid4

# db = CreateConnection()["users"]

# result = db["users"].insert_one({
#     "username": "admin3",
#     "password": "123123",
#     "email": "eragoln12@gmail.com"
# })
# filter = {"username": "yusuf"}

# resp = db.find_one({
#     "username": {
#         "$eq": "admin"
#     },
#     "password": {
#         "$eq": "12312312"
#     }
# })
# print(resp)
