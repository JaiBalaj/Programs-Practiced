if __name__=="__main__":
    num=int(input())
    for number in range(1,num+1):
        octnum=oct(number)
        hexnum=hex(number).upper()
        binnum=bin(number)
        octnum=octnum[2:]
        hexnum=hexnum[2:]
        binnum=binnum[2:]

        #print(number,end="\t")
        print(octnum+"\t"+hexnum+"\t"+binnum)