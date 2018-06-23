if __name__ == '__main__':
    namelist=[]
    scorelist=[]
    finalname=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        namelist.insert(i,name)
        scorelist.insert(i,score)
    print(namelist)
    print(scorelist)
    minscr=min(scorelist)
    minindex=scorelist.index(minscr)
    while minscr in scorelist:
        minindex=scorelist.index(minscr)
        scorelist.remove(minscr)
        namelist.remove(namelist[minindex])
    minscr=min(scorelist)
    print(namelist)
    print(scorelist)
    while minscr in scorelist:
        minindex=scorelist.index(minscr)
        name=namelist[minindex]
        finalname.insert(i,name)
        scorelist.remove(minscr)
        namelist.remove(namelist[minindex])
    print(finalname)
    finalname=(sorted(finalname))
    for each in finalname:
        print(each)