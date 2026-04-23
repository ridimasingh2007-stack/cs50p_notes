# OOP ---

# def main():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     print(f"{name} from {house}")

# def get_name():
#     return input("What is your name? ")

# def get_house():
#     return input("What is your house? ")

# if __name__ == "__main__":
#     main()

# def main():
#     name, house = get_student() # unpacking -- allows you to assign values from a sequence (like a tuple) to multiple variables in a single line of code.
#     print(f"{name} from {house}")

# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     return name, house
    
# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     if student[0] == "Harry":
#         student[1] = "Gryffindor"
#     print(f"{student[0]} from {student[1]}")

   

# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     return [name, house] # a tuple is immutable -- cannot be changed after it is created, while a list is mutable -- can be changed after it is created.
    
# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()

#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     student = {}
#     student["name"] = input("What is your name? ")
#     student["house"] = input("What is your house? ")
#     return student
    
# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     if student["name"] == "Harry":
#         student["house"] = "Gryffindor"

#     print(f"{student['name']} from {student['house']}")

# def get_student():
    
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()

# Class -- a blueprint for pices of data and functionality that can be created and used in a program. It defines the structure and behavior of objects that are created from it.
# it is a way to create your own data types and functions that operate on that data. It allows you to create objects that have both data (attributes) and behavior (methods) associated with them.

# Object -- an instance of a class. It is a specific piece of data that is created from a class and has its own unique identity and state.
#  An object can have attributes (data) and methods (functions) that operate on that data.


# class Student:
#     ....
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     student = Student() # here we are creating object of the Student class and assigning it to the variable student.
#     student.name = input("What is your name? ") # here . is used to access the attributes of the student object and assign values to them.
#     student.house = input("What is your house? ")
#     return student

# if __name__ == "__main__":
#     main()

# method -- a function that is defined inside a class and operates on the data (attributes) of an object. 
# It is a way to define behavior for objects created from a class.

# class Student:
#     def __init__(self, name, house):
#     # __init__ is a special method in Python that is called when an object is created from a class. It is used to initialize the attributes of the object. The self parameter refers to the instance of the class that is being created.
#         if not name:
#             raise ValueError("Missing name")
        
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
        
#         self.name = name
#         self.house = house
        
# def main():
 #     student = get_student()
 #     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self, name, house, patronus):
#         if not name:  
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")   
#         self.name = name
#         self.house = house
#         self.patronus = patronus
#         self.house = house
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#     def charm(self):
#         match self.patronus.lower():
#             case "stag":
#                 return "🐎" 
#             case "otter":
#                 return "🦦 "  
#             case "jack russell terrier":
#                 return "🐕"
#             case _:
#                 return "/"
# def main():
#     student = get_student()
#     print("Expecto Patronum!")
#     print(student.charm())

# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     patronus = input("What is your patronus? ")
#     return Student(name, house, patronus)

# if __name__ == "__main__":
#     main()


# class Student:
#         def __init__(self, name, house):
#             self.name = name
#             self.house = house
            
#         def __str__(self):
#             return f"{self.name} from {self.house}"
#         @property
#         def name(self):
#             return self._name

#         @name.setter
#         def name(self, name):
#             if not name:
#                 raise ValueError("Missing name")
#             self._name = name

#         @property
#         def house(self):
#             return self._house

#         @house.setter
#         def house(self, house):
#             if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#                 raise ValueError("Invalid house")
#             self._house = house

# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()

# import random

# class Hat:
#     houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#     @classmethod
#     def sort(cls, name):   
#         print(name, "is in", random.choice(cls.houses))

# Hat.sort("Harry")

# class Student:
#         def __init__(self, name, house):
#             self.name = name
#             self.house = house
            
#         def __str__(self):
#             return f"{self.name} from {self.house}"
        
#         @classmethod
#         def get(cls):
#             name = input("What is your name? ")
#             house = input("What is your house? ")
#             return cls(name, house)
# def main():
#     student = Student.get()
#     print(student)
# if __name__ == "__main__":
#     main()

# inheritance -- a way to create a new class that is a modified version of an existing class.
#  The new class (called the child class) inherits all the attributes and methods of the existing class (called the parent class) and can also have its own unique attributes and methods.

# class Wizard:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name

# class Student(Wizard):
#     def __init__(self, name, house):
#        super().__init__(name) # super() is a built-in function in Python that allows you to call a method from the parent class. In this case, we are calling the __init__ method of the Wizard class to initialize the name attribute of the Student class.
#        self.house = house      
# class Professor(Wizard):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
# wizard = Wizard("Albus")
# student = Student("Harry", "Gryffindor")
# professor = Professor("severus", "Defense Against the Dark Arts")

# operator overloading -- a way to define how operators (like +, -, *, etc.) should behave when applied to objects of a class.
class Valut: 
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Valut(galleons, sickles, knuts)


potter = Valut(100,15,200)
print(potter)

weasley = Valut(5, 10, 20)
print(weasley)
  
# galleons = potter.galleons + weasley.galleons
# sickles = potter.sickles + weasley.sickles
# knuts = potter.knuts + weasley.knuts

total = potter + weasley
print(total)