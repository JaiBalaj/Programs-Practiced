data=input("Enter the Message in Nokia 1100 with _ as delimeter: \n")
arr=data.split("_")
two="abc2"
three="def3"
four="ghi4"
fiv="jkl5"
six="mno6"
sev="pqrs7"
egiht="tuv8"
nine="wxyz9"
for each in arr:
    slen=(len(each))-1
    if each[0] == '2':
        i = slen % 4
        print(two[i],end="")
    if each[0] == '3':
        i = slen % 4
        print(three[i], end="")
    if each[0] == '4':
        i = slen % 4
        print(four[i], end="")
    if each[0] == '5':
        i = slen % 4
        print(fiv[i], end="")
    if each[0] == '6':
        i = slen % 4
        print(six[i], end="")
    if each[0] == '7':
        i = slen % 5
        print(sev[i], end="")
    if each[0] == '8':
        i = slen % 4
        print(egiht[i], end="")
    if each[0] == '9':
        i = slen % 5
        print(nine[i], end="")
    if each[0] == '0':
        print(" ", end="")
print()