s=input()
s1=s.lower()
s1=s1.split()
c=0
for i in s1:
    x=i
    if x==x[::-1]:
        c=c+1
print(c)
        