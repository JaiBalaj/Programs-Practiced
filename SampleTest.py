import re
string=input("Enter Your String: ")
atoz=re.findall('[A-Z]',string)
numz=re.findall('[0-9]+',string)
for i in range(len(atoz)):
    for j in range(i,len(atoz)-1):
        if atoz[j]>atoz[j+1]:
            temp=atoz[j]
            atoz[j]=atoz[j+1]
            atoz[j+1]=temp
numz=list(map(int,numz))
for each in atoz:
    print(each,end="")
print(sum(numz))

'''
AC2BEW3
ABCEW5
'''
