# from CS50_week_5 import square
# import pytest
from CS50_week_5 import hello
# def main():
#     test_square()
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
    
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")

#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")

# if __name__ == "__main__":
#     main()
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

# def test_positive():
#     assert square(2) == 4
#     assert square(3) == 9

# def test_negative():
#     assert square(-2) == 4
#     assert square(-3) == 9

# def test_zero():
#     assert square(0) == 0

# def test_str():
#     with pytest.raises(TypeError):
#         square("cat")


def test_default():
    assert hello("Ridima") == "hello, Ridinma"
def test_argument():
    assert hello() == "hello, world"





