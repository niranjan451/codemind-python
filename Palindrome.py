N=int(input())
l1=[]
for i in range(100,N+1):
    s=str(i)
    st=list(s)
    d=st[::-1]
    if st==d:
        l1.append(i)
if N in l1:
    print("True")
else:
    print("False")