def LetterCombination(digits,letter):
    ans=[]
    if not digits:
        return ans

    def rec(ind,ds):
        if ind==len(digits):
            ans.append(ds)
            return

        s = letter[digits[ind]]

        for char in s:
            rec(ind+1,ds+char)
        return

    rec(0,"")

    return ans

digits = "34"
letter = {'0':"",'1':"", '2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}

print(LetterCombination(digits,letter))