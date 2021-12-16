def factorial(num):
    return 1 if num==1 else (num*factorial(num-1))
num=5
print ("Factorial of {0} is {1}".format(num,factorial(num)))
