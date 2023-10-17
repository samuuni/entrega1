from utils import validar_celda,filas, columnas, validar_celda_contigua

class Jugador:


    def turno(self):
        self.realizar_accion()
        #meter un while true con try para realizar accion por si ponen algo diferente
        return
    def realizar_accion(self): #orden [medico, artillero, francotirador, inteligencia]
        equipo_restante = self.get_equipo()
        nombres = ['Medico','Artillero', 'Francotirador','Inteligencia']
        print('---- SITUACION DEL EQUIPO ----')
        for personaje in range(len(equipo_restante)):
            if equipo_restante[personaje].get_vida_actual() > 0 :
                print(f'{nombres[personaje]} está en {equipo_restante[personaje].get_posicion()} '
                      f'[Vida {equipo_restante[personaje].get_vida_actual()}/{equipo_restante[personaje].get_vida_max()}]')
            elif equipo_restante[personaje].get_vida_actual() == 0:
                del equipo_restante[personaje]
                del nombres[personaje]
        op_num = 1
        menu = []

        for opciones in range(len(equipo_restante)):
            print(f'{op_num}: Mover ({equipo_restante[opciones].get_nombre()})')
            menu.append({op_num: f'M{equipo_restante[opciones].get_codigo()}'})
            if equipo_restante[opciones].get_nombre() == 'Medico':
                heridos = 0
                for herido in equipo_restante:
                    if herido.get_vida_actual() < herido.get_vida_max():
                        heridos += 1
                if heridos > 0:
                    op_num += 1
                    print(f'{op_num}: {equipo_restante[opciones].get_habilidad()} ({equipo_restante[opciones].get_nombre()})')
                    menu.append({op_num : f'H{equipo_restante[opciones].get_codigo()}'})
                else:
                    op_num += 1
            else:
                op_num += 1
                print(f'{op_num}: {equipo_restante[opciones].get_codigo()}. ({equipo_restante[opciones].get_nombre()})')
                menu.append({op_num :  f'H{equipo_restante[opciones].get_codigo()}'})
                if opciones == len(equipo_restante)-1:
                    op_num = op_num
                else:
                    op_num += 1
        while True:
            try:
                eleccion = int(input('Seleccione la acción para este turno: '))
                if 1<=eleccion<=op_num:
                    break
                else:
                    raise OpcionInvalidadError
            except OpcionInvalidadError:
                print(f'Opción inválida, seleccione una opción 1-{op_num}')
            except:
                print(f'Opción inválida, seleccione una opción 1-{op_num}')
        for indx in menu:
            if indx == eleccion:
                resultado = menu[indx]
        if resultado[0] == 'M':
            cod = resultado[1]
            if cod == 'M':
                medico = self.get_equipo()[0]
                while True:
                    celda = input(f'Indica la celda a la que mover al Médico (Posicion actual: {medico.get_posicion()}): ')
                    mover = medico.mover(celda)
                    if mover:
                        break
                    else:
                        print(mover)
            elif cod == 'A':
                artillero = self.get_equipo()[1]
                while True:
                    celda = input(
                        f'Indica la celda a la que mover al Médico (Posicion actual: {artillero.get_posicion()}): ')
                    mover = artillero.mover(celda)
                    if mover:
                        break
                    else:
                        print(mover)
            elif cod == 'F':
                francotirador = self.get_equipo()[2]
                while True:
                    celda = input(
                        f'Indica la celda a la que mover al Médico (Posicion actual: {francotirador.get_posicion()}): ')
                    mover = francotirador.mover(celda)
                    if mover:
                        break
                    else:
                        print(mover)
            elif cod == 'I':
                inteligencia = self.get_equipo()[3]
                while True:
                    celda = input(
                        f'Indica la celda a la que mover al Médico (Posicion actual: {inteligencia.get_posicion()}): ')
                    mover = inteligencia.mover(celda)
                    if mover:
                        break
                    else:
                        print(mover)
        elif resultado[0] == 'H':
            cod = resultado[1]




        return eleccion

    def crear_equipo(self,personaje,celda):
        if personaje == 'Medico':
            personaje = Medicos()
            personaje.set_posicion(celda)
        elif personaje == 'Artillero':
            personaje = Artilleros()
            personaje.set_posicion(celda)
        elif personaje == 'Francotirador':
            personaje = Francotiradores()
            personaje.set_posicion(celda)
        elif personaje == 'Inteligencia':
            personaje = Inteligencias()
            personaje.set_posicion(celda)
        return personaje
    def posicionar_equipo(self):
        print('vamos a posicionar a nuestors personajes en el tablero!')
        equipo = []

        while True:
            try:

                pos_medico = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Medico: ')
                pos_medico = pos_medico.upper()
                if validar_celda(pos_medico, columnas(), filas()):
                    Medico = self.crear_equipo('Medico', pos_medico)
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
                pos_artillero = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Artillero: ')
                pos_artillero = pos_artillero.upper()
                if validar_celda(pos_artillero, columnas(), filas()):
                    Artillero = self.crear_equipo('Artillero',pos_artillero)
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
                pos_francotirador = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Francotirador: ')
                pos_francotirador = pos_francotirador.upper()
                if validar_celda(pos_francotirador, columnas(), filas()):
                    Francotirador = self.crear_equipo('Francotirador',pos_francotirador)
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
                pos_inteligencia = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Inteligencia: ')
                pos_inteligencia = pos_inteligencia.upper()
                if validar_celda(pos_inteligencia,  columnas(), filas()):
                    Inteligencia = self.crear_equipo('Inteligencia',pos_inteligencia)
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
        for personaje in range(len(equipo)):
            equipo2 = []
            equipo2.extend(equipo)
            del equipo2[personaje]
            equipo[personaje].set_equipo(equipo2[0],equipo2[1],equipo2[2])

        return equipo
    def __init__(self):
        self.oponente = str()
        self.equipo = self.posicionar_equipo()
        self.informe = str()
    def set_oponente(self, oponente):
        self.oponente = oponente
    def set_equipo(self,equipo):
        self.equipo = equipo
    def set_informe(self,informe):
        self.informe = informe
    def get_equipo(self):
        return self.equipo

