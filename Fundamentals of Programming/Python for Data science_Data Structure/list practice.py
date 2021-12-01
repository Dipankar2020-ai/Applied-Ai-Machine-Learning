>>> lst=['abc','def','ghi','ijk']
>>> print(len(lst))
4
>>> lst.insert(2,'mno')
>>> print(lst)
['abc', 'def', 'mno', 'ghi', 'ijk']
>>> lst.remove('ijk')
>>> lst
['abc', 'def', 'mno', 'ghi']
>>> a=[1,2,3,4]
>>> b=[5,6,7,8]
>>> a.append(b)
>>> a
[1, 2, 3, 4, [5, 6, 7, 8]]
>>> c=[10,11,12,13]
>>> a.extend(c)
>>> a
[1, 2, 3, 4, [5, 6, 7, 8], 10, 11, 12, 13]
>>> del a[1]
>>> a
[1, 3, 4, [5, 6, 7, 8], 10, 11, 12, 13]
>>> h=a.pop(1)
>>> print(b)
[5, 6, 7, 8]
>>> a
[1, 4, [5, 6, 7, 8], 10, 11, 12, 13]
>>> h
3
>>> if 4 in a:
	print('AI')

	
AI
>>> m=[5,1,9,4,12]
>>> j=m.sorted(m)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    j=m.sorted(m)
AttributeError: 'list' object has no attribute 'sorted'
>>> j=m.sorted()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    j=m.sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> j=sorted(m)
>>> j
[1, 4, 5, 9, 12]
>>> print(sorted(m,reverse=true))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(sorted(m,reverse=true))
NameError: name 'true' is not defined
>>> print(sorted(m,reverse=True))
[12, 9, 5, 4, 1]
>>> j.sort()
>>> j
[1, 4, 5, 9, 12]
>>> s="one,two,three,four"
>>> slst=s.split(',')
>>> print(slst)
['one', 'two', 'three', 'four']
>>> num=[1,2,3,4,5]
>>> print(num[0:4])
[1, 2, 3, 4]
>>> print(num[0:2])
[1, 2]
>>> lst1=['a','b','c','d']
>>> lst2=[1,2,3,4]
>>> new list=lst1+lst2
SyntaxError: invalid syntax
>>> new_lst=lst1+lst2
>>> new_lst
['a', 'b', 'c', 'd', 1, 2, 3, 4]
>>> nums=[1,2,3,1,2,1,1]
>>> print(nums.count(1))
4
>>> lst=[1,2,3,4,5]
>>> for i in lst:
	print(i)

	
1
2
3
4
5
>>> square=[]
>>> for i in range(10):
	square.append(i*i)

	
>>> print(aquare)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(aquare)
NameError: name 'aquare' is not defined
>>> print(square)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
