n=int(input())
l=list(map(int,input().split()))
l2=l[(n//2)::]
l1=l[:(n//2)]
l3=l2[::-1]+l1
print(*l3)