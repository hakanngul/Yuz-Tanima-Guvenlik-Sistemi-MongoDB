from Kisi import Kisi


class Isci(Kisi):
    def __init__(self, foto_path, full_name, email_adres, telefon, age, user_rol):
        super().__init__(full_name, email_adres, telefon, age, user_rol)
        self.foto_path = foto_path
