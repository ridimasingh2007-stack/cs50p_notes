 
# Basically revising things

# name = input("what's your name? ").strip().title() 
# print("hello,", name)
# name = name.strip() --- this removes spaces from user input
# name = name.capitalize() --- this capitalize only the very first letter
# name = name.title() -- this is for capitalizing all first letters of each words
#or print("hello, " + name)
# or print("hello, ", end="")
#print(name)
#print("hello,", name, sep='')
# #or print(f"hello, {name}")

# x = input("what is x? ")
# y = input("what is y? ")

# z = int(x) + int(y)
# print(z)

# or 

# x = int(input("what is value of x: "))
# y = int(input("what is value of y: "))

# print(x+y)

# x = float(input("what is value of x: "))
# y = float(input("what is value of y: "))

# print(round(x+y))

# x = int(input("what is value of x: "))
# y = int(input("what is value of y: "))

# z = round(x/y, 2)

# print(z)

# or to round use f method

# x = float(input("what is value of x: "))
# y = float(input("what is value of y: "))
# z = x / y
# print(f"{z:.2f}")

# def hello(to):
#     print("hello,", to)
# name = input("what's your name? ")
# hello(name) 

# to reorder the fuction top to bottom :-

# def main():
#     name = input("what's your name? ")
#     hello(name) 

# def hello(to="world"):
#     print("hello,", to)

# main()

def main():
    x = int(input("what's x? "))
    print("x square is", square(x))

def square(n):
    return pow(n, 2)
main()