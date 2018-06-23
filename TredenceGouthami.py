import re
import sys
'''string="Jaanagd"
for i in range(ord('z'),ord('a')-1,-1):
    ind=(string.find(chr(i)))
    if(ind!=-1):
        print(string[ind:])
        break'''
T=int(input())
for i in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    mine=arr[0]
    maxdiff=-sys.maxsize-1
    for i in range(1,len(arr)):
        maxdiff=max(maxdiff,arr[i]-mine)
        if arr[i]<mine:
            mine=arr[i]
    print(maxdiff)