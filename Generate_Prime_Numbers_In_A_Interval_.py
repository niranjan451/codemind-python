n=int(input())
m=int(input())
l1=[]
for i in range(n,m):
    if i==0 or i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)