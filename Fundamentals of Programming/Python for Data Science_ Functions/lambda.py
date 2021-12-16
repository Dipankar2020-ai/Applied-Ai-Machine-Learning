def double(x):
    return x*2
print(double(5))

double=lambda x:x*2
print(double(5))
lst=[1,2,3,4,5]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)

lst=[1,2,3,4,5]
new_lst=list(map(lambda x:x**2,lst))
print(new_lst)
lst=[1,2,3,4,5]
from functools import reduce
product_lst=reduce(lambda x,y:x*y,lst)
print(product_lst)

 
