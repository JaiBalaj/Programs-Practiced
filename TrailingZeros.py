def SOD(s0,s1,n):
    if(n==0):
        return s0
    if(n==1):
        return s1
    n-=1
    while n:
        val=s0*s1
        s0=s1
        s1=val
        n-=1
    return val

if __name__=="__main__":
    cnt=0
    s0=int(input())
    s1=int(input())
    n=int(input())
    val=SOD(s0,s1,n)
    val=int(val)
    print(val)
    while val>=0:
        if val%10==0:
            cnt+=1
            val=int(val/10)
            print(val)
        else:
            break
    print(cnt)