n=input()
m=n.split()
m1="".join(m)
m3=m1.lower()
l=list(m3)
l.sort()
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
        print(i,end="")