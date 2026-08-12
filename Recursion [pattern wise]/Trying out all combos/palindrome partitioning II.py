ans=[]
def ispalindrome(i,j):
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def partition(i,s,arr):
    if i==len(s):
        ans.append(arr.copy())
        return
    for j in range(i,len(s)):
        if ispalindrome(i,j):
            arr.append(s[i:j+1])
            partition(j+1,s,arr)
            arr.pop()

    return ans

s = "aab"
print(partition(0,s,[]))