n=int(input())
s1=0
p=1
s=str(n)
l=list(s)
for i in l:
    s1=s1+int(i)
    p=p*int(i)
print(abs(p-s1))