from random import randint


def create_board(dim):
    """
    Function that generates the game board.
    :param dim: the board's width
    :return: the board itself
    """

    board = []  # Initializing the board

    for i in range(dim ** 2):  # This loop will fill the board w/ the values
        x = int(i / dim + 1)  # component x of the board
        y = i % dim + 1  # component y of the board
        if i != dim ** 2 - 1:  # conditional that select the values
            pos = i + 1        # of the position and the initial
        else:                  # value of each node
            pos = 0
        # The values are stored in a dict w/ 4 keys
        newnode = {'x': x, 'y': y, 'pos': pos, 'val': pos}
        # Each dict is stored in the list 'board'
        board.append(newnode)
    return board


def print_board(board, dim):
    """
    This function will print a board on the prompt

    :param board: a given board
    :param dim: the board's width
    """
    print("---"*dim, " BOARD ", "---"*dim, "\n")
    for node in board:  # print the board
        if node["val"] == 0:  # print the blank node
            print('[', f'{"":^5}', '] ', end='')
        else:  # print the other nodes
            print('[', f'{node["val"]:^5}', '] ', end='')
        if node["pos"] % dim == 0:  # break the line
            print()

    print("\n", "----"*2*dim)


def find_blank(board):
    """
    Function that returns the blank of the board
    :param board: a given board
    :return blanknode: A dict containing the data of the blank node
    """

    for node in board:  # Look for the node w/ value 0
        if node["val"] == 0:
            blanknode = node
    return blanknode


def node_can_move(blank, move, size):
    """
    Function that evaluates if a given move is allowed
    Moves:
    8 - Move the node up
    2 - Move the node down
    6 - Move the node to the right
    4 - Move the node to the left

    :param blank: the blank node from the board
    :param move: the sort of move to be done
    :param size: the board's width
    :return: True or False
    """

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


def move_node(board, blank, dim, move):
    """
    Function that moves the blank node
    :param board: a given board
    :param blank: the blank node data
    :param dim: the board's width
    :param move: sort of move desired
    :return: the board after the move
    """

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


def misplaced_nodes(board):
    """
    Function that count how many nodes are not at the place they were supposed
    to be.
    :param board: a given board
    :return: the amount of misplaced nodes
    """
    mispnodes = 0

    for node in board:
        if node["pos"] != node["val"]:
            mispnodes = mispnodes + 1

    return mispnodes


while True:  # Catching the entries from the user
    try:  # Verifying if the user entered with a valid value
        size = int(input('Enter w/ a value n to create a nxn board: '))
        if size > 0:
            break
        else:
            print("Error: The dimension must be a positive integer.")
            continue
    except:
        print("Please, enter with a valid value.")
        continue
    else:
        break

# Generating the board's game
gameboard = create_board(size)

# Generating a random value between 50 and 100 to mix the board
nummoves = randint(50, 100)
count = 0

# Mixing the board
while count <= nummoves:
    blank = find_blank(gameboard)
    moves = [8, 6, 2, 4]
    op = randint(0, 3)
    choice = moves[op]
    if node_can_move(blank, choice, size):
        gameboard = move_node(gameboard, blank, size, choice)
        count += 1

attempts = 0

# Loop that runs until the board isn't solved
while misplaced_nodes(gameboard) != 0:
    print("Attempts: ", attempts)
    print_board(gameboard, size)
    blank = find_blank(gameboard)
    print("Move the blank position.")
    print("8 - Up | 2 - Down | 6 - Right | 4 - Left")
    try:
        choice = int(input("Choose a move to the blank node: "))
    except:
        print("\n\n\n\n\n")
        continue
    if node_can_move(blank, choice, size):
        gameboard = move_node(gameboard, blank, size, choice)
        attempts += 1
    else:
        print("\n\n\n\n\n MOVE NOT ALLOWED!!!! ")

# Spoiling the user haha...
print('CONGRATSSS! YOU DID IT.')