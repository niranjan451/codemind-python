t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l1=[]
    for i in range(1,n+1):
        l1.append(i)
    for i in l1:
        if i not in l:
            print(i)