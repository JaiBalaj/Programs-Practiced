if __name__=='__main__':
    string=""
    fp=open("new.txt","r")
    string=fp.read()
    import re
    names=re.findall('[A][m][a-z]*',string)
    print(names)
    for each in names:
        substr=each.split(",")
        for every in substr:
            yes="mi" in every
            if(yes):
                print(every)
            break
    print(fp.tell())