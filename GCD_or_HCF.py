n,m=map(int,input().split())
l=[]
for i in range(1,n+1):
    if n%i==0 and m%i==0:
        l.append(i)
print(max(l))