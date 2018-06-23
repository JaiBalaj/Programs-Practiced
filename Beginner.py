if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().strip().split(" ")))
    minele=min(arr)
    maxele=max(arr)
    print(minele,maxele)
    TillMax=(maxele*(maxele+1))//2
    minele-=1
    TillMin=(minele*(minele+1))//2
    print(TillMax,TillMin)
    diff=TillMax-TillMin
    arrsum=sum(arr)
    if diff==arrsum:
        print(True)
    else:
        print(False)
