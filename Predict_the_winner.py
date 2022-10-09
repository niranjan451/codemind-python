n=int(input())
l=list(map(int,input().split()))
if sum(l)%4==0:
    print("X")
else:
    print("Y")