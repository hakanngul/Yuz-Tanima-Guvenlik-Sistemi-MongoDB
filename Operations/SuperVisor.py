from Interfaces.ISuperVisor import ISuperVisor
from Interfaces.IPerson import IPerson


class SuperVisor(ISuperVisor, IPerson):

    def __init__(self):
        super(SuperVisor).__init__()

    def register(self):
        pass

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
