t=int(input())
l=[]
for i in range(t):
    l1=list(map(int,input().split()))
    l.append(l1)
m=l[::-1]
s1=0
for i in range(t):
    for j in range(len(l)):
        if i==j:
            s1=s1+l[i][j]
s2=0
for i in range(t):
    for j in range(len(m)):
        if i==j:
            s2=s2+m[i][j]
print('Principal Diagonal:{}'.format(s1))
print('Secondary Diagonal:{}'.format(s2))