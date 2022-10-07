n=int(input())
l=[]
for i in range(1,n*n):
    if i==1:
        l.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
if n in l:
    s=str(n)
    s1=s[::-1]
    if int(s1) in l:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    