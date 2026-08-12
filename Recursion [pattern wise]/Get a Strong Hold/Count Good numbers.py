MOD = 10**9 +7

def power(ans,x,n):
    if n==0:
        return ans
    if n%2==0:
        return power(ans,(x*x)%MOD,n//2)
    else:
        return power((ans*x)%MOD,x,n-1)

def goodnumber(n):
    even = (n+1)//2
    odd = n//2

    p1 = power(1,5,even)
    p2 = power(1,4,odd)

    return (p1 * p2) % MOD


n = int(input("Enter an number : "))
print(goodnumber(n))