from IPerson import IPerson
from bson.objectid import ObjectId


class IWorker(IPerson):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vardiya = kwargs.get("vardiya")
        self.user_role = "İşçi"

    def save(self): raise NotImplementedError

    def edit(self): raise NotImplementedError

    def delete(self): raise NotImplementedError

    def getWorker(self, _id): raise NotImplementedError
