Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mystring='Hello'
>>> print(mystring)
Hello
>>> mystring="hello"
>>> print(mystring)
hello
>>> mystring='''hello'''
>>> print(mystring)
hello
>>> print(mystring[0])
h
>>> print(mystring[2:5])
llo
>>> mystring[4]='p'
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    mystring[4]='p'
TypeError: 'str' object does not support item assignment
>>> del mystring
>>> s1="hello"
>>> s2=" Dipankar"
>>> print(s1+s2)
hello Dipankar
>>> print(s1*3)
hellohellohello
>>> count=0
>>> for l in "HelloWorld":
	if l=='0':
		count=count+1
print(count)
SyntaxError: invalid syntax
>>> 	print(count)
	
SyntaxError: unexpected indent
>>> print(count)
0
>>> print('l' in "hello world")
True
>>> print("or" in "hello world")
True
>>> "Hello".lower()
'hello'
>>> "Hello".upper()
'HELLO'
>>> "This will split all the words in a list".split()
['This', 'will', 'split', 'all', 'the', 'words', 'in', 'a', 'list']
>>> '-'.join('this','will','split''all','words','in','a','list')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    '-'.join('this','will','split''all','words','in','a','list')
TypeError: str.join() takes exactly one argument (7 given)
>>>  '-'.join('this','will','split','all','words','in','a','list')
 
SyntaxError: unexpected indent
>>> '-'.join('this','will','split','all','words','in','a','list')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    '-'.join('this','will','split','all','words','in','a','list')
TypeError: str.join() takes exactly one argument (8 given)
>>> "Good Morning".find("Mo")
5
>>> "Bad Morning".replace("Bad","Good")
'Good Morning'
>>> 