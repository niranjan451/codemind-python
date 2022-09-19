n=input()
m=n.split()
m1="".join(m)
print(min(m1),m1.count(min(m1)),max(m1),m1.count(max(m1)))