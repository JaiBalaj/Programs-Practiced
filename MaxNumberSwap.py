import sys
number=input()
arr=[]
j=0
for each in number:
    arr.insert(j,int(each))
    j+=1
arr.sort()
sortArr=arr[::-1]