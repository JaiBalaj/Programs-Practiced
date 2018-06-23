if __name__=="__main__":
    arr=input().strip()
    a='{'
    b='}'
    c="("
    d=")"
    e="["
    f="]"
    stack=[]
    strlen=arr.__len__()
    halflen=int((strlen/2))
    cnt=0
    if strlen%2!=0:
        print("False")
    else:
        for each in arr:
            if each in (a,c,e):
                stack.append(each)
            elif each in (b,d,f):
                x=stack.pop()
                if each==b and x==a or each==d and x==c or each==f and x==e:
                    cnt=cnt+1
        if cnt==halflen:
            print("True")
        else:
            print("False")