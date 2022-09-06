n=input()
y=n.split()
l1=[]
for i in range(0,len(y),1):
    if i%2==0:
        e=str(y[i])
        z=e[::-1]
        l1.append(z)
    else:
        l1.append(y[i])
print(*l1)
        
    