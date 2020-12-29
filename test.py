from Database.DataBaseConnection import CreateConnection
import os
from pathlib import Path
isciler = CreateConnection()["isciler"].find_one({
    'TcNo': {"$eq": "123456712"}
})
home = str(Path.home())
home = home + "/.faceAnalytics/program/worker/"

tcNo = "123123123"

home += tcNo
print(home)

try:
    reS: object = os.mkdir(home)
    print(reS)
except FileExistsError as err:
    print(err)
