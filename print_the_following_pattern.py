n=int(input())
for i in range(1,n+1):
    for j in range(n):
        print(chr(i+64),end=" ")
    print()