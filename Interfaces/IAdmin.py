class IAdmin:

    def register(self): raise NotImplementedError

    def createUser(self): raise NotImplementedError

    def editUser(self): raise NotImplementedError

    def deleteUser(self): raise NotImplementedError

    def addUserToSuperVisorShift(self): raise NotImplementedError

    def removeUserToSuperVisorShift(self): raise NotImplementedError

    def viewReport(self): raise NotImplementedError
