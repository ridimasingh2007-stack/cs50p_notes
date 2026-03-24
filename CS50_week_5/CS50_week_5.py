# Unit tests:--- testing individual units of the code, those units are mainly functions

# def main():
#     x = int(input("What's x? "))
#     print("x squared is", square(x))
# def square(n):
#     return n + n # creating bug intentionally 

# if __name__ == "__main__":
#     main()

# assert:-- claim that it's true, if not there's some error shown ## used in test_CS50_week_5.py

# AssertionError:- if the assert claim is wrong, this shows up

# pytest:-- it's a library that automates the testing of the code that is written, it comes with built-in conventions.
def main():
    name = input("What's your name? ")
    print(hello(name))
def hello(to="world"):
    return f"hello, {to}" # not using print cause it doesn't give any value

if __name__ == "__main__":
    main()


