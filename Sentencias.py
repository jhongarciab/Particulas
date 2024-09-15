class SentenciasSQL:
    CREAR_TABLA = '''
    CREATE TABLE IF NOT EXISTS {} (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        quarks VARCHAR(50),
        espín DECIMAL(3, 1) NOT NULL,
        extrañeza INT NOT NULL,
        carga_electrica DECIMAL(3, 1) NOT NULL,
        numero_barionico INT NOT NULL,
        numero_leptonico INT NOT NULL,
        masa DECIMAL(10, 3) NOT NULL
    );
    '''
    CREAR_TABLA_CONJUNTA = '''
    CREATE TABLE IF NOT EXISTS {} (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        quarks VARCHAR(50),
        espín DECIMAL(3, 1) NOT NULL,
        extrañeza INT NOT NULL,
        carga_electrica DECIMAL(3, 1) NOT NULL,
        numero_barionico INT NOT NULL,
        numero_leptonico INT NOT NULL,
        masa DECIMAL(10, 3) NOT NULL,
        grupo VARCHAR(20) NOT NULL  
    );
    '''
    
    INSERTAR_PARTICULA = '''
    INSERT INTO {} (nombre, quarks, espín, extrañeza, carga_electrica, numero_barionico, numero_leptonico, masa, grupo)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''


