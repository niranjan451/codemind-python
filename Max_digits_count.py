n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    s=str(i)
    s1=len(s)
    l1.append(s1)
e=l1.count(max(l1))
print(e)