string=input("Enter the String: ")
i=0
strlen=len(string)
print(strlen)
while i<=strlen:
    if ((i+1)!=strlen) and (string[i]==string[i+1]):
        continue
        cnt=1
        while ((i+1)!=strlen) and (string[i]==string[i+1]):
            cnt+=1
            i+=1
            if((i+1)==strlen):
                break
        print(string[i],cnt,end=" ")
        i+=1
    else:
        print(string[i],1,end=" ")
        i+=1
    if (i+1)>=strlen:
        break
if(i!=strlen):
    print(string[i],1,end=" ")

'''
    input wwwwaaadexxxxxxab
'''