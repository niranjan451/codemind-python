n,m=map(int,input().split())
a=[[0]*m]*n
for i in range(n):
    a[i]=list(map(int,input().split()))
e=0
o=0
for i in range(n):
    for j in range(m):
        if i%2==0:
            e=e+a[i][j]
        else:
            o=o+a[i][j]
print(e,o)