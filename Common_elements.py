n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=l1+l2
l4=[]
for i in l3:
    if (i in l1) and (i in l2):
        if i not in l4:
            l4.append(i)
print(*l4)
