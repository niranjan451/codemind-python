from math import *
def isprime(i):
    if i>1:
        for j in range(2,int(sqrt(i))+1):
            if i%j==0:
                return False
                break
        else:
            return True
    else:
        return False
n=int(input())
l1=[]
for i in range(1,n+1):
    if (n%i==0 and isprime(i)==True):
        l1.append(i)
if len(l1)>=2:
    print(*l1)
else:
    print(-1)
        
