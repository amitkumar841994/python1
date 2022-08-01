def list_even(srt,end):
    for i in range(srt,end+1,1):

        if(i%2)==0:
            print(i)

num1=int(input("Enter starting point"))
num2=int(input("Enter ending point"))
list_even(num1,num2)
