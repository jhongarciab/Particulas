from Cursor import CursorDelPool
from Sentencias import SentenciasSQL

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
                # Inserción de datos desde 'bariones'
                cursor.execute('''
                INSERT INTO particulas (nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo)
                SELECT nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, 'barion'
                FROM bariones;
                ''')

                # Inserción de datos desde 'leptones'
                cursor.execute('''
                INSERT INTO particulas (nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo)
                SELECT nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, 'lepton'
                FROM leptones;
                ''')

                # Inserción de datos desde 'mesones'
                cursor.execute('''
                INSERT INTO particulas (nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo)
                SELECT nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, 'meson'
                FROM mesones;
                ''')

                # Confirmar los cambios
                cursor.connection.commit()
                print("Datos unificados insertados correctamente.")

            except Exception as e:
                print(f"Ocurrió un error: {e}")
                cursor.connection.rollback()
