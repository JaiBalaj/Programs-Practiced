from itertools import combinations
n=int(input("Enter the Number of Elements: "))
arr=list(map(int,input("Enter the Elements:\n").split(" ")))
#arr=list(set(arr))
check=int(input("Enter the sum to be checked: "))
print("Possible solutions...")
tplset=[]
for i in range(1,n+1):
    cur=list(combinations(arr,i))
    for each in cur:
        if sum(each)==check:
            tplset.append(list(each))
tplset.append(None)
for i in range(len(tplset)-1):
    if tplset[i]!=tplset[i+1]:
        print(tplset[i],end=" ")