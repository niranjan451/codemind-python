n=input()
v=["a","e","i","o","u","A","E","I","O","U"]
l1=[]
for i in n:
    if i in v :
        if i not in l1:
            l1.append(i)
print(*l1)
    