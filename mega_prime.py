N=int(input())
s=str(N)
l1=[]
for i in range(2,N+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l1.append(i)
if N not in l1:
    print("Not Mega Prime")
elif N in l1:
    c=0
    while N>0:
        n=N%10
        N=N//10
        if n in l1:
            c=c+1
            continue
if c==len(s):
    print("Mega Prime")

else:
    print("Not Mega Prime")