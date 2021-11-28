a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print("{} is greater".format(a))
elif b>=c and b>=a :
    print("{} is greater ".format(b))
else:
    print("{} is c greater".format(c))
    
