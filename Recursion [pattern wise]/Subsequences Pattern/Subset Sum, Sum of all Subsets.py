def subsetSum(N,arr):
    ans=[]
    def rec(i,sum):
        if i==N:
            ans.append(sum)
            return 

        rec(i+1,sum+arr[i])
        rec(i+1,sum)
        return

    rec(0,0)

    return ans

N = 3
arr=[5,2,1]
ans=subsetSum(N,arr)
ans.sort()
print(ans)