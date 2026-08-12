def rec(ans,x,nn):
    if nn==0:
        return ans
    if nn%2 == 0:
        return rec(ans,x*x,nn//2)
    else:
        return rec(ans*x,x,nn-1)

def pow(x,n):
    nn = n
    ans=1
    if n<0:
        nn=nn*(-1)

    ans = rec(ans,x,nn)

    if n<0:
        ans = float(1.0)/float(ans)
    return ans

x = int(input("Enter the number : "))
n = int(input("Enter the power : "))
print(pow(x,n))