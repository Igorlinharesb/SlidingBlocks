from math import sqrt

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

def imprimeQuadro (board, dim):
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


def nodeCanMove(board, blank, move):

    if move == 8 and blank["x"] > 1:
        return True

    elif move == 6 and blank["y"] < int(sqrt(len(board))):
        return True

    elif move == 2 and blank["x"] < int(sqrt(len(board))):
        return True

    elif move == 4 and blank["y"] > 1:
        return True

    else:
        print("Movimento inválido.")
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

