from bson import ObjectId

from Controllers.Worker import Worker
from Database.DataBaseConnection import CreateConnection
from Controllers.CommonMethods import CommonMethods
test = CreateConnection()["isciler"]


def getWorker2(idNo):
    collection = CreateConnection()["isciler"]
    isci = collection.find_one({
        "_id": idNo
    })
    return isci


def getVardiya(vardiyaAdi):
    collection = CreateConnection()["vardiya"]
    vardiya = collection.find_one({
        "vardiya_adi": vardiyaAdi
    })['vardiya_iscileri']
    return vardiya

data = getVardiya("Sabah")
isciler = []
for i in data:
    isciler.append(CommonMethods.getWorker(i))

print(isciler)
print(type(isciler))
print(len(isciler))


# from datetime import date
#
# today = date.today()
#
# # dd/mm/YY
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)

# from datetime import datetime
#
# # datetime object containing current date and time
# now = datetime.now()
#
# print("now =", now)
#
# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)