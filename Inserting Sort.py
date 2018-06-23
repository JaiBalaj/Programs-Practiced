import sys
import bisect
l=[]
def insert(ele):
    bisect.insort(l,ele)

if __name__=="__main__":
    n=int(input("Enter the Number of Elements :"))
    print("Enter the Elements: ")
    for  i in range(n):
        insert(int(input()))
    print("Now the List Bisect sort is: ")
    for each in l:
        print("%d"%each)
    print("done")