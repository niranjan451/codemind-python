l=int(input())
n=input()
s=str(n)
l1=[]
for i in s:
    if i=="0":
        l1.insert(0,0)
    elif i=="1":
        l1.append(i)
for i in l1:
    print(i,end=" ")
