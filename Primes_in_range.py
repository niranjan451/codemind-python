from math import*
def isprime(a):
    if a>1:
        for i in range(2,int(sqrt(a)+1)):
            if a%i==0:
                return False
                break
        else:
            return True
    else:
        return False
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if isprime(i)==True:
        c=c+1
print(c)