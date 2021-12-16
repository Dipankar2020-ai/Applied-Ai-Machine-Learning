def fibonacci(num):
    return num if num<=1 else fibonacci(num-1)+fibonacci(num-2)
num=10
for i in range(num):
    print(fibonacci(i))
