s1=input()
s2=input()
s1=s1.split()
s2=s2.split()
s1=''.join(s1)
s2=''.join(s2)
s1=s1.lower()
s2=s2.lower()
l=[]
for i in s1:
    if(i in s2) and (i not in l):
        l.append(i)
for j in s2:
    if (j  in s1) and (j not in l ):
        l.append(j)
l.sort()
print(len(l))