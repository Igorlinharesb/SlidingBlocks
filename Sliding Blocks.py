from random import randint

def createBoard(dim):
    board = []
    for i in range(dim ** 2):
        x = int(i / dim + 1)
        y = i % dim + 1
        if i != dim ** 2 - 1:
            pos = i + 1
        else:
            pos = 0
        newnode = {'x': x, 'y': y, 'pos': pos, 'val': pos}
        board.append(newnode)
    return board

def printBoard(board, dim):
    print("---"*dim, " BOARD ", "---"*dim, "\n")
    for node in board:
        if node["val"] == 0:
            print('[', f'{"":^5}', '] ', end='')
        else:
            print('[', f'{node["val"]:^5}', '] ', end='')
        if node["pos"] % dim == 0:
            print()

    print("\n", "----"*2*dim)


def findBlankNode(board):
    for node in board:
        if node["val"] == 0:
            blanknode = node
    return blanknode


def nodeCanMove(blank, move, size):

    if move == 8 and blank["x"] > 1:
        return True

    elif move == 6 and blank["y"] < size:
        return True

    elif move == 2 and blank["x"] < size:
        return True

    elif move == 4 and blank["y"] > 1:
        return True

    else:
        return False


def moveNode (board, blank, dim, move):

    if move == 8:
        board[blank["pos"] - 1]["val"] = board[blank["pos"] - 1 - dim]["val"]
        board[blank["pos"] - 1 - dim]["val"] = 0
        print()

    elif move == 6:
        board[blank["pos"] - 1]["val"] = board[blank["pos"]]["val"]
        board[blank["pos"]]["val"] = 0
        print()

    elif move == 2:
        board[blank["pos"] - 1]["val"] = board[blank["pos"] - 1 + dim]["val"]
        board[blank["pos"] - 1 + dim]["val"] = 0
        print()
    elif move == 4:
        board[blank["pos"] - 1]["val"] = board[blank["pos"] - 2]["val"]
        board[blank["pos"] - 2]["val"] = 0
        print()

    return board


def misplacedNodes(board):
    mispnodes = 0

    for node in board:
        if node["pos"] != node["val"]:
            mispnodes = mispnodes + 1

    return mispnodes


# Gerando o quadro inicial
while True:
    try:
        size = int(input('Enter a value n to create a nxn board: '))
        if size > 0:
            break
        else:
            print("Error: The dimmension must be a positive integer.")
            continue
    except:
        print("Please, enter with a valid value.")
        continue
    else:
        break
gameboard = createBoard(size)

# Embaralhando o tabuleiro

nummoves = randint(50,100)
count = 0

while count <= nummoves:
    blank = findBlankNode(gameboard)
    moves = [8, 6, 2, 4]
    op = randint(0, 3)
    choice = moves[op]
    if nodeCanMove(blank, choice, size):
        gameboard = moveNode(gameboard, blank, size, choice)
        count += 1

attempts = 0
while misplacedNodes(gameboard) != 0:
    print("Attempts: ", attempts)
    printBoard(gameboard, size)
    blank = findBlankNode(gameboard)
    print("Move the blank position.")
    print("8 - Up | 2 - Down | 6 - Right | 4 - Left")
    try:
        choice = int(input("Choose a move to the blank node: "))
    except:
        print("\n\n\n\n\n")
        continue
    if nodeCanMove(blank, choice, size):
        gameboard = moveNode(gameboard, blank, size, choice)
        attempts += 1
    else:
        print("\n\n\n\n\n MOVE NOT ALLOWED!!!! ")

print('CONGRATSSS! YOU DID IT.')