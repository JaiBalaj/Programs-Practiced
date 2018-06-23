n1=input()
n2=input()
if int(n1)<0 :
    print("Invalid Input")
n1=n1[::-1]
n2=n2[::-1]
n1=int(n1)
n2=int(n2)
val=n1+n2
val=str(val)
val=val[::-1]
print(int(val))