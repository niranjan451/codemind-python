n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=l[::-1]
for i in range((len(l)//2)):
    l1.append(l[i])
    l1.append(l2[i])
if n%2!=0:
    x=(len(l)//2)
    l1.append(l[x])
    l1.append(0)
    print(*l1)
else:
    print(*l1)
    