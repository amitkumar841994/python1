def dict1():
    #each item as pair
    Dict=dict([('Name','Amitkumar'),('Surname','Pal')])
    print(type(Dict))
    print(Dict)
dict1()
print('\n# Creating a Nested Dictionary\n')
def nestdict():
    # Creating a Nested Dictionary
    Dict={'Name':'Amitkumar Pal',
          'Family':{'Father':'Chandraprakash','Mother':'Samala Devi','Brother':'Rahul','niece':'Bubbu'}}
    print(Dict)
nestdict()
print('\n Adding value in Dictonary using for loop\n')
def using_forlop():
    Dict={}
    key=''
    values=''
    for i in range(0,4,1):
        key=input("Enter the key from user")
        values=input("Enter values from user")
        Dict[key]=values
    print(Dict)
using_forlop()