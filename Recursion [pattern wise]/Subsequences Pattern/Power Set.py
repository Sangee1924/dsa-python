def powerset(s):
    ans=[]

    def rec(i,cur):
        if i == len(s):
            if cur:
                ans.append(cur)
            return

        rec(i+1,cur+s[i])

        rec(i+1,cur)

    rec(0,"")
    return ans


s = input("Enter user Input : ")
print(powerset(s))