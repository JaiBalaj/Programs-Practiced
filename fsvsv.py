n=int(input())
while n:
    n=n-1
    s1,s2=input().split(" ")
    ls1=len(s1)
    ls2=len(s2)
    i=0
    while ls1>0 and ls2>0:
        print(s1[i],end="")
        print(s2[i],end="")
        i=i+1
        ls1=ls1-1
        ls2=ls2-1
    while ls1>0:
        print(s1[i],end="")
        ls1=ls1-1
        i=i+1
    while ls2>0:
        print(s2[i],end="")
        ls2=ls2-1
        i=i+1
    print()