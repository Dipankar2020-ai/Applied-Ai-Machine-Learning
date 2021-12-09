Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=()
>>> t=(1,2,3)
>>> t
(1, 2, 3)
>>> t=(1,'raju',27,'abc')
>>> print(t)
(1, 'raju', 27, 'abc')
>>> t=('raju')
>>> type(t)
<class 'str'>
>>> t=('raju',)
>>> type(t)
<class 'tuple'>
>>> t=('ABC',('satish','naveen','Srinu'))
>>> print(t[1])
('satish', 'naveen', 'Srinu')
>>> print(t[1][2])
Srinu
>>> t=(1,2,3,4,5,6)
>>> print(t[1:4])
(2, 3, 4)
>>> print(t[:])
(1, 2, 3, 4, 5, 6)
>>> print(t[:-2])
(1, 2, 3, 4)
>>> t[2]=4
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
>>> t=(1,[2,3,4])
>>> t[1][0]='D'
>>> print(t)
(1, ['D', 3, 4])
>>> t=(2,3,4)+(9,8,7)
>>> print(t)
(2, 3, 4, 9, 8, 7)
>>> t=(('satish',)*4)
>>> print(t)
('satish', 'satish', 'satish', 'satish')
>>> del t
>>> t=(1,2,1,3,1,4)
>>> t.count(1)
3
>>> t.index(1)
0
>>> print(5 in t)
False
>>> print(3 in t)
True
>>> print(len(t))
6
>>> newt=sorted(t)
>>> print(newt)
[1, 1, 1, 2, 3, 4]
>>> 