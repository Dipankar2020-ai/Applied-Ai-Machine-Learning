num1=int(input())
isDiv=False
for i in range(2,num1):
    if num1%i==0:
        isDiv=True
        print("{} is divisible by {}".format(num1,i))
        break;
if(isDiv):
    print("{} is not a prime number".format(num1))
else:
    print("{} is a prime number".format(num1))
    
