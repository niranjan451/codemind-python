n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        c=c+1
print(c)