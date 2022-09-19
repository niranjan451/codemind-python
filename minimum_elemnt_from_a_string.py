n=input()
m=n.split()
m2=m[-1]
l1=[]
l2=[]
for i in m2:
    if i==i.upper():
        l1.append(i)
    else:
        l2.append(i)
if (min(l2).upper()) in l1:
    print(min(l2))
else:
    print(min(m2))