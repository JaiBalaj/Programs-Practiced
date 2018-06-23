n=int(input("Enter the Range of Numbers: "))
for i in range(1,n):
    every=str(i)
    if(every==every[::-1]):
        print(every)