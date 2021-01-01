from Interfaces.IWorker import IWorker
from Database.DataBaseConnection import CreateConnection
from bson.objectid import ObjectId


class Worker(IWorker):
    def __init__(self, tcNo=None):
        super().__init__()
        self.collection = CreateConnection()["isciler"]
        if tcNo is not None:
            self.tcNo = tcNo
            self.getWorker()

    def save(self):
        # TODO: TCKNO - Adı Soyadı - Vardiyası
        print(self.full_name)

        res = self.collection.insert_one({
            "TcNo": self.tcNo,
            "full_name": self.full_name,
            "vardiya": self.vardiya,
            "user_role": self.user_role,
            "imagePath": self.imagePath + "/"
        })
        if res is not None:
            print(f'{self.full_name} user is created')
            return True
        else:
            return False

    def edit(self):
        res = self.collection.find_one_and_update({"_id": ObjectId(self.id)}, {
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

    def addShift(self):
        pass

    def delete(self):
        res = self.collection.find_one_and_delete({
            '_id': ObjectId(self.id)
        })
        if res:
            return True
        else:
            return False

    def getWorker(self):
        isci = self.collection.find_one({
            "TcNo": self.tcNo
        })
        print(isci)
        self.id = isci['_id']
        self.tcNo = isci['TcNo']
        self.full_name = isci['full_name']
        self.vardiya = isci['vardiya']
        self.user_role = isci['user_role']
        self.imagePath = isci['imagePath']



    def getAllWorker(self):
        return list(self.collection.find())
