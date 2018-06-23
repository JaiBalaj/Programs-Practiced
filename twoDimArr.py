n,m=map(int,input("Enter the row and column of Array:").split())
arr=list(map(int,input().split()))
mat=[[arr[j*m+i]for i in range(m)]for j in range(n) ]
import numpy as np
arr=np.zeros([3,2],int)
print(arr)
print(arr[2])