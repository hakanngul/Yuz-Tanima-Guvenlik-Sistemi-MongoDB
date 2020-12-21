from db import baglantiOlustur
import uuid


class VardiyaSorumlusu():
    def __init__(self, full_name, username, email_adres, telefon, rol, password):
        self.full_name = full_name
        self.email_adres = email_adres
        self.telefon = telefon
        self.rol = rol
        self.username = username
        self.password = password

    def kayitOl(self):
        baglanti, cursor = baglantiOlustur()
        k_id = uuid.uuid4().hex
        print(k_id, self.full_name, self.username, self.password, self.telefon, self.email_adres, self.rol)
        sql = """
            INSERT INTO kisi SET id=%s,full_name=%s,username=%s,password=%s,email_adres=%s,telefon=%s,role=%s 
        """
        print("Veri geldi 2")

        try:
            result = cursor.execute(sql, (
                k_id, self.full_name, self.username, self.password, self.email_adres, self.telefon, self.rol))
            baglanti.commit()
            print(str(result) + " kullanıcı eklendi")
        except ValueError:
            print("Kontrol öncesi")
        finally:
            baglanti.close()

    def checkUsername(self, username):
        baglanti, cursor = baglantiOlustur()
        sql = 'Select username from kisi where username=%s'
        print(username)
        result = cursor.execute(sql, (username))
        baglanti.close()
        if result:
            return False
        else:
            return True
