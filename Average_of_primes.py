n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in l:
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        s=s+i
        c=c+1
x=s/c
print("%.2f"%x)