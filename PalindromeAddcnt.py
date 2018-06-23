import sys
s=input()
revS=s
if s==s[::-1]:
    print("String is itself in Palindrome")
else:
    for i in range(1,(len(revS))+1):
        add=revS[:i]
        add=add[::-1]
        print("add",add)
        revadd=s+add
        print("revad",revadd)
        if revadd==revadd[::-1]:
            print(True)
            print(i)
            break
