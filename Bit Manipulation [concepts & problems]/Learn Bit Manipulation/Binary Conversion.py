def convert2Binary(n):
    res=""
    while(n>0):
        res+= str(n&1)
        n=n>>1
    
    res=res[::-1]

    return res


n = int(input("Enter an number: "))
print(convert2Binary(n))