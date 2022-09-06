n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    x=str(abs(i))
    l1.append(len(x))
l2=[]
for i in range(len(l1)):
    if max(l1)==l1[i]:
        l2.append(l[i])
print(*l2)
        
    
