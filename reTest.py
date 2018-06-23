import sys
import re
string="w:/aa11\abb://sa1\a"
str2="iuvhwddddiu\w078679"
a="\\"
arr=re.findall('[a-z]:/[a-z]*[0-9]*.*[a-z]',string)
arr=re.findall('',str2)
for each in arr:
    print(each)