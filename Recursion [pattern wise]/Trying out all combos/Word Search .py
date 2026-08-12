def exist(board,word):
    row = len(board)
    col = len(board[0])

    def rec(i,j,ind):
        if ind==len(word):
            return True

        if i<0 or i>=row or j<0 or j>=col or board[i][j] != word[ind]:
            return False

        temp = board[i][j]
        board[i][j]="#"

        found = (rec(i,j+1,ind+1) or rec(i,j-1,ind+1) or rec(i+1,j,ind+1) or rec(i-1,j,ind+1))

        board[i][j]=temp

        return found

    for i in range(row):
        for j in range(col):
            if rec(i,j,0):
                return True

    return False

board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
print(exist(board, "ABCCED"))
print(exist(board, "SEE"))
print(exist(board, "ABCB"))