t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    l3=l+l1
    l3.sort()
    print(*l3)