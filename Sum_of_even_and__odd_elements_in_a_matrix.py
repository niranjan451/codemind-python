n,m=map(int,input().split())
a=[[0]*m]*n
for i in range(n):
    a[i]=list(map(int,input().split()))
c=0
c1=0
for i in range(n):
    for j in range(m):
        if a[i][j]%2==0:
            c=c+a[i][j]
        else:
            c1=c1+a[i][j]
print(c,c1)
            