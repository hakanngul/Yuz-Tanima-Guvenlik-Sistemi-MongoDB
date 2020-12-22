from Interfaces.ICommonMethods import ICommonMethods
from Database.DataBaseConnection import CreateConnection
import mysql.connector


class CommonMethods(ICommonMethods):

    def adminLogin(self, username, password):
        cnx, cursor = CreateConnection()
        print("test2")
        sql = "Select * from admin where username=%s and password=%s"
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

    def supervisorLogin(self, username, password):
        cnx, cursor = CreateConnection()
        sql = "Select * from supervisor where username=%s and password=%s"
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
        print("***")
        print(username)
        print("***")
        sql = "Select * from supervisor where username=%s"
        try:
            print("Test checkusername")
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("Error =>", err)
            return err
        finally:
            cnx.close()

    @staticmethod
    def checkEmail(email):
        cnx, cursor = CreateConnection()
        print("***")
        print(email)
        print("***")
        sql = "Select * from supervisor where email=%s"
        try:
            print("Test check Email")
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("Error =>", err)
            return err
        finally:
            cnx.close()

    def logout(self):
        pass
