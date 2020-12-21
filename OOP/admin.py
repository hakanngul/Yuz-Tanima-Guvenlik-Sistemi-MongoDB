
from Database.DataBaseConnection import CreateConnection

import uuid
from OOP.Kisi import Kisi


class Admin(Kisi):
    def __init__(self, full_name=None, username=None, email=None, telefon=None, rol=None, password=None):
        super().__init__(full_name, email, telefon, rol)
        self.username = username
        self.password = password

    def kayitOl(self):
        baglanti, cursor = CreateConnection()
        print("Veri geldi")
        k_id = uuid.uuid4().hex
        print(k_id, self.full_name, self.username, self.password, self.telefon, self.email, self.rol)
        sql = """
            INSERT INTO kisi SET id=%s,full_name=%s,username=%s,password=%s,email_adres=%s,telefon=%s,role=%s 
        """
        print("Veri geldi 2")
        try:
            result = cursor.execute(sql, (
                k_id, self.full_name, self.username, self.password, self.email, self.telefon, self.rol))
            baglanti.commit()
            print(str(result) + " kullanıcı eklendi")
        except ValueError:
            print("Kontrol öncesi")
        finally:
            baglanti.close()

    def checkUsername(self, username):
        baglanti, cursor = CreateConnection()
        sql = 'Select username from kisi where username=%s'
        print(username)
        result = cursor.execute(sql, (username))
        baglanti.close()
        if result:
            return False
        else:
            return True

    @staticmethod
    def login(username, password):
        baglanti, cursor = CreateConnection()
        print(username)
        print(password)
        sql = "Select * from kisi where username=%s and password=%s"
        cursor.execute(sql, (username, password))
        return cursor.fetchone()

    @staticmethod
    def raporGoruntule():
        pass
