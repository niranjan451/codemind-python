s=input()
s1=input()
s=s.lower()
s1=s1.lower()
for i in s:
    if i not in s1:
        print(False)
        break
else:
    print(True)