m,n=map(int,input().split())
a=[[0]*n]*m
l=[]
for i in range(m):
    a[i]=list(map(int,input().split()))
    l.append(sum(a[i]))
print(max(l))
