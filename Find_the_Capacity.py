a,b,c=map(int,input().split())
x=2*a*b*c*512
s=str(x//1024)
print(s+"KB")