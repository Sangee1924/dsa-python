def issafe(row,col,board):
    temprow=row
    tempcol=col

    while(tempcol>=0):
        if board[temprow][tempcol]=="Q":
            return False
        tempcol-=1

    temprow=row
    tempcol=col
    while(temprow>=0 and tempcol>=0):
        if board[temprow][tempcol]=="Q":
            return False
        temprow-=1
        tempcol-=1

    temprow=row
    tempcol=col
    while(temprow<len(board) and tempcol>=0):
        if board[temprow][tempcol]=="Q":
            return False
        temprow+=1
        tempcol-=1

    return True


def solve(col,ans,board):
    if col==n:
        temp=[''.join(row) for row in board]
        ans.append(temp)
        return
    for row in range(n):
        if issafe(row,col,board):
            board[row][col]="Q"
            solve(col+1,ans,board)
            board[row][col]="."


def NQueen(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    ans=[]
    solve(0,ans,board)

    return ans


n = int(input("enter User input: "))
print(NQueen(n))
