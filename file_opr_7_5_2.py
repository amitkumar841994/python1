def user():
    with open("user_data.txt",'a') as f:
        for i in range(0,3):
            name=input("Enter the name of user")
            f.writelines(input("Enter the password"))
        for i in range(0,3):

            print("username\n",name,"\n")

user()
