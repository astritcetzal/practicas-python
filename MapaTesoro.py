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

def esconder_secretos():
    tesoro = randrange(1,10)
    trampa = randrange(1,10)
    while trampa == tesoro:
        trampa= randrange(1,10)
    return (tesoro,trampa)

def ingresar_movimientos(tablero):
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
        sign = tablero[fila][columna]
        ok = sign not in ['O']
        if not ok:
            print("¡Cuadro ocupado, ingresa de nuevo otro numero")
            continue
    return movimiento

def actualizar_tablero(tablero, movimiento, secretos):
    if (movimiento + 1) == secretos[0]:
        return"¡Has ganado!"
    elif (movimiento + 1) == secretos[1]:
        return "¡Caiste en la trampa!"
    else:
        who = 'O'
        movimiento = int(movimiento)
        fila = movimiento//3
        columna = movimiento % 3
        tablero[fila][columna] = who

        return "Continua"
        
    
    
tablero= [[3 * j + i + 1 for i in range(3)] for j in range(3)]
display_board(tablero)
secretos = esconder_secretos()

intentos = 3
while intentos > 0:
    intentos-=1;
    
    jugada = ingresar_movimientos(tablero)
    
    resultado = actualizar_tablero(tablero, jugada, secretos)
    display_board(tablero)
    if resultado  == "¡Has ganado!":
        print("¡Has ganado, el juego ha terminado!", "El tesoro está en: ", secretos[0])
        break
    elif resultado == "¡Caiste en la trampa!":
        print("¡Has perdido!", resultado)  
        break
    else:
        if intentos ==0:
            print("¡Has perdido!", "¡Tus 3 intentos se han agotado")
        else:
            print("¡Continua!")

     

