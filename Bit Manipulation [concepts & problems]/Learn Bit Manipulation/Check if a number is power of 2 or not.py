def checkP2(num):

    if num & (num-1)==0:
        print(f"{num} is Power of 2")
    else:
        print(f"{num} is Not Power of 2")

    return

num = int(input("Enter an Number : "))
checkP2(num)