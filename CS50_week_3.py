#---"Exception" ---

# "ValueError" --- Error handling
#       |_ "try , except"
# try:
#     x = int(input("what's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# using else---
# try:
#     x = int(input("what's x? "))
   
# except ValueError:
#     print("x is not an integer")
# else:
#      print(f"x is {x}")

# while True: #try again and again util the user enters right input which is an integer here
#     try:
#         x = int(input("what's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break #when the input is correct the loop breaks and the bottom most print execures

# print(f"x is {x}")

# def main():
#     x = get_int()
#     print(f"x is {x}")
    
# def get_int():
#     while True:
#         try:
#             x = int(input("what's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x

# main()

# tightening up our code

# def main():
#     x = get_int()
#     print(f"x is {x}")
    
# def get_int():
#     while True:
#         try:
#             return int(input("what's x? "))
#         except ValueError:
#             print("x is not an integer")

# main()
# using pass---
def main():
    x = get_int()
    print(f"x is {x}")
    
def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
            pass

main()