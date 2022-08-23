N=int(input())
l1=[]
l2=[]
for i in range(2,2*N):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if i<N:
            l1.append(i)
        else:
            l2.append(i)
a=N-max(l1)
b=min(l2)-N
if N==2:
    print("0")
elif a<b:
    print(a)
elif a>b:
    print(b)
else:
    print(a)