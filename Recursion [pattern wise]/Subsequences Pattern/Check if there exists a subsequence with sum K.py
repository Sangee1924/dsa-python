def checksubsequencesumK(s,k):
    def rec(i,sum):
        if i==len(s):
            if sum==k:
                return True
            else:
                return False

        if rec(i+1,sum+s[i]) == True:
            return True
        if rec(i+1,sum) == True:
            return True
        
        return False

    return rec(0,0)


arr = [1,2]
k=0
print(checksubsequencesumK(arr,k))
