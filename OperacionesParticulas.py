from Cursor import CursorDelPool
from Sentencias import SentenciasSQL
from tabulate import tabulate

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
    def insertar_particula(nombre_tabla, nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo):
        """
        Inserta una partícula en la tabla especificada ('bariones', 'mesones' o 'leptones').
        """
        with CursorDelPool() as cursor:
            cursor.execute(SentenciasSQL.INSERTAR_PARTICULA.format(nombre_tabla), 
                           (nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo))
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
                INSERT INTO particulas (nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo)
                SELECT nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, 'barion'
                FROM bariones;
                ''')

                # Leptones
                cursor.execute('''
                INSERT INTO particulas (nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo)
                SELECT nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, 'lepton'
                FROM leptones;
                ''')

                # Mesones
                cursor.execute('''
                INSERT INTO particulas (nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo)
                SELECT nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, 'meson'
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
                cursor.execute(f"SELECT nombre, numero_barionico, numero_leptonico, carga_electrica, masa FROM particulas WHERE id = {particula_id};")
                resultado = cursor.fetchone()
                if resultado:
                    propiedades.append({
                        'nombre': resultado[0],
                        'numero_barionico': resultado[1],
                        'numero_leptonico': resultado[2],
                        'carga_electrica': resultado[3],
                        'masa': resultado[4]  # Energía en este caso sería representada por la masa
                    })
        return propiedades

    @staticmethod
    def verificar_leyes_conservacion(propiedades_iniciales, propiedades_finales):
        """
        Verifica las leyes de conservación entre el estado inicial y final.
        """
        # Inicializar acumuladores
        suma_barionica_inicial = sum([p['numero_barionico'] for p in propiedades_iniciales])
        suma_barionica_final = sum([p['numero_barionico'] for p in propiedades_finales])

        suma_leptonica_inicial = sum([p['numero_leptonico'] for p in propiedades_iniciales])
        suma_leptonica_final = sum([p['numero_leptonico'] for p in propiedades_finales])

        carga_inicial = sum([p['carga_electrica'] for p in propiedades_iniciales])
        carga_final = sum([p['carga_electrica'] for p in propiedades_finales])

        energia_inicial = sum([p['masa'] for p in propiedades_iniciales])
        energia_final = sum([p['masa'] for p in propiedades_finales])

        # Verificar si todas las leyes de conservación se cumplen
        conservacion_barionica = suma_barionica_inicial == suma_barionica_final
        conservacion_leptonica = suma_leptonica_inicial == suma_leptonica_final
        conservacion_carga = carga_inicial == carga_final
        conservacion_energia = energia_inicial == energia_final

        # Si todas las leyes se cumplen, el proceso es posible
        if conservacion_barionica and conservacion_leptonica and conservacion_carga and conservacion_energia:
            print("El proceso es físicamente posible ya que cumple con las leyes de conservación.")
        else:
            print("El proceso no es físicamente posible debido a la siguiente(s) ley(es) no conservada(s):")
            if not conservacion_barionica:
                print("- No se conserva el número bariónico.")
            if not conservacion_leptonica:
                print("- No se conserva el número leptónico.")
            if not conservacion_carga:
                print("- No se conserva la carga eléctrica.")
            if not conservacion_energia:
                print("- No se conserva la energía.")


