n=int(input())
s=str(n)
l=list(s)
l1=[]
c=0
for i in s:
    if i not in l1:
        l1.append(i)
    else:
        continue
if l==l1:
    print("Unique Number")
else:
    print("Not Unique Number")
        
        
    