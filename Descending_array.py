n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l),1):
    j=i+1
    if j<n:
        if l[i]>l[j]:
            c=c+1
if c+1==len(l):
    print("yes")
else:
    print("no")
        