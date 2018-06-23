if __name__=="__main__":
    a=[2,4,9,3,1,5,7,8,6]
    sec=a[0]
    lar=a[0]
    diff=0
    for i in range(int(len(a))):
        if(a[i]>lar):
            sec=lar
            lar=a[i]
    print(lar,sec)