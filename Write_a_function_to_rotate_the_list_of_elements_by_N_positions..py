n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in range(m):
    s1=l.pop(-1)
    l.insert(0,s1)
print(*l)