'''
3[b2[ca]]
bcacabcacabcaca

'''
'''def GetFinal(add,num):
    print("ADD is ",add)
    string="".join(add)
    string*=num
    print("String val is ",string)
    print("Before returning :",string)
    return string

Stack=[]
string=input("Enter the Stirng: ")
for each in string:
    Stack.append(each)
print(Stack)
add=[]
val=[]
final=""
while Stack:
    char=Stack.pop()
    if char>='a' and char<='z':
        add.insert(0,char)
        print("now ARR: ",add)
    if char>='1' and char<='9':
        add.append(final)
        final+=GetFinal(add,int(char))
        add=[]
print(final)
'''
#Another Solution
import re
if __name__=="__main__":
    string=input("Enter the String: ")
    nums=re.findall('[0-9]+',string)
    alpha=re.findall('[a-z]+',string)
    print(nums)
    print(alpha)
    final=""
    while nums:
        substr=alpha.pop()
        num=int(nums.pop())
        final=substr+final
        final*=num
    print(final)