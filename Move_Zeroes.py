n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i!=0:
        l1.append(i)
s1=l.count(0)
for i in range(s1):
    l1.append(0)
print(*l1)