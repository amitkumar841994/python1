ls=[]
ans =[]
for i in range(20,51,1):
    ls.append(i)
for j in ls:
    if(j>1):
        for k in range(2,j//2+1):
            if(j%k)==0:
                break
        else:
            ans.append(j)

print(ans)



