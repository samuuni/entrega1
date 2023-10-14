from utils import validar_celda,validar_celda_contigua

class Jugador:
    def crear_equipo(self):
        print('vamos a posicionar a nuestors personajes en el tablero!')
        equipo = []

        while True:
            try:
                Medico = Medicos()
                pos_medico = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Medico: ')
                pos_medico = pos_medico.upper()
                if validar_celda(pos_medico, 'D', 4):
                    Medico.set_posicion(pos_medico)
                    equipo.append(Medico)
                else:
                    raise CasillaInvalidaError
                break

            except CasillaInvalidaError:
                print('Ups... valor de celda incorrecto.')
            except:
                print('Ups... valor de celda incorrecto.')

        while True:
            try:
                Artillero = Artilleros()
                pos_artillero = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Artillero: ')
                pos_artillero = pos_artillero.upper()
                if validar_celda(pos_artillero, 'D', 4):
                    Artillero.set_posicion(pos_artillero)
                    equipo.append(Artillero)
                else:
                    raise CasillaInvalidaError
                if pos_artillero == pos_medico:
                    raise CasillaOcupadaError
                break
            except CasillaOcupadaError:
                print('Ups... la celda seleccionada esta ya ocupada')
            except CasillaInvalidaError:
                print('Ups... valor de celda incorrecto.')
            except:
                print('Ups... valor de celda incorrecto.')
        while True:
            try:
                Francotirador = Francotiradores()
                pos_francotirador = input(
                    'Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Francotirador: ')
                pos_francotirador = pos_francotirador.upper()
                if validar_celda(pos_francotirador, 'D', 4):
                    Francotirador.set_posicion(pos_francotirador)
                    equipo.append(Francotirador)
                else:
                    raise CasillaInvalidaError
                if pos_francotirador == pos_medico or pos_francotirador == pos_artillero:
                    raise CasillaOcupadaError
                break
            except CasillaOcupadaError:
                print('Ups... la celda seleccionada esta ya ocupada')
            except CasillaInvalidaError:
                print('Ups... valor de celda incorrecto.')
            except:
                print('Ups... valor de celda incorrecto.')
        while True:
            try:
                Inteligencia = Inteligencias()
                pos_inteligencia = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Inteligencia: ')
                pos_inteligencia = pos_inteligencia.upper()
                if validar_celda(pos_inteligencia, 'D', 4):
                    Inteligencia.set_posicion(pos_inteligencia)
                    equipo.append(Inteligencia)
                else:
                    raise CasillaInvalidaError
                if pos_inteligencia == pos_medico or pos_inteligencia == pos_artillero or pos_inteligencia == pos_francotirador:
                    raise CasillaOcupadaError
                break
            except CasillaOcupadaError:
                print('Ups... la celda seleccionada esta ya ocupada')
            except CasillaInvalidaError:
                print('Ups... valor de celda incorrecto.')
            except:
                print('Ups... valor de celda incorrecto.')
        return equipo
    def __init__(self):
        self.oponente = str()
        self.equipo = self.crear_equipo()
        self.informe = str()
    def set_oponente(self, oponente):
        self.oponente = oponente
    def set_equipo(self,equipo):
        self.equipo = equipo
    def set_informe(self,informe):
        self.informe = informe

class Personaje:

    def __init__(self):
        self.vida_maxima = int()
        self.vida_actual = int()
        self.danyo = int()
        self.posicion = str()
        self.enfriamiento_restante = int()
        self.equipo = list()
    def set_vida_actual(self,vida_actual):
        self.vida_actual = vida_actual
    def set_posicion(self,posicion):
        self.posicion = posicion
    def set_enfriamiento(self,enfriamiento):
        self.enfriamiento_restante = enfriamiento
    def get_vida_max(self):
        return self.vida_maxima()
    def get_posicion(self):
        return self.get_posicion()
    def get_enfriamiento(self):
        return self.enfriamiento_restante
class Medicos(Personaje):
    def __init__(self):
        super().__init__()
        self.vida_maxima = 1
        self.vida_actual = 1
        self.danyo = 0
        self.enfriamiento_restante = 0
    def curar(self,objetivo):
        if self.get_enfriamiento() == 0:
            objetivo.set_vida_actual(objetivo.get_vidamax())
            self.set_enfriamiento(1)
        else:
            print('Habilidad en enfriamiento, elija otra opción')
class Artilleros(Personaje):
    def __init__(self):
        super().__init__()
        self.vida_maxima = 2
        self.vida_actual = 2
        self.danyo = 1
        self.enfriamiento_restante = 0
    def disparar(self,objetivo):

        if self.get_enfriamiento() == 0:
            if validar_celda(objetivo,'D',4):
                columnas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                columnas = list(columnas)
                derecha = objetivo[0] + str(int(objetivo[1]) + 1)
                abajo = columnas[columnas.index(objetivo[0]) + 1] + objetivo[1]
                esquina = columnas[columnas.index(objetivo[0]) + 1] + str(int(objetivo[1]) + 1)
                if validar_celda(esquina,'D',4):
                    area = [objetivo, derecha, abajo, esquina]
                elif validar_celda(derecha,'D',4) and not validar_celda(abajo,'D',4):
                    area = [objetivo,derecha]
                elif not validar_celda(derecha,'D',4) and validar_celda(abajo,'D',4):
                    area = [objetivo,abajo]
                else:
                    area =[objetivo]
            else:
                return 'La casilla seleccionada no es valida'
        else:
            return 'La habilidad esta en enfriamiento'
        return area
class Francotiradores(Personaje):
    def __init__(self):
        super().__init__()
        self.vida_maxima = 3
        self.vida_actual = 3
        self.danyo = 3
        self.enfriamiento_restante = 0
    #def eliminar(self,objetivo):
class Inteligencias(Personaje):
    def __init__(self):
        super().__init__()
        self.vida_maxima = 2
        self.vida_actual = 2
        self.danyo = 0
        self.enfriamiento_restante = 0

#=================================================================================================
#aqui estan unas clases para errores custom para que sea mas comodo en los try y no usar errores de python que no vengan al caso
class CasillaInvalidaError(Exception):
    pass
class CasillaOcupadaError(Exception):
    pass

