n=input()
s=n.lower()
s1=s.split()
l1=["a","e","o","i","u"]
for i in s1:
    c=0
    for j in i:
        if j in l1:
            c=c+1
    print(c,end=" ")