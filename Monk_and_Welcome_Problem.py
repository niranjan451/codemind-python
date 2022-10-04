n=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
for i in range(n):
    l[i]=l1[i]+l[i]
print(*l)