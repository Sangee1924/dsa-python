def oddOReven(num):
    if num&1==1:
        print(f"{num} is ODD NUMBER")
    else:
        print(f"{num} is EVEN NUMBER")

    return

num = int(input("Enter Number :"))
oddOReven(num)