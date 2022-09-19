n=input()
m=n.split()
c=0
v='aeiouAEIOU'
for i in m:
    y=i[::-1]
    for j in range(0,(len(i)//2)):
        if ((i[j] in v) and (y[j] not in v)) or ((i[j] not in v) and (y[j] in v)):
            c=c+1
print(c)