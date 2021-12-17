import sys
lst=['b',0,2]
for entry in lst:
    try:
        print("The entry is ",entry)
        ans=1/int(entry)
    except:
        print("oops!",sys.exc_info()[0],"occured")
        print("Next entry")
        print("*************************")
print("The reciprocal of",entry,"is",ans)

        
