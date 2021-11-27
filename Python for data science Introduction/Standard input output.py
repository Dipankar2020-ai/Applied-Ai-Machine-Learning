>>> a=10;b=11
>>> print("the value of a and b is ",a,b)
the value of a and b is  10 11
>>> print("the value of a is {} and b is {}".format(a,b))
the value of a is 10 and b is 11
>>> print("The value of a is {1} and b is {0}",b,a))
SyntaxError: unmatched ')'
>>> print("The value of a is {1} and b is {0}".format(b,a))
The value of a is 10 and b is 11
>>> print("Hello{user},i am {Name}".format(user="Dipankar",Name="Computer"))
HelloDipankar,i am Computer
>>> num=int(input("Enter the value"))
Enter the value9
>>> print(num)
9
