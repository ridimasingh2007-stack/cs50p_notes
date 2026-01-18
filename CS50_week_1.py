# x = int(input("what's x? "))
# y = int(input("what's y? "))

# if x < y:
#     print("x is lesser than y")

# elif x > y:
#     print("x is greater than y")

# # elif x == y:
# #     print("x is equals to y")

# #  or use---> else like this:---

# else: 
#      print("x is equal to y")

# if x < y or x > y:
#     print("X is not equal y")

# else:
#     print("x is equal to y")

# if x == y:
#     print("x is equal to y")

# else:
#     print("x is not equal to y")
 


# score = int(input("score: "))

# if 90 <= score <= 100:
#    print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")
 
# other way --->

# if score >= 90:
#     print("Grade: A")
# elif score >= 80: 
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else: 
#     print("Grade: F")

# using operator %
# x = int(input("What's x? "))
# if x % 2 == 0:
#     print("even")
# else:
#     print("odd")

# def main():
#     x = int(input("What's x?"))
#     if is_even(x):
#         print("even")
#     else:
#         print("odd")

# # def is_even(n):
# #     if n % 2 == 0:
# #         return True
# #     else: 
# #         return False
    
# # main()

# #pythonic way -->
# # def is_even(n):
# #     return True if n % 2 == 0 else False
# # main()
# #or
# def is_even(n):
#     return n % 2 == 0
# main()

# match :--- it's a keyword

name = input("what's your name? ")

if name == "harry":
    print("gryffindor")
elif name == "hermione":
    print("gryffindor")
elif name == "Draco":
    print("slytherin")
else: 
    print("who?")

#or 

match name:
    # case "harry":
    #     print("gryffindor")
    # case "hermione":
    #     print("gryffindor")
    # case "ron":
    #     print("gryffindor")
    
    
#or this way --->
    case "harry" | "hermione" | "ron":
        print("gryffindor")
    case "draco":
        print("slytherin")

    case _:
        print("who?") 