class Personaje:
    def mover(self, celda):
        if validar_celda(celda, columnas(),filas()):
            if validar_celda_contigua(celda,self.get_posicion()):
                for equipo in self.get_equipo():
                    if celda == equipo.get_posicion():
                        return f'La celda esta ocupada por {equipo.get_nombre()}'
                self.set_posicion(celda)
                return True
            else:
                return 'La celda no es contiga'
        else:
            return 'La celda no es válida'
    def habilidad(self):
    def __init__(self):
        self.vida_maxima = int()
        self.vida_actual = int()
        self.danyo = int()
        self.posicion = str()
        self.enfriamiento_restante = int()
        self.equipo = list()
        self.nombre = str()
        self.habilidad_menu = str()
        self.codigo = str()
    def set_vida_actual(self,vida_actual):
        self.vida_actual = vida_actual
    def set_posicion(self,posicion):
        self.posicion = posicion
    def set_enfriamiento(self,enfriamiento):
        self.enfriamiento_restante = enfriamiento
    def set_equipo(self,personaje1,personaje2,personaje3):
        self.equipo = [personaje1,personaje2,personaje3]
    def get_vida_max(self):
        return self.vida_maxima
    def get_posicion(self):
        return self.posicion
    def get_enfriamiento(self):
        return self.enfriamiento_restante
    def get_vida_actual(self):
        return self.vida_actual
    def get_nombre(self):
        return self.nombre
    def get_habilidad(self):
        return self.habilidad_menu
    def get_codigo(self):
        return  self.codigo
    def get_equipo(self):
        return self.equipo
class Medicos(Personaje):
    def __init__(self):
        super().__init__()
        self.vida_maxima = 1
        self.vida_actual = 1
        self.danyo = 0
        self.enfriamiento_restante = 0
        self.nombre = 'Medico'
        self.habilidad_menu = 'Curar a un compañero'
        self.codigo = 'M'
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
        self.nombre = 'Artillero'
        self.habilidad_menu = 'Disparar en área (2x2). Daño 1'
        self.codigo = 'A'
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
        self.nombre = 'Francotirador'
        self.habilidad_menu = 'Disparar a una celda. Daño 3'
        self.codigo = 'F'
    #def eliminar(self,objetivo):
class Inteligencias(Personaje):
    def __init__(self):
        super().__init__()
        self.vida_maxima = 2
        self.vida_actual = 2
        self.danyo = 0
        self.enfriamiento_restante = 0
        self.nombre = 'Inteligencia'
        self.habilidad_menu = 'Revelar a los enemigos en un área 2x2'
        self.codigo = 'I'

#=================================================================================================
#aqui estan unas clases para errores custom para que sea mas comodo en los try y no usar errores de python que no vengan al caso
class CasillaInvalidaError(Exception):
    pass
class CasillaOcupadaError(Exception):
    pass
class CasillaNoContiguaError(Exception):
    pass
class OpcionInvalidadError(Exception):
    pass

