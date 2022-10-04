n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
l1=[]
for i in s:
    y=l.count(i)
    l1.append(y)
x=l1.index(max(l1))
print(s[x])
    