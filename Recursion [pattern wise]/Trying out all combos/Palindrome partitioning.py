def ispalindrome(i,j):
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def partition(i,s):
    if i==len(s):
        return 0
    mini=float('inf')
    for j in range(i,len(s)):
        if ispalindrome(i,j):
            ans= 1 + partition(j+1,s)
            mini=min(mini,ans)

    return mini

s = "aab"
print(partition(0,s)-1)