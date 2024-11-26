def solve_n_queens(n, board=[], solutions=[]):
    if len(board) == n: 
        solutions.append(board)
        return
    for col in range(n):
        valid = True
        for r, c in enumerate(board):
            if col == c or abs(len(board) - r) == abs(col - c):
                valid = False
                break
        if valid:
            solve_n_queens(n, board + [col], solutions)
    return solutions

n = int(input("Enter N: "))
for sol in solve_n_queens(n):
    for row in sol:
        for i in range(n):
            print("1" if i == row else "0", end=" ")
        print()
    print()
