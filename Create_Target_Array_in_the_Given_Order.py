n=int(input())
l=list(map(int,input().split()))
m=int(input())
l1=list(map(int,input().split()))
l2=[]
for i in range(n):
    l2.insert(l1[i],l[i])
print(*l2)