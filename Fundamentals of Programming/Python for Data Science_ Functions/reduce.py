import functools
product=1
lst=[1,2,3,4]
def multiply(x,y):
    return x*y
product=functools.reduce(multiply,lst)
print(product)
