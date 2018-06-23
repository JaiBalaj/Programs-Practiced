import sys
n=input()
while(len(n)>1):
    sum=0
    for each in n:
        sum+=int(each)
    n=str(sum)
print(n)