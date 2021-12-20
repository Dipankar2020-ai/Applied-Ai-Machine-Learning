import numpy as np 
a=np.random.randint(0,20,15)
print(a)
mask=(a%2==0)
extract_form_a=a[mask]
print(extract_form_a)
a[mask]=-1
print(a)
a=np.arange(0,100,10)
print(a)
print(a[[2,3,2,4,2]])
a[[9,7]]=-200
print(a)
