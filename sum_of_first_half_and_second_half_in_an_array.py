n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,len(l)):
    if i<n//2:
        s1=s1+l[i]
    else:
        s2=s2+l[i]
print(s1)
print(s2)