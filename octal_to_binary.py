def octal(i):
    if i=="0":
        return "000"
    elif i=="1":
        return "001"
    elif i=="2":
        return "010"
    elif i=="3":
        return "011"
    elif i=="4":
        return "100"
    elif i=="5":
        return "101"
    elif i=="6":
        return "110"
    elif i=="7":
        return "111"
n=input()
s=''
c=0
for i in n:
    s=s+octal(i)
for i in s:
    if i=="0":
        c=c+1
    else:
        break
print(s[c:])
