n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
s=0
l=0
for i in l1:
    s=s+(i*pow(2,l))
    l=l+1
print(s)
    