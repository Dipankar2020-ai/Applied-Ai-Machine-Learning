matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]
transpose=[]
for i in range(4):
    lst=[]
    for row in matrix:
        lst.append(row[i])
    transpose.append(lst)
print(transpose)
