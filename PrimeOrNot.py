def check(i):
    for x in range(2,((i//2))):
        if (i%x)==0:
            return 0
    return 1

def getPrime(l,r):
    arr=[]
    for i in range(l+1,r):
        if(check(i)):
            arr.insert(i,i)
    return arr

if __name__=="__main__":
    l,r=list(map(int,input().split(" ")))
    nums=[0,0,0,0,0,0,0,0,0,0]
    arr=getPrime(l,r)
    print(arr)
    for each in arr:
        while each:
            digit=each%10
            nums[digit]+=1
            each=each//10
    maxele=max(nums)
    atIndex=nums.index(maxele)
    print("Number ",(atIndex),"is Repeated ",maxele,"Number of times")