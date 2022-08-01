data=''
data1=''
with open("story.txt","r")as f:
    data=f.read()
with open("demo.txt",'r')as f1:
    data1=f1.read()

with open("merge.txt","w") as f2:
    f2.write(data)
    f2.write(data1)