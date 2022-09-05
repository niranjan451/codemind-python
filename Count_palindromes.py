n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    s=str(i)
    s1=s[::-1]
    if s==s1:
        c=c+1
print(c)