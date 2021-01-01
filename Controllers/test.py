from bson import ObjectId

from Controllers.Worker import Worker
from Database.DataBaseConnection import CreateConnection

test = CreateConnection()["isciler"]
no = "83469768934"
id = ObjectId("5fef3398f8204d5e7e332d12")

isci = test.find_one({
    "_id": id
})
print(isci)


test.update_one({
                "_id": id
            }, {"$set": {"vardiya": "yeniVardiya"}})
