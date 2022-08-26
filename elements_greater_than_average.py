n=int(input())
l=list(map(int,input().split()))
s=sum(l)
f=s//n
c=0
for i in range(0,len(l)):
    if l[i]>=f:
        c=c+1
print(c)
        