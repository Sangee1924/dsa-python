def SubsetII(arr):
    ans=[]
    def rec(ind,ds):
        ans.append(ds.copy())

        for i in range(ind,len(arr)):
            if i > ind and arr[i]==arr[i-1]:
                continue
            ds.append(arr[i])
            rec(i+1,ds)
            ds.pop()
        return

    rec(0,[])

    return ans

arr=[1,2,2]
arr.sort()

print(SubsetII(arr))