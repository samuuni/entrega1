from utils import validar_celda,filas, columnas, validar_celda_contigua

class Jugador:


    def turno(self):
        # informe
        self.realizar_accion()
        # recibir accion
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
                    op_num +=1
                else:
                    op_num += 1
            else:
                op_num += 1
                print(f'{op_num}: {equipo_restante[opciones].get_habilidad()}. ({equipo_restante[opciones].get_nombre()})')
                menu.append({op_num :  f'H{equipo_restante[opciones].get_codigo()}'})
                if opciones == len(equipo_restante)-1:
                    op_num = op_num
                else:
                    op_num += 1
        while True:
            try:
                eleccion = int(input('Seleccione la acción para este turno: '))
                if 1<=eleccion<=op_num:
                    for indx in menu:
                        if eleccion in indx:
                            resultado = indx[eleccion]
                    if resultado[0] == 'M': #Mover
                        cod = resultado[1]
                        if cod == 'M':
                            medico = self.get_equipo()[0]
                            while True:
                                try:
                                    celda = input(
                                        f'Indica la celda a la que mover al Médico (Posicion actual: {medico.get_posicion()}): ')
                                    celda = celda.upper()
                                    mover = medico.mover(celda)
                                    if mover == 1:
                                        break
                                    elif mover == 'Ocupada':
                                        raise CasillaOcupadaError
                                    elif mover == 'ContiguaError':
                                        raise CasillaNoContiguaError
                                    elif mover == 'Invalid':
                                        raise CasillaInvalidaError
                                    else:
                                        raise Exception
                                except CasillaOcupadaError:
                                    print('La casilla esta ocupada')
                                except CasillaNoContiguaError:
                                    print('La casilla no es contigua')
                                except CasillaInvalidaError:
                                    print('La casilla es invalida')
                                except:
                                    print('Valor invalido')
                        elif cod == 'A':
                            artillero = self.get_equipo()[1]
                            while True:
                                try:
                                    celda = input(
                                        f'Indica la celda a la que mover al Médico (Posicion actual: {artillero.get_posicion()}): ')
                                    celda = celda.upper()
                                    mover = artillero.mover(celda)
                                    if mover == 1:
                                        break
                                    elif mover == 'Ocupada':
                                        raise CasillaOcupadaError
                                    elif mover == 'ContiguaError':
                                        raise CasillaNoContiguaError
                                    elif mover == 'Invalid':
                                        raise CasillaInvalidaError
                                    else:
                                        raise Exception
                                except CasillaOcupadaError:
                                    print('La casilla esta ocupada')
                                except CasillaNoContiguaError:
                                    print('La casilla no es contigua')
                                except CasillaInvalidaError:
                                    print('La casilla es invalida')
                                except:
                                    print('Valor invalido')
                        elif cod == 'F':
                            francotirador = self.get_equipo()[2]
                            while True:
                                try:
                                    celda = input(
                                        f'Indica la celda a la que mover al Médico (Posicion actual: {francotirador.get_posicion()}): ')
                                    celda = celda.upper()
                                    mover = francotirador.mover(celda)
                                    if mover == 1:
                                        break
                                    elif mover == 'Ocupada':
                                        raise CasillaOcupadaError
                                    elif mover == 'ContiguaError':
                                        raise CasillaNoContiguaError
                                    elif mover == 'Invalid':
                                        raise CasillaInvalidaError
                                    else:
                                        raise Exception
                                except CasillaOcupadaError:
                                    print('La casilla esta ocupada')
                                except CasillaNoContiguaError:
                                    print('La casilla no es contigua')
                                except CasillaInvalidaError:
                                    print('La casilla es invalida')
                                except:
                                    print('Valor invalido')
                        elif cod == 'I':
                            inteligencia = self.get_equipo()[3]
                            while True:
                                try:
                                    celda = input(
                                        f'Indica la celda a la que mover al Médico (Posicion actual: {inteligencia.get_posicion()}): ')
                                    celda = celda.upper()
                                    mover = inteligencia.mover(celda)
                                    if mover == 1:
                                        break
                                    elif mover == 'Ocupada':
                                        raise CasillaOcupadaError
                                    elif mover == 'ContiguaError':
                                        raise CasillaNoContiguaError
                                    elif mover == 'Invalid':
                                        raise CasillaInvalidaError
                                    else:
                                        raise Exception
                                except CasillaOcupadaError:
                                    print('La casilla esta ocupada')
                                except CasillaNoContiguaError:
                                    print('La casilla no es contigua')
                                except CasillaInvalidaError:
                                    print('La casilla es invalida')
                                except:
                                    print('Valor invalido')
                        return None
                    elif resultado[0] == 'H': #Habilidad
                        oponente = self.get_oponente()
                        enemigos = oponente.get_equipo()
                        cod = resultado[1]
                        if cod == 'M':
                            medico = self.get_equipo()[0]
                            if medico.get_enfriamiento() == 0:
                                while True:
                                    try:
                                        herido = input('Indica el compañero al cual curar: ')
                                        herido = herido.lower()
                                        herido = herido.capitalize() # .capitalize() pone la primera letra mayuscula
                                        for compañero in equipo_restante:
                                            if compañero.get_nombre() == herido:
                                                herido_obj = compañero
                                        habilidad = medico.habilidad(herido_obj)
                                        if habilidad:
                                            break
                                        else:
                                            raise Exception
                                    except:
                                        print('Ups... valor inválido')
                                equipo = medico.get_equipo()
                                for aliado in equipo:
                                    if aliado.get_enfriamiento() == 1:
                                        aliado.set_enfriamiento(0)
                                cod_out = None
                                break
                            else:
                                raise HabilidadEnfriamientoError
                        elif cod == 'A':
                            artillero = self.get_equipo()[1]
                            if artillero.get_enfriamiento() == 0:
                                while True:
                                    try:
                                        celda = input(
                                            'Indica las coordenadas de la esquina superior izquierda en la que disparar (área 2x2): ')
                                        celda.upper()
                                        habilidad = artillero.habilidad(celda,enemigos)
                                        if habilidad:
                                            break
                                        else:
                                            raise CasillaInvalidaError
                                    except CasillaInvalidaError:
                                        print('Ups... valor de celda incorrecto.')
                                    except:
                                        print('Ups... valor incorrecto.')
                                equipo = artillero.get_equipo()
                                for aliado in equipo:
                                    if aliado.get_enfriamiento() == 1:
                                        aliado.set_enfriamiento(0)
                                cod_out = f'A{celda}'
                                break
                            else:
                                raise HabilidadEnfriamientoError
                        elif cod == 'F':
                            francotirador = self.get_equipo()[2]
                            while True:
                                celda = input(
                                    'Indica las coordenadas de la cerlda a la que disparar: ')
                                habilidad = francotirador.habilidad(celda,enemigos)
                                if habilidad:
                                    break
                                else:
                                    raise HabilidadEnfriamientoError
                            equipo = francotirador.get_equipo()
                            for aliado in equipo:
                                if aliado.get_enfriamiento() == 1:
                                    aliado.set_enfriamiento(0)
                            cod_out = f'F{celda}'
                            break
                        elif cod == 'I':
                            inteligencia = self.get_equipo()[3]
                            while True:
                                celda = input(
                                    'Indica las coordenadas de la esquina superior izquierda de la zona de observación (área 2x2): ')
                                habilidad = inteligencia.habilidad(celda,enemigos)
                                if habilidad:
                                    break
                                else:
                                    raise HabilidadEnfriamientoError
                            equipo = inteligencia.get_equipo()
                            for aliado in equipo:
                                if aliado.get_enfriamiento() == 1:
                                    aliado.set_enfriamiento(0)
                            cod_out = f'I{celda}'
                            break

                        return cod_out
                else:
                    raise OpcionInvalidadError

            except OpcionInvalidadError:
                print(f'Opción inválida, seleccione una opción 1-{op_num}')
            except HabilidadEnfriamientoError:
                print('La habilidad del personaje esta en enfriamiento, seleccione otra opción')
            except:
                print(f'Opción inválida, seleccione una opción 1-{op_num}')
    def informe(self,ofensivo,codigo,lista): #tengo que ver como hacerlo bien
        if ofensivo == True:    #si la accion es ofensiva
            if codigo[0] == 'A':
                for enemigo in lista:
                    if enemigo.get_vida_actual() < enemigo.get_vida_max():
                        print(f'{enemigo.get_nombre()} ha sido herido en {enemigo.get_posicion()} '
                              f'[Vida restante: {enemigo.get_vida_max()-enemigo.get_vida_actual()}]')
            elif codigo[0] == 'F':
            elif codigo[0] == 'I':
        else:   #si la accion es recibida

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
                print('Ups... va0lor de celda incorrecto.')
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
    def get_oponente(self):
        return self.oponente

