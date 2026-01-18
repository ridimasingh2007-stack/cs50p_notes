# loops:--

# while loop:-
# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1

# or 

# i = 1
# while i <= 3:
#     print("meow")
#     i += 1 

# List:--- data type

# for loop :--
# for i in [0, 1, 2]:
#     print("meow")

# for i in range(100):
#     print("meow")

#pythonic way:--
# for _ in range(3):
#     print("meow")
#or
#print("meow\n" * 3, end="")
# while True:
#     n = int(input("what's n? "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("meow")

# def main():
#     number = get_number()
#     meow(number)
# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             return n
# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

# using lists:---
# students = ["hermione", "harry", "ron"]

#print(students[0]) # it is used to get a single and specific str from lists, thde counting starts from 0

#for doing same thing but in a better way we use a loop..

# for student in students:
#     print(student)

# using len --
# for i in range(len(students)):
#     print(i + 1, students[i])

# using dict-- dict is a type od datatype. it is a collection of values that lets ypu associate keys with the values.
# students = ["hermione", "harry", "ron", "draco"]
# houses = ["gryffindir", "gryffindor", "gryffindor", "slytherin"]

# students = {
#     "hermione": "gryffindor",
#     "harry": "gryffindor",
#     "ron": "gryffindor",
#     "draco": "slytherin",
# }

# print(students["hermione"])
# print(students["harry"])

# for student in students:
#     print(student, students[student], sep=", ")

# mario game model(textual ofc):--
# for _ in range(3):
#     print("#") # this a 3 brick barrier for mario to jump over!

# def main():
#     print_column(3)
# def print_column(height):
#     print("#\n" * height, end="")
# main()

# mario gaining coins:
# def main():
#     print_row(4)
# def print_row(width):
#     print("?" * width)
# main()

# def main():
#     print_square(3)

# def print_square(size):
#     # for each row in square

#     for i in range(size):
#         # for each brick in row

#         for j in range(size):
#             #print brick

#             print("#", end="")

#         print() 


# main()

def main():
    print_square(3)
def print_square(size):
    for i in range(size):
        print("#" * size)

main()