if __name__=='__main__':
    n=int(input())
    unsorted=[]
    unsorted=list(input().split(' '))
    unsorted.sort(key=lambda element:(len(element),element))
    print(unsorted)