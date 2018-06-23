import sys
a=[1,4,0,3,8,9]
find=25
total=0
for i in range(len(a)):
    total+=a[i]
    index=i
    if total>=find:
        break
total=0
toindex=index
yes=0
for i in range(index,0,-1):
    total+=a[i]
    if(total==find):
        print("True")
        yes=1
        fromindex=i
        break

if(yes!=1):
    print("No Sub Array found")
else:
    print("Found from ",(fromindex),"to",(toindex))