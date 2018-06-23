if __name__=="__main__":
    n=int(input())
    arr=[input() for i in range(n)]
    #print(arr)
    from itertools import permutations
    arr=list(permutations(arr))
    FinalLen=0
    print(arr)
    for each in arr:
        string="-".join(each)
        print(string)
        flag=0
        for i in range(len(string)):
            if string[i]=='-':
                if string[i-1]!=string[i+1]:
                    maxl=string[:i]
                    print(maxl)
                    if len(maxl)>FinalLen:
                        FinalLen=len(maxl)
                        flag=1
                        break
            if flag==1:
                break
            else:
                maxl=string[:i+1]
                print(maxl)
        if flag!=1:
            maxl=len(string)
    print(FinalLen)