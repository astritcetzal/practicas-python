from random import randrange

def display_board(board):
    print ("+-------" * 3, "+", sep="")
    for fila in range(3):
        print ("|       " * 3, "|", sep = "")
        for columna in range(3):
            print("|    " + str(board[fila][columna]) + "  ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    ok = False
    while not ok:
        movimiento = input("Ingresa un movimiento: ")
        ok = len(movimiento) == 1 and movimiento >= '1' and movimiento <='9'
        if not ok: 
            print("Movimiento erroneo, ingrésalo nuevamente")
            continue
        movimiento = int(movimiento) - 1
        fila = movimiento//3
        columna = movimiento % 3
        sign = board[fila][columna]
        ok = sign not in ['O', 'X']
        if not ok:
            print("¡Cuadro ocupado, ingresa de nuevo otro numero")
            continue
    board[fila][columna] = 'O'

def make_list_of_free_fields(board):
    free = [] 
    for fila in range(3):
        for columna in range(3):
            if board[fila][columna] not in ['O','X']:
                free.append((fila, columna))
    return free


def victory_for(board, sgn):
    if sgn == "X":
        who = 'me'
    elif sgn == "O":
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] !=sgn:
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def draw_move(board):
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        fila, columna = free[this]
        board[fila][columna] = 'X'


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1]= 'X'
free = make_list_of_free_fields(board)
human_turn = True
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn 
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("¡Has ganado!")
elif victor == 'me':
    print("¡He ganado!")
else:
    print("¡Empate!")





