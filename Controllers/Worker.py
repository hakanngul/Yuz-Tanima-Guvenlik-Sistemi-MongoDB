from Interfaces.IWorker import IWorker
from Database.DataBaseConnection import CreateConnection
from bson.objectid import ObjectId


class Worker(IWorker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.collection = CreateConnection()["workers"]

    def save(self):
        # TODO: TCKNO - Adı Soyadı - Vardiyası
        sql = {
            "TcNo": self.tcNo,
            "full_name": self.full_name,
            "vardiya": self.vardiya,
            "user_role": self.user_role,
            "imagePath": self.imagePath
        }
        res = self.collection.insert_one(sql)
        if res:
            print(f'{self.full_name} user is created')
            return True
        else:
            return False

    def edit(self):
        res = self.collection.find_one_and_update({"_id": ObjectId(self._id)}, {
            '$set': {
                "TcNo": self.tcNo,
                "full_name": self.full_name,
                "vardiya": self.vardiya
            }
        })
        if res:
            return True
        else:
            return False

    def delete(self):
        res = self.collection.find_one_and_delete({
            '_id': ObjectId(self._id)
        })
        if res:
            return True
        else:
            return False

    def getWorker(self, _id):
        x = self.collection.find_one({
            '_id': {"$eq": ObjectId(_id)}
        })
        if x:
            self._id = x.get('_id')
            self.tcNo = x.get('tcNO')
            self.full_name = x.get('full_name')
            self.vardiya = x.get('vardiya')
            self.user_role = x.get('user_role')
            self.imagePath = x.get('imagePath')
            return self
        else:
            return False
