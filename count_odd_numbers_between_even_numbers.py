n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l),1):
    j=i+2
    if j<n:
        if (l[i]%2)==0 and (l[j]%2)==0:
            if (l[i+1]%2)!=0:
                c=c+1
print(c)