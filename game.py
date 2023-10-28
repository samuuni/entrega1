from utils import limpiar_terminal
from jugador import Jugador

def main():
    limpiar_terminal()
    print('Bienvenidos a Tactical Battle. A jugar!\n')
    input('Turno del Jugador 1. Pulsa intro para comenzar')
    j1 = Jugador()
    input('Jugador 1, pulsa terminar tu turno')
    limpiar_terminal()
    input('Turno del Jugador 2. Pulsa intro para comenzar')
    j2 = Jugador()
    input('Jugador 2, pulsa terminar tu turno')

    limpiar_terminal()
    j1.set_oponente(j2)
    j2.set_oponente(j1)
    final = False
    while not final:
        input('Turno del Jugador 1. Pulsa intro para comenzar')
        final = j1.turno()
        if final:
            print('***** El jugador 1 ha ganado la partida! *****\n'
                  '__          _______ _   _ \n'
                  '\ \        / /_   _| \ | |\n'
                  ' \ \  /\  / /  | | |  \| |\n'
                  '  \ \/  \/ /   | | | . ` |\n'
                  '   \  /\  /   _| |_| |\  |\n'
                  '    \/  \/   |_____|_| \_|\n'
                  )
            return 0
        input('Jugador 1, pulsa intro para terminar tu turno')
        limpiar_terminal()
        input('Turno del Jugador 2. Pulsa intro para comenzar')
        final = j2.turno()
        if final:
            print('***** El jugador 2 ha ganado la partida! *****\n'
                  '__          _______ _   _ \n'
                  '\ \        / /_   _| \ | |\n'
                  ' \ \  /\  / /  | | |  \| |\n'
                  '  \ \/  \/ /   | | | . ` |\n'
                  '   \  /\  /   _| |_| |\  |\n'
                  '    \/  \/   |_____|_| \_|\n'
                  )
            return 0
        input('Jugador 2, pulsa intro para terminar tu turno')
        limpiar_terminal()

if __name__ == '__main__':
    main()
    

'''
Te puse aqui abajo los cambios que haria para esta, en general tu codigo esta bien
los cambios que puse son para hacerlo mas lisible el feedback en general (por cierto me dio paja poner el ASCII ponlo tu xD):

División en funciones: El código original que hiciste estaba todo en main(), lo que hacía que fuera un poco difícil de entender debido a su longitud. Dividí el código en dos funciones: configurar_juego() y jugar_partida(). Esto hace que el código sea más modular y fácil de entender.

Nombres descriptivos: Cambié Los nombres de las variables para que sean más descriptivos. Por ejemplo, j1 y j2 te los cambié a jugador1 y jugador2. IDEM que antes, es para hacerlo mas lisible.

Comentarios: Te puse un par de comentarios descriptivos para explicar qué hace cada función.

Eliminación de líneas innecesarias: Te borré algunas líneas en blanco innecesarias para mantener un formato más limpio y siguiendo las convenciones de estilo de Python (PEP 8)(te recomiendo que te leas esa documentacion (https://peps.python.org/pep-0008/) si no los has hecho ya esta piola).

Robustez del programa: No agregé un manejo completo de errores, pero te digo que es importante que consideres un manejo de errores para abordar situaciones inesperadas que puedan ocurrir durante la ejecución del programa.

Osea que en conclusion, intenta hacerlo mas Modular (con mas funciones) y haz variables con nombres mas descriptivos te entendi pero en general es mejor poner los nobmres como tal, pusiste un par de lineas en blanco useless y lo del manejo de error, si no por el resto joya.


'''
    
'''
from utils import limpiar_terminal
from jugador import Jugador

def configurar_juego():
    limpiar_terminal()
    print('Bienvenidos a Tactical Battle. A jugar!\n')

def jugar_partida():
    jugador1 = Jugador()
    jugador2 = Jugador()
    jugador1.set_oponente(jugador2)
    jugador2.set_oponente(jugador1)
    final = False

    while not final:
        input('Turno del Jugador 1. Pulsa intro para comenzar')
        final = jugador1.turno()
        if final:
            print('***** El jugador 1 ha ganado la partida! *****')
            return 0
        input('Jugador 1, pulsa intro para terminar tu turno')
        limpiar_terminal()

        input('Turno del Jugador 2. Pulsa intro para comenzar')
        final = jugador2.turno()
        if final:
            print('***** El jugador 2 ha ganado la partida! *****')
            return 0
        input('Jugador 2, pulsa intro para terminar tu turno')
        limpiar_terminal()

if __name__ == '__main':
    configurar_juego()
    jugar_partida()
'''
