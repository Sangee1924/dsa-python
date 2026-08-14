def NoOfBitsToConvertA2B(A,B):
    xor=A^B
    cnt=0
    for i in range(31):
        if (xor & (1<<i)):
            cnt+=1
    return cnt


A = int(input("Enter a number : "))
B = int(input("Enter a number : "))

print(NoOfBitsToConvertA2B(A,B))