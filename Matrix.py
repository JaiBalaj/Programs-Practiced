if __name__=="__main__":
    print("Enter the Size of the Matrix: ")
    n,m=list(map(int,(input().split(" "))))
    print(n,m)
    matrix=[list(map(int,input().split(" "))) for i in range(n) ]
    for row in matrix:
        for each in row:
            print(each,end="\t")
        print()