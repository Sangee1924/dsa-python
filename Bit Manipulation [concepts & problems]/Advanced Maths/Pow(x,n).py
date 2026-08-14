def power(x,n):
    nn=n
    if n<0:
        n*=-1
    ans=1
    while(n>0):
        if n%2==0:
            x=x*x
            n=n//2
        else:
            ans*=x
            n-=1

    if nn<0:
        ans=1//ans
    return ans

x = 2
n = 10
print(power(x,n))