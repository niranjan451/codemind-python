n=int(input())
for i in range(n+1,n**2):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        s=str(i)
        s.split()
        y=s[::-1]
        if s==y:
            print(s)
            break