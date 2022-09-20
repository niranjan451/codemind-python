s1=input()
s2=input()
s3=s1.lower()
s4=s2.lower()
n=s3.split()
m=s4.split()
for i in m:
    if i in n:
        print(i,end=" ")
