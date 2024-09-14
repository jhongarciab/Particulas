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
    def insertar_particula(nombre_tabla, nombre, numero_cuantico, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa):
        """
        Inserta una partícula en la tabla especificada ('bariones', 'mesones' o 'leptones').
        """
        with CursorDelPool() as cursor:
            cursor.execute(SentenciasSQL.INSERTAR_PARTICULA.format(nombre_tabla), 
                           (nombre, numero_cuantico, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa))
            print(f"Partícula '{nombre}' insertada en la tabla '{nombre_tabla}'.")
    
    @staticmethod
    def seleccionar_particula(nombre_tabla, nombre):
        """
        Selecciona una partícula por su nombre de la tabla especificada ('bariones', 'mesones' o 'leptones').
        """
        with CursorDelPool() as cursor:
            cursor.execute(SentenciasSQL.SELECCIONAR_PARTICULA.format(nombre_tabla), (nombre,))
            return cursor.fetchone()

