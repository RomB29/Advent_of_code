import sys

def calculatePath(board, start, end, mo=0):
    h = len(board)
    w = len(board[0])

    timeMap = [[-1 for _ in range(w)] for _ in range(h)]

    timeMap[start[0]][start[1]] = 0
    
    for m in range(sys.maxsize):
        if timeMap[end[0]][end[1]] != -1:
            break
        newBoard = createBoardAfterMove(board, mo + m + 1)
        update = []

        for i in range(h):
            for j in range(w):
                if timeMap[i][j] == m:
                    for di, dj in directions:
                        if (i + di < h and j + dj < w) and (newBoard[i + di][j + dj] == '.'):
                            update.append([i + di, j + dj])

        for i, j in update:
            timeMap[i][j] = m + 1

    return timeMap[end[0]][end[1]]

def createBoardAfterMove(board, m):
    h = len(board)
    w = len(board[0])
    
    newBoard = [[None for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            newBoard[i][j] = '#' if board[i][j] == '#' else '.'

    for i in range(h):
        for j in range(w):
            if board[i][j] == '>':
                newBoard[i][(j - 1 + m) % (w - 2) + 1] = '>'
            if board[i][j] == '<':
                newBoard[i][((j - 1 - m) % (w - 2) + (w - 2)) % (w - 2) + 1] = '<'
            if board[i][j] == 'v':
                newBoard[(i - 1 + m) % (h - 2) + 1][j] = 'v'
            if board[i][j] == '^':
                newBoard[((i - 1 - m) % (h - 2) + (h - 2)) % (h - 2) + 1][j] = '^'

    return newBoard

# read input
with open('24.in', 'r') as f:
    input = f.read().split('\n')

board = [row.replace('\r', '') for row in input]

s = [0, 1]
d = [len(board) - 1, len(board[0]) - 2]

directions = [[0, 0], [-1, 0], [+1, 0], [0, -1], [0, +1]]

print(calculatePath(board, s, d))

m1 = calculatePath(board, s, d, 0)
m2 = calculatePath(board, d, s, m1)
m3 = calculatePath(board, s, d, m1 + m2)
print(m1 + m2 + m3)