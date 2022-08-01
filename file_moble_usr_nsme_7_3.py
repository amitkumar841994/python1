
with open("user_mobile","a") as f:
    num1=int(input("Number of User"))
    print("Enter User name and mobile number ")
    for i in range(0,num1):
        f.write('\n')
        f.write(input())

with open("user_mobile","r") as f2:
    print(f2.read())

