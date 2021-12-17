import sys
lst=['b',0,2]
for entry in lst:
    try:
        print("********************")
        print("The entry is ",entry)
        r=1/int(entry)
    except(ValueError):
        print("This is value error")
    except(ZeroDivisionError):
        print("This is zero divison error")
    except:
        print("Other error")
print("the reciprocal of",entry,"is",r)
