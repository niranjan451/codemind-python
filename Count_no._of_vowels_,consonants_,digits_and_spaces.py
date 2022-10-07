n=input()
v1="AEIOUaeiou"
v=0
c=0
d=0
s=0
for i in n:
    if i.isalpha()==True:
        if i in v1:
            v=v+1
        else:
            c=c+1
    elif i.isdigit()==True:
        d=d+1
    elif i==" ":
        s=s+1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",s)
        