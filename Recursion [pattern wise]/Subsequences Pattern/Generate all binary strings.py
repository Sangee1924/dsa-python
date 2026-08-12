def generateAllbinary(n):
    ans=[]

    def binary(s):
        if len(s) == n:
            ans.append(s)
            return
        binary(s + "0")

        if not s or s[-1] == "0":
            binary(s + "1")

    binary("") 

    return ans

n = int(input("Enter an number : "))
print(generateAllbinary(n))