n=int(input())
x=0
y=1
l1=[0,1]
c=2
for i in range(1,n*n):
    c=c+1
    z=x+y
    l1.append(z)
    x=y
    y=z
    if c==n:
        break
for i in l1:
    print(i,end=" ")