from Interfaces.IPerson import IPerson


class IAdmin(IPerson):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.user_role = "admin"

    def save(self): raise NotImplementedError

    def addUserToSuperVisorShift(self, data): raise NotImplementedError

    def removeUserToSuperVisorShift(self, data): raise NotImplementedError

    def viewReport(self): raise NotImplementedError
