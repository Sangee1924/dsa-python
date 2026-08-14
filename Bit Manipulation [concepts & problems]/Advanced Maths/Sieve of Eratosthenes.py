def PrimeCount(queries):
    ans=[]
    N = max(q[1] for q in queries) + 1
    prime=[1]*N

    for i in range(2,int(N**0.5)+1):
        if prime[i]==1:
            for j in range(i*i,N,i):
                prime[j]=0

    for j in range(len(queries)):
        l=[]
        for i in range(queries[j][0],queries[j][1]+1):
            if prime[i]==1:
                l.append(i)
        ans.append(l)

    return ans


queries = [ [2, 5], [4, 7] ]
print(PrimeCount(queries))