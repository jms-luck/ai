def is_valid(board, r, c, n):
    if n in board[r]:
        return False
    if n in [board[i][c] for i in range(4)]:
        return False
    start_row, start_col = (r // 2) * 2, (c // 2) * 2
    for i in range(2):
        for j in range(2):
            if board[start_row + i][start_col + j] == n:
                return False
    return True

def solve(board):
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                for n in range(1, 5):
                    if is_valid(board, r, c, n):
                        board[r][c] = n
                        if solve(board):
                            return True
                        board[r][c] = 0
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

board = [
    [1, 0, 0, 0],
    [0, 0, 3, 0],
    [0, 2, 0, 0],
    [0, 0, 0, 4]
]

if solve(board):
    print_board(board)
else:
    print("No solution")
