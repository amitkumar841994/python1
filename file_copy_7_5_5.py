def cpy():
    list1=[]
    list2=[]
    with open("story.txt","r")as f,open("demo1.txt","a")as f1:

        for i in f:
            list1=i.split()
            for j in list1:
                if len(j)>4:
                    f1.write(j)


cpy()