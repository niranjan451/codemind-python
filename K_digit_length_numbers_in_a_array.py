n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in l:
    x=str(abs(i))
    l1.append(len(x))
c=0
for i in range(len(l1)):
    if k==l1[i]:
        c=c+1
print(c)