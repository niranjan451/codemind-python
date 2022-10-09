n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    x=l[i]
    c=0
    for j in l:
        if x>int(j):
            c=c+1
    l1.append(c)
print(*l1)