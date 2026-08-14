def FindNumAppearsOnce(arr):
    ans =0
    for i in arr:
        ans^=i

    return ans


arr=[4,1,2,1,2]
print(FindNumAppearsOnce(arr))