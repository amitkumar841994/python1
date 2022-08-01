num1=int(input('Enter the number for fibonacci series ='))
temp=0
if(num1<=0):
    print('Enter valid number')
print('Enter the',num1,'number for fibonacci series')
for i in range(num1):
    num2=int(input())
    temp=num2+temp

print(temp,end=' ')
