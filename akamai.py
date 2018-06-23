'''import sys
n=input()
if int(n)<10 or n==n[::-1]:
    print("Invalid Input")
    sys.exit(0)
val=(abs(int(n)-int(n[::-1])))
print(val)
cnt=0
while True:
    if val%2==0:
        cnt+=1
        val=val//2
    else:
        break
print(cnt)
'''
n=int(input("Enter the number of Elements: "))
print("Enter the Elements: ")
arr=input().split(" ")
sum1=""
sum2=""
for i in range(0,n,2):
    sum1+=str(arr[i])
for i in range(1,n,2):
    sum2+=str(arr[i])
print(int(sum1)+int(sum2))