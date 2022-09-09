s=input()
s1=s.lower()
n=s1.split()
l1=["a","e","i","o","u"]
l=[]
for i in n:
    c=0
    for j in i:
        if j in l1:
            c=c+1
    l.append(c)
print(min(l))