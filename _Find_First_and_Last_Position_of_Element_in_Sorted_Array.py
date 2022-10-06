n=int(input())
l=list(map(int,input().split()))
m=int(input())
l1=[]
for i in range(len(l)):
    if l[i]==m:
        l1.append(i)
if len(l1)==0:
    print(-1,-1)
else:
    print(min(l1),max(l1))
        