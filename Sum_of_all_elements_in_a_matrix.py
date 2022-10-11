n,m=map(int,input().split())
a=[[0]*m]*n
for i in range(n):
    a[i]=list(map(int,input().split()))
s=0
for i in range(n):
    for j in range(m):
        s=s+a[i][j]
print(s)