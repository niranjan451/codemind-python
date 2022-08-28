n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=[]
for i in range(0,len(l)):
    if l.count(l[i])==k:
        if l[i] not in l1:
            l1.append(l[i])
if len(l1)!=0:
    print(*l1)
else:
    print(-1)