s=input()
l=s.split()
v="aeiou"
l1=[]
for i in l:
    c=0
    for j in i:
        if j in v:
            c=c+1
    l1.append(c)
e=l1.count(max(l1))
print(e)