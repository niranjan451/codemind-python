n=int(input())
l=list(map(int,input().split()))
d=0
for i in range(0,n):
    if i%2==0:
        continue
    else:
        d=d+l[i]
print(d)