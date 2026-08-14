def powerSet(userInput):
    N = len(userInput)
    ans=[]
    for i in range(2**N):
        S=""
        for j in range(N):
            if i & (1<<j):
                S+=userInput[j]
        ans.append(S)

    return ans


UserInput = input("Enter User Input : ")
print(powerSet(UserInput))