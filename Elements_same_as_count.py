n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i==l.count(i):
        if i not in l1:
            l1.append(i)
if len(l1)!=0:
    print(*l1)
else:
    print(-1)
        