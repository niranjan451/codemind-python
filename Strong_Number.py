n=int(input())
s2=str(n)
l=[]
for i in s2:
    s1=1
    for j in range(int(i),0,-1):
        s1=s1*j
    l.append(s1)
if sum(l)==n:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")
    
    