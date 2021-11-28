num1=int(input())
num2=int(input())

for i in range(num1,num2):
    flag=False
    for j in range(2,i):
        if i%j==0:
            flag=True
    if(not flag and i>1):
        print(i)

                
        
        
        
