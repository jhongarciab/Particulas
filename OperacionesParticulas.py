from Cursor import CursorDelPool
from Sentencias import SentenciasSQL
from tabulate import tabulate
from itertools import combinations

class OperacionesParticulas:
    
    @staticmethod
    def crear_tabla(nombre_tabla):
        """
        Crea una tabla genérica en la base de datos (bariones, mesones o leptones).
        """
        with CursorDelPool() as cursor:
            cursor.execute(SentenciasSQL.CREAR_TABLA.format(nombre_tabla))
            print(f"Tabla '{nombre_tabla}' creada o ya existe.")
    
    @staticmethod
    def crear_tabla_conjunta(nombre_tabla):
        """
        Crea una tabla general.
        """
        with CursorDelPool() as cursor:
            cursor.execute(SentenciasSQL.CREAR_TABLA_CONJUNTA.format(nombre_tabla))
            print(f"Tabla '{nombre_tabla}' creada o ya existe.")

    @staticmethod
    def insertar_particula(nombre_tabla, nombre, quarks, momento_angular, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo):
        """
        Inserta una partícula en la tabla especificada ('bariones', 'mesones' o 'leptones').
        """
        with CursorDelPool() as cursor:
            cursor.execute(SentenciasSQL.INSERTAR_PARTICULA.format(nombre_tabla), 
                           (nombre, quarks, momento_angular, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo))
            print(f"Partícula '{nombre}' insertada en la tabla '{nombre_tabla}'.")
    
    @staticmethod
    def seleccionar_particula(nombre_tabla, nombre):
        """
        Selecciona una partícula por su nombre de la tabla especificada ('bariones', 'mesones' o 'leptones').
        """
        with CursorDelPool() as cursor:
            cursor.execute(SentenciasSQL.SELECCIONAR_PARTICULA.format(nombre_tabla), (nombre,))
            return cursor.fetchone()

    @staticmethod
    def insertar_datos_unificados():
        """
        Inserta los datos unificados de las tablas bariones, mesones y leptones en la tabla particulas.
        """
        with CursorDelPool() as cursor:
            try:
                # Bariones
                cursor.execute('''
                INSERT INTO particulas (nombre, quarks, momento_angular, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo)
                SELECT nombre, quarks, momento_angular, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, 'barion'
                FROM bariones;
                ''')

                # Leptones
                cursor.execute('''
                INSERT INTO particulas (nombre, quarks, momento_angular, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo)
                SELECT nombre, quarks, momento_angular, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, 'lepton'
                FROM leptones;
                ''')

                # Mesones
                cursor.execute('''
                INSERT INTO particulas (nombre, quarks, momento_angular, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo)
                SELECT nombre, quarks, momento_angular, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, 'meson'
                FROM mesones;
                ''')

                cursor.connection.commit()
                print("Datos unificados insertados correctamente.")

            except Exception as e:
                print(f"Ocurrió un error: {e}")
                cursor.connection.rollback()

    @staticmethod
    def mostrar_datos(nombre_tabla):
        """
        Muestra los datos de la tabla especificada en un formato de tabla estética.
        """
        with CursorDelPool() as cursor:
            cursor.execute(f"SELECT * FROM {nombre_tabla};")
            datos = cursor.fetchall() 
            headers = [desc[0] for desc in cursor.description]  
            print(tabulate(datos, headers=headers, tablefmt='grid')) 

    @staticmethod
    def solicitar_cantidad_particulas():
        """
        Solicita al usuario cuántas partículas hay en los estados inicial y final.
        """
        try:
            num_particulas_inicial = int(input("Ingrese el número de partículas en el estado inicial: "))
            num_particulas_final = int(input("Ingrese el número de partículas en el estado final: "))
            print(f"Estado inicial: {num_particulas_inicial} partículas.")
            print(f"Estado final: {num_particulas_final} partículas.")
            return num_particulas_inicial, num_particulas_final
        except ValueError:
            print("Por favor ingrese un número válido.")
            return OperacionesParticulas.solicitar_cantidad_particulas()

    @staticmethod
    def seleccionar_particulas(num_inicial, num_final):
        """
        Permite al usuario seleccionar partículas para el estado inicial y final según el número ingresado.
        """
        particulas_iniciales = []
        particulas_finales = []

        # Estado inicial
        print(f"Seleccione {num_inicial} partículas del estado inicial:")
        while len(particulas_iniciales) < num_inicial:
            particula_id = input(f"Ingrese el ID de la(s) partícula(s) iniciales ({len(particulas_iniciales)+1}/{num_inicial}): ")
            try:
                particula_id = int(particula_id)
                particulas_iniciales.append(particula_id)
            except ValueError:
                print("Por favor ingrese un número válido.")

        # Estado final
        print(f"Seleccione {num_final} partículas del estado final:")
        while len(particulas_finales) < num_final:
            particula_id = input(f"Ingrese el ID de la(s) partícula(s) finales ({len(particulas_finales)+1}/{num_final}): ")
            try:
                particula_id = int(particula_id)
                particulas_finales.append(particula_id)
            except ValueError:
                print("Por favor ingrese un número válido.")
        
        return particulas_iniciales, particulas_finales
    
    @staticmethod
    def obtener_todas_las_particulas():
        """
        Obtiene todas las partículas de la base de datos.
        """
        with CursorDelPool() as cursor:
            cursor.execute("SELECT nombre, masa FROM particulas;")
            particulas = cursor.fetchall()
            return [{'nombre': p[0], 'masa': p[1]} for p in particulas]


    @staticmethod
    def mostrar_interaccion(particulas_iniciales, particulas_finales):
        """
        Muestra la interacción de las partículas seleccionadas en el formato A + B --> C + D + F.
        """
        with CursorDelPool() as cursor:
            iniciales = []
            finales = []
            
            # Partículas iniciales
            for particula_id in particulas_iniciales:
                cursor.execute(f"SELECT nombre FROM particulas WHERE id = {particula_id};")
                nombre = cursor.fetchone()
                if nombre:
                    iniciales.append(nombre[0])
            
            # Partículas finales
            for particula_id in particulas_finales:
                cursor.execute(f"SELECT nombre FROM particulas WHERE id = {particula_id};")
                nombre = cursor.fetchone()
                if nombre:
                    finales.append(nombre[0])
            
            print(" + ".join(iniciales) + " ---> " + " + ".join(finales))

    @staticmethod
    def obtener_propiedades_particulas(particulas_ids):
        """
        Obtiene las propiedades de las partículas seleccionadas por su ID.
        Retorna una lista de diccionarios con los valores de cada propiedad.
        """
        propiedades = []
        with CursorDelPool() as cursor:
            for particula_id in particulas_ids:
                cursor.execute(f"SELECT nombre, momento_angular, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa FROM particulas WHERE id = {particula_id};")
                resultado = cursor.fetchone()
                if resultado:
                    propiedades.append({
                        'nombre': resultado[0],
                        'momento_angular': resultado[1] if resultado[1] is not None else 0,
                        'extrañeza': resultado[2],
                        'carga_electrica': resultado[3],
                        'numero_barionico': resultado[4],
                        'numero_leptonico': resultado[5],
                        'masa': resultado[6]  
                    })
        return propiedades

    @staticmethod
    def generar_lista_momentos_angulares(momentos_angulares):
        """
        Genera todas las combinaciones posibles de momentos angulares sumados y restados entre sí.
        """
        if len(momentos_angulares) == 1:
            return [momentos_angulares[0]]
        
        # Tomamos el primer par y generamos la primera combinación de suma y resta
        j1 = momentos_angulares[0]
        j2 = momentos_angulares[1]
        
        primera = [j1 + j2, abs(j1 - j2)]
        if primera[0] - 1 != primera[1]:
            primera.append(primera[0] - 1)
            primera.sort()

        # Iteramos sobre las partículas restantes
        for i in range(2, len(momentos_angulares)):
            j = momentos_angulares[i]
            nueva_lista = []
            # Para cada valor en la lista actual, sumamos y restamos el nuevo momento angular
            for val in primera:
                if val + j not in nueva_lista:
                    nueva_lista.append(val + j)
                if abs(val - j) not in nueva_lista:
                    nueva_lista.append(abs(val - j))
            
            nueva_lista.sort()
            primera = nueva_lista

        return primera

    @staticmethod
    def verificar_conservacion_momento_angular(particulas_iniciales, particulas_finales):
        """
        Verifica si se conserva el momento angular entre las partículas iniciales y finales.
        La conservación se cumple si al menos un valor del momento angular de las combinaciones iniciales 
        coincide con algún valor de las combinaciones finales.
        """
        # Extraer los momentos angulares de las partículas iniciales y finales
        momentos_iniciales = [p.get("momento_angular", 0) for p in particulas_iniciales]
        momentos_finales = [p.get("momento_angular", 0) for p in particulas_finales]

        # Generar las combinaciones de momentos angulares posibles para los estados inicial y final
        combinaciones_iniciales = OperacionesParticulas.generar_lista_momentos_angulares(momentos_iniciales)
        combinaciones_finales = OperacionesParticulas.generar_lista_momentos_angulares(momentos_finales)

        # Verificar si existe al menos un valor en común entre las combinaciones iniciales y finales
        for momento_inicial in combinaciones_iniciales:
            if momento_inicial in combinaciones_finales:
                return True  # Se encontró una coincidencia, momento angular conservado

        return False  # No se encontró ninguna coincidencia, momento angular no conservado

    @staticmethod
    def verificar_leyes_conservacion(propiedades_iniciales, propiedades_finales, particulas_posibles):
        """
        Verifica las leyes de conservación entre el estado inicial y final, y sugiere nuevas partículas si hay masa sobrante.
        """
        # Inicializar acumuladores
        suma_barionica_inicial = sum([int(p['numero_barionico']) for p in propiedades_iniciales])
        suma_barionica_final = sum([int(p['numero_barionico']) for p in propiedades_finales])
        
        suma_leptonica_inicial = sum([p['numero_leptonico'] for p in propiedades_iniciales])
        suma_leptonica_final = sum([p['numero_leptonico'] for p in propiedades_finales])

        carga_inicial = sum([p['carga_electrica'] for p in propiedades_iniciales])
        carga_final = sum([p['carga_electrica'] for p in propiedades_finales])

        masa_inicial = sum([p['masa'] for p in propiedades_iniciales])
        masa_final = sum([p['masa'] for p in propiedades_finales])

        extrañeza_inicial = sum([p['extrañeza'] for p in propiedades_iniciales])
        extrañeza_final = sum([p['extrañeza'] for p in propiedades_finales])

        # Verificar conservación del momento angular
        conservacion_momento_angular = OperacionesParticulas.verificar_conservacion_momento_angular(propiedades_iniciales, propiedades_finales)

        # Verificar si todas las leyes de conservación se cumplen
        conservacion_barionica = suma_barionica_inicial == suma_barionica_final
        conservacion_leptonica = suma_leptonica_inicial == suma_leptonica_final
        conservacion_carga = carga_inicial == carga_final
        conservacion_masa = masa_inicial >= masa_final
        conservacion_extrañeza = extrañeza_inicial == extrañeza_final

        proceso_posible = (conservacion_barionica and conservacion_leptonica and 
                        conservacion_carga and conservacion_masa and conservacion_momento_angular)

        if proceso_posible:
            if masa_inicial > masa_final:
                masa_sobrante = masa_inicial - masa_final
                print(f"Masa sobrante: {masa_sobrante}")

                particulas_filtradas = [p for p in particulas_posibles if p['masa'] <= masa_sobrante]
                
                for r in range(1, len(particulas_filtradas) + 1):
                    for combinacion in combinations(particulas_filtradas, r):
                        suma_masas = sum([p['masa'] for p in combinacion])
                        
                        if abs(suma_masas - masa_sobrante) < 1.0:
                            conservacion_barionica_extra = (sum([p.get('numero_barionico', 0) for p in combinacion]) == 0)
                            conservacion_leptonica_extra = (sum([p.get('numero_leptonico', 0) for p in combinacion]) == 0)
                            conservacion_carga_extra = (sum([p.get('carga_electrica', 0) for p in combinacion]) == 0)
                            conservacion_momento_angular_extra = OperacionesParticulas.verificar_conservacion_momento_angular(propiedades_finales, combinacion)

                            if (conservacion_barionica_extra and conservacion_leptonica_extra and
                                conservacion_carga_extra and conservacion_momento_angular_extra):
                                
                                nombres_particulas = [p['nombre'] for p in combinacion]
                                if not conservacion_extrañeza:
                                    print(f"No se conserva la extrañeza.")
                                print(f"El proceso es físicamente posible y la masa sobrante puede convertirse en: {' + '.join(nombres_particulas)}")
                                return

                print("El proceso es físicamente posible, pero no se encontraron partículas adecuadas para la masa sobrante.")
            else:
                print("El proceso es físicamente posible ya que cumple con todas las leyes de conservación.")

            if not conservacion_extrañeza:
                print("Aunque no se conserva la extrañeza.")
        else:
            print("El proceso no es físicamente posible debido a la(s) siguiente(s) ley(es) no conservada(s):")
            if not conservacion_barionica:
                print("- No se conserva el número bariónico.")
            if not conservacion_leptonica:
                print("- No se conserva el número leptónico.")
            if not conservacion_carga:
                print("- No se conserva la carga eléctrica.")
            if not conservacion_masa:
                print("- No se conserva la energía.")
            if not conservacion_momento_angular:
                print("- No se conserva el momento angular.")
