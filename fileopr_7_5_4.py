def readfl():
    num_line=0
    num_wrds=0
    num_spc=0
    list1=[]
    with open("story.txt","r") as f:
        for i in f:#printing count of line
            num_line += 1
            list1=i.split()
            for j in list1:#printing count of words
                if(len(j)>=1):
                    num_wrds +=1
            for k in i:#printing space
                if k==' ':
                    num_spc+=1
        print("number of lines=", num_line)
        print("number of words=",num_wrds)
        print("number of spaces=",num_spc)

readfl()

