import sys
try:
    
    f=open("subha.text")
except(FileNotFoundError):
    print("File is not present")
    
finally:
    print("Closing the file")
    f.close()
