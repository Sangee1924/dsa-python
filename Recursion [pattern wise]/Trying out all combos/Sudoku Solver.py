def canplace(k,row,col,board):
    for i in range(9):
        if board[row][i]==k:
            return False
        if board[i][col]==k:
            return False
        if board[3*(row//3)+i//3][3*(col//3)+i%3]==k:
            return False

    return True

def sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==".":
                for k in range(1,10):
                    if canplace(str(k),i,j,board):
                        board[i][j]=str(k)
                        if sudoku(board):
                            return True
                        board[i][j]="."
                return False

    return True

def main():
    board = [
        ['9', '5', '7', '.', '1', '3', '.', '8', '4'],
        ['4', '8', '3', '.', '5', '7', '1', '.', '6'],
        ['.', '1', '2', '.', '4', '9', '5', '3', '7'],
        ['1', '7', '.', '3', '.', '4', '9', '.', '2'],
        ['5', '.', '4', '9', '7', '.', '3', '6', '.'],
        ['3', '.', '9', '5', '.', '8', '7', '.', '1'],
        ['8', '4', '5', '7', '9', '.', '6', '1', '3'],
        ['.', '9', '1', '.', '3', '6', '.', '7', '5'],
        ['7', '.', '6', '1', '8', '5', '4', '.', '9']
    ]

    sudoku(board)
    for row in board:
        print(row)


main()