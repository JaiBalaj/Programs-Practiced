import sys
a=[1,2,2,7,8,9,4,5,3,99,24,6,677,677]
largest=a[0]
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
seclar=a[0]
for i in range(len(a)):
    if a[i]>seclar and a[i]!=largest:
        seclar=a[i]
print(seclar)
