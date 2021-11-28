n=int(input())
i=2
isDiv=False
while i<n:
    if n%i==0:
        isDiv=True
        print("{} is divisible by {}".format(n,i))
    i=i+1
if isDiv:
    print("{} is not a Prime Number".format(n))
else:
    print("{} is  a Prime Number".format(n))
