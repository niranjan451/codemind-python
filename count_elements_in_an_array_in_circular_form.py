n=int(input())
l=list(map(int,input().split()))
c=0
x=l[1]
y=l[-1]
a=l[0]
z=l[-2]
if (x%2==0 and y%2!=0 ) or (x%2!=0 and y%2==0):
    c=c+1
if (a%2==0 and z%2!=0) or (a%2!=0 and z%2==0):
    c=c+1
for i in range(0,len(l),1):
    j=i+2
    if j<n:
        if l[i]%2==0 and l[j]%2!=0:
            c=c+1
        elif l[i]%2!=0 and l[j]%2==0:
            c=c+1
print(c)