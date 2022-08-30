n=int(input())
l=list(map(int,input().split()))
d1=0
d2=0
for i in range(0,len(l)):
    if i<n//2 :
        d1=d1+l[i]
    else:
        d2=d2+l[i]
print(abs(d1-d2))