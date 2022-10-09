n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    s1=l.pop(0)
    l.append(s1)
print(*l)