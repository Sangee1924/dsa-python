def combinationSumII(arr,target):
    ans=[]
    arr.sort()
    def rec(ind,target,ds):
        if target==0:
            ans.append(ds.copy())
            return
        if ind == len(arr):
            return

        for j in range(ind,len(arr)):
            if j>ind and arr[j]==arr[j-1]:
                continue

            if arr[j]>target:
                break

            ds.append(arr[j])
            rec(j+1,target-arr[j],ds)
            ds.pop()
        return    

    ds=[]
    rec(0,target,ds)

    return ans
   

arr = [2,5,2,1,2]
target = 5

print(combinationSumII(arr,target))