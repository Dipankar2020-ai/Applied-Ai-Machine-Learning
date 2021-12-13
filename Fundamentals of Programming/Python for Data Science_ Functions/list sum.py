def get_sum(lst):
    sum=0
    for i in range(0,len(lst)):
        sum=sum+lst[i]
    return sum
lst=[1,2,3,4,5]
print("The list sum is ",get_sum(lst))
