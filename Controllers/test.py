from Database.DataBaseConnection import CreateConnection
from bson.objectid import ObjectId

user = CreateConnection()["users"]
vardiya = CreateConnection()["vardiya"]
degisecek_vardiya = "Gece"

eskiSorumlu = vardiya.find_one({
    "vardiya_adi": degisecek_vardiya
})["vardiya_sorumlu"]

print(eskiSorumlu)
print(type(eskiSorumlu))

user.find_one_and_update({
    "_id": ObjectId(eskiSorumlu)
}, {
    "$set": {"vardiya": "null"}
})

yeniSorumlu = "5fe349ce87b3d01ed73e1cec"
x = "5fe88825080f12b54025a52e"
user.find_one_and_update({
    "_id": ObjectId(yeniSorumlu)
}, {
    "$set": {"vardiya": degisecek_vardiya}
})
vardiya.update_one({
    "vardiya_adi": degisecek_vardiya
}, {
    "$set": {"vardiya_sorumlu": yeniSorumlu}
}
)