class Personaje:
    def area_2x2(self,objetivo): #para artillero e inteligencia
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
    def mover(self, celda):
        if validar_celda(celda, columnas(),filas()):
            if validar_celda_contigua(celda,self.get_posicion()):
                for equipo in self.get_equipo():
                    if celda == equipo.get_posicion():
                        return 'Ocupada'
                self.set_posicion(celda)
                return 1
            else:
                return 'ContiguaError'
        else:
            return 'Invalid'
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
    def habilidad(self,objetivo):
        vida = objetivo.get_vida_max()
        objetivo.set_vida_actual(vida)
        self.set_enfriamiento(1)
        return True
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

    def habilidad(self,objetivo,oponente):
        if validar_celda(objetivo,columnas(),filas()):
            area = self.area_2x2(objetivo)
            enemigos = []
            for enemigo in oponente:
                if enemigo.get_posicion() in area:
                    enemigos.append(enemigo)
                    vida = enemigo.get_vida_actual()
                    enemigo.set_vida_actual(vida-1)
            self.set_enfriamiento(1)
            return enemigos
        else:
            return False

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
    #def habilidad(self,objetivo):
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
    def habilidad(self, objetivo, oponente):
        if validar_celda(objetivo,columnas(),filas()):
            area = self.area_2x2(objetivo)
            for enemigo in oponente:
                if enemigo.get_posicion() in area:
                    vida = enemigo.get_vida_actual()
                    enemigo.set_vida_actual(vida-1)
            self.set_enfriamiento(1)
            return True
        else:
            return False
#===============================================================================================================================
#aqui estan unas clases para errores custom para que sea mas comodo en los try y no usar errores de python que no vengan al caso
class CasillaInvalidaError(Exception):
    pass
class CasillaOcupadaError(Exception):
    pass
class CasillaNoContiguaError(Exception):
    pass
class OpcionInvalidadError(Exception):
    pass
class HabilidadEnfriamientoError(Exception):
    pass
