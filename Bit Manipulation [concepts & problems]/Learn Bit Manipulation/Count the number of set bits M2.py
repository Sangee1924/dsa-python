def Countsetbit(num):
    count=0
    while(num>0):
        count+=1
        num=num&num-1

    return count



num = int(input("Enter an Number:"))
print(Countsetbit(num))