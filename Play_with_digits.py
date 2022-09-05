n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    x=str(i)
    for j in x:
        y=int(j)
        c=c+y
print(c)
    