def fibo(n):
    a=0
    b=1
    #print(b,end=" ")
    arr=[]
    arr.insert(0,b)
    while n-1:
        val=a+b
        a=b
        #print(val,end=" ")
        arr.append(val)
        b=val
        n-=1
    #print(arr)
    return arr
if __name__=="__main__":
    arr=fibo(100)
    #n=int(input())
    #inputs=[input() for i in range()]
    yes=1
    while yes:
        each=(input())
        if each.isdigit():
            if int(each)==0:
                print(0)
            else:
                index=((int(each))-1)
                print(arr[index])
        else:
            yes=0