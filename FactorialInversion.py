#Factorial Iversion
#for example
#1->1
#2->2
#6->3
#24->4
#120->5

n=int(input("Enter the Nth Factorial Value: "))
start=1
i=1
while True:
    start*=i
    if start>=n:
        break
    i += 1
fact=1
N=i
while(i):
    fact*=i
    i-=1
if(fact==n):
    print("Start: ",start,"i: ",N)
else:
    print(n,"Is not and Factorial")