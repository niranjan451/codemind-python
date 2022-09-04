n1=int(input())
n2=int(input())
s=n1+n2
for i in range(s+1,s*s):
    if i==1 or i==0:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        x=i
        break
print(x-s)