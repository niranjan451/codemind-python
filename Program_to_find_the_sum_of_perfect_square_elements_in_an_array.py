n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    for j in range(0,(i+1)):
        if int(j)*int(j)==int(i):
            s=s+int(i)
print(s)
    