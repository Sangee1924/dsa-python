def setRightmostBit(num):
    if (num & (num+1)) ==0:
        return num

    return num | (num+1)


num = int(input("Enter an Number : "))
print(setRightmostBit(num))