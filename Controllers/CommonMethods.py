from Interfaces.ICommonMethods import ICommonMethods

from Database.DataBaseConnection import CreateConnection

from bson.objectid import ObjectId


class CommonMethods(ICommonMethods):

    def Login(self, username, password, userType=False):
        db = CreateConnection()["users"]
        if userType:
            result = db.find_one({
                "username": {"$eq": username},
                "password": {"$eq": password},
                "user_role": {"$eq": "admin"}
            })
            if result:
                return result
            else:
                return False
        else:
            result = db.find_one({
                "username": {"$eq": username},
                "password": {"$eq": password}
            })
            if result:
                return result
            else:
                return False

    def checkAdmin(self):
        pass

    @staticmethod
    def vardiya_degistir(yeniSorumlu, degisecek_vardiya):
        global x
        print(yeniSorumlu)
        print(type(yeniSorumlu))
        print(degisecek_vardiya)

        user = CreateConnection()["users"]
        vardiya = CreateConnection()["vardiya"]
        eskiSorumlu = vardiya.find_one({
            "vardiya_adi": degisecek_vardiya
        })["vardiya_sorumlu"]
        print(eskiSorumlu)
        if len(eskiSorumlu) > 20:
            x = user.update_one({
                "_id": ObjectId(eskiSorumlu)
            }, {
                "$set": {"vardiya": "null"}
            })
            print(x)
        y = user.update_one({
            "_id": ObjectId(yeniSorumlu)
        }, {
            "$set": {"vardiya": degisecek_vardiya}
        })
        print(y)
        z = vardiya.update_one({
            "vardiya_adi": degisecek_vardiya
        }, {
            "$set": {"vardiya_sorumlu": yeniSorumlu}
        })
        print(z)

    @staticmethod
    def checkUserName(username):
        if username is not None:
            db = CreateConnection()["users"]
            result = db.find_one({
                "username": {
                    "$eq": username
                }
            })
            print(f'checkUserName {result}')
            if result is not None:
                return True
            else:
                return False
        else:
            print("Username gelmedi")

    @staticmethod
    def checkEmail(email):
        if email is not None:
            db = CreateConnection()["users"]
            result = db.find_one({
                "email": {
                    "$eq": email
                }
            })
            print(f'checkEmail {result}')
            if result is not None:
                return True
            else:
                return False
        else:
            print("Username gelmedi")

    def logout(self):
        pass
