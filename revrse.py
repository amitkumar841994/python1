num1=int(input('enter the number'))
rev=0
while(num1>0):
    rev=(rev*10)+num1%10
    num1=num1//10
print(rev)
