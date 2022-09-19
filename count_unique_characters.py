n=input()
m=n.split()
s="".join(m)
s2=s.lower()
s1=set(s2)
c=0
for i in s1:
    if s.count(i)==1:
        c=c+1
print(c)
