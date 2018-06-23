def SOD(num):
    total=0
    while num>0:
        digit=num%10
        num=num//10
        total+=digit
    return total

if __name__ == '__main__':
    num=SOD(100)
    print("called")
    print(num)