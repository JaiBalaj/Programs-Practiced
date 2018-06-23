import sys
string=input()
key=int(input("Enter the Key :"))
ch=int(input("\n1.Encrytion\n2.Decrytion\nEnter Your Choice: "))
key = key % 26
start = ord('a')
ending = ord('z')
if ch==1:
    for each in string:
        if each==' ':
            print(' ',end="")
            continue
        check=ord(each)+key
        if check>ending:
            froma=check-ending
            print(chr(start+froma-1),end="")
        else:
            print(chr(check),end="")
if ch==2:
    for each in string:
        check=ord(each)-key
        if check<start:
            fromz=ending-(start-check)+1
            #print(check,start,chr(check))
            print(chr(fromz),end="")
        else:
            print(chr(check),end="")
