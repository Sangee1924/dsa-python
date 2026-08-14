def convert2decimal(b):
    N = len(b)-1
    ans=0
    p2=1
    for i in range(N,-1,-1):
        if b[i]=='1':
            ans+=p2
        p2*=2
    return ans

b = input("Enter Binary : ")
print(convert2decimal(b))