#simple list
print("simple list")
list5=["Amitkumar","Pal",24,45]
print(list)
#--------------------*--------------------------*----------------------------*------------------------------------------
list1=[]
print("This is empty list",list1)
print("the value of list",list[1])
print(" value of list",list[0])
#--------------------------------------------*************--------------------------------------------------------------
print("Accessing elements from a multi-dimensional list")
list2=[["Amitkumar","Pal"],["Chandraprakash","Pal"]]
print(list2[0][0])
print(list2[1][0])
print("Negative Indexing")
print(list[-1])
print("Printing the length of string")
print(len(list5),len(list1),len(list2))
#------------------------------------************************************************-----------------------------------
print("Tanking input in Python List")
str1=input("Enter the one sentence")
lst3=str1.split()
print(lst3)
print('For the Integeger Value')
n = int(input('Enter size of list'))
lst4 = list(map(int, input("Enter the integer\elements:").strip().split()))[:n]
print(lst4)
#------------------------------------********************************************---------------------------------------
print("Adding value in List")
print("Old list=",list5)
print("Adding value through the Append",list5.append('abc'))
print("Adding value through the Insert",list5.insert(0,'Hello'))
print("Adding value through the Extend ",list5.extend('ITvedant',700,'Python'))
