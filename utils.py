def limpiar_terminal():
    print(chr(27) + "[2J")
def validar_celda(celda, max_col, max_row):
    columnas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    columnas = list(columnas)
    limit = columnas.index(max_col)+1
    columnas_max = columnas[:limit]
    if celda[0] in columnas_max and int(celda[1]) <= max_row:
        verif = True
    else:
        verif = False
    return verif
# Para comprobar si una celda "B5" está dentro es una posición válida del tablero que comprende entre A1 y (max_col, max_row)
def comprobar_celda_disponible(celda, equipo):
    if celda not in equipo:
        return True
    else:
        return False
# Para comprobar si un miembro del equipo ya ocupa una celda dada
def validar_celda_contigua(celda1, celda2) :
    celda1.upper()
    celda2.upper()
    columnas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    columnas = list(columnas)
    if celda1[0] == celda2[0]:
        if int(celda2[1]) == int(celda1[1]) + 1 or int(celda2[1]) == int(celda1[1]) - 1 :
            return True
        else:
            return False
    if celda1[1] == celda2[1]:
        if columnas.index(celda2[0]) == columnas.index(celda1[0]) + 1 or columnas.index(celda2[0]) == columnas.index(celda1[0]) - 1:
            return True
        else:
            return False
# Para comprobar si la celda 1 es contigua a la celda 2