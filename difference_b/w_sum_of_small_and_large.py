n=input()
m=n.split()
s=0
l=0
for i in m:
    s=s+(ord(min(i)))
    l=l+(ord(max(i)))
print(l-s)