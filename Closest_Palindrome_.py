N=int(input())
l1=[]
l2=[]
for i in range(100,2*N):
    x=i
    x2=str(x)
    x1=list(x2)
    y=x1[::-1]
    if x1==y:
        if x<N:
            l1.append(x)
        elif x==y:
            continue
        elif x>N:
            l2.append(x)
x=max(l1)-N
y=N-min(l2)
if x>y:
    print(max(l1))
elif x<y:
    print(min(l2))
else:
    print(max(l1),min(l2))

        
    