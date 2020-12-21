from Interfaces.ISuperVisor import ISuperVisor
from Interfaces.IPerson import IPerson
from Database.DataBaseConnection import CreateConnection
import mysql.connector


class SuperVisor(ISuperVisor, IPerson):

    def __init__(self):
        super(SuperVisor).__init__()

    def register(self):
        import uuid
        cnx, cursor = CreateConnection()
        userid = uuid.uuid4().hex
        sql = "INSERT INTO kisi(id,full_name,username,password,email,phone,user_role)VALUES (%s,%s,%s,%s,%s,%s,%s)"
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
