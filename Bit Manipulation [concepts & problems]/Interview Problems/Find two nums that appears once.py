def Find2NumAppearsOnce(nums):
    xor=0
    for i in nums:
        xor^=i

    SetBit = (xor & (xor-1)) ^ xor

    b1=0
    b2=0

    for i in nums:
        if i & SetBit:
            b1^=i
        else:
            b2^=i

    return b1,b2


nums = [1, 2, 1, 3, 5, 2]
print(Find2NumAppearsOnce(nums))