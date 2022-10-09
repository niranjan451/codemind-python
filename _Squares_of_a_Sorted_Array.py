n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    x=i*i
    l1.append(x)
l1.sort()
print(*l1)
