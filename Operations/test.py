import Admin
from Database import DataBaseConnection

test = Admin.Admin()

test = test.login("test", "123456")
print(test[1])
