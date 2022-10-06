n=int(input())
l=list(map(int,input().split()))
oc=0
ec=0
for i in range(0,len(l),2):
    ec=ec+l[i]
for j in range(1,len(l),2):
    oc=oc+l[j]
d=oc-ec
if d==0:
    print("YES")
else:
    print("NO")