import sys
try:
    num=int(input("Enter a positive number"))
    if num<=0:
        raise ValueError("Error:entered a negative number")
except ValueError as e:
    print(e)
