x = [2,4,6,8,10]
y= [12,13,14]
a = ["hey","there","hello","world"]
x.append('eleven')
print('Adding one value \n',x)
x.insert(0,'one')
print('Adding the value at 1st position\n',x)
z=x+y
print('afyer meging 2 list\n',z)
z.reverse();
print('After reverse\n',z)
z.remove('one')
print('After removing ONE\n',z)
print('Loop')
for i in a:
    print(i,end=' ')