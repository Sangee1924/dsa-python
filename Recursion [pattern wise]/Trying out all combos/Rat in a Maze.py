def rat(row,col,n,grid,visited,temp,ans):
    if row==n-1 and col==n-1:
        ans.append(temp)
        return

    visited[row][col]=True

    if row<n-1 and not visited[row+1][col] and grid[row+1][col]==1:
        rat(row+1,col,n,grid,visited,temp+"D",ans)

    if col>0 and not visited[row][col-1] and grid[row][col-1]==1:
        rat(row,col-1,n,grid,visited,temp+"L",ans)

    if col<n-1 and not visited[row][col+1] and grid[row][col+1]==1:
            rat(row,col+1,n,grid,visited,temp+"R",ans)

    if row>0 and not visited[row-1][col] and grid[row-1][col]==1:
            rat(row-1,col,n,grid,visited,temp+"U",ans)

    visited[row][col]=False

    return ans

def main():
    n = 4
    grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
    visited = [[False] * n for _ in range(n)]

    if grid[0][0]==1:
         ans = rat(0,0,n,grid,visited,"",[])
    print(ans)


main()