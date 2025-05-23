
N = 8

def printSolution(board):
    for row in board:
        for i in range(N):
            print("Q" if row[i] else ".", end=" ")
        print()
    print()  


def isSafe(board, row, col):
    
    for i in range(row):
        if board[i][col]:
            return False

    
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j]:
            return False

    return True


def solve(board, row):
    if row == N:
        print("One possible solution is:")
        printSolution(board)
        return True  

    for col in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1  
            if solve(board, row + 1):  
                return True  
            board[row][col] = 0  

    return False


def eightQueens():
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve(board, 0):
        print("Solution does not exist")
        
eightQueens()
