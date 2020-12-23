class ISuperVisor:

    def save(self): raise NotImplementedError

    def createWorker(self): raise NotImplementedError

    def editWorker(self): raise NotImplementedError

    def deleteWorker(self): raise NotImplementedError

    def addWorkerToShift(self): raise NotImplementedError

    def removeWorkerFromShift(self): raise NotImplementedError

    def viewReport(self): raise NotImplementedError
