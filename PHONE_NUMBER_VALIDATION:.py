n=int(input())
s=str(n)
if len(s)==10:
    if s[0]=="0":
        print("Invalid")
    else:
        print("Valid")
else:
    print("Invalid")