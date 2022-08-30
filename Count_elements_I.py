n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=l1+l2
s=set(l3)
c=0
for i in s:
    if (i in l1) and (i in l2):
        c=c+1
print(c)