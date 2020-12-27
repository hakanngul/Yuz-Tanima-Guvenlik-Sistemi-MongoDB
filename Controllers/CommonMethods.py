from Interfaces.ICommonMethods import ICommonMethods

from Database.DataBaseConnection import CreateConnection


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
