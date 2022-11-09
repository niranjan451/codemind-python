n=int(input())
l=list(map(int,input().split()))
s=set(l)
c=0
for i in s:
    x=(l.count(i))
    if x>1:
        x1=x//2
        c=c+x1
print(c)