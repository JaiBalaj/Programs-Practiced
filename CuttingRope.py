def SingleDigit(arr,n):
    for a in arr:
        sum=1
        cnt=0
        while(sum<n):
            sum*=a
            cnt+=1


from itertools import combinations
if __name__=="__main__":
    n=int(input("Enter the Length of N meters: "))
    arr=[]
    for i in range(2,n):
        arr.append(i)
    print(arr)
    arrlen=len(arr)
    checkHere=[]
    j=0
    while(arrlen):
        finalList=(list(combinations(arr,arrlen)))
        for each in finalList:
            checkHere.insert(j,each)
            j+=1
        arrlen-=1
    #print(checkHere)
    MaxProduct=0
    for each in checkHere:
        if (sum(each)==n):
            print(each)
            product=1
            for every in each:
                product*=every
            if(product>MaxProduct):
                MaxProduct=product
    print("Max Product is",MaxProduct)
    getMax=SingleDigit(arr,n)