N = 8

board = [[0 for i in range(N)] for i in range(N)]


def is_safe(row, col):
    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False


def main():
    # Place first queen at position (0, 0)
    board[0][0] = 2

    if solve(1):
        print("8 Queens Solution:")
        for row in board:
            print(row)
    else:
        print("No solution exists")


if __name__ == "__main__":
    main()