def FindXor(L,R):
    if L>R:
        return "Invaild Inputs"
    XorL=0
    for i in range(L):
        XorL^=i
    XorR=0
    for i in range(R+1):
        XorR^=i

    return XorL ^ XorR


L = 3
R = 5
print(FindXor(L,R))