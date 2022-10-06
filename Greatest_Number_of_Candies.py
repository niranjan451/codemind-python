n=int(input())
l=list(map(int,input().split()))
m=int(input())
l1=[]
for i in l:
    if i+m>=max(l):
        l1.append("True")
    else:
        l1.append("False")
print(*l1)