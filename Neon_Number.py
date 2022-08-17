N=int(input())
s=0
for i in range(1,N+1):
    n=N*N
    r=n%10
    n=n//10
    s=s+r
if s==N:
    print("Neon Number")
else:
    print("Not Neon Number")