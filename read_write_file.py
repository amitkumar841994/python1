with open("demo.txt","a") as f:
    for i in range(0,3,1):
        f.write(input('\n'))

'''with open("demo.txt","r+") as f2: # this is used for clear data in the file
    f2.truncate()'''

with open("demo.txt","r") as f1:

    print(f1.readlines())

