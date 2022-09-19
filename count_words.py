n=input()
k=n.split()
c=0
v='aeiouAEIOU'
for i in k:
    if (i[0] in v) and (i[-1] not in v):
        c=c+1
print(c)