s=input()
v=input()
for i in s:
    if i==v:
        print("True")
        print(s.index(i))
        break
else:
    print("False")