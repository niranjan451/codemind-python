n,k,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    x=l.pop()
    l.insert(0,x)
for i in range(q):
    n=int(input())
    print(l[n])