from Interfaces.IWorker import IWorker
from Database.DataBaseConnection import CreateConnection
from bson.objectid import ObjectId


class Worker(IWorker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save(self):
        # TODO: TCKNO - Adı Soyadı - Vardiyası
        print(self.full_name)
        self.collection = CreateConnection()["isciler"]
        res = self.collection.insert_one({
            "TcNo": self.tcNo,
            "full_name": self.full_name,
            "vardiya": self.vardiya,
            "user_role": self.user_role,
            "imagePath": self.imagePath
        })
        if res is not None:
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

    def getWorker(self, TcNo):
        x = self.collection.find_one({
            'TcNo': {"$eq": TcNo}
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
