#File I/O

# names = []
# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("what's your name? ")
# # open -- opens a file in with all the contents get saved
# file = open("name.txt", "a") # "w" -- for write "a" append
# file.write(f"{name}\n")
# file.close() #-- this also saves the file 

# with -- to automatically open and close the file

# name = input("what's your name? ")

# with open("name.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("name.txt", "r") as file:
#     lines = file.readlines()
# for line in lines:
#     print("hello,", line.rstrip()) # line.rstrip is used for keeping no space in between two lines

# with open("name.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names):
#     print(f"Hello,{name}")

# Simpler way --
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())

# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
# #         print(f"{row[0]} is in {row[1]}")
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house} 
#         students.append(student)

# def get_name(student): # for sorting according to student name we defined their name 
#     return student["name"]

# for student in sorted(students, key=get_name): # key is used here to specify what are we sorting for ex: we are here sorting names, we can also sort house!
#     print(f"{student['name']} is in {student['house']}")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house} 
#         students.append(student)

# for student in sorted(students, key=lambda student: student["name"]): # lambda is a function but it is not named, it can used many times and we further specify our fuction parameter.
#     print(f"{student['name']} is in {student['house']}")

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]): 
#     print(f"{student['name']} is in {student['home']}


# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]}) # named the columns .. same logic 0 - name and 1 - home

# for student in sorted(students, key=lambda student: student["name"]): 
#     print(f"{student['name']} is in {student['home']}")

# import csv 

# name = input("What's your name? ")
# home = input("Where's your name? ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# import csv 

# name = input("What's your name? ")
# home = input("Where's your name? ")

# with open("students.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name,"home": home})

# * Pillow --- python lib for image files

import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
