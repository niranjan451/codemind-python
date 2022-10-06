s=input()
s4=s.split()
s3="".join(s4)
l=[]
for i in s3:
    l.append(ord(i))
x=min(l)
y=max(l)
a=l.count(x)
b=l.count(y)
print(chr(x),a,chr(y),b)

    
