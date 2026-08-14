def divide(Dividend,Divisor):
    if Divisor == 0:
        return "Division by zero is not allowed"
    if Dividend==Divisor:
        return 1

    sign = True
    if (Dividend>=0 and Divisor<0) or (Dividend<0 and Divisor>=0):
        sign=False

    n = abs(Dividend)
    d = abs(Divisor)

    q = 0

    while(n>=d):
        cnt=0
        while(n>=(d<<(cnt+1))):
            cnt+=1
        q+=(1<<cnt)
        n-= (d<<cnt)

    if q > 2**31 -1 and sign:
        return 2**31-1
    if q > 2**31 and not sign:
        return -2**31

    return q if sign else -1*q    



Dividend = int(input("Enter an number : "))
Divisor = int(input("Enter an number : "))

print(divide(Dividend,Divisor))