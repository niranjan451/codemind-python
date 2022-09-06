n=int(input())
m=int(input())
l1=[]
for i in range(n,m+1):
    if i<=9:
        l1.append(i)
    elif i>9 and i%10!=0:
        s=str(i)
        c=0
        for j in s:
            if i%(int(j))==0:
                c=c+1
        if len(s)==c:
            l1.append(i)
print(*l1)
        