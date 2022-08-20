n=int(input())
s=str(n)
l=list(s)
l1=[]
c=0

for i in l:
    if i=="9":
        l1.append(i)
    elif i=="6":
        c=c+1
        if c==1:
            l1.append("9")
            continue
        l1.append(i)
for j in l1:
    print(j,end="")

