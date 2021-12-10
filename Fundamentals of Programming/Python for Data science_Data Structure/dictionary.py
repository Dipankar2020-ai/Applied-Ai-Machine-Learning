Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_dict={}
>>> print(type(my_dict))
<class 'dict'>
>>> my_dict={1:'abc',2:'xyz'}
>>> print(my_dict)
{1: 'abc', 2: 'xyz'}
>>> my_dict=dict()
>>> my_dict=dict([(1,'abc'),(2,'xyz')])
>>> print(my_dict)
{1: 'abc', 2: 'xyz'}
>>> my_dict={'name':'Raju',1:['abc','xyz']}
>>> print(my_dict)
{'name': 'Raju', 1: ['abc', 'xyz']}
>>> my_dict={'name':'Satish','age':27,'address':'guntur'}
>>> print(my_dict['name'])
Satish
>>> print(my_dict['weight'])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(my_dict['weight'])
KeyError: 'weight'
>>> print(my_dict.get('address'))
guntur
>>> print(my_dict.get('degree'))
None
>>> my_dict['name']='raju'
>>> my_dict
{'name': 'raju', 'age': 27, 'address': 'guntur'}
>>> my_dict['degree']='M.tech'
>>> my_dict
{'name': 'raju', 'age': 27, 'address': 'guntur', 'degree': 'M.tech'}
>>> print(my_dict.pop('age'))
27
>>> my_dict
{'name': 'raju', 'address': 'guntur', 'degree': 'M.tech'}
>>> my_dict.popitem()
('degree', 'M.tech')
>>> my_dict
{'name': 'raju', 'address': 'guntur'}
>>> squares={2:4,3:9,4:16,5:25}
>>> del squares[2]
>>> squares
{3: 9, 4: 16, 5: 25}
>>> my_dict=squares.copy()
>>> my_dict
{3: 9, 4: 16, 5: 25}
>>> subjects={}.fromkeys(['math','english,'bengali'],0)
		      
SyntaxError: invalid syntax
>>> subjects={}.fromkeys(['math','english','bengali'],0)
>>> subjects
{'math': 0, 'english': 0, 'bengali': 0}
>>> subjects=my_dict.copy()
>>> subjects
{3: 9, 4: 16, 5: 25}
>>> print(subjects.values())
dict_values([9, 16, 25])
>>> d={}
>>> print(dir(d))
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d={'a':1,'b':2,'c':3}
>>> for pair in d.items():
	print(pair)

('a', 1)
('b', 2)
('c', 3)
>>> new_dict={k+'c':v*2 for k,v in d.items() if v>2}
>>> new_dict
{'cc': 6}
>>> 