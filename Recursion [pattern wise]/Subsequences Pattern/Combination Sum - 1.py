def combinationSum(arr,target):
    ans=[]
    def rec(i,target,ds):
        if i == len(arr):
            if target==0:
                ans.append(ds.copy())
            return
        if arr[i]<=target:
            ds.append(arr[i])
            rec(i,target-arr[i],ds)
            ds.remove(arr[i])
                
        rec(i+1,target,ds)
        return

    ds=[]
    rec(0,target,ds)

    return ans
   

arr = [2,3,6,7]
target = 7
print(combinationSum(arr,target))