#(2n-1) for every digit upto n

n=input("Enter Upto n: ")
sum=0
val=0
for i in range(1,n+1):
    val=((2*i)-1)+sum
    