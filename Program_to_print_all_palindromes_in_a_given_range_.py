n=int(input())
m=int(input())
l1=[]
for i in range(n,m+1):
    s=list(str(i))
    s1=s[::-1]
    if s==s1:
        l1.append(i)
print(*l1)