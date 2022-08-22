n=int(input())
x=0
y=1
l1=[]
for i in range(1,n+1):
    z=x+y
    l1.append(z)
    x=y
    y=z
if n in l1:
    print("True")
else:
    print("False")