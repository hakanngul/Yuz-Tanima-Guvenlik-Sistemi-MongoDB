from Interfaces.IAdmin import IAdmin
from Interfaces.IPerson import IPerson
from Database.DataBaseConnection import CreateConnection


class Admin(IAdmin, IPerson):

    def __init__(self, username=None, password=None):
        super(Admin).__init__()
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
        print(sql)
        try:
            db = CreateConnection()
            res = db["users"].insert_one(sql)
            if res:
                print(f'{self.full_name} user is created')
                return True
            else:
                return False
        except Exception as err:
            print(err)

    def createUser(self):
        pass

    def editUser(self):
        pass

    def deleteUser(self):
        pass

    def addUserToSuperVisorShift(self):
        pass

    def removeUserToSuperVisorShift(self):
        pass

    def viewReport(self):
        pass
