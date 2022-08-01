num1= int(input('enter number'))
rev=0
num2=num1
while(num1>0):
    rev=(rev*10)+num1%10
    num1=num1//10
if(rev==num2):
    print(num2,'Iis','Palidrome',num1)
else:
    print(num2,'is','Not palidrome')
