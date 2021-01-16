import os
from pathlib import Path

home = str(Path.home()) + "/.faceAnalytics/worker/"
print(home)
employees = []
home2 = "C:/Users/Hakan/.faceAnalytics/program/worker"
for r, d, f in os.walk(home2):  # r=root, d=directories, f = files
    for file in f:
        if '.jpg' in file:
            exact_path = r + "/" + file
            employees.append(exact_path)
        if '.png' in file:
            exact_path = r + "/" + file
            employees.append(exact_path)

print(employees)