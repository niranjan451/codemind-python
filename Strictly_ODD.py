n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(0,len(l)):
    if i%2!=0 and l[i]%2!=0:
        l1.append(i)
    elif l[i]%2:
        l2.append(i)
if len(l2)==0:
    print("True")
else:
    print("False")