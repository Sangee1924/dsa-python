def primeFactor(num):
    ans=[]
    iter=int(num**0.5)+1
    for i in range(2,iter):
        if num%i==0:
            ans.append(i)
            while(num%i==0):
                num=num//i

    if num!=1:
        ans.append(num)

    return ans


num = int(input("Enter a number : "))
print(primeFactor(num))