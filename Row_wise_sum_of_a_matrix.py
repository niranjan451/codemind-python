n,m=map(int,input().split())
a=[[0]*m]*n
for i in range(n):
    a[i]=list(map(int,input().split()))
l=[]
for i in range(n):
    s=0
    for j in range(m):
        s=s+a[i][j]
    l.append(s)
print(*l)