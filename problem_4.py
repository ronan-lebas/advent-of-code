def check(i, j, board):
    c = 0
    if j + 3 < len(board[0]):
        if board[i][j] == 'X' and board[i][j+1] == 'M' and board[i][j+2] == 'A' and board[i][j+3] == 'S':
            c += 1
    if i + 3 < len(board):
        if board[i][j] == 'X' and board[i+1][j] == 'M' and board[i+2][j] == 'A' and board[i+3][j] == 'S':
            c += 1
    if i + 3 < len(board) and j + 3 < len(board[0]):
        if board[i][j] == 'X' and board[i+1][j+1] == 'M' and board[i+2][j+2] == 'A' and board[i+3][j+3] == 'S':
            c += 1
    if i - 3 >= 0:
        if board[i][j] == 'X' and board[i-1][j] == 'M' and board[i-2][j] == 'A' and board[i-3][j] == 'S':
            c += 1
    if j - 3 >= 0:
        if board[i][j] == 'X' and board[i][j-1] == 'M' and board[i][j-2] == 'A' and board[i][j-3] == 'S':
            c += 1
    if i - 3 >= 0 and j - 3 >= 0:
        if board[i][j] == 'X' and board[i-1][j-1] == 'M' and board[i-2][j-2] == 'A' and board[i-3][j-3] == 'S':
            c += 1
    if i - 3 >= 0 and j + 3 < len(board[0]):
        if board[i][j] == 'X' and board[i-1][j+1] == 'M' and board[i-2][j+2] == 'A' and board[i-3][j+3] == 'S':
            c += 1
    if i + 3 < len(board) and j - 3 >= 0:
        if board[i][j] == 'X' and board[i+1][j-1] == 'M' and board[i+2][j-2] == 'A' and board[i+3][j-3] == 'S':
            c += 1
    return c

def check2(i, j, board):
    c = 0
    if board[i][j] == 'A' and set([board[i-1][j-1], board[i][j], board[i+1][j+1]]) == set(['M', 'A', 'S']) and set([board[i+1][j-1], board[i][j], board[i-1][j+1]]) == set(['M', 'A', 'S']):
        c += 1
    return c

def solve1(path):
    board = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            board.append([x for x in line.strip()])
    return sum([check(i, j, board) for i in range(len(board)) for j in range(len(board[0]))])


def solve2(path):
    board = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            board.append([x for x in line.strip()])
    return sum([check2(i, j, board) for i in range(1, len(board)-1) for j in range(1, len(board[0])-1)])

if __name__ == '__main__':
    print(solve1('input_4.txt'))
    print(solve2('input_4.txt'))