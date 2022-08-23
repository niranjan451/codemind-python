n=int(input())
l=list(map(int,input().split()))
s=0
d=0
for i in range(0,len(l)):
    if i%2==0:
        s=s+l[i]
    else:
        d=d+l[i]
t=abs(s-d)
print(t)