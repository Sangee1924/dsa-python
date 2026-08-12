def countsum(s,k):
    def rec(i,sum):
        if i==len(s):
            if sum==k:
                return 1
            else:
                return  0

        left = rec(i+1,sum+s[i])

        right = rec(i+1,sum)

        return left+right

    ans = rec(0,0)
    return ans


arr = [1,2,3,4,5]
k = 10
print(countsum(arr,k))