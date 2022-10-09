m=int(input())
l=list(map(int,input().split()))
n=int(input())
l1=list(map(int,input().split()))
l.sort()
l1.sort()
if l==l1:
    print(True)
else:
    print(False)