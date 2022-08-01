dict1 = {'username': 'amit' , 'pasword': 'amit123'}
def glo_paswrd(username1,password1):
    for i in dict1:
        if dict1[i] == username1 and password1:
            print('Login sucessful')
            break

        else:
            print('Invalid username or password')
            break

username2= input('Enter username')
password2=input('enter password')
glo_paswrd(username2,password2)
