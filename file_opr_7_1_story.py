def files():

    num_wrd=0
    with open("story.txt","r") as f:
         lines=len(f.readlines())

         print(lines)
         f.seek(0)
         j=0
         for i in range(0,lines):
             for j in f:
                if j[i]!='T':
                    #print(j[i])
                    num_wrd+=1


    print('Count of line which is not start form T =',num_wrd)
files()

'''Question of display function'''

def display_words():
    with open("story.txt","r") as f1:
        list1=[]
        for i in f1:
            list1=i.split()
            #print(list1)
            for j in list1:
                if len(j)<4:
                    print(j)
display_words()

'''Question 3 to copy1 text file to another file'''
with open("story.txt",'r')as first,open("story1.txt","w") as sec:
    for i in first:
        sec.write(i)







