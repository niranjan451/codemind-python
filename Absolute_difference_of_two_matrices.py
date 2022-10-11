n=int(input())
a=[[0]*n]*n
b=[[0]*n]*n
c=[[0]*n]*n
for i in range(n):
    a[i]=list(map(int,input().split()))
for i in range(n):
    b[i]=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        c[i][j]=abs(a[i][j]-b[i][j])
    print(*c[i])