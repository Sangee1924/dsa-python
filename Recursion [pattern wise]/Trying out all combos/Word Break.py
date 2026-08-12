def rec(ind,s,wordsdict):
    if ind==len(s):
        return True
    
    for i in range(ind,len(s)):
        word=s[ind:i+1]

        if word in wordsdict:
            if rec(i+1,s,wordsdict):
                return True

    return False

def wordbreak(s,words):
    wordsdict=set(words)

    return rec(0,s,wordsdict)

def main():
    s = "catsandog"
    words = ["cat", "cats", "and", "sand", "dog"]
    print(wordbreak(s,words))


main()