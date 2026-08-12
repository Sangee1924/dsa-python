def CombinationSumIII(k,n):
    arr=[1,2,3,4,5,6,7,8,9]
    ans=[]

    def rec(ind,sum,ds):
        if len(ds)==k:
            if sum==n:
                ans.append(ds.copy())
            return

        for i in range(ind,len(arr)):
            ds.append(arr[i])
            rec(i+1,sum+arr[i],ds)
            ds.pop()

        return

    rec(0,0,[])

    return ans

k = 3
n = 9

print(CombinationSumIII(k,n))