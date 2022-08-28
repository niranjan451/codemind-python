
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,len(l)):
    if i%2==0 and l[i]%2==0:
        continue
    elif l[i]%2==0:
        l1.append(i)
if len(l1)==0:
    print("True")
else:
    print("False")
        