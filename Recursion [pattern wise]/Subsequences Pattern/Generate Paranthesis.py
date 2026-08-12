def GenerateParanthesis(n):
    ans=[]

    def paranthesis(s,open,close):
        if len(s) == 2*n:
            ans.append(s)
            return

        if open < n:
            paranthesis(s + "(", open+1, close)

        if close < open:
            paranthesis(s + ")", open, close+1)

    paranthesis("",0,0)

    return ans


n = int(input("Enter no of pairs of parentheses : "))
print(GenerateParanthesis(n))