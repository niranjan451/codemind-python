s=input()
s2=s.split()
s1="".join(s2)
c=0
for i in s1:
    if i==i.upper():
        c=c+1
print(c)