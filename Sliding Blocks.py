from random import randint

def criaQuadro(dim):
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

def imprimeQuadro(board, dim):
    print("---------------- QUADRO ----------------\n")
    for node in board:
        if node["val"] == 0:
            print('[', f'{"":^5}', '] ', end='')
        else:
            print('[', f'{node["val"]:^5}', '] ', end='')
        if node["pos"] % dim == 0:
            print()

    print("\n----------------------------------------")


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


def nosDeslocados(board):
    mispnodes = 0

    for node in board:
        if node["pos"] != node["val"]:
            mispnodes = mispnodes + 1

    return mispnodes


# Gerando o quadro inicial
while True:
    try:
        size = int(input('Digite o valor de n para o tabuleiro nxn ser gerado: '))
        if size > 0:
            break
        else:
            print("Erro: A dimensão do tabuleiro não pode ser nula ou negativa.")
            continue
    except:
        print("Por favor, um valor válido.")
        continue
    else:
        break
quadro = criaQuadro(size)

# Embaralhando o tabuleiro

nummoves = randint(50,100)
count = 0

while count <= nummoves:
    blank = findBlankNode(quadro)
    moves = [8, 6, 2, 4]
    op = randint(0,3)
    choice = moves [op]
    if nodeCanMove(blank, choice, size):
        quadro = moveNode(quadro, blank, size, moves[op])
        count +=1

imprimeQuadro(quadro, size)