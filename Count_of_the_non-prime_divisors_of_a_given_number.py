n=int(input())
l1=[]
l2=[]
for i in range(1,n+1):
    if n%i==0:
        l1.append(i)
for i in range(1,n+1):
    if i==0 or i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l2.append(i)
c=0
for i in l1:
    if i not in l2:
        c=c+1
print(c)
    