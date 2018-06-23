import math

EncryptedData = []
EncryptedDataModed = []
ModVal = []
ModInv= []
DivVal = []
InvEncryptedData= []
data = []
p, q =1,4

def Encrypt():
    print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    msg = input("Enter the message to Send\n")
    if msg!="":
        AsiForm = []

        for chart in msg:
            AsiForm.append(ord(chart))
        '''KEY GENERATING FUNCTION CALL HERE'''
        '''KEY SELECTING PART HERE'''
        print("Selected key pair are ", p, "and", q)
        print("\nMessage in ASCII:")
        print(AsiForm)

        #Encryption part here...pells equation
        for chart in AsiForm:
            EncryptedData.append((int((chart**p)/(chart**q))))
        print("===============================================================================")
        print("\nEncryped data:")
        print(EncryptedData)

        #Mod with 1028
        for chart in EncryptedData:
            ModVal.append(int(chart%1028))
            DivVal.append(int(chart/1028))
        print("Sending data to Reciver:")
        print(ModVal)
        print("===============================================================================")
    else:
        print("Input cannot be Empty")

def Decrypt():
    r = p-q
    print("Recived data:")
    print(ModVal)

    #inverse Mod Function
    for chart in range(len(ModVal)):
        ModInv.append(int((((DivVal[chart]*1028))+ModVal[chart])))
    #inverseing and pells EQ
    for chart in ModInv:
        InvEncryptedData.append(int(round(chart**(1/r))))
    print("Recvied converted")
    print(InvEncryptedData)
    #inverseing ASCII
    for chart in InvEncryptedData:
        data.append(chr(int(chart)))
    msg="".join(data)
    print("==============================================================================")
    print("Decrypted data")
    print(msg)
    print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


while True:
    if q>p:
        t=p
        p=q
        q=t
    Encrypt()
    Decrypt()