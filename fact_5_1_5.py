def fact(x):
    if x==1:
        return 1
    else:
        return (x*fact(x-1))

num1=int(input("Enter number"))
print('factorial of number is ',fact(num1))