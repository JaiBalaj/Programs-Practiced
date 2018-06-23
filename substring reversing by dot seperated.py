n=int(input())
while n:
    n=n-1
    arr=input().split(".")
    arr=(reversed(arr))
    new=""
    for each in arr:
        new=new+each+"."
    new=new[:len(new)-1]
    print(new)