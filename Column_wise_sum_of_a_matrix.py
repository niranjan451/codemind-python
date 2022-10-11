m,n=map(int,input().split())
a=[[0]*n]*m
for i in range(m):
    a[i]=list(map(int,input().split()))
l=[]
for i in range(n):
    s=0
    for j in range(m):
        s=s+a[j][i]
    l.append(s)
print(*l)