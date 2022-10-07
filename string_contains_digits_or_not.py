t=int(input())
for i in range(t):
    n=input()
    for i in n:
        if i.isdigit()==True:
            print("Yes")
            break
    else:
        print("No")
    