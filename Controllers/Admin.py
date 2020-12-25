from Interfaces.IAdmin import IAdmin
from Database.DataBaseConnection import CreateConnection


class Admin(IAdmin):

    def __init__(self):
        super(Admin).__init__()

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

    def getSupervisor(self):
        user = CreateConnection()["users"].find_one({
            "username": {"$eq": self.username},
            "password": {"$eq": self.password},
            "user_role": {"$eq": "admin"}
        })
        return user

    def addUserToSuperVisorShift(self, data):
        from Controllers.SuperVisor import SuperVisor
        user = SuperVisor()
        # getSupervisor2(data[0])

        shiftCollection = CreateConnection()["shift"]
        res = shiftCollection.find_one_and_update({
            "name": {"$eq": data[-1]}
        }, {
            '$set': {
                "supervisor": user._id
            }
        })

        if res:
            return True
        else:
            return False

    def removeUserToSuperVisorShift(self, data):
        pass

    def viewReport(self):
        pass
