s=input()
m=s.split()
m1="".join(m)
c=0
for i in m1:
    if m1.count(i)==1:
        c=c+1
        d=i
        break
if c==0:
    print(-1)
else:
    print(d)
    