n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
c=0
for i in range(0,len(l)):
    if i%2==0:
        l2.append(i)
    else:
        l1.append(i)
if n%2==0:
    x=l2[-1]
    print(x+1)
else:
    x=l1[-1]
    print(x+1)
        