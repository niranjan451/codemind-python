n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i==1:
        c=c+1
for i in l:
    if i<1:
        l.remove(i)
if c==0:
    print(1)
else:
    l1=list(range(min(l),max(l)+1))
    for i in l1:
        if i not in l:
            print(i)
            break
    else:
        print(max(l)+1)