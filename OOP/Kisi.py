import uuid


class Kisi:
    def __init__(self, full_name, email, telefon,  rol):
        self.id = uuid.uuid4()
        self.full_name = full_name
        self.email = email
        self.telefon = telefon
        self.rol = rol
