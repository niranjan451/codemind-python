n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in l:
        if i<a or i>b:
            c=c+1
            print(i,end=" ")
else:
    if c==0:
        print(-1)
        
        