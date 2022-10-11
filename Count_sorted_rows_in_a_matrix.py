m,n=map(int,input().split())
a=[[0]*n]*m
c=0
for i in range(m):
    a[i]=list(map(int,input().split()))
for i in a:
    l=sorted(i)
    l1=l[::-1]
    if i==l or i==l1:
        c=c+1
print(c)