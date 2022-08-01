print("********Electricity Bill Calculation********")
unit=float(input('Enter the BILL unit'))
if(unit>100 and unit<=200):
    a=unit*5
    print('Your electricity bill is = ',a)
elif(unit>200):
    b=(100*5)-(unit-100)*10
    print('Your electricity bill is = ',b)
else:
    print('Your electricity is freee')


