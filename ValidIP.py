import sys
IP=input("Enter a Valid IP : ")
arr=IP.split(".")
flag=0
if len(arr)!=4:
    flag=1
    print("Invalid")
    sys.exit()
for each in arr:
    if(int(each)>255):
        flag=1
        print("Invalid")
    if(len(each)>1 and int(each)<=9):
        print("Invalid")
        flag=1
    if(len(each)>2 and int(each)<=99):
        print("Invalid")
        flag = 1
if(flag!=1):
    print("Valid")