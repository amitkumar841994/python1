import mysql.connector
import random
import pywhatkit
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='emp'
)
mycursor=mydb.cursor()

number=int(input("Enter 10 digit mobile number"))
otp=random.randint(10000,99999)
sql="INSERT INTO otp(mobile,otp) VALUES(%s,%s)"
val=(number,otp)
mycursor.execute(sql,val)
mydb.commit()

sql1="select otp from otp where mobile=%s"
val1=[number]
mycursor.execute(sql1,val1)
abc=mycursor.fetchone()
number1 = str(number)
number2 = '+91' + number1
abc2 = str(abc[0])
pywhatkit.sendwhatmsg_instantly(number2, abc2, 15)
print(abc[0])
otp1=int(input("Enter the otp for varification"))

if otp1==abc[0]:
    print("Success")
else:
    print("failes")
