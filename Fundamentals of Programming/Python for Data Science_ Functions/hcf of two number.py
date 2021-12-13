def hcf(a,b):
    if a>b:
        ans=b
    else:
        ans=a
    for i in range(1,ans+1):
        if(a%i==0) and (b%i==0):
            hcf=i
    return hcf
print("Hcf of two number is ",hcf(19,18))
