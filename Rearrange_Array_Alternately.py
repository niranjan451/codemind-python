t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l1=[]
    for i in range(len(l)):
        if len(l)>1:
            s=l.index(max(l))
            s1=l.index(min(l))
            s2=l.pop(s)
            s3=l.pop(s1)
            l1.append(s2)
            l1.append(s3)
        else:
            l1.extend(l)
            break
    print(*l1)