def checkset(binary,i):
    if binary & (1 << i):
        print(f"In {binary}, bit {i} is set bit")
    else:
        print(f"In {binary}, bit {i} is not set bit")

    return

binary = int(input("Enter binary number : "))
i = int(input("Enter an bit number : "))
checkset(binary,i)