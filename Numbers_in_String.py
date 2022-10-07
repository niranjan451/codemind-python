n=input()
s=n.split()
c=0
for i in s:
    for j in i:
        if j.isdigit()==True:
            c=c+int(j)
print(c)