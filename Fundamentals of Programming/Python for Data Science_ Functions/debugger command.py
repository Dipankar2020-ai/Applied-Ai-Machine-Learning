Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Diploma in machine learning applied ai/applied ai machine learning/Practice/debugger.py
> c:\diploma in machine learning applied ai\applied ai machine learning\practice\debugger.py(5)seq()
-> print(i)
(Pdb) p i
0
(Pdb) p n
5
(Pdb) p locals()
{'n': 5, 'i': 0}
(Pdb) continue
0
> c:\diploma in machine learning applied ai\applied ai machine learning\practice\debugger.py(4)seq()
-> pdb.set_trace()
(Pdb) p locals()
{'n': 5, 'i': 1}
(Pdb) continue
1
> c:\diploma in machine learning applied ai\applied ai machine learning\practice\debugger.py(5)seq()
-> print(i)
(Pdb) p locals()
{'n': 5, 'i': 2}
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) quit
Traceback (most recent call last):
  File "C:/Diploma in machine learning applied ai/applied ai machine learning/Practice/debugger.py", line 7, in <module>
    seq(5)
  File "C:/Diploma in machine learning applied ai/applied ai machine learning/Practice/debugger.py", line 5, in seq
    print(i)
  File "C:/Diploma in machine learning applied ai/applied ai machine learning/Practice/debugger.py", line 5, in seq
    print(i)
bdb.BdbQuit
>>> 