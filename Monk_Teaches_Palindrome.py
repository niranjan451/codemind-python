t=int(input())
for i in range(t):
    n=input()
    m=n[::-1]
    if n==m:
        if len(n)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")