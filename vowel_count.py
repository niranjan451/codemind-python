n=input()
x=n.lower()
s="aeiou"
c=0
for i in x:
    if i in s:
        c=c+1
print(c)
        