from Interfaces.ISuperVisor import ISuperVisor
from Interfaces.IPerson import IPerson
from Database.DataBaseConnection import CreateConnection


class SuperVisor(IPerson, ISuperVisor):

    def __init__(self, username=None, password=None):
        super(SuperVisor).__init__()
        self.username = username
        self.password = password

    def save(self):
        sql = {
            "full_name": self.full_name,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "phone": self.phone,
            "user_role": self.user_role
        }
        # print(sql)
        db = CreateConnection()
        res = db["users"].insert_one(sql)
        if res:
            print(f'{self.full_name} user is created')
            return True
        else:
            return False

    def createWorker(self):
        pass

    def editWorker(self):
        pass

    def deleteWorker(self):
        pass

    def addWorkerToShift(self):
        pass

    def removeWorkerFromShift(self):
        pass

    def viewReport(self):
        pass
