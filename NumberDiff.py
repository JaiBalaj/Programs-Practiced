def values(num1,num2):
    print(num1,num2)
    jnext=0
    count=0
    for val1 in num1:
        j=jnext
        for val2 in num2:
            print(val1,num2[j])
            jnext+=1
            while(val1):
                digit1=val1%10
                digit2=val2%10
                val1=val1//10
                val2=val2//10
                if((digit1-digit2)>0):
                    diff=digit1-digit2
                    count+=diff
                elif((digit2-digit1)>0):
                    diff=digit2-digit1
                    count+=diff
            break
    print(count)
if __name__=="__main__":
    a=[2323]
    b=[2452]
    values(a,b)