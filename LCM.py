a,b=map(int,input().split())
big=max(a,b)
small=min(a,b)
a=big
i=2
while True:
    if (big%small==0):
        print(big)
        break
    else:
        big=a*i
        i=i+1
