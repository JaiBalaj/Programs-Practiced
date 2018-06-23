if __name__=="__main__":
    a=[9,8,7,6,5,4,3,2,4,3,5,7,8,1,0]
    if(a[0]>a[1]):
        lar=a[0]
        sec=a[1]
    else:
        lar=a[1]
        sec=a[0]
    diff=lar-sec
    for i in range(2,len(a)):
        diff=lar-sec
        if a[i]>lar:
            sec=lar
            lar=a[i]
        else:
            if ((lar-a[i])<diff):
                sec=a[i]
    print("First Largest",lar,"\nSecond Largest",sec)
