from abc import ABC

from Interfaces.IAdmin import IAdmin
from Interfaces.IPerson import IPerson
from Database import DataBaseConnection
import mysql.connector


class Admin(IAdmin, IPerson, ABC):

    def __init__(self, username=None, password=None):
        super(Admin).__init__()
        self.username = username
        self.password = password

    def checkUserName(self, *args):
        return True

    def register(self):
        response = self.checkUserName()
        if response:
            import uuid
            cnx, cursor = DataBaseConnection.CreateConnection()
            userid = uuid.uuid4().hex
            sql = """
                    INSERT INTO kisi(id,full_name,username,password,email,phone,user_role)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                    """
            data = (userid, self.full_name, self.username, self.password, self.email, self.phone, self.user_role)
            print(data)
            try:
                cursor.execute(sql, data)
                cnx.commit()
                print(f'{cursor.rowcount} Kayıt Eklendi')
                return True
            except mysql.connector.Error as err:
                print("Error =>", err)
                return False
            finally:
                cnx.close()
        else:
            return False

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
