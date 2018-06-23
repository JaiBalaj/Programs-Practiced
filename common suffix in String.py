def longestCommonPrefix(A):
        first=A[0]
        a=1
        for each in A:
            if a==1:
                a=0
                continue
            str1=first
            str2=each
            comms=""
            if len(str1)>len(str2):
                for i in range(0,len(str2)):
                    if str1[i]!=str2[i]:
                        break
                    else:
                        comms=comms+str1[i]
            else:
                for i in range(0,len(str1)):
                    if str1[i]!=str2[i]:
                        break
                    else:
                        comms=comms+str1[i]
            first=comms
        return first

if __name__=="__main__":
    A=["Jai Balaj","Jayan","Jaban ji"]
    print("Longest Common Substring is :",longestCommonPrefix(A))




#Longest Prefix and Suffix in a string:
#eg abab here ab is the max pre anf suf

n=int(input())
for X in range(n):
    inp=input()
    slen=len(inp)
    i=1
    flag=0
    while(slen):
        slen=slen-1
        prefix=inp[:slen]
        suffix=inp[i:]
        i=i+1
        if prefix==suffix:
            print(len(prefix))
            flag=1
            break
    if flag==0:
        print("0")