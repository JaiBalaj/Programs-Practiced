import sys
n=int(input())
binval=[]
while n:
    num=n%2
    binval.insert(0,num)
    n=n//2
print(binval)
binval=list(map(str,binval))
string="".join(binval)
print(string)
