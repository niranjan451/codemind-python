n=input()
s=n.lower()
v=["a","e","i","o","u"]
l1=[]
for i in s:
    if i  in v:
        if i not in l1:
            l1.append(i)
if len(l1)==len(v):
    print(0)
else:
    for j in v:
        if j not in l1:
            print(j,end=" ")
        