import os

path = os.getcwd().split("\\")[:-1]

print(path)

birlestir = ""
# for i in path:
#    birlestir += i +"/"

birlestir = '/'.join(path)
print(birlestir)
