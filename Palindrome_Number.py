t=int(input())
for i in range(t):
    n=int(input())
    s=str(n)
    s1=s[::-1]
    if s==s1:
        print(True)
    else:
        print(False)