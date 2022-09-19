n=input()
m=n.split()
m1="".join(m)
for i in m:
    x=(ord(min(i)))
    y=(ord(max(i)))
    print(abs(x-y),end=" ")