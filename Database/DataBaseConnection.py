# import mysql.connector
from pymongo import MongoClient


# def CreateConnection():
#     db = mysql.connector.connect(host='localhost', user='root', password='', db='bitirmeprojesi')
#     cursor = db.cursor(buffered=True)
#     return db, cursor

def CreateConnection():
    db = MongoClient(
        "mongodb+srv://hakangul:J0tdnWc4dqpMni11@cluster0.wvlyd.mongodb.net/node-app?retryWrites=true&w=majority")
    myDb = db["python-project"]
    return myDb
