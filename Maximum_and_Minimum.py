n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i==l.count(i):
        l1.append(i)
if len(l1)!=0:
    print(min(l1),max(l1))
else:
    print(-1)