T=int(input())
for i in range(T):
    N=int(input())
    l1=[]
    l2=[]
    for i in range (1,2*N):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            if i<N:
                l1.append(i)
            else:
                l2.append(i)
    a=max(l1)
    b=min(l2)
    x=N-a
    y=b-N
    if x<y:
        print(a)
    elif x>y:
        print(b)
    else:
        print(a)
    