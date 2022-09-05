n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    i=abs(i)
    s=str(i)
    s1=len(s)
    l1.append(int(s1))
print(*l1)