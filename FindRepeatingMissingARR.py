n=int(input("Enter the Array Size: "))
print("Enter the Array elements: ")
arr=list(map(int,input().split(" ")))
maxEle=max(arr)
HashMap=[]
for i in range(maxEle+1):
    HashMap.append(0)

print("HasMap Before processing: ",HashMap)

for each in arr:
    HashMap[each]+=1

print("HashMap val",HashMap)

for i in range(1,len(HashMap)):
    if HashMap[i]==0 or HashMap[i]>1:
        print(i,end=" ")

'''
Enter the Array Size: 6
Enter the Array elements: 
4 3 6 2 1 1
HasMap Before processing:  [0, 0, 0, 0, 0, 0, 0]
HashMap val [0, 2, 1, 1, 1, 0, 1]
1 5 
'''