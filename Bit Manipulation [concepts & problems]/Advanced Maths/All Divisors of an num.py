def AllDivisor(num):
    ans=[]
    iter=int(num**0.5)+1
    for i in range(1,iter):
        if num%i==0:
            ans.append(i)
            if num//i!=i:
                ans.append(num//i)

    return ans


num = int(input("Enter an Number : "))
print(AllDivisor(num))