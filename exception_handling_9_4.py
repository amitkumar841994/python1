#Create a function that take the inputs of filename and read the file content. Handle Exception by exception handling  if file not found.
import os.path
def file():
    class FileNotFound(Exception):
        pass
    try:
        str1 = input("Enter file")
        f1=os.path.exists(str1)
        if f1==True:
             with open(str1,'r') as f:
                 print(f.read())
        else:
            raise FileNotFound;
    except FileNotFound:
        print("File not found")
        print()
file()
