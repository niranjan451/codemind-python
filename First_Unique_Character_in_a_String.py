c=input()
c.lower()
c1=0
for i in range(len(c)):
    if c.count(c[i])==1:
        d=i
        c1=c1+1
        break
if c1==0:
    print(-1)
else:
    print(d)

        