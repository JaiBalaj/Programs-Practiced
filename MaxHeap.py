def check(arr,i):
     lEle=(2*i)+1
     rEle=(2*i)+2
     lEle=arr[lEle]
     rEle=arr[rEle]
     if arr[i]>=(lEle+rEle):
         check(arr,(i+1))
     else:
         return False

if __name__=="__main__":
    arr=[90,15,10]
    print(arr)
    retval=check(arr,0)
    if retval!=False:
        print("1")
    else:
        print("0")