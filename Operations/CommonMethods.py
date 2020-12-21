from Interfaces.ICommonMethods import ICommonMethods
from Database.DataBaseConnection import CreateConnection
import mysql.connector


class CommonMethods(ICommonMethods):

    def login(self, username, password):
        cnx, cursor = CreateConnection()
        sql = "Select * from kisi where username=%s and password=%s"
        try:
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            if result:
                return result
            return False
        except mysql.connector.Error as err:
            print("Error =>", err)
            print("Test 3")
            return err
        finally:
            cnx.close()

    @staticmethod
    def checkUserName(username):
        cnx, cursor = CreateConnection()
        sql = "Select username from kisi where username=%s"
        try:
            result = cursor.execute(sql, (username,))
            if result:
                return False
            else:
                return True
        except mysql.connector.Error as err:
            print("Error =>", err)
            return err
        finally:
            cnx.close()

    def logout(self):
        pass
