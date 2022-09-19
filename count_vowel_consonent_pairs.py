n=input()
m=n[::-1]
c=0
v='aeiouAEIOU'
for i in range(0,(len(n)//2)):
    if ((n[i] in v) and (m[i] not in v)) or ((n[i] not in v) and (m[i] in v)):
        if ((n[i]!=' ') and (m[i]!=' ')):
            c=c+1
print(c)