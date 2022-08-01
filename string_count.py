str= ['abc', 'xyz', 'aba', '1221','343','def' ]
cnt=0
for i in str:
    if len(i)>2 and i[0]==i[-1]:
        cnt+=1
print('string which length is 2 && last,1st position same ',cnt)