global arr,n
global SX,SY,DX,DY

def check():
    diff=10000
    for i in range(n):
        if PX[i]!=-1 or PY[i]!=-1:
            if (abs(SX-PX[i])+abs(SY-PY[i]))<diff:
                diff=(abs(SX-PX[i])+abs(SY-PY[i]))
                ind=i
    return (ind,diff)

n=int(input("Enter the number of locations:"))
arr=list(map(int,input().split()))
SX=arr[0]
SY=arr[1]
DX=arr[2]
DY=arr[3]
print(arr)
PX=[arr[i] for i in range(4,n*2+4,2)]
PY=[arr[i] for i in range(5,n*2+4,2)]
N=n
res=0
while N:
    ind=list(check())
    SX=PX[ind[0]]
    SY=PY[ind[0]]
    PX[ind[0]]=-1
    PY[ind[0]]=-1
    print(ind[1])
    N=N-1
    res=res+ind[1]
res=res+abs(SX-DX)+abs(SY-DY)
print(res)