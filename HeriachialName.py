if __name__=="__main__":
    n=int(input())
    newlist=[]
    k=0
    arr=[input() for i in range(n)]
    name=input("Entre the Name: ")
    row=[each.split(" ") for each in arr]
    print(row)
    arr1=[]
    arr2=[]
    global j
    j=0
    for each in row:
        arr1.insert(j,each[0])
        arr2.insert(j,each[1])
        j+=1
    j=0
    global finalList
    finalList=[]
    index=arr1.index(name)
    finalList.insert(j,arr1[index])
    j+=1
    finalList.insert(j,arr2[index])
    j+=1
    global find
    find=arr2[index]
    arr1.remove(arr1[index])
    arr2.remove(arr2[index])
    for each in arr1:
        if each==find:
            index=arr1.index(each)
            finalList.insert(j,arr2[index])
            j+=1
            arr1.remove(each)
            arr2.remove(arr2[index])
