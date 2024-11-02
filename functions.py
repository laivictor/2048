from random import randint

def start(): # creates a 4x4 board with 2 random 2s
    board = []
    for i in range(4):
        board.append([0]*4)
    spawn(board)
    spawn(board)
    return board

def spawn(board): # spawns a 2 in a random empty cell
    x, y = randint(0,3), randint(0,3)
    while board[x][y] != 0:
        x, y = randint(0,3), randint(0,3)
    board[x][y] = 2

def status(board): # 1: win, 0: continue, -1: lose
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                return 1
            elif board[i][j] == 0:
                return 0
    return -1

def move(board, x): # checks and moves
    match x:
        case 'w':
            for j in range(4):
                temp = vertical(board, j)
                for i in range(4-len(temp)):
                    temp.append(0)
                for i in range(4):
                    board[i][j] = temp[i]
        case 's':
            for j in range(4):
                temp = vertical(board, j)
                for i in range(4-len(temp)):
                    temp.insert(0, 0)
                for i in range(4):
                    board[i][j] = temp[i]
        case 'a':
            for i in range(4):
                temp = horizontal(board, i)
                for j in range(4-len(temp)):
                    temp.append(0)
                for j in range(4):
                    board[i][j] = temp[j]
        case 'd':
            for i in range(4):
                temp = horizontal(board, i)
                for j in range(4-len(temp)):
                    temp.insert(0, 0)
                for j in range(4):
                    board[i][j] = temp[j]

def horizontal(board, i): # merges elements in a specific row
    temp = []
    for j in range(4):
        if board[i][j] != 0:
            temp.append(board[i][j])
    for j in range(len(temp)-1):
        if temp[j] == temp[j+1]:
            temp[j] *= 2
            temp[j+1] = 0
    temp = [j for j in temp if j != 0]
    return temp

def vertical(board, j): # merges elements in a specific column
    temp = []
    for i in range(4):
        if board[i][j] != 0:
            temp.append(board[i][j])
    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            temp[i] *= 2
            temp[i+1] = 0
    temp = [i for i in temp if i != 0]
    return temp

def show(board): # displays board
    for r in board:
        print(r)