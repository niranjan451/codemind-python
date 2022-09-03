n=int(input())
l=list(map(int,input().split()))
l1=[]
s=set(l)
for i in s:
    if i==l.count(i):
        l1.append(i)
if len(l1)!=0:
    x=(sum(l1)/len(l1))
    print("%0.2f"%x)
else:
    print(-1)