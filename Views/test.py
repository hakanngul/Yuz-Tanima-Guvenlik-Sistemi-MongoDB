from Controllers.SuperVisor import SuperVisor

# test = SuperVisor()
# users = test.getAllSuperVisor()
#
# print(users[0])
# print(users[0]['_id'])
# print(type(users[0]['_id']))

# res = test.editSupervisorShift(users[0]['_id'], "Gece")

# print(res)


from Database.DataBaseConnection import CreateConnection

collection = CreateConnection()["vardiya"]
vardiya = "Gece"
collection = collection.find_one({
    "name": vardiya
})

print(collection['sorumlu'])
