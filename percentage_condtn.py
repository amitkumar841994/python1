per=float(input('Enter the Student percentage'))
if(per>90):
    print('Student grade is =','A')
elif(per>80 and per<=90):
    print('Student grade is=','B')
elif(per>60 and per<=80):
    print('Student grade is=','C')
elif(per<60 and per>45):
    print('Student grade is=','D')
else:
    print("Student result is=",'Failed')

