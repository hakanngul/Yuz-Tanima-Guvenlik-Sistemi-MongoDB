from Interfaces.ICommonMethods import ICommonMethods
from Database import DataBaseConnection
import mysql.connector
from Database.test import CreateConnection


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
            if result is not None:
                return True
            else:
                return False
        else:
            print("Username gelmedi")

    def logout(self):
        pass
