Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1+2+3+\
   +4+5+6+\
   +7+8+9
>>> print(a)
45
>>> a=20;b=30;c=40
>>> x=3
>>> print(id(x))
2458426567024
>>> y=3
>>> print(id(y))
2458426567024
>>> x==y
True
>>> print(type(x))
<class 'int'>
>>> print(isinstance(1+2j,complex))
True
>>> a=[10,20.5,"Hello"]
>>> a[1]
20.5
>>> a[0]
10
>>> c=(1,1.5,"ML")
>>> print(c)
(1, 1.5, 'ML')
>>> t[1]=1
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    t[1]=1
NameError: name 't' is not defined
>>> g={10,20,20,30,40,30}
>>> print(g)
{40, 10, 20, 30}
>>> s={'a':"apple","b":"bat"}
>>> print(s['a'])
apple
>>> float(5)
5.0
>>> int(600.98)
600
>>> str(20)
'20'
>>> user="sachin"
>>> lines=100
>>> print("Congrulations"+user+"!you just wrote"+str(lines)+"Lines")
Congrulationssachin!you just wrote100Lines
>>> print("Congrulations"+user+"!you just wrote "+str(lines)+" Lines")
Congrulationssachin!you just wrote 100 Lines
>>> a=[1,2,3]
>>> print(type(a))
<class 'list'>
>>> r=set(a)
>>> print(type(r))
<class 'set'>
>>> list("Hello")
['H', 'e', 'l', 'l', 'o']
>>> 