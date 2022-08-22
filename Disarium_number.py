N=int(input())
s=str(N)
l=list(s)
a=1
s1=0
for i in l:
    x=int(i)
    r=pow(x,a)
    s1=s1+r
    a+=1
if s1==N:
    print("True")
else:
    print("False")
    
    