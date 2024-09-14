class SentenciasSQL:
    CREAR_TABLA = '''
    CREATE TABLE IF NOT EXISTS {} (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        carga_electrica DECIMAL(3, 1) NOT NULL,
        numero_barionico INT NOT NULL,
        numero_leptonico INT NOT NULL,
        masa DECIMAL(10, 3) NOT NULL
    );
    '''
    
    INSERTAR_PARTICULA = '''
    INSERT INTO {} (nombre, carga_electrica, numero_barionico, numero_leptonico, masa)
    VALUES (%s, %s, %s, %s, %s);
    '''
    
    SELECCIONAR_PARTICULA = '''
    SELECT * FROM {} WHERE nombre = %s;
    '''

