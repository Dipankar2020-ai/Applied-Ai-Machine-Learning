mystr=input()
mystr=mystr.lower()
newstr=reversed(mystr)
if list(mystr)==list(newstr):
    print("Given string is palindrome")
else:
    print("Given string is not a palindrome")
    
