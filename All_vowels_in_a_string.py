s=input()
n=s.split()
m=''.join(n)
k=m.lower()
v=["a","i","e","o","u"]
l1=[]
for i in m:
    if i in v :
        if i not in l1:
            l1.append(i)
if len(l1)==5:
    print("True")
else:
    print("False")
