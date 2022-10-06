t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l=[]
    for j in range(n+m):
        if (j*j)%m==n:
            l.append(j)
    if len(l)==0:
        print(-1)
    else:
        print(min(l))