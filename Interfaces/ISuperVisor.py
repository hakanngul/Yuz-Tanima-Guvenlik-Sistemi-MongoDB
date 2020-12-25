from Interfaces.IPerson import IPerson


class ISuperVisor(IPerson):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.user_role = "admin"

    def save(self): raise NotImplementedError

    def createWorker(self, *args): raise NotImplementedError

    def editWorker(self, *args): raise NotImplementedError

    def deleteWorker(self, *args): raise NotImplementedError

    def addWorkerToShift(self, *args): raise NotImplementedError

    def removeWorkerFromShift(self, *args): raise NotImplementedError

    def viewReport(self): raise NotImplementedError
