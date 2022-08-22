n=int(input())
b=len(str(n))
c=int()
c=n*n
d=c%(pow(10,b))
if d==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")