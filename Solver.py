



grid = [
    [0, 6, 0, 0, 8, 0, 0, 3, 0],
    [1, 0, 0, 6, 0, 5, 0, 0, 7],
    [0, 0, 5, 0, 0, 0, 2, 0, 0],
    [0, 9, 0, 3, 0, 7, 0, 1, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 1, 0, 4, 0, 6, 0, 8, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [8, 0, 0, 9, 0, 1, 0, 0, 5],
    [0, 5, 0, 0, 4, 0, 0, 7, 0]
]
def prettyprint(a):
    for i in range(9):
        for j in range(9):
            print(a[i][j], end=" ")
        print()


def checkNum(row, col, num):
    for y in range(9):
        if grid[row][y] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solve(row, col):

    if (row == 8 and col == 9):
        return True

    if col == 9:
        row += 1
        col = 0

    if grid[row][col] != 0:
        return solve(row, col + 1)

    for num in range(1, 10):
        if checkNum(row, col, num):
            grid[row][col] = num
            if solve(row, col + 1):
                return True
        grid[row][col] = 0
    return False
    
solve(0, 0)
prettyprint(grid)
