str="hello this is  amit pal"
str3='amit'
str4='Amitkumar4'
str5='5687559'
#capitalize function
print('Capitalize fuction ',str.capitalize())
#Uppercase
str1=str.upper()
print('This upper case ',str1)
#Lowercase
print('This is lower case=',str1.lower())
#ISUPPER
print('Lower case ',str.isupper())
print('Upper case ',str1.isupper())
#ISLOWEr
print('Lower case ',str.islower())
print('Upper case ',str1.islower())
#split
str2=str.split()
print('After spilitting',str2)
#Join
print(" ".join(str2))
#startswith
print(str.startswith('hello'))
print(str.startswith('amit'))
print(str.startswith('amit',11,15))
#Endwith
print(str.endswith('pal'))
print(str.endswith('amit'))
print(str.endswith('amit',11,15))
#Replacr
print(str.replace('amit','Amitkumar'))
#Find
print(str.find('Amitkumar'))
print(str.find('i',5,15))
#ISalpha
print(str3.isalpha())
print(str4.isalpha())
#isdigit
print(str5.isdigit())
print(str4.isdigit())
#isalphnum
print(str4.isalnum())
