n=input()
n1=n.lower()
n2=n1.split()
n3="".join(n2)
n4=set(n3)
l=[]
for i in n4:
    c=0
    for j in n2:
        if i in j:
            c=c+1
            if c==len(n2):
                l.append(i)
if len(l)!=0:
    print(min(l))
else:
    print(-1)