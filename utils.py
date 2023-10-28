
def limpiar_terminal():
    print(chr(27) + "[2J")
def validar_celda(celda, max_col, max_row):
    if len(celda) > 2:
        return  False
    columnas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    columnas = list(columnas)
    limit = columnas.index(max_col)+1
    columnas_max = columnas[:limit]
    if celda[0] in columnas_max and 0 < int(celda[1]) <= max_row:
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
def area_2x2(objetivo): #para artillero e inteligencia
    colum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    colum = list(colum)
    derecha = objetivo[0] + str(int(objetivo[1]) + 1)
    abajo = colum[colum.index(objetivo[0]) + 1] + objetivo[1]
    esquina = colum[colum.index(objetivo[0]) + 1] + str(int(objetivo[1]) + 1)
    if validar_celda(esquina, columnas(), filas()):
        area = [objetivo, derecha, abajo, esquina]
    elif validar_celda(derecha, columnas(), filas()) and not validar_celda(abajo, columnas(), filas()):
        area = [objetivo, derecha]
    elif not validar_celda(derecha, columnas(), filas()) and validar_celda(abajo, columnas(), filas()):
        area = [objetivo, abajo]
    else:
        area = [objetivo]
    return area
def columnas(): #esto es para si hay que cambiar la cantidad de filas o columnas sea mas facil
    col = 'D'
    return col
def filas():
    fil = 4
    return fil

'''

Ok en esta si te puse un par de cambios que yo haria personalemente:

La función validar_celda:

Podrias simplificarla usando directamente la longitud de la cadena para verificar la longitud de la celda: 
if len(celda) != 2:.
En lugar de crear una variable verif, puede devolver el resultado directamente: 
return celda[0] in columnas_max and 0 < int(celda[1]) <= max_row.

para esta

def comprobar_celda_disponible(celda, equipo):
    if celda not in equipo:
        return True
    else:
        return False
 Podría simplificarse eliminando el uso de if y directamente devolviendo la expresión booleana: 
 return celda not in equipo.
 
La función area_2x2 creo entender que calcula 2x2 alrededor de un objetivo.
Podrias hacerla mas clara y simplificarla En lugar de realizar múltiples comprobaciones, podrias hacerlo de manera mas concisa para hacer area mas eficiente.
Puede usar un bucle para generar las celdas en lugar de escribirlas explícitamente. Esto haría que la función sea más escalable si se necesita un área más grande en el futuro (no se si lo necesitarias pero bueno, again buena practica).

para columnas y filas
Lo que hiciste esta bien para el futuro, lo que pasa es que en general si puedes evitar usar constantes mejor, si estas 100% seguro que no las vas a cambiar evitalas, si no la constante esta bien.

En general buen trabajo amigo, solo falta pulir un poco pero todo bastante bien.
'''