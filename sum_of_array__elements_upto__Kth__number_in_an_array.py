n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=0
for i in range(0,len(l)):
    if i<k:
        s=s+l[i]
print(s)