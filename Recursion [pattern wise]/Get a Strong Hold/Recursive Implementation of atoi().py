def rec(ans,s,i):
    if (i>=len(s) or not('0'<= s[i] <= '9')):
        return ans

    digit = int(s[i])
    if ans > (2**31 -1)//10 or (ans == (2**31 -1)//10 and digit>7):
        return (2**31)

    ans = ans*10 + digit

    return rec(ans,s,i+1)

def atoi(s):
    sign = 1
    i = 0
    ans = 0

    while(i<len(s) and s[i]==" "):
        i+=1
    if(i<len(s) and s[i]=="-"):
        sign=-1
        i+=1
    elif(i<len(s) and s[i]=="+"):
        sign=1
        i+=1

    ans = rec(ans,s,i)

    if ans == (2**31):
        return (2**31)-1 if sign==1 else -(2**31)
    
    ans = ans*sign
    return ans


s = input("enter : ")
print(atoi(s))
