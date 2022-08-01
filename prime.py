num1 = int(input("Enter number"))
if (num1 > 1):
    for i in range(2, (num1//2)+1):
        if (num1 % i)==0:
            print('its not prime number')
            break
    else:
        print('prime number')

else:
    print('not prime')

