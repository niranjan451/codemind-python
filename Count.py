n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in l:
    if i%2==0:
        c=c+1
    else:
        d=d+1
print(c,d)